# Jarvis

Jarvis is a Python-based virtual assistant that responds to voice commands. It utilizes speech recognition and text-to-speech capabilities for interaction.

## Installation

1. Install dependencies: `pip install -r requirements.txt`.
2. Set up necessary API keys and configurations.

## Usage

1. Run `main.py`.
2. Jarvis will greet you and await commands.
3. Speak a command.
4. Jarvis will execute and respond.

>[!NOTE]
> Jarvis may experience delays in processing speech and occasional pauses before executing commands. Please look for the "Listening..." or "Recognizing speech..." console logs.

## Commands

| Command                                              | Keywords                           | Description                                                   | Example                                      |
|------------------------------------------------------|------------------------------------|---------------------------------------------------------------|----------------------------------------------|
| Wikipedia [query]                                   | "Wikipedia"                        | Search Wikipedia.                                            | "Wikipedia Jenson Button"         |
| Open [Notepad/Steam/Spotify]                        | "Open"                             | Launch specified application.                                | "Open Steam"                                 |
| Open Website [query]                                | "Open website"                     | Navigate to given website.                                   | "Open website example(dot)com"                   |
| Search YouTube [query]                              | "Search YouTube for"               | Search YouTube videos.                                       | "Search YouTube for funny cat videos"       |
| Play [song name]                                    | "Play"                             | Play specified song.                                         | "Play Bohemian Rhapsody"                    |
| Weather [city name] or What's the weather in [city name]? | "Weather" | Fetch weather forecast.                                     | "What's the weather in London"          |
| Calendar                                            | "Calendar" or "event"             | Fetch next calendar event.                                   | "What's my next event?" or "What's on my calendar?"                                   |
| News or Read me the news                            | "News"                             | Retrieve news articles.                                      | "Read me the news"                          |

## Disclaimer

This application is not a replacement for established voice assistants as it is no where near polished enough. It draws inspiration from J.A.R.V.I.S. in Iron Man.
