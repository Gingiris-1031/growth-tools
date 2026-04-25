---
layout: post
title: "GitHub Trendingに載る方法：AFFiNEが5ヶ月で28回登場した戦略（2026年版）"
date: 2026-04-07
lang: ja
canonical_url: https://gingiris.github.io/growth-tools/blog/2026/04/07/github-trending-guide-ja/
description: "AFFiNEのCOOが公開。5ヶ月でGitHub Trendingに28回登場した実際の戦略。スター獲得からREADME最適化まで完全解説。"
categories: [github, opensource, japanese]
tags: [GitHub, Trending, オープンソース, スター]
hreflang_en: https://gingiris.github.io/growth-tools/en/
---

2022年の火曜日の朝、午前5時。上海のオフィスで私はひとりMacBookを開いていた。

AFFiNEのリポジトリを開き、GitHub Trendingのページを更新した瞬間——「AFFiNE」という文字が画面に現れた。初めてTrendingに載った朝だ。（正直、寝不足のせいで幻覚かと思った）

その週末、スターは一気に2,000以上増えた。「GitHub Trendingってこういうことか」と、そこで初めて本当に理解した。

---

## GitHub Trendingとは何か、なぜ重要なのか

GitHub Trendingは、過去24時間・1週間・1ヶ月の間に最もスターを集めたリポジトリを言語別・全言語でランキング表示するページだ。

エンジニアが「今注目されているものは何か」を確認する定番の場所であり——ここに載ると、開発者コミュニティ全体への自然な露出が得られる。広告費ゼロで。

---

## AFFiNEのKey Stats

| 指標 | 数値 |
|------|------|
| GitHubスター総数 | **60,000+** |
| GitHub Trending登場回数 | **28回**（最初の5ヶ月で） |
| Product Hunt #1獲得 | **30回** |
| 最大単日スター増加 | **3,200+** |

これらの数字は偶然ではなく、再現可能な戦術の結果だ。

---

## GitHub Trendingのアルゴリズムを理解する

まず仕組みを知らなければ戦えない。

Trendingは「総スター数」ではなく**「一定期間のスター獲得速度」**で決まる。つまり、10万スターのプロジェクトも、今日スターをほとんど集めていなければTrendingには載らない。

逆に言えば——新規プロジェクトでも、集中的に注目を集めればランクインできる。（これがAFFiNEが初期から狙えた理由だ）

**3つの重要なタイミング**
- 24時間トレンド：最も競争が激しいが最大露出
- 週間トレンド：持続的なスター流入で載れる
- 月間トレンド：大型リリースと連動させると効果的

---

## 戦術1：「Trending点火」のタイミングを作る

最初のスパイクは人工的に作っても構わない。

**具体的な方法：**
- Hacker News Show HNに投稿する（月曜〜火曜の朝9時UTC前後が最適）
- Redditの関連サブレディットに同日投稿する（r/programming, r/selfhostedなど）
- TwitterとLinkedInで同時に告知する

重要なのは**分散させないこと**。同じ日の同じ数時間に集中させる——これが「点火」の原理だ。

AFFiNEで実際に使った手順：前日にDMで告知 → 当日朝6時JSTにHN投稿 → 9時に全SNS展開 → その日だけで1,000スター超。

---

## 戦術2：READMEを「Trending映え」させる

GitHub Trendingに載ると、知らない人が初めてリポジトリを訪れる。その人を5秒で引き止めるREADMEが必要だ。

**Trending映えREADMEの3要素：**

1. **視覚的インパクト** — ヒーロー画像またはGIFを最上部に置く。スクリーンショット一枚で「何ができるか」が伝わること
2. **即座の価値提示** — "What is this?"を最初の1〜2文で答える。技術的説明は後回し
3. **スター誘導** — バッジ表示、Star Historyチャート、「⭐ Star to support」の一言

（AFFiNEのREADMEは3回作り直した。最初のバージョンは技術者向けすぎて一般エンジニアに刺さらなかった）

---

## 戦術3：コミュニティ資産を先に作る

Trendingは「爆発」のトリガーにすぎない——その後の流入を受け止めるコミュニティが必要だ。

**最低限用意すべきもの：**
- Discordサーバー（Trending当日に招待リンクをREADMEに追加）
- Issueテンプレート（新規訪問者が貢献しやすいフォーマット）
- CONTRIBUTING.mdと「good first issue」タグ

Trendingに載った後、Discordの参加者が数百人増えた経験が何度もある。彼らが次のTrendingの担い手になる。

---

## 戦術4：連続登場のサイクルを作る

1回載るだけでは足りない——28回載るには「サイクル」が必要だ。

**月1回のTrendingサイクル：**
- 月初：大型機能リリースに合わせた告知
- 月中：ブログ記事またはケーススタディの公開
- 月末：マイルストーン達成報告（「⭐ 10K Stars達成！」など）

各イベントで小さなスパイクを作る。週間・月間Trendingは累積スターで載れるため、月1〜2回のスパイクで継続的にランクインできる。

---

## 戦術5：言語別Trendingを狙う

全言語Trendingは競争が激しい。だが**言語別Trendingは狙いやすい**。

TypeScriptやRustで書かれたプロジェクトなら、その言語のTrendingでの競争は全言語比で大幅に少ない——にもかかわらず、その言語コミュニティの開発者に直接リーチできる。

AFFiNEはTypeScript製。TypeScript Trendingに載るたびに、フロントエンド開発者コミュニティから新規スターが集まった。

---

## 避けるべき3つの失敗

**1. スターの購入** — Githubはこれを検知する。垢BANリスクがある上、スターを買ったリポジトリはTrendingアルゴリズムでむしろ不利になる

**2. タイミングのバラバラな告知** — 1週間かけてゆっくり告知しても速度が出ない。集中させることが命

**3. Trendingだけを目的にする** — Trendingは手段だ。本質は「良いプロダクトを作って、それを適切なタイミングに適切な場所で見せること」——この順序を間違えると一時的な数字にしかならない

---

## まとめ：再現可能な戦術として

GitHub Trendingは運ではない。アルゴリズムを理解し、告知を集中させ、コミュニティを育てれば——誰でも複数回ランクインできる。

2022年の上海の朝、あのTrending初登場から3年経った今も、私は同じ戦術を使ってクライアントのプロジェクトをTrendingに載せている。（成功率は上がった。寝不足は変わらない）

より詳しい戦術は [GitHub Stars完全ガイド](https://gingiris.github.io/growth-tools/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/) を参照してほしい。

---

*Iris · Gingiris主理人 · 元AFFiNE COO · オープンソース海外展開コンサルタント*
