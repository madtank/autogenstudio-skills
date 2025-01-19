# AutoGenStudio Slack

The goal of this skill is to help build a chatbot that can query specific slack channels for answers to a question.  This repository contains a Python script designed as a skill for AutoGenStudio, a framework for building and managing autonomous AI systems. This skill enables searching the questions and retrieving the relevant questions and answers in Slack.

## Skill Overview

- `slack_search.py`: This script is responsible for connecting to the Slack REST API and searching for messages matching a string.

## Usage

1. Create a new Slack Bot User OAuth Token.  This step is quite involved and may require permissions from your slack administrator so won't be documented here.  Once you have your Slack app approved and installed, you will be able to find your Slack Bot User OAuth Token by navigating Your Apps -> (click on your app) -> OAuth & Permissions.  Your Bot User Oauth Token will be listed under OAuth Tokens for Your Workspace.
2. Before running AutoGenStudio, set the environment variable SLACK_API_KEY to this key.  e.g.
```commandline
export SLACK_API_KEY="yourkeygoeshere"
```
3. Edit `slack_search.py` and set the names of the channels you want to search
```python
        # Replace these example channel names with the actual channel names you want to search
        self.channel_names = ["random", "general"]
```

### Running commandline

To test the script is set up properly, you can test it commandline as follows where "searchterm" is a word inside a message on Slack in one of the channels you included in your script:
```commandline
export SLACK_API_KEY="yourkeygoeshere"
python slack_search.py searchterm
```

## Integration with AutoGenStudio for GPT-4

To integrate the `slack_search.py` skill with AutoGenStudio for use in GPT-4 workflows:

1. **Create a New Skill:**
   - Navigate to the Build > Skills section within AutoGenStudio.
   - Create a new skill and give it a relevant name that easily identifies its purpose, such as "slack".

2. **Add the Python Script:**
   - Copy the content of the `slack_search.py` script into the code area of the new skill.
   - Ensure that the script is complete and correctly formatted to run as a standalone skill within the AutoGenStudio environment.

3. **Configure your Channel Names:**
   - Locate the `self.channel_names` variable within the script and set it to list of channel names you intend to search

5. **Incorporate Into Workflow:**
   - Once testing is successful, incorporate the skill into your desired workflow.
   - Build -> Workflow -> + New Workflow
   - Name: Pick a name (e.g. SOF Workflow)
   - Click primary_assistant
   - Remove and re-add your gpt model to ensure it picks up your API key (this feels like a bug in the current version that hopefully goes away in the future)
   - At the bottom add your skill
   - MOST IMPORTANT STEP:  Add this text to the bottom of the System Message:

> Before answering a question, use SlackSearcher defined in the slack skill to retrieve relevant answers from Slack.  Before calling SlackSearcher, convert the question to a small slack query string that will have the most likely chance of matching messages concerning the topic of the question


## Integration with AutoGenStudio for GPT-4 and Skill Execution Monitoring

See rag/README.md for instructions on how to monitor this skill.  The approach is the same.

## Contributing

Contributions to improve these skills or extend their capabilities are welcome. Please submit pull requests or open issues to discuss potential enhancements.
