#!/usr/bin/python3
class CountedIterator:
    def __init__(self, iterator,counter=0):
        self.iterator = iter(iterator)
        self.counter = counter

    def get_count(self):
        return self.counter

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

    def __iter__(self):
        return self
