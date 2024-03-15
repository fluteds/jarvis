import pywhatkit

def play_song(command):
    # Extract the song name from the command
    song_name = command.replace('play', '').strip()
    # Play the song using pywhatkit
    pywhatkit.playonyt(song_name)
