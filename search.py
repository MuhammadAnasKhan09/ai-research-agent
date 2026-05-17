from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to Tavily
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query, max_results=5):
    """Search the web for a given query."""
    response = tavily.search(
        query=query,
        max_results=max_results,
        search_depth="basic"
    )
    return response['results']

def multi_search(queries):
    """Search multiple queries and combine results."""
    all_results = []
    for query in queries:
        print(f"  🔎 Searching: {query}")
        results = search_web(query)
        all_results.extend(results)
    return all_results

def format_results(results):
    """Format search results into clean text for the AI."""
    formatted = ""
    for i, r in enumerate(results, 1):
        formatted += f"\nSource {i}: {r['title']}\n"
        formatted += f"URL: {r['url']}\n"
        formatted += f"Content: {r['content']}\n"
        formatted += "-" * 40 + "\n"
    return formatted