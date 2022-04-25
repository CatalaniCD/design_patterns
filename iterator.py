#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:00:28 2022

@author: q

___Iterator

Def. is used to traverse a container and access the container's 
elements. The iterator pattern decouples algorithms from containers;
in some cases, algorithms are necessarily container-specific 
and thus cannot be decoupled.

classes
    iterator

"""

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
            
if __name__ == '__main__':
    
    # create an object
    numbers = PowTwo(10)

    # Using next to get to the next iterator element
    for number in numbers:
        print(number)