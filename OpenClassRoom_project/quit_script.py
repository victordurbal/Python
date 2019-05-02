# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:35:52 2019

@author: VDURBAL
"""
import time
import os
import sys

def attemptToQuit():
    dontQuitScript = True
    while dontQuitScript:
        try:
            wantToQuit = input("Do you want to quit ? (Y/N) : ")
            if wantToQuit.upper() == "N":
                dontQuitScript = False
                break
            elif wantToQuit.upper() == "Y":
                dontQuitScript = False
                print('you are exiting ...')
                time.sleep(2)
                sys.exit()
            else:
                dontQuitScript = True
                try:
                    raise ValueError("invalid input, please try again.")
                except ValueError as wrong_input:
                    print(wrong_input)
        except EOFError:
            dontQuitScript = False
            print('you are exiting ...')
            time.sleep(2)
            sys.exit()
    
    return

def tryagain():
    dontQuitScript = True
    while dontQuitScript:
        try:
            wantToTryAgain = input("Do you want to try again ? (Y/N) : ")
            if wantToTryAgain.upper() == "Y":
                dontQuitScript = False
                break
            elif wantToTryAgain.upper() == "N":
                dontQuitScript = False
                print('you are exiting ...')
                time.sleep(2)
                sys.exit()
            else:
                dontQuitScript = True
                try:
                    raise ValueError("invalid input, please try again.")
                except ValueError as wrong_input:
                    print(wrong_input)
        except EOFError:
            dontQuitScript = False
            print('you are exiting ...')
            time.sleep(2)
            sys.exit()
    
    return