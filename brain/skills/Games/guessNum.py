""" This file Desiciption can be found in the comment below """
# Author: Marissa Langham
# Date: 03/15/2023
# Description: Guess the Number game file for Ellie
# File Name: guessNum.py

import random
import speech_recognition as sr
from gtts import gTTS
import os


def getTheMaxNum (maxNum,difficultyLevel):
    if 1 in difficultyLevel:
        maxNum == 100
    elif 2 in difficultyLevel:
        maxNum == 500
    elif 3 in difficultyLevel:
        maxNum == 1000
    elif 4 in difficultyLevel:
        maxNum == 10000
    elif 5 in difficultyLevel:
        maxNum == 100000
    return maxNum

def getTheNum(maxNum, number):
    number = random.randint(1, maxNum)
    return number

    
  