#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:32:57 2022

@author: q

___Mediator
Def. object that encapsulates how a set of objects interact.
communication between objects is encapsulated within a mediator object. 
Objects no longer communicate directly with each other, but instead 
communicate through the mediator. This reduces the dependencies between 
communicating objects, thereby reducing coupling. 

ControlTower (Mediator)
Airplane (Component)
Runway (Component)

classes

    Mediator
        *defines the interface for communication 
        between Components objects
        
    Components 
        *defines the interface for communication 
        with other Components through its Mediator

"""

class Component():
    
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name
    
    def receive(self, msg, comp):
        print(f'{comp} ~> {self.name} | received : {msg}')
        pass
    
    def sendResponse(self, msg):
        self.mediator.sendRequest(msg = msg, component = self)
        pass

    def __str__(self):
        return self.name
    
    pass


class Mediator():
    
    def __init__(self):
        self.components = []
        pass
    
    def addComponent(self, comp : Component) -> None:
        if comp not in self.components:
            self.components += [comp]
        pass
    
    def sendRequest(self, msg, component):
        for comp in self.components:
            if comp != component:
                comp.receive(msg = msg, comp = component)

    pass


if __name__ == '__main__':
    
    mediator = Mediator()
    
    comp0 = Component(mediator = mediator, name = 'Node0')
    comp1 = Component(mediator = mediator, name = 'Node1')
    comp2 = Component(mediator = mediator, name = 'Node2')
    
    for comp in [comp0, comp1, comp2]:
        mediator.addComponent(comp = comp)
        
    mediator.sendRequest('GetMarketData()', comp0)
    
    comp2.sendResponse(msg = 'MarketData.csv')
