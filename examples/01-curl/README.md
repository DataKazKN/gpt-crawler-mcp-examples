# 01 - cURL synchronous run

**When to use:** quick one-off crawls, scripting, CI pipelines, "I just want a JSON file" use cases.

## Setup

```bash
export APIFY_TOKEN="your_token_here"  # Get from console.apify.com → Settings → Integrations
```

## Run

```bash
./run.sh
```

The output lands in `knowledge.json`. Drop into ChatGPT custom GPT → Knowledge.
