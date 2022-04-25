#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:41:13 2022

@author: q

___Singleton

Def. restricts the instantiation of a class to one "single" instance. 
This is useful when exactly one object is needed to coordinate 
actions across the system. 

classes
    Singleton

"""

class Singleton():
    
    __instance = None
    
    def __init__(self):
        if type(self).__instance == None:
            type(self).__instance = self
        else:
            raise ValueError('This Class is a Singleton')
        pass
    
    def get_instance(self):
        if type(self).__instance == None:
            Singleton()
        
        return Singleton.__instance
        
    def __str__(self):
        return "__Singleton__"


if __name__ == '__main__':

    sing = Singleton()
    
    print(sing.get_instance())

    sing = Singleton()


        