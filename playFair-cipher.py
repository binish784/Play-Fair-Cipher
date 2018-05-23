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
        self.invertKey=[[0 for x in range(w)] for y in range(h)]
    
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
        
        print("\n\tInverted Key:\n")    
        for i in range(5):
            row=""
            for j in range(5):
                self.invertKey[i][j]=self.key[j][i]
                row=row+self.invertKey[i][j]+" "
            print("\t"+row)
            
    def encrypt(self,plain_text):
        ruleA=self.rule1(plain_text)
        print("\nstep 1 : "+str(ruleA))
        ruleB=self.rule2(ruleA)  
        print("\nstep 2 : "+str(ruleB))
        ruleC=self.rule3(ruleB)
        print("\nstep 3 : "+str(ruleC))
        exit(1)
        
        
    def rule1(self,plain_text):
        new_plain_list=[]
        plain_list=list(plain_text)
        while (len(plain_list)>1):
            list_block=[]
            list_block.append(plain_list[0])
            if(plain_list[0]!=plain_list[1]):
                list_block.append(plain_list[1])
                del plain_list[1]
            elif(plain_list[0]==plain_list[1]):
                list_block.append('x')
            del plain_list[0]
            list_block.append(0)
            new_plain_list.append(list_block)
        if(len(plain_list)==1):
            list_block=[]
            list_block.append(plain_list[0])
            list_block.append('x')
            list_block.append(0)
            new_plain_list.append(list_block)
        return(new_plain_list)
     
    def rule2(self,plain_list):
        for item in plain_list:   
            for i in range(5):
                if(item[0] in self.key[i] and item[1] in self.key[i]):
                    index_0=self.key[i].index(item[0])+1
                    index_1=self.key[i].index(item[1])+1
                    if(index_0==5):
                        index_0=0
                    if(index_1==5):
                        index_1=0
                    item[0]=self.key[i][index_0]
                    item[1]=self.key[i][index_1]
                    item[2]=1
                    break
        return(plain_list)            
             
                 
    def rule3(self,plain_list):
        for item in plain_list:
            if(item[2]==1):
                continue
            else:
                for i in range(5):
                        if(item[0] in self.invertKey[i] and item[1] in self.invertKey[i]):
                            index_0=self.invertKey[i].index(item[0])+1
                            index_1=self.invertKey[i].index(item[1])+1
                            if(index_0==5):
                                index_0=0
                            if(index_1==5):
                                index_1=0
                            item[0]=self.invertKey[i][index_0]
                            item[1]=self.invertKey[i][index_1]
                            item[2]=1
                            break
            return(plain_list)            
                     
                    
                
print("\n    Play Fair Cipher\n")    
x=playFair()
x.defineKeyword("monarchy")
x.makeKey()
x.encrypt("balloon")