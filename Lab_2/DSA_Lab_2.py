#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 23:39:17 2025

@author: hassan-riaz
"""

class Node:
    def __init__(self,i):
        self.item = i
        self.nxt  = None
        self.prev = None
        
        
class Dllist:
    def __init__(self):
        self.sentinel = Node(63)
        self.sentinel.prev = self.sentinel
        self.sentinel.nxt  = self.sentinel
        
        self.len = 0
        
    def AddFirst(self,i):
        newfirst          = Node(i)
        oldfirst          = self.sentinel.nxt
        newfirst.prev     = self.sentinel
        newfirst.nxt      = oldfirst
        oldfirst.prev     = newfirst
        self.sentinel.nxt = newfirst
        
        self.len += 1
        
    def AddLast(self,i):
        newlast            = Node(i)
        oldlast            = self.sentinel.prev
        oldlast.nxt        = newlast
        newlast.prev       = oldlast
        newlast.nxt        = self.sentinel
        self.sentinel.prev = newlast
        
        self.len += 1
        
    def IsEmpty(self):
        if self.len == 0:
            print("The list is currently empty.")
            
        else:
            print("The list is not empty.")
            
    def Size(self):
        print("The size of the list is:", self.len)
        
    def Get(self, i):
        if i < 0 or i >= self.len:
            return "Null"
        
        current = self.sentinel.nxt
        
        for x in range(i):
            current = current.nxt
        
        return current.item
        
    def RemoveFirst(self):
        delnode = self.sentinel.nxt
        self.sentinel.nxt = delnode.nxt
        delnode.nxt = self.sentinel
        
        delnode.nxt = None
        delnode.prev = None
        delnode.item = None
        
        self.len -= 1
        
    def RemoveLast(self):
        delnode = self.sentinel.prev
        self.sentinel.prev = delnode.prev
        delnode.prev = self.sentinel
        
        delnode.nxt = None
        delnode.prev = None
        delnode.item = None
        
        self.len -= 1