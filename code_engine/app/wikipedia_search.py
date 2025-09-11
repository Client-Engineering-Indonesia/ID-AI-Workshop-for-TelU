import wikipedia

def search_wikipedia(query: str, sentences: int = 3) -> dict:
    """
    Retrieve definition or background info from Wikipedia.
    """
    try:
        summary = wikipedia.summary(query, sentences=sentences)
        page = wikipedia.page(query)
        return {
            "query": query,
            "summary": summary,
            "url": page.url
        }
    except Exception as e:
        return {"error": str(e)}
