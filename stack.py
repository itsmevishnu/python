#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:21:04 2023

@author: vishnujayan
"""

#set the size 
class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.stack = [0 for i in range(size)]
        
    def push(self, value):
        if self.top >= self.size:
            return "Stack overflow"
        self.top +=1
        self.stack[self.top] = value
        return "Succesfully pushed the value"

    def pop(self):
        if self.top == -1:
            return "Nothing to delete"
        self.stack[self.top] = 0
        self.top -= 1
        return f"Successfully poped the last element"
    

stack = Stack(5)
for i in range(1,6):
    print(stack.push(i))
print(stack.stack)

print(stack.pop())
print(stack.stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.stack)
