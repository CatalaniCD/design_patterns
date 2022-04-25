#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:33:09 2022

@author: q

___State
Def. allows an object to alter its behavior when its internal state changes.
This pattern is close to the concept of finite-state machines. 
The state pattern can be interpreted as a strategy pattern, 
which is able to switch a strategy through invocations of methods 
defined in the pattern's interface.

Used to encapsulate varying behavior for the same object, 
based on its internal state. This can be a cleaner way for an object to 
change its behavior at runtime without resorting to conditional statements 
and thus improve maintainability.

classes
    
    Context
        transition_to
        request0
        request1
        
    State
        handle0
        handle1
    
"""

import random

class State():
    
    n = 0
    
    def __init__(self):
        self.id = type(self).n
        type(self).n += 1
        self.context = None
        pass        
    
    def set_context(self, context):
        self.context = context
        pass
    
    def handle0(self):
        print(f'State.id -> {self.id} | ' + 'Handle 0')
        pass
    
    def handle1(self):
        print(f'State.id -> {self.id} | ' + 'Handle 1')
        pass

    def __repr__(self):
        return f'State.id -> {self.id}'
    
class StateA(State):
    
    def __init__(self):
        super().__init__()

    def handle1(self):
        print(f'State.id -> {self.id} | ' + 'Handle 1')
        print(f'StateA transtition to StateB')
        self.context.transition_to(state = StateB())
        pass
    
class StateB(State):
    
    def __init__(self):
        super().__init__()
        pass

    def handle0(self):
        print(f'State.id -> {self.id} | ' + 'Handle 0')
        print(f'StateB transtition to StateA')
        self.context.transition_to(state = StateB())
        pass

class Context():
    
    def __init__(self, state):
        self.transition_to(state = state)
        pass
        
    def transition_to(self, state):
        self.state = state
        self.state.set_context(context = self)
        pass        

    def request0(self):
        self.state.handle0()
        pass
    
    def request1(self):
        self.state.handle1()
        pass

if __name__ == '__main__':
    
    states = [State() for i in range(3)]
    
    print('\n___AvailableStates___\n')
    for state in states:
        print(state)
    
    print('\n___TestStateTransitions___\n')
    for state in states:
        context = Context(state = state)
        if random.uniform(0, 1) > 0.5:
            context.request0()
        else:
            context.request1()
    
    print('\n___AB_StateTransitions___\n')
    state = StateA()
    context = Context(state = state)
    for i in range(5):
        if random.uniform(0, 1) > 0.5:
            context.request0()
        else:
            context.request1()
        
        