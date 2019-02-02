# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 00:12:39 2018

@author: maxwe
"""

import pickle
import os

while(True): 
    print("Type 'exit' at any time to safely exit the program.")
    team_number = input("Enter team number: ")
    if team_number == "exit":
        break
    match_number = input("Enter match number, type 'c' to cancel: ")
    if match_number == "exit":
        break
    elif match_number != "c":  
        scan = input("Press enter to begin scan, type any other value to cancel: ")
        if scan == "exit":
            break
        elif scan == "":
            keyword = True
            pickle.dump((team_number,match_number,keyword), open( "entry data.p", "wb" ))
    keyword = False
    clear = lambda: os.system('cls')
    clear()