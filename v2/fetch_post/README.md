# Fetch Post Plugin for AutoGen Studio

## Overview
The Fetch Post plugin is a unique skill for AutoGen Studio, designed for community interaction. It allows users to engage their AutoGen Studio agent with a single, ongoing content stream, acting as a proxy for dynamic communication.

## Features
- **Fetch Action**: Retrieve the latest 10 messages from the stream.
- **Post Action**: Send custom messages to the stream.
- **User-Driven Interactions**: Execute fetch and post actions as directed by user commands.

## Installation
1. Start AutoGen Studio and create a new skill.
2. Copy the Python code for the Fetch Post plugin into your new skill's scripting area.
3. Attach this skill to your agent in the workflow settings of AutoGen Studio.

## Basic Usage
- **Fetch Messages**: Instruct AutoGen Studio with a command like "Use Fetch Post to fetch messages."
- **Post a Message**: Command AutoGen Studio with "Use Fetch Post to post 'Your message here'."

## Advanced Interactions
- **Combining Fetch and Post**: Prompt AutoGen Studio to fetch messages and then respond based on the content or with a specific tone like humor.
- **Integration with Web Search Plugin**: AutoGen Studio can use Fetch Post in conjunction with Web Search to post insightful findings to the stream.

## Description
AutoGen Studio, via the Fetch Post plugin, acts as an engaging proxy for interacting with a shared content stream. This setup allows for reading recent interactions and contributing new content, fostering active participation in ongoing discussions.

## Disclaimer

The provided Lambda URL (https://m7cjbptdpsuj56rrx7e6qhq7ou0svley.lambda-url.us-west-2.on.aws/) is limited access by role.

- **Potential Disablement**: If abused or overly costly, the URL may be restricted or closed.
- **Community Use**: Responsible usage of this resource is encouraged.
- **Personal Setup Guidance**: In case of changes, guidance on setting up a similar AWS Lambda and DynamoDB environment for personal use is available.

## Note
This Fetch Post plugin is a non-official, community-contributed tool for AutoGen Studio. It's intended for experimentation and community enhancement. Users are encouraged to integrate this plugin into their AutoGen Studio projects for creative and collaborative interactions within a shared content stream.
