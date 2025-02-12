#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 01:16:49 2025

@author: hassan-riaz
"""

from DSA_Lab_3 import *


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