"""Crawl any docs site → embed with OpenAI → store in Chroma."""
import os
import sys
from apify_client import ApifyClient
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


def crawl_to_docs(start_url: str, max_pages: int = 100) -> list[Document]:
    """Run the Apify actor and yield LangChain Documents."""
    client = ApifyClient(token=os.environ["APIFY_TOKEN"])
    match = start_url.rstrip("/") + "/**"
    run = client.actor("kazkn/gpt-crawler-mcp").call(run_input={
        "urls": [start_url],
        "match": match,
        "maxPagesToCrawl": max_pages,
        "outputFormat": "json",
    })
    docs = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        text = item.get("text", "").strip()
        if not text:
            continue
        docs.append(Document(
            page_content=text,
            metadata={
                "url": item["url"],
                "title": item.get("title", ""),
                "tokens": item.get("tokens", 0),
            },
        ))
    return docs


def main(start_url: str) -> None:
    print(f"→ Crawling {start_url} ...")
    docs = crawl_to_docs(start_url)
    print(f"  Got {len(docs)} pages")

    print("→ Embedding with OpenAI ...")
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory="./chroma_store",
        collection_name="docs",
    )
    print(f"  Stored {db._collection.count()} chunks in ./chroma_store")

    # Quick test
    query = "How does pricing work?"
    hits = db.similarity_search(query, k=3)
    print(f"\n→ Test query: {query!r}")
    for i, h in enumerate(hits, 1):
        print(f"  {i}. {h.metadata['title']} ({h.metadata['url']})")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python crawl_and_embed.py <start_url>")
    main(sys.argv[1])
