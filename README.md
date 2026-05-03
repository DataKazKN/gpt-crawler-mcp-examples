# GPT Crawler MCP — Examples

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-97D700?logo=apify&logoColor=000)](https://apify.com/kazkn/gpt-crawler-mcp)
[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](LICENSE)
[![Built on BuilderIO/gpt-crawler](https://img.shields.io/badge/Built%20on-BuilderIO%2Fgpt--crawler-orange)](https://github.com/BuilderIO/gpt-crawler)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#-contributing)
[![Apify users](https://img.shields.io/badge/Try-free%20tier-blue)](https://apify.com/kazkn/gpt-crawler-mcp)

Working code examples for [**GPT Crawler MCP**](https://apify.com/kazkn/gpt-crawler-mcp) — the hosted web-crawler that turns any website into a clean knowledge file for ChatGPT custom GPTs, Claude Projects, and RAG pipelines. **No `pip install`, no Playwright debugging at 11 pm.**

> 👋 New here? Skip to [⚡ Quick start](#-quick-start) — you can have a knowledge file in your hands in 90 seconds.

---

## 🎯 Key features

- **Zero setup.** Run from the Apify Console, the API, n8n, Zapier, Make, or your terminal. No local Chromium, no Node version dance, no environment hell.
- **Pay only for what you crawl.** $0.001/page in batch mode (PPE — Pay Per Event). $0.05 flat per call in MCP mode. **No subscription**, no monthly fee. Apify free tier covers ~100 pages/month.
- **MCP server mode for AI agents.** Drop the URL into Claude Desktop, Cursor, Windsurf, or any MCP-compatible client and let your assistant call `crawl_to_knowledge` live, mid-conversation. No pre-indexing required.
- **Battle-tested crawl logic.** Built on [BuilderIO/gpt-crawler](https://github.com/BuilderIO/gpt-crawler) (19k+ ★, ISC). Handles dynamic content, sitemaps, link selectors, body selectors, and exclusion rules out of the box.
- **Apify infrastructure under the hood.** Auto retries, automatic proxy rotation, full run logs, dataset persistence. Production-grade reliability without managing a single server.

---

## ⚡ Quick start

### Option A — One-click in the Apify Console (recommended for first time)

1. Go to [apify.com/kazkn/gpt-crawler-mcp](https://apify.com/kazkn/gpt-crawler-mcp).
2. Click **Try for free** (no credit card on the free tier).
3. The form is prefilled to crawl Apify docs as a demo. Hit **Save & Start**.
4. Wait ~30–60 s. Open the run's **Storage → Key-value store** tab and download `output.json`.
5. Drop the JSON into your custom GPT → **Knowledge** slot. Done.

### Option B — From the command line

```bash
curl -X POST "https://api.apify.com/v2/acts/kazkn~gpt-crawler-mcp/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://docs.your-product.com"],
    "match": "https://docs.your-product.com/**",
    "maxPagesToCrawl": 50,
    "outputFormat": "json"
  }' > knowledge.json
```

You now have a 50-page knowledge file in `knowledge.json`. Total cost: **$0.05** at $0.001/page.

---

## 📦 Installation / setup

You don't install anything — this is a **hosted Actor**. The only thing you need is an Apify token, free at [apify.com/sign-up](https://apify.com/sign-up).

| Step | What |
|---|---|
| 1. Sign up | [apify.com/sign-up](https://apify.com/sign-up) — 30 s, no credit card. |
| 2. Get your token | Apify Console → **Settings** → **Integrations** → **Personal API token**. |
| 3. (optional) Install a client | [`apify-client`](https://docs.apify.com/api/client/js) for Node.js or [`apify-client`](https://docs.apify.com/api/client/python) for Python. The cURL approach has zero dependencies. |

---

## 💡 Usage examples

### 1. cURL — synchronous run (blocking, returns the dataset directly)

```bash
curl -X POST "https://api.apify.com/v2/acts/kazkn~gpt-crawler-mcp/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://docs.anthropic.com"],
    "match": "https://docs.anthropic.com/**",
    "maxPagesToCrawl": 30,
    "outputFormat": "markdown"
  }' > anthropic-docs.md
```

**When to use:** quick one-off crawls, scripting, CI pipelines. Synchronous mode blocks until the run finishes (typically 30 s – 3 min).

### 2. Python — official `apify-client` SDK

```python
from apify_client import ApifyClient

client = ApifyClient(token="YOUR_APIFY_TOKEN")

run = client.actor("kazkn/gpt-crawler-mcp").call(
    run_input={
        "urls": ["https://nextjs.org/docs"],
        "match": "https://nextjs.org/docs/**",
        "maxPagesToCrawl": 100,
        "outputFormat": "json",
    }
)

# Iterate results from the default dataset
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["url"], "→", item["tokens"], "tokens")
```

**When to use:** RAG pipelines (LangChain, LlamaIndex), automated weekly re-crawls, Python-native data flows.

### 3. Node.js — official `apify-client` SDK

```javascript
import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor("kazkn/gpt-crawler-mcp").call({
  urls: ["https://docs.stripe.com/api"],
  match: "https://docs.stripe.com/api/**",
  maxPagesToCrawl: 200,
  outputFormat: "json",
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(`Crawled ${items.length} pages`);
```

**When to use:** Next.js apps, Express servers, server-side AI agents that need fresh context on demand.

### 4. Claude Desktop — MCP server mode (live tool calls)

Drop this into `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or the equivalent on Windows/Linux:

```json
{
  "mcpServers": {
    "gpt-crawler": {
      "type": "url",
      "url": "https://kazkn--gpt-crawler-mcp.apify.actor/mcp?token=YOUR_APIFY_TOKEN",
      "timeout": 180000
    }
  }
}
```

Restart Claude Desktop. Now ask it:

> *"Use gpt-crawler to crawl `https://docs.stripe.com/api/customers`, max 5 pages, return as JSON."*

You'll see a JSON knowledge file with 5 page entries within ~30 seconds.

> ⚠️ **Set `timeout: 180000`** (180 s). The default MCP client timeout is 30 s, which is shorter than most crawls. Skipping this will give you "interrupted connection" errors.

### 5. n8n — workflow integration (no code)

In n8n, drag in the **Apify** node, choose action **Run an Actor**, pick `kazkn/gpt-crawler-mcp`, and wire your input:

```json
{
  "urls": ["{{ $json.docs_url }}"],
  "match": "{{ $json.match_pattern }}",
  "maxPagesToCrawl": 50,
  "outputFormat": "markdown"
}
```

Pipe the output to your downstream node (Pinecone embedder, Notion writer, OpenAI custom GPT updater, etc.).

**When to use:** non-developer workflows, scheduled re-crawls, multi-tool integrations.

---

## 🛠 Use cases

### 📚 Build a Custom GPT for your product docs

Crawl `docs.your-product.com`, drop the JSON file into ChatGPT → **Create a GPT** → **Knowledge**. Your GPT now answers support questions in your product's voice, cites exact URLs, and stops hallucinating about features that don't exist.

### 🚨 Beat the Claude Project knowledge limit

Hitting `"knowledge exceeds maximum, remove some to continue"`? Set `outputFormat: "markdown"`, get one consolidated `.md` file, upload that single file to your Project knowledge. Token-equivalent to 20+ raw HTML pages, fits comfortably under the file-count cap.

### 🧠 Bootstrap a RAG pipeline (LangChain / LlamaIndex / pgvector)

Crawl 200 pages of technical content, get a clean JSON, embed each `text` field with OpenAI / Cohere / Voyage embeddings, store in Pinecone or pgvector. The output is already chunk-friendly with `tokens` field included, no manual chunking required.

### 🤖 Live MCP tool for AI agents

Switch to MCP standby mode. Your support agent (Claude Desktop, Cursor, Windsurf) calls `crawl_to_knowledge` whenever the user asks about a topic that isn't already in the cache. **Always-fresh context, zero pre-indexing.**

### 🛒 Competitive intelligence for B2B SaaS

Schedule a weekly crawl of your top 3 competitors' marketing sites. Diff the resulting knowledge files to detect new features, pricing changes, or messaging pivots before they hit your Slack.

---

## ⚙️ Configuration options

The full input schema is documented on the [Apify Store page](https://apify.com/kazkn/gpt-crawler-mcp/input-schema). The most-used fields:

| Field | Type | Default | Description |
|---|---|---|---|
| `urls` | `string[]` | — *(required)* | Start URLs. Sitemap `.xml` URLs are auto-detected. |
| `match` | `string` | `**` | Glob pattern controlling which links to follow. Use `https://yoursite.com/**` to scope to one domain. |
| `selector` | `string` | `body` | CSS or XPath selector for content extraction. Override only if you want to drop nav / sidebar / footer (e.g. `main`, `article`, `.docs-content`). |
| `maxPagesToCrawl` | `integer` | `10` | Hard cap on pages crawled. **Also caps your cost.** |
| `outputFormat` | `enum` | `json` | `json` (default) / `markdown` (best for ChatGPT/Claude) / `txt` (lightweight). |
| `outputFileName` | `string` | `output.json` | Name of the combined knowledge file. |
| `headless` | `boolean` | `true` | Run Chromium headless. Disable only for local debugging. |
| `waitForSelectorTimeout` | `integer` | `1000` | ms to wait for the content selector. Bump to `3000` on JS-heavy sites. |
| `cookie` | `string` *(secret)* | — | Optional `name=value` cookie for sites behind a cookie wall or auth. Stored encrypted. |
| `maxTokens` | `integer` | `0` | Optional cap on tokens per output file. `0` = no limit. **Set to 100,000 to fit ChatGPT's 512 KB ceiling.** |
| `mcpMode` | `boolean` | `false` | Enable MCP server (Standby) mode. Apify Standby auto-enables this. |

**Cost reference** (batch mode, `$0.001/page`):

| `maxPagesToCrawl` | Wall time | Cost |
|---|---|---|
| `10` | ~30 s | ~$0.01 |
| `100` | ~3 min | ~$0.10 |
| `500` | ~10 min | ~$0.50 |
| `1000` (max) | ~20 min | ~$1.00 |

---

## ❓ Common questions / troubleshooting

### Why is my output empty?

Three usual suspects (in order of likelihood):

1. **`match` pattern too narrow.** If your start URL is `https://docs.foo.com/intro` and `match` is `https://docs.foo.com/intro/**`, you'll only crawl the start page. Widen to `https://docs.foo.com/**`.
2. **JS hydration too slow.** On React/Vue/Next.js sites, content may not be in the DOM at the default 1 s wait. Bump `waitForSelectorTimeout` to `3000`.
3. **Selector too specific.** The default `body` works for 95 % of sites. If you set `selector` to `.markdown-body` and the site uses `.docs-content`, you'll get empty pages. Revert to `body` and check.

### Why does my custom GPT fail to upload the JSON?

ChatGPT custom GPTs accept a **maximum of 20 files at 512 KB each**. If your JSON is over 512 KB, ChatGPT silently refuses with a vague error. Fix:

- Set `maxTokens: 100000` to auto-truncate the crawl to fit under 512 KB.
- For larger sites, split into 3–5 thematic crawls (e.g. one per docs section) and upload each as a separate knowledge file.

### Why am I getting `Invalid or expired MCP authentication` in Claude Desktop?

The default MCP client timeout is **30 s**, shorter than most crawls. Add `"timeout": 180000` (180 s) to your `claude_desktop_config.json` server entry. Same fix applies to Cursor (`requestTimeoutMs: 180000` in MCP settings) and Windsurf.

### How do I crawl a site behind a login?

Pass a cookie via the `cookie` input field in `name=value` format (e.g. `session=abc123`). It's stored encrypted (`isSecret: true`) and never appears in logs. For multi-step OAuth, [open an issue](https://github.com/DataKazKN/gpt-crawler-mcp/issues) — we'll add it.

### Does it respect `robots.txt`?

By default, yes. The underlying `BuilderIO/gpt-crawler` honors robots.txt. **You are responsible for what you crawl.** For competitive/copyrighted content, don't. For your own docs, your customer's docs (with permission), or public technical documentation that explicitly invites indexing — go for it.

### What's the difference between batch mode and MCP mode?

- **Batch mode** (default): you specify URLs once, get a file. Best for *building a static knowledge base* you upload to a custom GPT or RAG store. Cost: $0.001/page.
- **MCP mode**: an AI agent calls the crawler *live, mid-conversation*. Best for *agentic workflows* where the URL to crawl isn't known ahead of time. Cost: $0.05 flat per tool call, regardless of page count.

---

## 🔗 Links

- 🛒 **Apify Store actor:** [apify.com/kazkn/gpt-crawler-mcp](https://apify.com/kazkn/gpt-crawler-mcp)
- 📦 **Source code (ISC):** [github.com/DataKazKN/gpt-crawler-mcp](https://github.com/DataKazKN/gpt-crawler-mcp)
- 🏗️ **Built on:** [BuilderIO/gpt-crawler](https://github.com/BuilderIO/gpt-crawler) — credit to the upstream maintainers.
- 📖 **Apify docs:** [docs.apify.com](https://docs.apify.com/)
- 🤖 **MCP spec:** [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- ⚡ **Apify Standby docs:** [docs.apify.com/platform/actors/running/standby](https://docs.apify.com/platform/actors/running/standby)
- 🐛 **Issues / feature requests:** [GitHub Issues](https://github.com/DataKazKN/gpt-crawler-mcp/issues) (fastest reply)
- 💬 **Apify Console issues:** [Issues tab on the Actor page](https://console.apify.com/actors/4UAPrwZb1XOlkCJKK/issues)

---

## 🤝 Contributing

PRs welcome. The fastest way to add value:

1. **Add a new example** in your favorite language or framework — Ruby, Go, PHP, Bash, Make, anything. Drop a snippet in this README under [💡 Usage examples](#-usage-examples) with a short *"When to use"* note.
2. **Add an integration recipe** — Notion sync, Pinecone embedder, weekly Slack diff, custom GPT auto-updater, etc.
3. **Improve a use case** — got a real-world scenario the README misses? Open a PR with the recipe.
4. **File a bug** — runtime error, weird output, MCP client incompatibility — [open an issue](https://github.com/DataKazKN/gpt-crawler-mcp/issues) with your run ID. Server logs always tell the truth.

Style notes for PRs:

- One example per PR is fine.
- Code blocks have a language tag for syntax highlighting (` ```python `, ` ```bash `, etc.).
- Prefer real, runnable code over pseudo-code.
- Add a one-sentence *"When to use"* line so readers can scan.

---

## 📜 License

ISC — same as the upstream [BuilderIO/gpt-crawler](https://github.com/BuilderIO/gpt-crawler). Free for personal and commercial use. No attribution required, but appreciated.

---

**Maintained by [@DataKazKN](https://apify.com/kazkn) · Switzerland-based indie dev · ⭐ Star the repo if it saved you an evening.**
