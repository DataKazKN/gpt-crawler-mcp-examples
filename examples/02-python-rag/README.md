# 02 - Python + LangChain RAG bootstrap

**When to use:** building a RAG pipeline (LangChain / LlamaIndex / pgvector), automated weekly re-crawls, Python-native data flows.

## Setup

```bash
pip install -r requirements.txt
export APIFY_TOKEN="your_token"
export OPENAI_API_KEY="your_openai_key"
```

## Run

```bash
python crawl_and_embed.py https://docs.your-product.com
```

Crawls the docs site, embeds each page with OpenAI `text-embedding-3-small`, and stores in a local Chroma collection. Total cost: ~$0.10 for a 100-page docs site.
