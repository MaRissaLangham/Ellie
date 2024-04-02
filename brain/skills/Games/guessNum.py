""" This file Desiciption can be found in the comment below """
# Author: Marissa Langham
# Date: 03/15/2023
# Description: Guess the Number game file for Ellie
# File Name: guessNum.py

import random
import speech_recognition as sr
from gtts import gTTS
import os



def setDifficultyLevel (userDifficultyLevel):
    if "1" in userDifficultyLevel:
        userDifficultyLevel == 1
    elif "2" in userDifficultyLevel:
        userDifficultyLevel == 2
    elif "3" in userDifficultyLevel:
        userDifficultyLevel == 3
    elif "4" in userDifficultyLevel:
        userDifficultyLevel == 4
    elif "5" in userDifficultyLevel:
        userDifficultyLevel == 5
    return userDifficultyLevel

def getTheMaxNum (maxNum,userDifficultyLevel):
    if 1 in userDifficultyLevel:
        maxNum == 100
    elif 2 in userDifficultyLevel:
        maxNum == 500
    elif 3 in userDifficultyLevel:
        maxNum == 1000
    elif 4 in userDifficultyLevel:
        maxNum == 10000
    elif 5 in userDifficultyLevel:
        maxNum == 100000
    return maxNum

def getTheNum(maxNum, number):
    number = random.randint(1, maxNum)
    return number

    
  