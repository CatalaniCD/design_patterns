#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 13:47:47 2022

@author: q

___Builder
Def. The intent of the Builder design pattern is to separate 
the construction of a complex object from its representation.

classes
    Director
        .construct
    Builder
        .build
    Product
        Parts
        
"""
import time

class Body():
    model = "SUV"    
    def __repr__(self):
        return type(self).model

class Engine():
    model = "V8"    
    def __repr__(self):
        return type(self).model

class Wheel():
    model = "34x12.50R18LT"    
    def __repr__(self):
        return type(self).model

class Jeep():
    
    def __init__(self):
        self.id = time.time_ns()
        self.body = None
        self.engine = None
        self.wheels = []
        pass
        
    def __repr__(self):
        name = 'Mod.: ' + type(self).__name__
        bodyn = '\nId.: ' + str(self.id)
        body = '\nBody : ' + str(self.body)
        engine = '\nEngine : ' + str(self.engine)
        wheels = '\nWheels : ' + str(self.wheels)
        return name + bodyn + body + engine + wheels 
    
class Builder():
    
    def reset(self):
        pass
    
    def addPart(self):
        pass

    def getProduct(self):
        pass

class JeepBuilder(Builder):
    
    def __init__(self):
        pass

    def reset(self):
        self._product = Jeep()        
        pass
    
    def addPart(self, part):
        
        if isinstance(part, Body):
            self._product.body = part
        
        elif isinstance(part, Engine):    
            self._product.engine = part
            
        elif isinstance(part, Wheel):
            self._product.wheels.append(part)
        pass
    
    def getProduct(self):
        return self._product
            
    
class Director():
    
    __builder = None
    
    def __init__(self, builder : Builder):
        self.__builder = builder()
        pass
    
    def getProduct(self):
        
        self.__builder.reset()

        # car body
        self.__builder.addPart(part = Body())
       
        # car engine
        self.__builder.addPart(part = Engine())
        
        # 4 wheels
        for i in range(4):
            self.__builder.addPart(part = Wheel())
            
        return self.__builder.getProduct()    
        
    
    
if __name__ == '__main__':
    
    dt = Director(builder = JeepBuilder)
    
    print(dt.getProduct())
    print()
    print(dt.getProduct()) 
    