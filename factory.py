#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:27:26 2022

@author: q

___FactoryMethod

Def. deal with the problem of creating objects without having 
    to specify the exact class of the object that will be created.

Classes
    Creator
    Product

"""

import time
import random

class Transport():
    
    def __init__(self):
        self.path = []
        self.id = time.time_ns()
        pass
    
    def addPath(self, path):
        self.path += path
        pass
    
    def step(self):
        if self.path:
            return self.path.pop(0)
        else:
            raise ValueError('No path available')

class Ship(Transport):
    
    def __init__(self):
        super().__init__()
        pass
    
    def __repr__(self):
        return f'Bulk Carrier Ship\nid : {self.id}\nTrack : {self.path}' 

class Aircraft(Transport):
    
    def __init__(self):
        super().__init__()
        pass
    
    def __repr__(self):
        return f'Heavy Cargo Aircraft\nid : {self.id}\nTrack : {self.path}' 



class Logistics():
    
    def __init__(self):
        self.plan = []
        pass
        
    def planDelivery(self, nodes):
        self.plan += nodes
        pass
    
    def createSeaTransport(self):
        ship = Ship()
        ship.addPath(path = self.plan)
        return ship
        
    def createAirTransport(self):
        ship = Aircraft()
        ship.addPath(path = self.plan)
        return ship
    
    
if __name__ == '__main__':
    
    
    path = ['BuenosAires', 'Rio de Janeiro', 'Lisbon', 'London', 'Hamburg']
    
    agency = Logistics()
    agency.planDelivery(nodes = path)
    for i in range(3):
        random.shuffle(agency.plan)
        ship = agency.createSeaTransport()
        print(ship)
    print()

    for i in range(3):
        random.shuffle(agency.plan)
        aircraft = agency.createAirTransport()
        print(aircraft)

