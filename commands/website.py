import subprocess

def open_website(url):
    firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # Path to Firefox executable
    subprocess.Popen([firefox_path, url])
