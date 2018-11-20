"""
gets dimensions from user and wordset - creates and instance of CrosswordGenerator
handles output once crossword is outputted
"""

from crosswordgenerator import CrosswordGenerator

# get size from user
try:
    size = int(input('Input crossword dimension:'))
except ValueError:
    print("Not a number")

# this should be replaced with the actual dataset list
words = []

# crossword generator instance
crossword = CrosswordGenerator(size, words)
