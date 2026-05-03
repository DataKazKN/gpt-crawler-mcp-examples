// app/api/crawl/route.ts — Next.js App Router
import { ApifyClient } from "apify-client";
import { NextRequest, NextResponse } from "next/server";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN! });

export const maxDuration = 300; // Vercel: extend timeout to 5 min for slow crawls

export async function POST(req: NextRequest) {
  const { url, maxPages = 30 } = await req.json();
  if (!url) return NextResponse.json({ error: "url required" }, { status: 400 });

  const match = url.replace(/\/$/, "") + "/**";
  const run = await client.actor("kazkn/gpt-crawler-mcp").call({
    urls: [url],
    match,
    maxPagesToCrawl: maxPages,
    outputFormat: "json",
  });

  const { items } = await client.dataset(run.defaultDatasetId).listItems();
  return NextResponse.json({
    pageCount: items.length,
    items: items.map((it: any) => ({
      url: it.url,
      title: it.title,
      text: it.text,
      tokens: it.tokens,
    })),
  });
}
