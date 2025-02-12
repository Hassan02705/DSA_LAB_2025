#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:17:56 2025

@author: hassan-riaz
"""

import array as arr
class AList:
    def __init__(self):
        self.items = arr.array('i',[0 for x in range(5)])
        self.current_size = 0
        self.capacity = 5
    
    def AddLast(self,i):
        if(self.current_size == self.capacity):
            old_capacity = self.capacity
            self.capacity = self.capacity*2
            p = arr.array('i', [0 for x in range(self.capacity)])
            for z in range(old_capacity):
                p[z] = self.items[z]
                
            self.items = p
                    
        self.items[self.current_size] = i
        self.current_size += 1
        
    def GetLast(self):
        return self.items[self.current_size-1]
        
    def Get(self,i):
        return self.items[i]
        
    def Size(self):
        return self.current_size
    
    def RemoveLast(self):
        self.items[self.current_size-1] = 0
        self.current_size -= 1
        
        if(self.current_size/self.capacity < 0.25):
            old_capacity = self.capacity
            self.capacity = self.capacity//2
            p = arr.array('i', [0 for x in range(self.capacity)])
            for z in range(old_capacity):
                p[z] = self.items[z]
                
            self.items = p
