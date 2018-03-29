# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:51:51 2018

@author: Binish125
"""

class playFair:
    
    w,h=5,5
    final_list=[]
        
    def __init__(self):
        self.key=[[0 for x in range(self.w)] for y in range(self.h)]
        
    def defineKeyword(self,key_letters):
        key_letters=key_letters.replace("j","i")
        letters='abcdefghiklmnopqrstuvwxyz'
        letters_list=list(letters)
        key_list=list(key_letters)
        for key in key_list:
            if key not in self.final_list:
                self.final_list.append(key)
        for letter in letters_list:
            if letter not in self.final_list:
                self.final_list.append(letter)

    def makeKey(self):
        print("\n\tKey:\n")
        a=0
        for i in range(5):
            row=""
            for j in range(5):
                self.key[i][j]=self.final_list[a]
                a=a+1
                row=row+self.key[i][j]
            print("\t"+row)
            
x=playFair()
x.defineKeyword("monarchjiji")
x.makeKey()