import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import webbrowser
import wikipedia


# Logging configuration
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

# Taking the male voice from the system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")


# for i in voices:
#     print(i.id)

engine.setProperty("voice", voices[0].id)


def speak(text):
    """This function converts text to speech

    Args:
        text
    returns:
        voice
    """
    engine.say(text)
    engine.runAndWait()
# speak("Hello sir, I am Jarvis")


def takeCommand():
    """This function takes command and recognizes it

    Returns:
        text as query
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google_cloud(audio, language="en-in")
        print(f"User said:{query}\n")
    except Exception as e:
        logging.info(e)
        speak("Say that again please...")
        return "None"
    return query



# This function will wish
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir! How are you doing?")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Sir! How are you doing?")
    else:
        speak("Good Evening Sir! How are you doing?")

    speak("I am Jarvis. How can I help you?")

# wish_me()    




# text = takeCommand()
# print(text)
# speak(text)

wish_me()

while True:
    # wish_me()
    query = takeCommand().lower()
    # print(query)
    # speak(query)
    if "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
    elif "name" in query:
        speak("My name is Jarvis")
    elif "exit" in query:
        speak("Good Bye Sir!")
        exit()
    elif "open google" in query:
        speak("ok sir. please type here what do you want to search")
        webbrowser.open("google.com")

    # for search something in wikipedia
    elif "wikipedia" in query:
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

