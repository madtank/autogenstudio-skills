import requests
import json
import logging

# Configuration for Azure Application Insights
APP_ID = ""
API_KEY = ""
API_ENDPOINT = f"https://api.applicationinsights.io/v1/apps/{APP_ID}/query"

def execute_kql_query(kql_query):
    """
    Executes a KQL query against the Application Insights REST API.
    
    Parameters:
    - kql_query (str): The KQL query string to execute.
    
    Returns:
    - A JSON object containing the query results.
    """
    headers = {
        "x-api-key": API_KEY
    }
    params = {
        "query": kql_query
    }

    try:
        response = requests.get(API_ENDPOINT, headers=headers, params=params)
        if response.ok:
            return response.json()
        else:
            logging.error(f"Failed to execute KQL query. Response: {response.text}")
            return "Failed to execute KQL query."
    except Exception as e:
        logging.exception(f"An error occurred while executing KQL query: {str(e)}")
        return f"An error occurred while executing KQL query: {str(e)}"

# Example KQL query - Replace with your actual query
kql_query = """
traces
| where timestamp > ago(30d)
| limit 10
"""

# Execute the query
query_result = execute_kql_query(kql_query)
print(query_result)
