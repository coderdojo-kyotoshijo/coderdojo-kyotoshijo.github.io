# CoderDojo 京都四条 公式サイト

[Jekyll](https://jekyllrb.com/) で構築された CoderDojo 京都四条 の公式 Web サイトです。GitHub Pages で公開します。

---

## まず最初に見てほしいもの（Jekyll 不要）

`preview.html` をブラウザ（Chrome / Safari / Edge など）で開くと、トップページのおおよその見た目をすぐ確認できます。Jekyll や Ruby のセットアップは不要です。

> 💡 Windows / Mac いずれも、エクスプローラー or Finder から `preview.html` をダブルクリックすれば開きます。

---

## ファイル構成

```
website/
├── _config.yml             # Jekyll の基本設定（サイト名・URL・SNSリンク・会場情報など）
├── Gemfile                 # Ruby gem 一覧（GitHub Pages 互換）
├── .gitignore              # Git で無視するファイル
├── README.md               # このファイル
├── preview.html            # ★ Jekyll なしで見られるトップページのプレビュー
│
├── index.html              # トップページ（Liquid テンプレート）
├── about.md                # Dojo について
├── getting-started.md      # はじめての方へ
├── events.md               # 開催情報
├── access.md               # アクセス
│
├── _layouts/
│   ├── default.html        # 全ページ共通レイアウト（ヘッダー/フッター込み）
│   └── page.html           # 通常ページ用（中央寄せ・カード型）
├── _includes/
│   ├── header.html         # ヘッダー（ナビ）
│   └── footer.html         # フッター
├── assets/
│   ├── css/style.css       # スタイルシート
│   └── img/                # 画像置き場（顔ぼかし済み・1枚300KB以下推奨）
└── .github/workflows/
    └── jekyll.yml          # GitHub Actions による自動デプロイ設定
```

---

## デザインの考え方

- **色：** 紺 `#1F3A5F`（信頼感）＋ 暖色オレンジ `#F39A4B`（あたたかさ）＋ クリーム背景 `#FAFAF7`
- **フォント：** ヒラギノ／游ゴシック／メイリオを優先（OS 標準・読みやすい）
- **モバイルファースト：** スマホで申込みボタンが押しやすい配置を優先
- **アクセシビリティ：** ナビゲーションは `aria-label` 付き、コントラスト比は AA 以上を目安

---

## デプロイ手順（GitHub Pages）

### 1. GitHub にリポジトリを作る

1. GitHub にログイン
2. 新しい organization `coderdojo-kyoto-shijo` を作る（推奨）
3. その下に Public リポジトリを作る。リポジトリ名は **`coderdojo-kyoto-shijo.github.io`** にすると `https://coderdojo-kyoto-shijo.github.io/` でそのまま公開されます

### 2. このフォルダの中身をプッシュ

```bash
cd "CoderDojo 京都四条 運営/website"
git init
git branch -M main
git add .
git commit -m "Initial commit: site prototype"
git remote add origin git@github.com:coderdojo-kyoto-shijo/coderdojo-kyoto-shijo.github.io.git
git push -u origin main
```

### 3. GitHub Pages を有効化

リポジトリの `Settings` → `Pages` で:

- **Source**: `GitHub Actions` を選択（このリポジトリ内 `.github/workflows/jekyll.yml` が自動実行されます）

数分待つと `https://coderdojo-kyoto-shijo.github.io/` で公開されます。

> 🔁 以降は `main` に push するたびに自動でデプロイされます。

---

## ローカルで Jekyll を動かす（任意）

GitHub に push する前にローカルで確認したい場合のみ必要です。

### Mac

```bash
# 1. Ruby（system付属でOK、または rbenv 等で 3.2 系を入れる）
# 2. bundler
gem install bundler --user-install

# 3. このフォルダで
bundle install
bundle exec jekyll serve
```

ブラウザで http://localhost:4000 を開く。

### Windows

[RubyInstaller](https://rubyinstaller.org/) で Ruby+Devkit (3.2.x x64) をインストール → 同じ手順。

> 💡 ローカルセットアップが面倒なら、`preview.html` を直接開く方法でもトップページの見た目は確認できます。

---

## 更新の仕方（運営者向け）

普段の更新は、**GitHub の Web エディタ** だけで完結できます（ローカル環境不要）。

### 文章を直したい

1. リポジトリの該当ファイル（例：`about.md`）を GitHub 上で開く
2. 右上の鉛筆アイコンをクリック
3. 編集 → 下部の `Commit changes` で保存
4. 数分後に自動公開

### 写真を追加したい

1. `assets/img/` フォルダに画像をアップロード（300KB 以下推奨、[Squoosh](https://squoosh.app/) で圧縮）
2. Markdown 内で `![説明](/assets/img/ファイル名.jpg)` のように埋め込む

### 次回開催を更新したい

`index.html` の「次回開催」セクション（`<div class="next-event">` 周辺）の日付・回数・受付状況を書き換える。
`events.md` の表にも 1 行追加する。

> 🤖 AIパートナーに「Webサイトの次回開催を◯月◯日の第◯回に更新して」と依頼すれば、差分のテキストを返します。

---

## 5/31 開催当日に向けたチェックリスト

- [ ] `_config.yml` の `links.x` / `links.facebook` をアカウント開設後の正しい URL に差し替え
- [ ] `index.html` の「次回開催」の日付・回数を最新の開催に合わせる
- [ ] `assets/img/` に活動写真を 2〜3 枚（顔ぼかし済み）配置
- [ ] GitHub にプッシュ、GitHub Pages の公開を確認
- [ ] 公開 URL の QR コードを生成（[qr.quel.jp](https://qr.quel.jp/) など）
- [ ] QR コードを A5 で印刷して当日受付に掲示

---

## ライセンス

サイトコンテンツの著作権は CoderDojo 京都四条 に帰属します。
「CoderDojo」「コーダー道場」は CoderDojo Foundation の登録商標です。
