# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:20:03 2019

@author: VDURBAL
"""

import os
import functions
import data
import quit_script
#import csv
import pickle

print('           #########################')
print('')
print("=== Welcome in the hangman game 'HANG BILLY the hanged man' ===")
print('')
print('           #########################')
print('')

playTheHangman = True
curDir = os.getcwd()
dictScore = dict()

#try:
#    with open(file_score + '.txt', "r+") as fileScore:
#        dataScore = fileScore.read()
#except Exception as mssg:
#    print('Error message : ' + mssg)
#    print('creating the file ...')
#    with open(file_score + '.txt', "w+") as fileScore:
#        dataScore = fileScore.read()

# Get the scores, if non existing, create the file
#try:
#    with open(file_score + '.txt') as fileScore:
#         spamreader = csv.reader(fileScore, delimiter=' ')
#         for row in spamreader:
#             a = ':'.join(row)
#             b,c = a.split(':')
#             print(b + ' has score of ' + c)
#             dictScore[b] = c
#except FileNotFoundError as mssgError:
#    print(str(mssgError))
#    print('creating the file ...')
#    with open(file_score + '.txt', "w+") as fileScore:
#        dictScore = dict() 
        

try:
    with open(file_score,'rb') as fileScore:
         my_depickler = pickle.Unpickler(fileScore)
         dictScore = my_depickler.load()
except FileNotFoundError as mssgError:
    print(str(mssgError))
    print('creating the file ...')
    with open(file_score, "w+") as fileScore:
        dictScore = dict() 


# Get player name
try:
    namePlayer = input("please write your name (or input 'quit' to exit) : ").lower()
    
    namePlayer = namePlayer.replace('\\','')
    namePlayer = namePlayer.replace('\n','n')
    if namePlayer == 'quit':
        raise EOFError
except EOFError:
    try:
        attemptToQuit()
    except SystemExit:
        playTheHangman = False

# Get the score list into a dictionary
#sep = ColumnSeperated(dataScore,'\n')
#dictName = dict()
#for iSep in range(len(sep)):
#    strTodict = ColumnSeperated(sep[iSep],' : ')
#    print(strTodict)
#    dictName[strTodict[0]] = strTodict[1]

if namePlayer != 'quit':
    try:
        print('Your name is ' + namePlayer + ' and your latest score is : ' + dictScore[namePlayer])
    except:
        print('You have not been recorded before, your score is now set to 0')
        dictScore[namePlayer] = '0'
        with open(file_score, "wb") as fileScore:
            for iElement in dictScore:
                dataToSave = pickle.Pickler(fileScore)
                dataToSave.dump(dictScore)

# Game start
while playTheHangman:
    
    motCache = random_word(mots)
    
    hiddenWord = '';
    for star in motCache:
        hiddenWord = hiddenWord + '*'
    
    print('\nWord is :  ', hiddenWord, ' [', len(motCache),' letters long]')
    
    chance = chance
    print('you have ', chance,' chances to save Billy')
    listOfLetterUsed = ''
    wordIsDiscovered = False
    toQuit = False
    while chance > 0 and not wordIsDiscovered:
        
        goOnAsking = True
        while goOnAsking:
            try:
                chosenLetter = input("Choose a letter (or type 'quit' to exit) : ").lower()
                while (not chosenLetter.isalpha() or len(chosenLetter) != 1 or chosenLetter in listOfLetterUsed) and chosenLetter != 'quit':
                    if not chosenLetter.isalpha():
                        print('Chosen letter is not a letter, please try again')
                        print('you still have ', chance,' remaining chance')
                    elif len(chosenLetter) > 1:
                        print('Chosen letter is more than one letter, please try again')
                        print('you still have ', chance,' remaining chance')
                    elif chosenLetter in listOfLetterUsed:
                        print('Chosen letter has been tried already, please try again')
                        print('list of letters you tried : ', listOfLetterUsed)
                        print('you still have ', chance,' remaining chance')
                    chosenLetter = input("Choose a letter (or type 'quit' to exit) : ").lower()
                else:
                    if chosenLetter == 'quit':
                        raise EOFError
                    else:
                        print('Chosen letter is : ', chosenLetter)
                    goOnAsking = False
                    break
            except EOFError:
                try:
                    attemptToQuit()
                except SystemExit:
                    toQuit = True
                    goOnAsking = not toQuit
                    chance = 0
                    break
            
        if not toQuit:
            ispartOfStr, placeOfLetter = isInList(motCache,chosenLetter)
            
            if ispartOfStr is False:
                print(chosenLetter, ' is not in the word you need to discover')
            else:
                for placeNbr in placeOfLetter:
                    hiddenWord = replaceStar(hiddenWord,chosenLetter,placeNbr)
            
            if not '*' in hiddenWord:
                wordIsDiscovered = True
            else:
                print('How much you know of the word so far : ', hiddenWord)
                listOfLetterUsed = lettersUsed(listOfLetterUsed,chosenLetter)
                print('list of letters you tried : ', listOfLetterUsed)
                chance = chanceRemaining(chance,ispartOfStr)
                print('you have ', chance,' remaining chance')
    else:
        if wordIsDiscovered:
            print("word was '",motCache,"'")
            print('Well done, Billy is free')
            dictScore[namePlayer] = str(chance)
            print('Your score is now : ' + dictScore[namePlayer])
            print('... Wanna try to hang him again ? ')
        elif chance < 1:
            print('You lost ... and Billy too')
            print("word was '",motCache,"'")
            print('Looks like Billy the hanged man has been hanged')
           
            print('    ------------')
            print('    |/         |')
            print('    |          |')
            print('    |          O')
            print('    |        ----')
            print('    |          |')
            print('    |         / \\')
            print(' ___|_____________')
            
            print('')
            dictScore[namePlayer] = str(0)
            print('Your score is now : ' + dictScore[namePlayer])
            print("Do you want to try again (We'll find another Billy for you) ?")
        
    try:
        with open(file_score, "wb") as fileScore:
            dataToSave = pickle.Pickler(fileScore)
            dataToSave.dump(dictScore)
        tryagain()
    except SystemExit:
        print('See you next time')
        playTheHangman = False
# terminated
