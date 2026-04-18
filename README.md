# 📊 YouTube × Gemini Analytics Pipeline v2.0

> **실시간 한국 YouTube 트렌딩 분석 + Gemini 2.5 Flash AI 인사이트 엔진**
>
> YouTube Data API에서 한국 트렌딩 영상을 자동 수집하고, Gemini 2.5 Flash를 호출해 카테고리별·참여율별 인사이트를 생성하는 분석 파이프라인.

[![AI](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)
[![YouTube](https://img.shields.io/badge/Data-YouTube%20Data%20API-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://developers.google.com/youtube/v3)
[![Deploy](https://img.shields.io/badge/Deploy-GitHub%20Pages-181717?style=flat-square&logo=github&logoColor=white)](https://dongsoojung.github.io/youtube-gemini-pipeline/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 🎯 Problem

한국 YouTube 트렌드는 분 단위로 변화하지만, **어떤 콘텐츠가 어떤 참여율을 만들고 있는지**를 구조화된 데이터로 파악하기는 어렵습니다. 단순 조회수 랭킹만으로는 **카테고리별 포지셔닝·참여 품질·시청자 반응**을 읽을 수 없습니다.

## ✨ Solution

이 파이프라인은 **수집 → 가공 → 생성형 분석 → 시각화** 4단계를 자동화합니다.

```
YouTube Data API v3 → 한국 트렌딩 영상 수집
    ↓
참여율(좋아요/댓글/조회수) 계산 · 카테고리 집계
    ↓
Gemini 2.5 Flash → 카테고리별 인사이트 · TOP 5 engagement 분석
    ↓
단일 HTML 대시보드 (Chart.js + 카드 레이아웃)
```

## 📊 Dashboard Panels

| 패널 | 내용 |
|------|------|
| 🔄 **파이프라인 아키텍처** | 데이터 흐름 다이어그램 (수집→분석→렌더) |
| 📊 **카테고리별 조회수 분포** | 엔터테인먼트·게임·음악·뉴스·스포츠 등 도넛/바 차트 |
| 💬 **참여율(Engagement) TOP 5** | 좋아요+댓글 대비 조회수 비율이 높은 상위 5개 |
| 🤖 **Gemini 인사이트** | 트렌드 요약 · 시청자 반응 패턴 · 카테고리 포지셔닝 |

## 🛠 Tech Stack

- **데이터 수집**: YouTube Data API v3 (`videos.list` - chart=mostPopular, regionCode=KR)
- **AI 분석**: Gemini 2.5 Flash (빠른 응답 + 한국어 강화)
- **시각화**: Chart.js 4.x CDN (도넛·바·시계열)
- **프론트**: Vanilla HTML + CSS (단일 파일, 22KB)
- **호스팅**: GitHub Pages

## 🚀 Live Demo

**▶ https://dongsoojung.github.io/youtube-gemini-pipeline/**

## 📂 Structure

```
youtube-gemini-pipeline/
└── index.html    # 단일 페이지 대시보드 + 인라인 인사이트
```

## 🌏 Scope

- **지역**: 한국 (KR) 트렌딩 전용
- **갱신 주기**: 온디맨드 (수동 재생성) — 향후 GitHub Actions cron 전환 계획
- **데이터 스냅샷**: 2026.04.05 KST

## 📄 License

MIT © 2026 Dongsoo Jung / Stargate Corporation

---

<p align="center">
  <sub>Built with <a href="https://ai.google.dev/">Gemini 2.5 Flash</a> · Part of <a href="https://stargate11.com">Stargate Corp</a> AI experiment portfolio</sub>
</p>
