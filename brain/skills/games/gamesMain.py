""" This file Desiciption can be found in the comment below """
# Author: Marissa Langham
# Date: 03/21/2023
# Description: Main games file for all games
# File Name: gamesMain.py

"""from skills.games.guessNum import 
from skills.games.snaps import 
from skills.games.twentyQuestions import 
from skills.games.trivia import 
from skills.games.wordAssociation import 
from skills.games.wordle import """

gameList = ["twenty questions", "guess the number", "snaps", "trivia", "word association", "wordle"]

def displayGameList():
    return gameList

def whichGame(item):
    for i, gameList in enumerate(gameList):
        if gameList == item:
           return f"Sure lets play {item} {i}."
    else:
        return f"Oh I am sorry. I do not have the game {item}. please try again."
        