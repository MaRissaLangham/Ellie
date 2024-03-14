""" This file Desiciption can be found in the comment below """
# Author: Marissa Langham
# Date: 03/12/2023
# Description: Main file for Ellie
# File Name: main.py

#import libaries & files
import speech_recognition as sr
import os
import re
import datetime
import pyjokes

from gtts import gTTS
from skills.jokes import tellJoke, tellReallyFunnyJoke
from skills.calculations import performCalculation
from skills.todoList import addTodoItem, removeTodoItem, displayTodoList


# Initialize the recognizer
r = sr.Recognizer()

def speak(text):
    """Uses the Google Text-to-Speech engine to speak the given text."""
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    os.system("afplay speech.mp3")  # Use 'afplay' on macOS

def listen():
    """Listens for audio input and returns the recognized text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that. Please try again.")
        return None
    except sr.RequestError:
        speak("Could not request results; check your internet connection.")
        return None

def greetingTime():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
       speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")

def handleCommand(command):
    """Handles the given command."""
    if "joke" in command:
        if "really funny" in command:
            speak(tellReallyFunnyJoke())
        else:
            speak(tellJoke())
    elif "calculate" in command:
        result = performCalculation(command)
        speak(f"The result is {result}")
    elif "add to my to do list" in command:
        while True:
            speak("What would you like to add to your to do list?")
            item = listen()
            speak(f"You would like me to add {item} to your to do list?")
            """NEED TO ASSIGN LISTEN COMAND TO CONFIRM ITEM. CURRENTLY IN-PROGRESS - ML"""
            if "yes" in command:
                break
            else:
                speak("I didn't catch that. Please try again.")
        while True:
            speak(f"What is the priority level for {item}? Please say 1, 2, or 3.")
            priority = listen()
            if priority and priority in ["one", "two", "three"]:
              speak(addTodoItem(item, priority))
              break
            else:
                speak("Sorry, that's not a valid priority level. Please try again.")
    elif "remove from my to do list" in command:
        item = command.replace("remove from my to-do list", "").strip()
        if item:
            speak(removeTodoItem(item))
        else:
            speak("Please tell me what you want to remove from your to-do list.")
    elif "ellie what's on my to do list" in command or "tell me my to-do list" in command:
        speak(displayTodoList())
    elif "goodbye ellie" in command:
        speak("Goodbye!")
        return "stop"
    else:
        speak("Sorry, I didn't understand that. Can you please repeat?")

def main():
    """The main function that runs the voice assistant."""
    greetingTime()
    speak("Hello, I'm Ellie, your personal desk assistant. How can I help you?")

    while True:
        command = listen()
        if command:
            result = handleCommand(command)
            if result == "stop":
                break
        else:
            continue

if __name__ == "__main__":
    main()
