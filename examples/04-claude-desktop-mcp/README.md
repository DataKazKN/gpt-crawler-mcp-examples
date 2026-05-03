# 04 - Claude Desktop MCP config

**When to use:** you want Claude Desktop to crawl websites *live, mid-conversation*, with no pre-indexing. Best for fast-moving docs (LangChain, OpenAI API, anything that ships weekly).

## Setup (3 steps)

1. Get your Apify token at [console.apify.com](https://console.apify.com) → Settings → Integrations.

2. Open Claude Desktop config:

   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux:** `~/.config/Claude/claude_desktop_config.json`

3. Merge the snippet from `claude_desktop_config.json` (in this directory) into your existing config.

   Replace `YOUR_APIFY_TOKEN` with your real token.

4. **Restart Claude Desktop.** The `gpt-crawler` server should appear in the MCP servers list.

## Use it

Ask Claude:

> *"Use gpt-crawler to crawl `https://docs.stripe.com/api/customers`, max 5 pages, return as JSON."*

You'll see a JSON knowledge file with 5 page entries within ~30 seconds.

## ⚠️ Critical: timeout

The default MCP client timeout is **30 s**, shorter than most crawls. The config in this example sets `timeout: 180000` (180 s). Without it you'll see "interrupted connection" errors.

## Compatibility

| Client | Default | Recommended | How to configure |
|---|---|---|---|
| Claude Desktop | 30 s | 180 s | `"timeout": 180000` (this example) |
| Cursor IDE | 30 s | 180 s | Settings → MCP → Request timeout (ms) → `180000` |
| Windsurf | 60 s | 180 s | MCP config → `requestTimeoutMs: 180000` |
| Continue.dev | 30 s | 180 s | `requestTimeoutMs: 180000` in MCP config |
