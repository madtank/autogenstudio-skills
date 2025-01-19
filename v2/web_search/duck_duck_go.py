from duckduckgo_search import DDGS

def search_duckduckgo(query, region='wt-wt', safesearch='off', max_results=5):
    """Search DuckDuckGo for the given query and return the results."""
    ddg = DDGS()
    results = ddg.text(keywords=query, region=region, safesearch=safesearch, max_results=max_results)
    
    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['href']}")
        print(f"Snippet: {result['body']}\n")
    
    return results

# Test the function
if __name__ == "__main__":
    query = "Web scraping with Python"
    search_duckduckgo(query)

# Example usage for autogen agent
# Create a new Python script (e.g., execute_search.py) and import the function:
# from skills import search_duckduckgo  
# query = "autogenstudio"  
# search_duckduckgo(query)