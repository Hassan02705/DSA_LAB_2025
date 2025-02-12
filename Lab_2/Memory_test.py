#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 01:13:46 2025

@author: hassan-riaz
"""

from DSA_Lab_2 import *

import tracemalloc

# Initialize DLL
dll = Dllist()

# Start tracking memory
tracemalloc.start()

# Add 10,000 items
for i in range(10000):
    dll.AddLast(i)

# Check memory usage after adding
print("Memory usage after adding 10,000 items:", tracemalloc.get_traced_memory())

# Remove 9,999 items
for i in range(9999):
    dll.RemoveFirst()

# Check memory usage after removal
print("Memory usage after removing 9,999 items:", tracemalloc.get_traced_memory())

# Stop tracking memory
tracemalloc.stop()