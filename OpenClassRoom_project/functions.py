# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:23:22 2019

@author: VDURBAL
"""

from random import *
from math import ceil
import sys
import os

## determine the word to be find
def random_word(mots):
    
    nb_mots = len(mots)
    
    return mots[randrange(nb_mots)]

## verify if letter chosen by user is part of the word, and if it is, how many times and where
def isInList(stringRef,choix):
    
    intermediate = stringRef.find(choix)
    letterInString = [intermediate]
    whileControl = True
    
    while whileControl:
        intermediate = stringRef[letterInString[-1]+1:].find(choix)
        if intermediate == -1:
            whileControl = False
        else:
            letterInString = letterInString + [letterInString[-1] + 1 + intermediate]
    
    if letterInString[0] is -1:
        ispartOfStr = False
        
    else:
        ispartOfStr = True
        
    return ispartOfStr, letterInString

## show the discovered word so far
def replaceStar(hiddenWord,correctLetter,placeNbr):
    
    hiddenWord = hiddenWord[:placeNbr] + correctLetter + hiddenWord[placeNbr+1:]
    
    return hiddenWord

## remaining chance
def chanceRemaining(nChance,ispartOfStr):
    if ispartOfStr:
        remainC = nChance
    elif nChance < 1:
        remainC = 0
    else:
        remainC = nChance - 1
        
    return remainC

## store already tried letters
def lettersUsed(lettersPrev,letterTried):
    
    if lettersPrev is '':
        letters = [letterTried]
    else:
        letters = lettersPrev + [letterTried]
    
    return letters

## score management
def ColumnSeperated(stringToSperate,separator):
    
#    separator = '\n'
#    separator = ' : '
    listSeparated = []
    enumPlace = []
    for letter, _ in enumerate(stringToSperate):
        if stringToSperate[letter:letter + len(separator)] == separator:
            enumPlace = enumPlace + [letter]
         
    enumPlace = [0] + enumPlace
#    stringToSperate = stringToSperate.replace(separator,'')
    
    for iLetter in range(1,len(enumPlace)):
        listSeparated = listSeparated + [stringToSperate[enumPlace[iLetter-1]:enumPlace[iLetter]]]
      
    listSeparated = listSeparated + [stringToSperate[enumPlace[-1]:]]
    
    for nElement in range(len(listSeparated)):
        listSeparated[nElement] = listSeparated[nElement].replace(separator,'')
    
    while '' in listSeparated:
        listSeparated.remove('')
    
    return listSeparated
