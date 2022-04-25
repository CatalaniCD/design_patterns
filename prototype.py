#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:55:06 2022

@author: q

___Prototype

Def. It is used when the type of objects to create is determined 
by a prototypical instance, which is cloned to produce new objects.
This pattern is used to avoid subclasses of an object creator in 
the client application, like the factory method pattern does 
and to avoid the inherent cost of creating a new object in 
the standard way (e.g., using the 'new' keyword) 
when it is prohibitively expensive for a given application. 

classes
    Prototye
        .clone()
"""

from abc import ABC, abstractmethod
import time
import copy
import random

class Prototype(): # abstract class
    
    def __init__(self):
        self.energy = 10
        self.size = 10        
        pass
    
    @abstractmethod
    def clone():
        pass
    

class Cell(Prototype): # concrete class

    def __init__(self):
        super().__init__()
        self.dna = hex(time.time_ns())
        self.level = random.uniform(a = 0, b = 1)
        pass
         
    # clone method
    def clone(self):
        return copy.deepcopy(self)        
    
    def interact(self, other):  
        """ Interaction between cells
        Similar Cells add to each other
        """
        diff = abs(self.level - other.level)
        if diff == 0:
           self.size += 1
        if diff < 0.5:
           self.energy += 1
           other.energy += 1
        else:
            self.energy -= 1
            other.energy -= 1
        return self.test_energy()
        
    def test_energy(self):
        """ Energy based event -> Die or Reproduce """
        if self.energy >= 15:
            self.energy = 5
            return self.clone()
        else:
            return None
        
    def __str__(self):
        return str(vars(self))
    
    
def append_object(elem, array, obj):   
    if isinstance(elem, obj) and elem.energy > 0 :
        array += [elem]
    
if __name__ == '__main__':
    
    print('\n___Cell Reproduction and Survival___\n')
    
    cells = [Cell() for i in range(100)]

    colony = lambda x: len(x) < 10000

    while cells and colony(cells):
        
        # pick a random cell
        random.shuffle(cells)
        cell = cells.pop()
        
        # interact with all others
        for other in cells:
            # test for cell repr or die
            new = cell.interact(other = other)
            # add if apply
            append_object(new, cells, Cell)
        # add if apply
        append_object(cell, cells, Cell)
    
    most = {}
    for cell in cells:
        if cell.dna not in most:
            most[cell.dna] = 1
        else:
            most[cell.dna] += 1
    
    for k, v in sorted(most.items(), key = lambda x: x[1], reverse = True)[:12]:
        print(f'{k} ~> {v}')
    
    
    
    