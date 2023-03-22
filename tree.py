#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:42:37 2023

@author: vishnujayan
"""

class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        

def implement_tree():
    root = Tree("Institute")
    
    civil =  Tree("Civil")
    
    mechanical = Tree('Mechanical')
    
    root.add_child(civil)
    root.add_child(mechanical)
    

if __name__ == '__main__':
    implement_tree()
