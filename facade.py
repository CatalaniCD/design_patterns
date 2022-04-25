#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:30:24 2022

@author: q

__Facade

Object that serves as a front-facing interface masking more 
complex underlying or structural code. A facade can:

1. improve the readability and usability of a software library 
by masking interaction with more complex components behind a 
single (and often simplified) API

2. provide a context-specific interface to more generic 
functionality (complete with context-specific input validation)

3. serve as a launching point for a broader refactor of monolithic 
or tightly-coupled systems in favor of more loosely-coupled code

classes
    MainSystem (Facade)
    SubSystem0
    SubSystem1

"""

class ElectricalSystem():
    
    def __init__(self):
        self.voltage = 0
        self.power = False        
    
    def setVoltage(self, value):
        self.voltage = value
        pass

    def turnOn(self):    
        if not self.power:
            self.power = not self.power
        pass
    
    def turnOff(self):    
        if self.power:
            self.power = not self.power
        pass
    pass

    def __repr__(self):
        return f'\nElectrical System\nPower : {self.power}\nVoltage : {self.voltage} Volts'

class PlumbingSystem():
    
    def __init__(self):
        self.pressure = 0
        self.temp = 0
        
    def setPressure(self, value):
        self.pressure = value
        pass
    
    def setTemperature(self, value):
        self.temp = value
        pass
        
    def __repr__(self):  
        return f'\nPlumbing System\nPressure : {self.pressure} Pa\nTemperature : {self.temp} Fahrenheit'


class House():
    
    def __init__(self):
        self.electrical_sys = ElectricalSystem()
        self.plumbing_sys = PlumbingSystem()
        pass
    
    def turnOnSystems(self):
        self.electrical_sys.setVoltage(value = 110)
        self.electrical_sys.turnOn()
        self.plumbing_sys.setPressure(value = 500)
        self.plumbing_sys.setTemperature(value = 100)
        pass
    
    def turnOffSystems(self):
        self.electrical_sys.setVoltage(value = 0)
        self.electrical_sys.turnOff()
        self.plumbing_sys.setPressure(value = 0)
        self.plumbing_sys.setTemperature(value = 0)
        pass
    
    def __repr__(self):
        return f'House Systems\n{self.electrical_sys}\n{self.plumbing_sys}'
    
    
if __name__ == '__main__':
    
    home = House()
    
    print('\n__PowerOn__\n')
    
    home.turnOnSystems()

    print(home)   
    print()
    
    print('\n__PowerOff__\n')
    
    home.turnOffSystems()

    print(home)   
    
    