# Web Search Plugin for AutoGen Studio

This plugin enables AutoGen Studio to perform web searches, retrieving titles, URLs, and snippets of information based on user queries. It's designed to integrate seamlessly with AutoGen Studio, allowing the creation of skills that leverage web search capabilities.

## Usage

To incorporate this plugin into an AutoGen Studio skill, you will need to insert the provided Python code into your skill's scripting area. The plugin allows the skill to execute web searches and return useful information.

Here's how you can use the plugin within a skill:

```python
# In your AutoGen Studio skill
query_results = web_search("Example search query")

## Parameters

- **query**: The search query string.
  - Type: `str`
  - Required: `true`

## Returns

- **results**: A list of search results, each including its title, URL, and a snippet.
  - Type: `List[Tuple[str, str, str]]`

## Configuration

Configure the plugin with your preferred search provider and the number of results to return:

```yaml
provider: bing # Options: "bing" or "google"
result_count: 3 # Number of results to return; should be a small number less than 10
```

### Bing Web Search API Configuration

Register a search resource on the Azure Portal ([https://aka.ms/bingapisignup](https://aka.ms/bingapisignup)) and obtain your API key:

```yaml
bing_api_key: YOUR_BING_API_KEY_HERE
```

### Google Custom Search API Configuration

Get your search engine ID from [https://cse.google.com/all](https://cse.google.com/all) and your API key from [https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials):

```yaml
google_search_engine_id: YOUR_GOOGLE_SEARCH_ENGINE_ID_HERE
google_api_key: YOUR_GOOGLE_API_KEY_HERE
```

## Installation

AutoGen Studio can be installed via pip:

```bash
pip install autogenstudio requests
```

After installation, ensure to configure your API keys to use the Web Search Plugin.
