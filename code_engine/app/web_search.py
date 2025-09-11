from duckduckgo_search import DDGS

def search_web(query: str, max_results: int = 5) -> list:
    """
    Search the web for financial news and analyst reports using DuckDuckGo.
    """
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=max_results))
    return results
