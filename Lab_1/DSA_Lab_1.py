#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:03:24 2025

@author: hassan-riaz
"""

class Node:
    def __init__(self,i):
        self.item = i
        self.nxt  = None
        
class SLList:
    def __init__(self):
        self.sentinel = Node(63)
        self.len = 0
        
    def AddFirst(self, i):
        oldfirst = self.sentinel.nxt
        self.sentinel.nxt = Node(i)
        self.sentinel.nxt.nxt = oldfirst
        self.len += 1
        
        
    def AddLast(self, i):
        
        current = self.sentinel.nxt
        for x in range(self.len-1):
            current = current.nxt
            
        current.nxt = Node(i)
        self.len += 1
        
        
        
    def GetFirst(self):
        return self.sentinel.nxt.item
    
    def Size(self):
        return self.len
        