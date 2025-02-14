#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:39:39 2025

@author: hassan-riaz
"""

from DSA_Lab_1 import *

L = SLList()
L.AddFirst(5)
L.AddFirst(10)
L.AddLast(20)
L.AddLast(30)
L.AddLast(40)
L.AddFirst(2)
L.AddFirst(1)
print(L.sentinel.nxt.item) #Expected 1
assert(L.sentinel.nxt.item == 1) #Expected True, no error
print(L.GetFirst()) #Expected 1
print(L.Size()) #Expected 7