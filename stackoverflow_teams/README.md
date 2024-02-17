# AutoGenStudio StackOverflow for Teams

The goal of this skill is to help build a chatbot that can query a corporate knowledge base managed by StackOverflow for Teams.  This repository contains a Python script designed as a skill for AutoGenStudio, a framework for building and managing autonomous AI systems. This skill enables searching the questions and retrieving the relevant questions and answers in StackOverflow for Teams.

## Skill Overview

- `stackoverflow_teams.py`: This script is responsible for connecting to the StackOverflow for Teams REST API and searching for questions matching a string.

## Usage

1. Create a new StackOverflow for Teams API Key by clicking on the top right of the web UI and selecting Account Settings -> API - Personal Access Tokens
2. Before running AutoGenStudio, set the environment variable STACK_OVERFLOW_TEAMS_API_KEY to this key.  e.g.
```commandline
export STACK_OVERFLOW_TEAMS_API_KEY="yourkeygoeshere"
```
3. Edit `stackoverflow_teams.py` and set your Stackoverflow for Teams team name (sometimes also called a "team slug") on this line:
```python
 team_name = "yourteamname"  # TODO Set your team name here
```

### Running commandline

To test the script is set up properly, you can test it commandline as follows where "searchterm" is a word inside a title of a question on StackOverflow for Teams:
```commandline
export STACK_OVERFLOW_TEAMS_API_KEY="yourkeygoeshere"
python stackoverflow_teams.py searchterm
```


## Integration with AutoGenStudio for GPT-4

To integrate the `stackoverflow_teams.py` skill with AutoGenStudio for use in GPT-4 workflows:

1. **Create a New Skill:**
   - Navigate to the Build > Skills section within AutoGenStudio.
   - Create a new skill and give it a relevant name that easily identifies its purpose, such as "StackOverflow for Teams".

2. **Add the Python Script:**
   - Copy the content of the `stackoverflow_teams.py` script into the code area of the new skill.
   - Ensure that the script is complete and correctly formatted to run as a standalone skill within the AutoGenStudio environment.
   - Ensure `yourteamname` is set to your team name in the script

3. **Configure your Team Name:**
   - Locate the team_name variable within the script and set it to your team name.

5. **Incorporate Into Workflow:**
   - Once testing is successful, incorporate the skill into your desired workflow.
   - Build -> Workflow -> + New Workflow
   - Name: Pick a name (e.g. SOF Workflow)
   - Click primary_assistant
   - Remove and re-add your gpt model to ensure it picks up your API key (this feels like a bug in the current version that hopefully goes away in the future)
   - At the bottom add your skill
   - MOST IMPORTANT STEP:  Add this text to the bottom of the System Message:

> Before answering a question, use StackOverflowTeamsSearcher defined in the sof skill to retrieve relevant answers from stackoverflow for teams.  Call StackOverflowTeamsSearcher will only match exact matches in the stack overflow question title, so pick out the three most critical words in the question and only search for those individual keywords


## Integration with AutoGenStudio for GPT-4 and Skill Execution Monitoring

See rag/README.md for instructions on how to monitor this skill.  The approach is the same.

## Contributing

Contributions to improve these skills or extend their capabilities are welcome. Please submit pull requests or open issues to discuss potential enhancements.
