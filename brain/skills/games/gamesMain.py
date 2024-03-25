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

gameList = ["twenty questions", "guess the number", "trivia", "word association", "wordle"]

def displayGameList():
    gameListStr = "Here's the games I have:\n"
    for item in gameList:
        gameListStr += f" - {item[0]}\n"
    return gameListStr

def whichGame(item):
    if gameList == item:
           return f"Sure let's play {item} "
    else:
        return f"Oh I am sorry. I do not have the game {item}. please try again."
