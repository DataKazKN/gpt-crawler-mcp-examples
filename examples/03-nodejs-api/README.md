# 03 - Next.js API route wrapper

**When to use:** server-side AI agents that need fresh context on demand, Next.js apps, Express servers, internal tools.

## Setup

```bash
npm install apify-client
# .env.local
APIFY_TOKEN=your_token
```

## Use

Drop `route.ts` into `app/api/crawl/route.ts` (Next.js App Router). Then:

```bash
curl -X POST http://localhost:3000/api/crawl \
  -H "Content-Type: application/json" \
  -d '{"url":"https://docs.stripe.com/api","maxPages":50}'
```

Returns a JSON array of `{url, title, text, tokens}` ready for embedding or LLM context.
