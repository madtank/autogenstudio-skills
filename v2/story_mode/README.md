---

# Story Mode Adventure Skill

The Story Mode Adventure Skill is an interactive storytelling experience powered by Python, Tkinter, and OpenAI's DALL-E image generation. This skill allows users to embark on a textual and visual adventure where their choices shape the narrative.

## Prerequisites

Before using the Story Mode Adventure Skill, ensure you have the following prerequisites met:

- Python 3.6 or higher installed on your system.
- Tkinter installed and working (comes with Python for Windows and macOS).
- PIL (Pillow) library installed for image processing.
- Requests library installed for HTTP requests.
- OpenAI Python library installed for interacting with the OpenAI API.

You can install the necessary Python libraries using pip:

```sh
pip install Pillow requests openai
```

## Setting Up OpenAI API Credentials

To use the `generate_images` skill, you must have a valid OpenAI API key. Follow these steps to set up your API key:

1. Obtain an API key from [OpenAI](https://openai.com/).
2. Export your API key as an environment variable before starting the `autogenstudio`. This can be done as follows:

   On macOS/Linux:
   ```sh
   export OPENAI_API_KEY='your-api-key'
   ```

   On Windows:
   ```cmd
   set OPENAI_API_KEY=your-api-key
   ```

   Replace `your-api-key` with the actual key you obtained from OpenAI.

## Using the Story Mode Skill

To start an adventure, you will need to import and call the `story_mode` function from the `skills.py` file. This function requires an AI-generated message to begin.

Here's how to use the `story_mode` skill:

1. Ensure that the `generate_images` skill is in the same directory or a place where Python can import it.
2. Call the `story_mode` function with a starting message:

   ```python
   from skills import story_mode
   
   story_mode("You stand at the crossroads of destiny. Which path do you choose?")
   ```

3. Interact with the GUI that pops up. Enter your choices or responses in the input box and click "Submit" to proceed with the story.

## AI Storytelling Mode Instructions

When using this skill, the AI acts as a master storyteller. It should follow these specific instructions to engage the user:

1. Begin with a compelling opening statement to set the scene.
2. Prompt the user for input at key points in the story.
3. Use the user's input to dynamically generate the next part of the story and possibly new images.
4. Provide clear options for the user to choose from, guiding them through the adventure.
5. Continuously call `story_mode` with new AI messages based on the user's choices to progress the story.

Please note that the `story_mode` skill is designed for interactive use and does not return values that the AI can print directly. The AI must capture user input and use it to continue the story within the interactive GUI environment.

## Contribution

Your contributions to improving the Story Mode Adventure Skill are welcome. Please feel free to fork the repository, make your improvements, and submit a pull request.