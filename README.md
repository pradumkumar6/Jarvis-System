
# Jarvis Assistant System

A Python-based voice-controlled assistant, inspired by Jarvis from Iron Man, that can perform various tasks like telling the time, searching Wikipedia, and opening Google. This project demonstrates voice-to-text, text-to-speech, and API usage to create an interactive assistant.

## Features

- Voice Recognition: Converts spoken language into text commands.
- Text-to-Speech: Provides vocal responses using a speech synthesis engine.
- Task Automation:
   - Provides the current time.
   -   Opens Google in a web browser.
   -  Fetches brief Wikipedia summaries based on user queries.
- Logging: Tracks system activity and errors to facilitate debugging and maintenance


## Tech Stack

**Programming Language:** Python

**Libraries:**
- speech_recognition: For capturing and converting voice commands.
- pyttsx3: For text-to-speech functionality.
- wikipedia-api: For fetching information from Wikipedia.
- webbrowser: To open browser windows programmatically.
- logging: To record system events and errors.


## Installation

Install my-project with npm

```bash
  pip install -r requirements.txt

  python main.py
```
    
## Usage

**Usage:**
1. When prompted, speak into your microphone. The assistant will recognize commands such as:
- “What is the time?”
- “Open Google”
- “Tell me about [something] on Wikipedia”
2. To end the session, simply say “exit.”
**Commands:**
- Time Inquiry: "What time is it?"
- Wikipedia Search: "Tell me about Python on Wikipedia"
- Open Google: "Open Google"
**Logging:**
The system generates logs stored in the logs/application.log file. These logs include:

- Command processing
- Errors encountered during voice recognition
- Actions taken by the assistant




## Future Improvements
- Natural Language Processing (NLP): Enhance response capabilities for more complex queries.
- Integration with External APIs: Expand the assistant's functionality.
- Graphical Interface: Create a simple frontend for an enhanced user experience.
