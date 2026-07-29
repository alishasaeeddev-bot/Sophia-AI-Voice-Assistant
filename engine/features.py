import os
import re
import sqlite3
import webbrowser
import requests
import threading
from datetime import datetime
from playsound import playsound
import eel
import pywhatkit as kit

from engine.command import speak
from engine.config import ASSISTANT_NAME


conn = sqlite3.connect("sophia.db", check_same_thread=False)
cursor = conn.cursor()

WEATHER_API_KEY = "9b092637b3ecba6de6ba813c092bff0a"
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def playAssistantSound():
    def run():
        playsound("www\\assets\\audio\\start_sound.mp3")

    threading.Thread(target=run, daemon=True).start()


@eel.expose
def playClickSound():
    def run():
        playsound("www\\assets\\audio\\click_sound.mp3")

    threading.Thread(target=run, daemon=True).start()


def get_weather(query):
    try:
        query = query.lower()

        match = re.search(r"weather in (.*)", query)
        city = match.group(1) if match else query

        remove_words = [
            "tell me", "what is", "the", "weather", "in",
            "please", "is", "show", "me"
        ]

        for word in remove_words:
            city = city.replace(word, "")

        city = city.strip()

        if not city:
            speak("Please tell me the city name")
            return

        url = f"{WEATHER_BASE_URL}?q={city}&appid={WEATHER_API_KEY}&units=metric"

        response = requests.get(url, timeout=3)
        data = response.json()

        if data.get("cod") != 200:
            speak("Sorry, I could not find this city")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        speak(f"The weather in {city} is {temp} degree Celsius with {desc}")

    except Exception as e:
        print("Weather error:", e)
        speak("Sorry, I could not fetch weather")


# ---------------- TIME ---------------- #
def tell_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


# ---------------- DATE ---------------- #
def tell_date():
    now = datetime.now()
    current_date = now.strftime("%d %B %Y")
    speak(f"Today's date is {current_date}")


# ---------------- OPEN COMMAND ---------------- #
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "").strip().lower()

    if not query:
        return

    web_apps = {
        "canva": "https://www.canva.com",
        "news": "https://news.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
    }

    if query in web_apps:
        speak("Opening " + query)
        webbrowser.open(web_apps[query])
        return

    try:
        cursor.execute('SELECT path FROM sys_command WHERE LOWER(name)=?', (query,))
        result = cursor.fetchall()

        if result:
            speak("Opening " + query)
            os.startfile(result[0][0])
            return

        cursor.execute('SELECT url FROM web_command WHERE LOWER(name)=?', (query,))
        result = cursor.fetchall()

        if result:
            speak("Opening " + query)
            webbrowser.open(result[0][0])
            return

        speak("Trying to open " + query)
        os.system('start ' + query)

    except Exception:
        speak("Error opening command")


def PlayYoutube(query):
    search_term = extract_yt_term(query)

    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Sorry, I couldn't understand.")


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else ""