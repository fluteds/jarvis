# Jarvis

Jarvis is a Python-based application that acts as a virtual assistant capable of performing various tasks through voice commands. It utilizes speech recognition and text-to-speech capabilities to understand user commands and provide responses accordingly.

## Installation

1. Install dependencies: `pip install -r requirements.txt`
2. Ensure you have the necessary API keys and configurations set up.

## Usage

1. Run `main.py`.
2. Jarvis will greet you and listen for your voice commands.
3. Speak a command.
4. Jarvis will execute the command and respond accordingly.

>[!NOTE]
> Jarvis is slow to process speech and sometimes can't catch everything you say instantly.

## Commands

### Wikipedia Search

- Command: `Wikipedia [query]`
- Description: Allows the user to search for information on Wikipedia using a specified query. Jarvis fetches relevant Wikipedia articles based on the provided query.

### Open Notepad / Steam / Spotify

- Command: `Open [Notepad/Steam/Spotify]`
- Description: Opens the given application on the user's system.

### Open Website

- Command: `Open Website [query]` Example: `Open website Twitch(dot)tv`
- Description: Opens a given website.

### Search YouTube

- Command: `Search YouTube [query]`
- Description: Enables the user to search for videos on YouTube using a specified query. Jarvis opens the default web browser and displays search results for the provided query.

### Play Music

- Command: `Play [song name]`
- Description: Plays the specified song using the PyWhatKit library. Jarvis searches for the song on YouTube and plays the first result.

### Weather Forecast

- Command: `Weather [city name]` or `What's the weather in [city name]`
- Description: Fetches the current weather forecast for the specified city using the OpenWeatherMap API. Jarvis provides information on temperature, humidity, and wind speed for the given city.

## Disclaimer

This is not a solid alternative to any other voice assistant applications as it will probably never be as robust enough to do the job. I was inspired by J.A.R.V.I.S in Iron Man.
