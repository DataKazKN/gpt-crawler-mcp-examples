#!/usr/bin/env bash
# Synchronous run — blocks until the crawl finishes (~30 s for 30 pages)
set -e

: "${APIFY_TOKEN:?Set APIFY_TOKEN env var first (https://console.apify.com → Settings → Integrations)}"

curl -X POST "https://api.apify.com/v2/acts/kazkn~gpt-crawler-mcp/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://docs.apify.com/platform/actors"],
    "match": "https://docs.apify.com/platform/actors/**",
    "maxPagesToCrawl": 30,
    "outputFormat": "json"
  }' | tee knowledge.json | jq '.[].url'
