---
layout: post
title: "GitHub Trending 등록 방법: 5개월 만에 28번 오른 비결 (2026년)"
date: 2026-04-07
lang: ko
hreflang_en: https://gingiris.tools/blog/2026/04/06/how-to-get-on-github-trending/
hreflang_ja: https://gingiris.tools/blog/2026/04/07/github-trending-guide-ja/
canonical_url: https://gingiris.tools/blog/2026/04/07/github-trending-guide-ko/
description: "AFFiNE이 5개월간 GitHub Trending에 28번 등록된 실제 전략. 점화 타이밍, README 최적화, 커뮤니티 활용법까지."
categories: [github, trending, korean]
tags: [GitHub, Trending, 오픈소스, 스타]
last_modified_at: 2026-06-03
faq:
  - q: "GitHub Trending에 오르려면 하루에 스타가 몇 개 필요한가요?"
    a: "기준은 카테고리와 경쟁 상황에 따라 다르지만, 전체 언어 Daily Trending은 보통 하루 80~150개 스타, TypeScript·Rust 같은 언어별 Trending은 30~60개 스타가 목표선입니다. Weekly Trending은 7일간 300~500개. AFFiNE은 오픈소스 출시 5일째에 하루 약 200개 스타로 전체 언어 Daily Trending에 진입했습니다. 핵심은 총량이 아니라 속도 — 24시간 안에 집중시키는 것이 알고리즘 진입의 열쇠입니다."
  - q: "GitHub Trending에 한번 오르면 얼마나 유지되나요?"
    a: "Daily Trending은 보통 1~7일, Weekly Trending은 1~4주 유지됩니다. 유지 기간은 초기 스파이크 이후에도 스타 속도를 얼마나 지속하느냐로 결정됩니다. AFFiNE이 5개월 동안 28번이나 Trending에 오를 수 있었던 이유는 하나의 거대한 스파이크가 아니라, Trending에 오를 때마다 기준선(baseline)이 높아지고 다음 스파이크를 만들어 다시 Trending에 진입시키는 사이클을 의도적으로 설계했기 때문입니다 — 월 1~2회 정도의 릴리즈 알림 패턴이 가장 안정적이었습니다."
  - q: "TypeScript Trending과 전체 언어 Trending 중 어느 것을 노려야 하나요?"
    a: "초기 프로젝트라면 무조건 언어별 Trending이 더 현실적입니다. 전체 언어 Trending은 진입 장벽이 훨씬 높고 경쟁이 치열한 반면, TypeScript·Rust·Python 같은 언어별 Trending은 상대적으로 낮은 스타 수로도 오를 수 있고, 같은 언어를 쓰는 개발자 커뮤니티에 직접 도달합니다. AFFiNE은 TypeScript로 개발되어 있어 TypeScript Trending에 오를 때마다 프론트엔드 개발자 커뮤니티에서 신규 스타가 들어왔습니다. 언어별 Trending에 먼저 오르고 baseline을 쌓은 후 전체 언어 Trending을 노리는 단계적 접근을 추천합니다."
---
2023년 1월 어느 월요일 아침, 팀원이 슬랙 메시지를 보냈다.

"지금 GitHub Trending에 우리가 있어."

상하이 오피스 전체가 일어났다. 화면을 캡처하고, 스크린샷을 찍고 — 마치 회사 최초의 사건처럼 소란스러웠다.

그게 첫 번째였다. 5개월 후 우리는 28번째 Trending 등록을 기록했다. (더 이상 소란스럽지 않았지만, 여전히 기뻤다.)

---

## Key Stats: AFFiNE GitHub 성장 지표

| 지표 | 수치 |
|------|------|
| 총 GitHub 스타 | 60,000+ |
| GitHub Trending 등장 | 28회 (5개월) |
| Product Hunt #1 달성 | 30회 |
| 오픈소스 기여자 | 300+ |
| 月 활성 사용자 | 100,000+ |

---

## GitHub Trending 알고리즘을 이해하라

먼저 명확히 할 것: GitHub Trending은 "가장 스타 많은 프로젝트" 순위가 아니다.

GitHub Trending은 **스타 증가 속도**를 기준으로 한다.

즉, 하루에 100개 스타를 받은 프로젝트가 총 스타 100만 개 프로젝트보다 Trending에 오를 수 있다.

이게 핵심이다 — 총량이 아니라 속도.

GitHub Trending 랭킹은 세 가지 기간으로 나뉜다:
- 오늘 (Daily)
- 이번 주 (Weekly)
- 이번 달 (Monthly)

각기 다른 전략이 필요하다. 우리는 대부분 "오늘" 카테고리를 목표로 했다.

---

## 스타 속도를 만드는 방법

단순히 많은 스타를 받는 게 아니라, **짧은 시간에 집중적으로** 받아야 한다.

우리가 사용한 방법들:

**방법 1: 플랫폼 동시 출시**
Product Hunt, Hacker News, Reddit을 같은 날에 출시했다. 각 플랫폼의 트래픽이 GitHub으로 집중됐다.

2023년 2월, 이 방식으로 48시간 만에 1,400개 스타를 받았다. 그 주 GitHub Trending Daily, Weekly 두 카테고리에 모두 올랐다.

**방법 2: 대형 릴리즈에 커뮤니티 알림**
새 버전이 나올 때마다 Discord(1만 2천 명), Reddit 서브레딧, 이메일 리스트에 동시 공지했다.

공지 타이밍은 항상 화요일~수요일 오전 (미국 동부 기준)이었다. 주말은 피했다.

**방법 3: 인플루언서 협업**
YouTube 개발자 채널, Twitter 테크 계정과 미리 협의해 릴리즈 당일 커버리지를 맞췄다.

(돈을 낸 게 아니었다. 미리 관계를 쌓고 독점 미리보기를 제공했다.)

---

## README를 Trending 최적화하라

GitHub Trending에 올랐을 때, 갑자기 수천 명이 처음으로 당신의 README를 보게 된다.

이 순간을 낭비하지 마라.

**Trending 트래픽을 위한 README 체크리스트:**

첫 화면에서 즉시 보여야 할 것들:
- 프로젝트가 무엇인지 한 줄로 설명
- 실제 작동하는 GIF 또는 스크린샷
- Quick Install 명령어 (복사 가능)
- 스타 수, 라이선스, 최신 버전 배지

스크롤 없이 보이는 영역에서:
- "왜 [경쟁 제품]보다 나은가" 비교표
- 실제 사용 사례 3개
- Discord/슬랙/커뮤니티 링크

AFFiNE은 Trending에 오를 때마다 README 클릭 분석을 확인했다. 가장 클릭 많은 요소는 항상 데모 GIF와 Install 명령어였다.

---

## 언어별 Trending을 활용하라

GitHub Trending에는 전체 언어 외에 특정 프로그래밍 언어별 카테고리가 있다.

TypeScript, Rust, Python 같은 언어별 Trending은 경쟁이 낮아 진입이 더 쉽다.

AFFiNE은 TypeScript로 개발됐는데, TypeScript Trending에는 총 언어 Trending보다 훨씬 적은 스타로도 올랐다.

전략:
- 당신의 주요 언어 Trending을 별도로 타겟팅하라
- 그 언어 커뮤니티 (TypeScript Weekly 뉴스레터 등)에 제출하라
- 언어별 Discord, Slack 서버에 공유하라

---

## Trending 등록 후 다음 48시간

GitHub Trending에 올랐다는 건 기회가 열린 것이다.

빠르게 해야 할 것들:

**1. 소셜 증거 활용**
"현재 GitHub Trending #3 — TypeScript" 같은 트윗을 올려라. Trending에 오른 것 자체가 신뢰 신호다.

**2. 새 이슈 신속 대응**
Trending 트래픽은 새 이슈 폭발을 동반한다. 24시간 내 모든 이슈에 응답하라 — 이때 만들어지는 인상이 기여자를 붙잡는다.

**3. 다음 릴리즈 티저**
"다음 버전에서 이런 게 나옵니다" 프리뷰를 올려 관심을 유지하라. Watch 하는 사용자들이 늘어난다.

---

## Trending은 수단이지 목적이 아니다

28번 Trending에 올랐지만 솔직히 말하면: Trending 자체보다 중요한 건 그날 유입된 사용자들이 다시 돌아왔느냐다.

우리 데이터에서 Trending 유입 사용자 중 7일 후 재방문율은 평균 12%였다. (이 숫자를 높이는 게 Trending보다 더 어렵고 더 중요하다.)

Trending을 유입 채널로 활용하되, 진짜 목표는 리텐션이다.

GitHub 스타와 Trending은 프로덕트가 좋을 때 따라오는 결과다. 그 순서를 잊지 마라.

---

<!-- gingiris-cluster-v1 -->

### 📚 Read the full series

This article is part of the **[How to Get More GitHub Stars: The Definitive Guide](/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/)** series. Other guides in the cluster:

- [GitHub Star Growth Tactics](/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/)
- [GitHub README Best Practices](/blog/2026/04/02/github-readme-template-guide/)
- [Developer Community Directory](/blog/2026/04/07/developer-community-directory-where-to-find-your-first-1000-users/)

*Find all 90+ playbooks at [gingiris.tools](https://gingiris.tools).*

