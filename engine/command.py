import pyttsx3
import speech_recognition as sr
import eel

# ---------------- GLOBAL ENGINE---------------- #
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)


# ---------------- SPEAK ---------------- #
def speak(text):
    try:
        print("SOPHIA:", text)
        eel.DisplayMessage(text)

        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Speak error:", e)


# ---------------- TAKE COMMAND FASTER ---------------- #
@eel.expose
def takeCommand():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            eel.DisplayMessage("Listening...")

            r.pause_threshold = 0.6
            r.adjust_for_ambient_noise(source, duration=0.2)

            audio = r.listen(source, timeout=5, phrase_time_limit=6)

    except Exception:
        return ""

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")

        query = r.recognize_google(audio, language="en-IN")

        print("User said:", query)
        eel.DisplayMessage(query)

        return query.lower().strip()

    except Exception:
        return ""


# ---------------- COMMAND HANDLER ---------------- #
@eel.expose
def allCommands():
    from engine.features import (
        openCommand,
        PlayYoutube,
        get_weather,
        tell_time,
        tell_date
    )

    query = takeCommand()
    print("FINAL QUERY:", query)

    if not query:
        return

    if "open" in query:
        openCommand(query)

    elif "youtube" in query:
        PlayYoutube(query)

    elif "weather" in query:
        get_weather(query)

    elif "time" in query:
        tell_time()

    elif "date" in query or "today" in query:
        tell_date()

    else:
        speak("Command not recognized")

    eel.ShowHood()