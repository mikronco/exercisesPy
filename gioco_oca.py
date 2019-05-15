#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:53:28 2019

@author: Michele
"""

import random 

def GiocOca(a = "Marco", b = "Paola", c = "Giovanni", *args):
    
    players  = [a,b,c]+ [args[i] for i in range(len(args))]
    
    print("Stanno giocando: ")
    for i in players:
      print(i)
      
    pos = dict(zip(players,[0]*len(players)))
    
    
    t = 1 
    p = dict(zip(players,[0]*len(players)))
    rolling = dict(zip(players,[0]*len(players)))
    
    
    print("Turno 1")
    print("casella:")
    print(pos)
    
    for i in pos.keys():
        
        rolling[i] = random.randint(1,6) + random.randint(1,6)
        pos[i] = pos[i] + rolling[i]
        if (pos[i]%9 ==0 or pos[i] == 6 or ((pos[i]-5)%9 == 0 and (pos[i]-5) != 0)) and pos[i] < 63:
                
                print(i+ " ha trovato un'oca o un ponte!")
                pos[i] = pos[i] + rolling[i]
             
    print("lancio dadi:") 
    print(rolling)
 
    while 63 not in pos.values():
        
        t += 1
        print("Turno " + str(t))
        print("casella:")
        print(pos)
        
        for i in pos.keys():
                                     
            if pos[i] == 42:
                
                pos[i] -= 3
           
            elif pos[i] == 58:
                
                pos[i] = 1
                
            elif pos[i] > 63:
                
                pos[i] = 63 - (pos[i]-63)
            
            elif pos[i] == 19:
                
                if p[i] <3:
                    
                    print(i + " prigioniero!")
                    pos[i] = pos[i]
                    p[i] +=1 
                else:
                     rolling[i] = random.randint(1,6) + random.randint(1,6)
                     pos[i] = pos[i] + rolling[i]  
                     print(i + " libero!")
                         
            elif pos[i] == 31 or pos[i] == 52:
                 
                 
                 if pos[i] not in {j:pos[j] for j in pos if j!=i}.values():
                      
                      print(i + " prigioniero!")
                      pos[i] = pos[i]
                 
                 else:
                     
                     print(i + " libero!")
                     rolling[i] = random.randint(1,6) + random.randint(1,6)
                     pos[i] = pos[i] + rolling[i]
                      
            else: 
                 rolling[i] = random.randint(1,6) + random.randint(1,6)
                 pos[i] = pos[i] + rolling[i]
                 if (pos[i]%9 ==0 or pos[i] == 6 or ((pos[i]-5)%9 == 0 and (pos[i]-5) != 0)) and pos[i] < 63:
                
                    print(i+ " ha trovato un'oca o un ponte!")
                    pos[i] = pos[i] + rolling[i]
            
        print("lancio dadi:")
        print(rolling)        
     
            
   
    for i in pos.keys():    
        
        if pos[i] == 63:
            
            print("Il vincitore e' " + i)
            break             
        
           
                
                
            
        