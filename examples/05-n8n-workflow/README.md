# 05 - n8n workflow

**When to use:** non-developer workflows, scheduled re-crawls, multi-tool integrations (Notion / Slack / Pinecone / OpenAI).

## What this workflow does

1. **Schedule trigger** fires every Monday at 09:00.
2. **Apify node** runs `kazkn/gpt-crawler-mcp` against your docs URL (env-configurable).
3. **OpenAI Embeddings node** chunks + embeds each page with `text-embedding-3-small`.
4. **Pinecone node** upserts vectors into your index.
5. **Slack node** posts a summary to `#docs-updates`: "Re-indexed N pages this week, ~$X cost".

## Setup

1. Import `workflow.json` into n8n: **Settings → Import workflow → from file**.
2. Set credentials for Apify, OpenAI, Pinecone, Slack via the node config panels.
3. Set workflow variables (Settings → Variables):
   - `DOCS_URL` — start URL
   - `MAX_PAGES` — page cap (default 100)
   - `PINECONE_INDEX` — index name
   - `SLACK_CHANNEL` — channel for digest

## Cost reference

100 pages/week × $0.001 = **$0.10/week** for the crawl. OpenAI embeddings + Pinecone are extra (typically $0.05/week for a 100-page docs site).
