#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 01:15:06 2025

@author: hassan-riaz
"""

from DSA_Lab_2 import *

L = Dllist()

# Check if list is initially empty
L.IsEmpty()  # Expected: "The list is currently empty."

# Add elements
L.AddFirst(10)
L.AddFirst(20)
L.AddLast(30)
L.AddLast(40)

# Print size after adding elements
L.Size()  # Expected: 4

# Check elements using Get()
print("Get(0):", L.Get(0))  # Expected: 20 (First element)
print("Get(1):", L.Get(1))  # Expected: 10
print("Get(2):", L.Get(2))  # Expected: 30
print("Get(3):", L.Get(3))  # Expected: 40
print("Get(4):", L.Get(4))  # Expected: "Null" (Out of bounds)

# Remove first and last elements
L.RemoveFirst()  # Removes 20
L.RemoveLast()   # Removes 40

# Print size after removals
L.Size()  # Expected: 2

# Check elements after removals
print("Get(0):", L.Get(0))  # Expected: 10
print("Get(1):", L.Get(1))  # Expected: 30
print("Get(2):", L.Get(2))  # Expected: "Null" (Out of bounds)

# Check if list is empty after removing all elements
L.RemoveFirst()  # Removes 10
L.RemoveLast()   # Removes 30

L.IsEmpty()  # Expected: "The list is currently empty."

# Final Size Check
L.Size()  # Expected: 0