# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 18:23:25 2022

@author: net_g
"""
#Loop back to this point once code finishes
loop = 1

while (loop < 10):
    #All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun= input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
    
    #Displays the story based on the users input
    
    print("---------------------------------")
    print(f"Be kind to your {noun}- footed{p_noun}")
    print(f"Fro a duck may be somebody's {noun2}")
    print(f"Be kind to your{p_noun} in {place}")
    print(f"Where the weather is always{adjective}.") 
    print()
    print(f"You may think that is this the {noun3}")
    print("Well it is.")
    print("---------------------------------")
    
    loop = loop + 1