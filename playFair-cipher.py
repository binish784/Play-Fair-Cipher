# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 15:51:51 2018

@author: Binish125
"""

class playFair:
    
    final_list=[]
        
    def __init__(self):
        w,h=5,5
        self.key=[[0 for x in range(w)] for y in range(h)]
        
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
                row=row+self.key[i][j]+" "                
            print("\t"+row)
            
    def encrypt(self,plain_text):
        print("\nstep 1 : "+ str(self.rule1(plain_text)))
            
    def rule1(self,plain_text):
        new_plain_list=[]
        plain_list=list(plain_text)
        while (len(plain_list)>1):
            new_plain_list.append(plain_list[0])
            if(plain_list[0]!=plain_list[1]):
                new_plain_list.append(plain_list[1])
                del plain_list[1]
            elif(plain_list[0]==plain_list[1]):
                new_plain_list.append('x')
            del plain_list[0]
        if(len(plain_list)==1):
            new_plain_list.append(plain_list[0])
            new_plain_list.append('x')
        return(new_plain_list)
     
        
print("\n\tPlay Fair Cipher\n")    
x=playFair()
x.defineKeyword("monarchy")
x.makeKey()
x.encrypt("balloon")