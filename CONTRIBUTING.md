# Contributing

PRs welcome. The fastest way to add value:

1. **Add a new example** in your favorite language or framework — Ruby, Go, PHP, Bash, Make, anything. Drop a runnable project under `examples/<NN>-<name>/` with its own `README.md` explaining setup + run.
2. **Add an integration recipe** — Notion sync, Pinecone embedder, weekly Slack diff, custom GPT auto-updater, etc.
3. **Improve a use case** — got a real-world scenario the README misses? Open a PR with the recipe.
4. **File a bug** — runtime error, weird output, MCP client incompatibility — [open an issue](https://github.com/DataKazKN/gpt-crawler-mcp/issues) on the actor repo with your run ID. Server logs always tell the truth.

## PR style notes

- One example per PR is fine.
- Code blocks have a language tag for syntax highlighting (` ```python `, ` ```bash `, etc.).
- Prefer real, runnable code over pseudo-code.
- Add a one-sentence *"When to use"* line at the top of each example's README.
- Test locally before submitting (use the Apify free tier — first ~100 pages/month are free).

## Project layout

```
examples/
├── 01-curl/                # cURL synchronous run
├── 02-python-rag/          # Python + LangChain RAG bootstrap
├── 03-nodejs-api/          # Next.js API route wrapping the actor
├── 04-claude-desktop-mcp/  # Claude Desktop MCP config + walkthrough
└── 05-n8n-workflow/        # n8n exported workflow JSON
```

## Code of Conduct

Be kind. We're all here because we'd rather be writing code than fighting Playwright.
