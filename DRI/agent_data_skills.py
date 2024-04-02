import requests
import json
import logging

# Configuration for BUE REST API
BEARER_TOKEN = ""
API_ENDPOINT = f"url"

def fetch_agent_details(agent):
    """
    Fetches agent profile information from BUE REST API.
    
    Parameters:
    - agent (str): The agent name for fetching profile information.
    
    Returns:
    - A JSON object containing the agent information.
    """
    authorization = {
        "Authorization": BEARER_TOKEN
    }
    

    try:
        response = requests.get(API_ENDPOINT + agent, headers=authorization)
        if response.ok:
            return response.json()
        else:
            logging.error(f"Failed to fetch agent details. Response: {response.text}")
            return "Failed to fetch agent details."
    except Exception as e:
        logging.exception(f"An error occurred while fetching agent details: {str(e)}")
        return f"An error occurred while fetching agent details: {str(e)}"


agent="agent@microsoft.com"
# Execute the api invocation
result = fetch_agent_details(agent)
print(result)
