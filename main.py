import pyttsx3
import speech_recognition as sr
import random
import winsound
from datetime import datetime

from config import BOTNAME, USERNAME

# Import individual command functions
from commands.wikipedia import search_wikipedia
from commands.applications import notepad, steam, spotify
from commands.youtube import search_youtube
from commands.music import play_song
from commands.website import open_website
from commands.weather import get_weather

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set the voice to a female one


# List of random greetings
def get_greeting():
    current_time = datetime.now()
    hour = current_time.hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def get_random_greeting():
    greetings = [
        f"{get_greeting()}, {USERNAME}",
        "What can I help you with?",
        "How may I be of service?",
        f"{USERNAME}, What's on your mind?",
    ]
    return random.choice(greetings)

def get_random_success_message():
    messages = [
        f"On it, {USERNAME}.",
        f"Working on it, {USERNAME}.",
        f"Got it, {USERNAME}.",
        f"Sure thing, {USERNAME}.",
    ]
    return random.choice(messages)

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to play a sound (you can customize this)
def play_sound():
    winsound.MessageBeep()
    print("Playing wake-up sound...")

# Function to take voice input and convert it to text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print("User said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down. Please try again later.")
            return ""

# Select a random greeting
random_greeting = get_random_greeting()
speak(f"{random_greeting}")

# Main loop for continuous interaction
while True:
    command = take_command()
    if command:
        if 'wikipedia' in command:
            search_wikipedia(command)  # Call the Wikipedia command function
            speak(get_random_success_message())
        elif 'open notepad' in command:
            notepad()  # Call the notepad command function
            speak(get_random_success_message())
        elif 'open steam' in command:
            steam()  # Call the steam command function
            speak(get_random_success_message())
        elif 'open spotify' in command:
            spotify()  # Call the Spotify command function
            speak(get_random_success_message())
        elif 'search youtube for:' in command:
            query = command.replace('search youtube for:', '').strip()
            search_youtube(query)  # Call the YouTube command function with the query
            speak(get_random_success_message())
        elif 'open website' in command:
            # Extract the URL from the command
            url = command.replace('open website', '').strip()
            open_website(url)  # Call the open_website function with the URL
            speak(get_random_success_message())
        elif 'play' in command:
            play_song(command)  # Call the play song command function
            speak(get_random_success_message())
        elif 'weather' in command:
            city = command.replace('weather in', '').strip()
            weather_report = get_weather(city)
            speak(weather_report)
            speak(get_random_success_message())

        else:
            speak("Sorry, I didn't understand that command.")