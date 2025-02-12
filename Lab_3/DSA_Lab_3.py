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

            
# The following is the test code

a = AList() # Creates a list

for i in range(10,110,10): # Adds 10 elements to the last of the list
    a.AddLast(i)


print("The first element is:", a.Get(0)) # Should print 10
print("The last element is:", a.GetLast()) # Should print 100
print("Element at index 1 is:", a.Get(1)) # Should print 20
print("Element at index 4 is:", a.Get(4)) # Should print 50
print("Element at index 7 is:", a.Get(7)) # Should print 80
print("Size:", a.Size())  # Should print 10


a.RemoveLast()
print("After removing last, the new last element is:", a.GetLast())  # Should print 90
print("Size after removal:", a.Size())  # Should print 9

a.RemoveLast()
print("After removing last, the new last element is:", a.GetLast())  # Should print 80
print("Size after removal:", a.Size())  # Should print 8

a.RemoveLast()
print("After removing last, the new last element is:", a.GetLast())  # Should print 70
print("Size after removal:", a.Size())  # Should print 7

a.RemoveLast()
print("After removing last, the new last element is:", a.GetLast())  # Should print 60
print("Size after removal:", a.Size())  # Should print 6

print("The final size is:", a.Size()) # Should Print 6
print("The first element is:", a.Get(0)) # Should Print 10
print("The last element is:", a.GetLast()) # Should Print 60