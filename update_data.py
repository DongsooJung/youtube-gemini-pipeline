#!/usr/bin/env python3
"""
YouTube Data Auto-Refresh Script
Fetches KR trending videos and AI education videos via YouTube Data API v3,
then updates index.html with fresh data.
"""

import os
import json
import re
from datetime import datetime
from googleapiclient.discovery import build

API_KEY = os.environ.get("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)


def fetch_trending_kr(max_results=20):
    """Fetch Korea trending videos."""
    resp = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode="KR",
        maxResults=max_results,
    ).execute()

    category_map = {}
    cat_resp = youtube.videoCategories().list(
        part="snippet", regionCode="KR", hl="ko"
    ).execute()
    for c in cat_resp.get("items", []):
        category_map[c["id"]] = c["snippet"]["title"]

    results = []
    for item in resp.get("items", []):
        s = item["snippet"]
        st = item.get("statistics", {})
        views = int(st.get("viewCount", 0))
        likes = int(st.get("likeCount", 0))
        comments = int(st.get("commentCount", 0))
        ratio = round((likes + comments) / views, 4) if views else 0
        cat_name = category_map.get(s.get("categoryId", ""), s.get("categoryId", ""))
        results.append({
            "id": item["id"],
            "title": s["title"].replace("'", "\\'").replace('"', '\\"'),
            "channel": s["channelTitle"].replace("'", "\\'").replace('"', '\\"'),
            "cat": cat_name,
            "views": views,
            "likes": likes,
            "comments": comments,
            "ratio": ratio,
        })
    return results


def fetch_ai_education(max_results=15):
    """Fetch AI education related videos in Korean."""
    queries = ["AI êµì¡ ê°ì 2025", "ì¸ê³µì§ë¥ íì© êµì¡", "AI í¸ë ë íêµ­"]
    seen_ids = set()
    results = []

    for q in queries:
        resp = youtube.search().list(
            part="snippet",
            q=q,
            type="video",
            regionCode="KR",
            relevanceLanguage="ko",
            maxResults=max_results,
            order="relevance",
        ).execute()
        for item in resp.get("items", []):
            vid = item["id"]["videoId"]
            if vid in seen_ids:
                continue
            seen_ids.add(vid)
            s = item["snippet"]
            pub = s.get("publishedAt", "")[:10].replace("-", ".")
            results.append({
                "title": s["title"].replace("'", "\\'").replace('"', '\\"'),
                "channel": s["channelTitle"].replace("'", "\\'").replace('"', '\\"'),
                "date": pub,
            })
        if len(results) >= 13:
            break

    return results[:13]


def compute_kpis(trending):
    """Compute dashboard KPI values."""
    total_views = sum(v["views"] for v in trending)
    total_likes = sum(v["likes"] for v in trending)
    avg_ratio = round(sum(v["ratio"] for v in trending) / len(trending), 4) if trending else 0

    cat_counts = {}
    for v in trending:
        cat_counts[v["cat"]] = cat_counts.get(v["cat"], 0) + 1
    top_cat = max(cat_counts, key=cat_counts.get) if cat_counts else "N/A"
    top_cat_pct = round(cat_counts.get(top_cat, 0) / len(trending) * 100) if trending else 0

    return {
        "total_views": total_views,
        "total_likes": total_likes,
        "avg_ratio": avg_ratio,
        "top_cat": top_cat,
        "top_cat_pct": top_cat_pct,
    }


def format_number(n):
    """Format large numbers for display (e.g., 24.7M, 3.17M)."""
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(n)


def build_trending_js(data):
    """Build JS array string for trendingData."""
    lines = []
    for d in data:
        lines.append(
            f'  {{id:"{d["id"]}",title:"{d["title"]}",channel:"{d["channel"]}",'
            f'cat:"{d["cat"]}",views:{d["views"]},likes:{d["likes"]},'
            f'comments:{d["comments"]},ratio:{d["ratio"]}}}'
        )
    return "const trendingData = [\n" + ",\n".join(lines) + "\n];"


def build_ai_js(data):
    """Build JS array string for aiData."""
    lines = []
    for d in data:
        lines.append(
            f'  {{title:"{d["title"]}",channel:"{d["channel"]}",date:"{d["date"]}"}}'
        )
    return "const aiData = [\n" + ",\n".join(lines) + "\n];"


def update_html(trending, ai_videos, kpis):
    """Read index.html and replace data sections."""
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Replace trendingData array
    new_trending = build_trending_js(trending)
    html = re.sub(
        r"const trendingData\s*=\s*\[[\s\S]*?\];",
        new_trending,
        html,
        count=1,
    )

    # Replace aiData array
    new_ai = build_ai_js(ai_videos)
    html = re.sub(
        r"const aiData\s*=\s*\[[\s\S]*?\];",
        new_ai,
        html,
        count=1,
    )

    # Update KPI values in HTML
    today = datetime.now().strftime("%Y.%m.%d")
    html = re.sub(
        r'(<div class="kpi-value" id="kpi-views">)[^<]*(</div>)',
        f'\\g<1>{format_number(kpis["total_views"])}\\2',
        html,
    )
    html = re.sub(
        r'(<div class="kpi-value" id="kpi-engagement">)[^<]*(</div>)',
        f'\\g<1>{kpis["avg_ratio"]*100:.2f}%\\2',
        html,
    )
    html = re.sub(
        r'(<div class="kpi-value" id="kpi-category">)[^<]*(</div>)',
        f'\\g<1>{kpis["top_cat_pct"]}% {kpis["top_cat"]}\\2',
        html,
    )
    html = re.sub(
        r'(<div class="kpi-value" id="kpi-likes">)[^<]*(</div>)',
        f'\\g<1>{format_number(kpis["total_likes"])}\\2',
        html,
    )

    # Update last-updated timestamp
    html = re.sub(
        r"(Last Updated:\s*)<[^>]*>[^<]*<",
        f'\\1<span style="color:#00e5ff">{today} (Auto)</span><',
        html,
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[{today}] index.html updated successfully!")
    print(f"  - Trending videos: {len(trending)}")
    print(f"  - AI education videos: {len(ai_videos)}")
    print(f"  - Total views: {format_number(kpis['total_views'])}")


if __name__ == "__main__":
    print("Fetching YouTube KR trending data...")
    trending = fetch_trending_kr()
    print(f"  Got {len(trending)} trending videos")

    print("Fetching AI education videos...")
    ai_videos = fetch_ai_education()
    print(f"  Got {len(ai_videos)} AI education videos")

    kpis = compute_kpis(trending)
    update_html(trending, ai_videos, kpis)
