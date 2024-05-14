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
from skills.games.gamesMain import whichGame, displayGameList
from skills.games.guessNum import setDifficultyLevel, getTheNum, getTheMaxNum


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
        r.adjust_for_ambient_noise(source)
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
            speak("What would you like to add to your to-do list?")
            item = listen()
            speak(f"Did you say you want to add '{item}' to your to-do list?")
            confirmation = listen()  # Listen for the user's confirmation
            if "yes" in confirmation:
                break # Break if the user confirms
            else:
                speak("Let's try that again. Please tell me what to add.")
        while True: # After confirmation, proceed to ask for priority
            speak(f"What is the priority level for '{item}'? Please say 1, 2, or 3.")
            priority = listen()
            if priority in ["one", "two", "three"]:
                # Ensure conversion from words to numbers if needed, or directly add the numeric value
                priority_map = {"one": "1", "two": "2", "three": "3"}
                numeric_priority = priority_map.get(priority, priority)
                speak(addTodoItem(item, numeric_priority))
                break
            else:
                speak("Sorry, that's not a valid priority level. Please try again.")

    elif "remove from my to do list" in command:
        item = command.replace("remove from my to-do list", "").strip()
        if item:
            speak(removeTodoItem(item))
        else:
            speak("Please tell me what you want to remove from your to-do list.")

    elif "what's on my to do list" in command or "tell me my to-do list" in command:
        speak(displayTodoList())

    elif "play a game" in command:
        speak("Sure! Do you want to hear the games I have?")
        yesOrNo = listen() 
        if "yes" in yesOrNo:
            speak(displayGameList())
        else:
            speak("which game would you like to play?")
            item = listen()
            whichGame(item)

            if "guess the number" in item:
                # get and set difficulty for the game.

                speak ("Welcome to the guess the number game! Is this your first time playing?")
                yesOrNo2 = listen()

                if "yes" in yesOrNo2:

                    gameIntroStr = """In this game, I'll think of a number within a certain range, and you have to guess what it is.
                    There are five difficulty levels, each with a different range of numbers. Level 1 is up to 100.
                    Level 2 is up to 500. Level 3 is up to 1000. Level 4 is up to 10000. and Level 5 is up to 100000.
                    You'll guess a number, and I'll tell you if my number is higher or lower than your guess. 
                    Keep guessing until you find the right number. Good luck!"""

                    speak(gameIntroStr)

                elif "no" in yesOrNo2:
                    speak("Cool! let's play!")
                
                else: speak("I couldn't quite catch that. Please say yes or no next time. Try again.")

                speak("There are 5 difficultiues, not including 0. What difficulty do you want to play?")

                """Getting diff. level"""
                userDifficultyLevel = listen()
                
                """Setting Diff. Level"""
                setDifficultyLevel(userDifficultyLevel)

                speak(f"The difficulty level you are wanting is {userDifficultyLevel}.")

                yesOrNo3 = listen()
                if "yes" in yesOrNo3:
                    speak("Great let's continue!")
                elif "no" in yesOrNo3:
                    speak ("Oh no, let's try again!")
                    while "no" in yesOrNo3:
                        difficultyLevel = listen()
                    
                        setDifficultyLevel(userDifficultyLevel)
                        speak(f"The difficulty level you are wanting is {userDifficultyLevel}.")
                        yesOrNo3 = listen()
                else:
                    speak("I couldn't quite catch that. Please say yes or no next time. Try again.")
                
                #Getters for maxNum & Number
                maxNum = getTheMaxNum(maxNum)
                number = getTheNum(maxNum, number)

                speak(f"I'm thinking of a number between 1 and {maxNum}.")
                attempts = 0

                while True:
                    speak("What's your guess?")
                    guessNum = listen() # Implement the listen function to capture user input
                    try:
                        guessNum = int(guessNum)
                        attempts += 1
                        if guessNum < number:
                            speak("It's higher.")
                        elif guessNum > number:
                            speak("It's lower.")
                        else:
                            speak(f"Correct! You've guessed my number in {attempts} attempts.")
                        break
                    except ValueError:
                        speak("Please say a number.")

            elif "twenty questions" in item:
                speak ("Welcome to the twenty questions game! Is this your first time playing?")
                yesOrNo2 = listen()
                if "yes" in yesOrNo2:

                    gameIntroStr = """In this game,..... Good luck!"""

                    speak(gameIntroStr)

                elif "no" in yesOrNo2:
                    speak("Cool! let's play!")
                else:
                    speak("I couldn't quite catch that. Please say yes or no next time. Try again.")

                """Logic function for game"""

            elif "trivia" in item:
                speak ("Welcome to the trivia game! Is this your first time playing?")
                yesOrNo2 = listen()
                if "yes" in yesOrNo2:

                    gameIntroStr = """In this game,..... Good luck!"""

                    speak(gameIntroStr)

                elif "no" in yesOrNo2:
                    speak("Cool! let's play!")
                else:
                    speak("I couldn't quite catch that. Please say yes or no next time. Try again.")
                
                """Logic function for game"""

            else:
                speak("I couldn't quite catch that. Please say yes or no next time. Try again.")

    elif "goodbye ellie" in command:
        speak("Goodbye, Marissa!")

        return "stop"
    
    else:
        speak("Sorry, I didn't understand that. Please try again.")

def main():
    """The main function that runs the voice assistant."""
    greetingTime()
    speak("I'm Ellie, your personal desk assistant. How can I help you?")

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
