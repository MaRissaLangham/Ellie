""" This file Desiciption can be found in the comment below """
# Author: Marissa Langham
# Date: 03/15/2023
# Description: Guess the Number game file for Ellie
# File Name: guessNum.py

import random
import speech_recognition as sr
from gtts import gTTS
import os

def guessNumDifficulty(difficultyLevel, maxNum):
    if "1" or "one" in difficultyLevel:
         maxNum == 100
    elif "2" or "two" in difficultyLevel:
        maxNum == 500
    elif "3" or "three" in difficultyLevel:
        maxNum == 1000
    elif "4" or "four" in difficultyLevel:
        maxNum == 10000
    elif "5" or "five" in difficultyLevel:
        maxNum == 100000

def guessTheNumber(maxNum):
    number = random.randint(1, maxNum)
    attempts = 0
    return number

    
  