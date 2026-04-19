# 📺 YouTube × Gemini Analytics Pipeline

> **한국 YouTube 트렌딩 실시간 분석 + Gemini 2.5 Flash AI 인사이트 추출 대시보드**
> Real-time Korean YouTube trending analytics with Gemini 2.5 Flash AI insights

[![Live Dashboard](https://img.shields.io/badge/Live-Dashboard-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://dongsoojung.github.io/youtube-gemini-pipeline/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)
[![YouTube API](https://img.shields.io/badge/API-YouTube%20Data%20v3-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://developers.google.com/youtube/v3)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

---

## 🎯 Problem

한국 YouTube 트렌딩은 **국내 콘텐츠 시장의 초단위 선행지표**입니다. 하지만:

- 트렌딩 페이지는 **스냅샷만** 보여줄 뿐, 카테고리·조회수·참여율 분포를 분석하지 못함
- 크리에이터·마케터·투자자가 **"왜 이 영상이 뜨는가"** 를 알려면 수십 개 영상을 수동 분석해야 함
- 단순 통계만으로는 **"다음에 뜰 콘텐츠"** 예측 어려움

## 💡 Solution

**2단 파이프라인**으로 데이터 수집부터 AI 인사이트 추출까지 자동화:

```
┌─────────────────┐       ┌──────────────────┐       ┌─────────────────┐
│  YouTube API v3 │  ───► │  정량 분석 계층  │  ───► │  Gemini 2.5 AI  │
│  트렌딩 데이터  │       │  (카테고리/참여) │       │  정성 인사이트  │
└─────────────────┘       └──────────────────┘       └─────────────────┘
   상위 50개 영상           차트·분포·TOP 5            "왜 뜨는가" 설명
```

## 📊 Dashboard Sections

| 섹션 | 내용 | 시각화 |
|------|------|--------|
| **🔄 파이프라인 아키텍처** | 2단계 데이터 흐름 시각화 | Active step indicator |
| **📊 카테고리별 조회수 분포** | 음악/교육/엔터 등 카테고리 통계 | Bar chart |
| **🎬 참여율(Engagement) TOP 5** | (좋아요+댓글)/조회수 비율 상위 | Ranked table |
| **🤖 Gemini AI 인사이트 패널** | 트렌드 데이터 → 프롬프트 → AI 해석 | Interactive chat UI |

## 🛠 Tech Stack

- **Data Collection**: YouTube Data API v3 (`mostPopular` endpoint, `regionCode=KR`)
- **AI Analysis**: Google Gemini 2.5 Flash (저지연·저비용 모델)
- **Visualization**: Vanilla JS + Chart.js (외부 프레임워크 없음)
- **Hosting**: GitHub Pages (정적 배포)
- **Design**: 다크 그라데이션 `#1a1a2e → #0f3460`, 민트 액센트 `#4ecca3`

## 🎨 AI Prompt Patterns (프리셋)

대시보드에는 4가지 프리셋 프롬프트가 탑재되어 있어, 데이터 컨텍스트와 함께 Gemini에 전송됩니다:

1. **Trend Summary** — "지금 뜨는 카테고리 3개와 공통 패턴은?"
2. **Engagement Deep-dive** — "참여율 상위 5개 영상의 성공 요인은?"
3. **Content Gap Analysis** — "트렌딩에 부족한 카테고리로 기회는?"
4. **Creator Strategy** — "내 채널이 트렌드에 올라타려면?"

## 🚀 Quick Start

```bash
# 1. 리포 클론
git clone https://github.com/DongsooJung/youtube-gemini-pipeline.git
cd youtube-gemini-pipeline

# 2. API 키 준비
#    - YouTube Data API v3 키: https://console.cloud.google.com/apis/library/youtube.googleapis.com
#    - Gemini API 키: https://ai.google.dev/

# 3. index.html 내 apiKey 변수 수정 후 브라우저에서 열기
#    (또는 정적 서버)
python -m http.server 8000
```

## 📅 Roadmap

- [x] v1.0: YouTube 트렌딩 + 기본 차트
- [x] v2.0: Gemini 2.5 Flash AI 통합 (2026-04-05)
- [ ] v2.1: 카테고리 필터 + 시간대별 비교
- [ ] v2.2: 키워드 워드클라우드 (형태소 분석)
- [ ] v3.0: 일간 리포트 자동 생성 (Supabase + cron)
- [ ] v3.1: 한국 Shorts 전용 탭 (Reels/TikTok 대비 분석)

## 🎓 Author

**정동수 (Dongsoo Jung)** — Stargate Corporation CEO
- AI × 데이터 × 콘텐츠 분석
- SNU 스마트도시공학 박사 수료 · 공간계량 연구자
- [GitHub](https://github.com/DongsooJung) · [Portfolio](https://dongsoojung.github.io) · [Company](https://stargate11.com)

## 📄 License

MIT License.

---

> *"Data without context is noise. Context without AI is manual labor. This pipeline is the bridge."*
