""" This file Desiciption can be found in the comment below """
# Author: Marissa Langham
# Date: 03/12/2023
# Description: jokes skill file for Ellie
# File Name: jokes.py

import random
import pyjokes

jokesList = [
    "Why don't scientists trust atoms? Because they make up everything.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "I told my computer I needed a break, and it said... No problem, I'll just go on a little byte.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them."


]

def tellJoke():
    return pyjokes.get_joke()

def tellReallyFunnyJoke():
    return random.choice(jokesList)
