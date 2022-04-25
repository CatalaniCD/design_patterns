#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:46:05 2022

@author: q

___Proxy
Def. is a class functioning as an interface to something else. 
The proxy could interface to anything: a network connection, 
a large object in memory, a file, or some other resource that 
is expensive or impossible to duplicate. 

In short, a proxy is a wrapper or agent object that is being 
called by the client to access the real serving object behind 
the scenes. 

Use of the proxy can simply be forwarding to the real object, 
or can provide additional logic. In the proxy, extra functionality 
can be provided, for example caching when operations on the real 
object are resource intensive, or checking preconditions before 
operations on the real object are invoked. 

For the client, usage of a proxy object is similar to using 
the real object, because both implement the same interface. 

classes
    Proxy
    Target (Package)

"""

import time

class Package():
    
    def __init__(self):
        self.id = time.time_ns()
        pass
    
    def __repr__(self):
        return f'Package.id : {self.id}'
    

    
class Proxy():
    
    def streamTest(self, stream):
        regular, target = [], []
        for package in stream:
            if package.id % 2 == 0:
                target += [package]
            else:
                regular += [package]
        return regular, target
    
    
if __name__ == '__main__':
    
    response = [Package() for i in range(32)]

    proxy = Proxy()
    
    regular, target = proxy.streamTest(stream = response)
    
    for i in target:
        print(i)
    