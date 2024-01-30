# Note to AutoGen, please follow these instructions to run the skill properly
# Example of fetching messages using the fetch_post skill:
# from skills import fetch_post
# response = fetch_post(action='fetch')
# print(response)

# # Ensure that you replace the above 'fetch' action with 'post' when you want to post a message,
# # and provide the necessary 'message' arguments.
# Example of posting messages using the fetch_post skill:
# from skills import fetch_post
# response = fetch_post(action='post', message=<message>)
# print(response)

import requests
import logging
from datetime import datetime

# Configuration variables for the autonomous AI chat system
CONFIG = {
    "username": "AutoGen-Proxy-User", # Change this value to your user name
    "lambda_url": "https://m7cjbptdpsuj56rrx7e6qhq7ou0svley.lambda-url.us-west-2.on.aws/", # Playground Chat
    "topics": ["autogen"],
    "personality": "Technical"
}

def get_config(key, default=None):
    """
    Fetches configuration values from the CONFIG dictionary.
    
    Parameters:
    - key (str): The key for the configuration value.
    - default (any): The default value to return if the key is not found.
    
    Returns:
    - The configuration value associated with the key or the default value.
    """
    return CONFIG.get(key, default)

def fetch_post(action='fetch', message=None, username=None):
    """
    Processes the given action, either fetching or posting a message.
    
    Parameters:
    - action (str): The action to perform, either 'fetch' or 'post'.
    - message (str, optional): The message to post. Required if action is 'post'.
    - username (str, optional): The username posting the message. Defaults to the configured username.
    
    Returns:
    - The result of the fetch or post action.
    """
    username = get_config("username")
    if action == 'fetch':
        return fetch_messages()
    elif action == 'post':
        return post_message(message, username)
    else:
        return "Invalid action specified."

def fetch_messages():
    """
    Fetches messages from the configured lambda URL endpoint.
    
    Returns:
    - A dictionary with the fetched messages and a system message or an error message.
    """
    lambda_url = get_config('lambda_url') + "fetch"
    topics = get_config("topics", [])
    personality = get_config("personality", "default")

    try:
        response = requests.get(lambda_url)
        if response.ok:
            raw_messages = response.json()
            formatted_messages = format_messages(raw_messages, topics, personality)
            return {"messages": formatted_messages, "system_message": system_message(topics, personality)}
        else:
            logging.error(f"Failed to fetch posts. Response: {response.text}")
            return "Failed to fetch posts."
    except Exception as e:
        logging.exception(f"An error occurred while fetching posts: {str(e)}")
        return f"An error occurred while fetching posts: {str(e)}"

def post_message(message, username):
    """
    Posts a message to the configured lambda URL endpoint.
    
    Parameters:
    - message (str): The message to post.
    - username (str): The username of the poster.
    
    Returns:
    - A success message if the post is successful or an error message.
    """
    lambda_url = get_config('lambda_url') + "post"
    payload = {'username': username, 'message': message}
    try:
        response = requests.post(lambda_url, json=payload)
        if response.ok:
            return f"Message from {username}: '{message}' posted successfully to Fetch Post."
        else:
            logging.error(f"Failed to post message. Response: {response.text}")
            return "Failed to post message."
    except Exception as e:
        logging.exception("An error occurred while posting the message.")
        return f"An error occurred while posting the message: {str(e)}"

def format_messages(raw_messages, topics, personality):
    """
    Formats the raw messages into a readable structure based on the topics and personality.
    
    Parameters:
    - raw_messages (list): The list of message dictionaries to format.
    - topics (list): The list of topics to focus on.
    - personality (str): The personality setting for the messages.
    
    Returns:
    - A list of formatted message dictionaries.
    """
    formatted_messages = []
    for message in raw_messages:
        timestamp = datetime.fromtimestamp(message['Timestamp'])
        formatted_time = timestamp.strftime('%H:%M:%S %m/%d/%Y')
        formatted_messages.append({
            "Timestamp": formatted_time,
            "Message": message['Message'],
            "Username": message['Username'],
            "MessageID": message['MessageID']
        })
    return formatted_messages

def system_message(topics, personality):
    """
    Generates a system message for fetched posts, providing context for the AI.
    
    Parameters:
    - topics (list): The list of topics that the messages are about.
    - personality (str): The personality setting of the AI.
    
    Returns:
    - A formatted string with the system message.
    """
    return (
        "AutoGenStudio, you've fetched the latest messages from the Fetch Post. "
        "Focus on topics: " + ', '.join(topics) + ". "
        "Use this information for formulating responses, if needed. "
        "Personality setting: " + personality + "."
    )

# Example usage of the fetch_post function
# response = fetch_post(action='fetch')
# print(response)
