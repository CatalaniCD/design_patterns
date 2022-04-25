#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:07:10 2022

@author: q

___Observer
Def. an object, named the subject, maintains a list of its dependents,
called observers, and notifies them automatically of any state changes, 
usually by calling one of their methods. 

It is mainly used for implementing distributed event handling systems,
in "event driven" software. In those systems, the subject is usually 
named a "stream of events" or "stream source of events", while 
the observers are called "sinks of events". The stream nomenclature 
alludes to a physical setup where the observers are physically 
separated and have no control over the emitted events from the 
subject/stream-source. This pattern then perfectly suits any process 
where data arrives from some input that is not available to the CPU 
at startup, but instead arrives "at random" (HTTP requests, GPIO data,
user input from keyboard/mouse/..., distributed databases and 
blockchains, ...). Most modern programming-languages comprise 
built-in "event" constructs implementing the observer-pattern 
components.

While not mandatory, most 'observers' implementations 
would use background threads listening for subject-events and other 
support mechanisms provided by the kernel (Linux epoll, ...). 

classes
    Subject
    Observers

"""

# import warnings
# warnings.filterwarnings('ignore')
# import threading

import time

class Subject():
    
    def __init__(self):
        self.observers = []
        self.event = self.update_data()
        pass
    
    def update_data(self):
        return time.time_ns()
    
    def update_event(self):
        self.event = self.update_data()
        pass
    
    def notify(self):
        if self.observers:
            for observer in self.observers:
                observer.update(value = self.event)
        pass
    
    def subscribe(self, observer):
        if observer not in self.observers:
            self.observers += [observer]
        pass
    
    def unsubscribe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
        pass


class Observer():
    
    _id = 0
    
    def __init__(self):
        self.id = type(self)._id
        type(self)._id += 1
        pass

    def update(self, value):
        print(f'Observer n : {self.id}, updated value : {value}')
        
    
if __name__ == '__main__':
    
    subject = Subject()
    
    observers = [Observer() for _ in range(4)]

    for observer in observers:
        subject.subscribe(observer = observer)
        
        # th = threading.Thread(target = observer, daemon = False)
        # th.start()
        
    for i in range(3):
        
        subject.update_event()
        subject.notify()
        
        print()
        time.sleep(3)

