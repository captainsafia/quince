"""
This file defines the specification for a Genome that quince will work with.
A Genome is an iterable object that represents a sequence of mutable and 
interchangeable points that represent a particular datum.
"""
class Genome(object):
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values

    def __iter__(self):
        pass
