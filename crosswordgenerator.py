"""
This file contains the CrosswordGenerator class. This class will contain the
Constrain Satisfaction problem and find a solution.
crosswordinput.py gets dimensions and wordset and creates and instance of CrosswordGenerator
"""


class CrosswordGenerator:

    def __init__(self, size, words):
        self.size = size
        self.words = words
        print(f"size is {size}")
