import os
import subprocess as sp
paths={
   'notepad':r"C:\Program Files\Notepad++\notepad++.exe",
   'steam': "C:\Program Files (x86)\Steam\steam.exe",
   'spotify': r"C:\Users\%username%\AppData\Roaming\Spotify\Spotify.exe"
   
}
def notepad():
    os.startfile(paths['notepad'])

def steam():
    os.startfile(paths['steam'])

def cmpt():
    os.system('start cmd')
    
def spotify():
    os.startfile(paths['spotify'])
    