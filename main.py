import pyttsx3
import speech_recognition as sr
import random
import winsound
from datetime import datetime
import time

# Import individual command functions
from commands.wikipedia import search_wikipedia
from commands.applications import notepad, steam, spotify
from commands.youtube import search_youtube
from commands.music import play_song
from commands.website import open_website
from commands.weather import get_weather
from commands.calendar import fetch_calendar_events, get_next_event

from config import USERNAME

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

def get_random_goodbye_message():
    goodbye_messages = [
        "No worries. I'll be here if you need me.",
        "Alright. Feel free to ask if you need anything else.",
        "Sure thing. Let me know if you require any further assistance.",
        "Okay. Don't hesitate to reach out if you need help later.",
    ]
    return random.choice(goodbye_messages)

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
        audio = r.listen(source)  # Listen indefinitely without a time limit
        try:
            command = r.recognize_google(audio, language="en-US", show_all=False)
            print("User said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down. Please try again later.")
            return ""


# Start with a greeting
random_greeting = get_random_greeting()
speak("I am JARVIS. Your personal assistant.")
speak("Please leave a few seconds after the following message for me to start taking your questions.")
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
        elif 'calendar' in command:
            calendar_data = fetch_calendar_events()
            if calendar_data:
                next_event = get_next_event(calendar_data)
                if next_event:
                    event_date, event_start_time, event_end_time, event_summary = next_event
                    speak(f"Your next event is {event_summary} starting at {event_start_time} and ending at {event_end_time}.")
                else:
                    speak("You don't have any upcoming events.")
            else:
                speak("Failed to fetch calendar events.")
                
    speak("Can I help you with anything else?")  # Ask for further assistance
    response = take_command().lower()  # Check if user needs further assistance

# TODO Fix bug that stops taking command input if no response or response given
    # Wait for response or timeout after 5 seconds
    start_time = time.time()
    while time.time() - start_time < 5:
        if response:
            time.sleep(0.1)  # Wait for a short time before checking again

    if 'no' in response:
        speak(get_random_goodbye_message())  # Bid goodbye with a random message
        continue
    elif 'yes' in response:
        speak(get_random_greeting())  # Greet the user again
        continue  # Restart the loop
    else:  # Handle case where there's no response
        speak(get_random_goodbye_message())  # Bid goodbye with a random message
        continue  # Restart the loop
