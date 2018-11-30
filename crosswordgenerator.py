"""
This file contains the CrosswordGenerator class. This class will contain the
Constrain Satisfaction problem and find a solution.
crosswordinput.py gets dimensions and wordset and creates and instance of CrosswordGenerator
"""
from random import *

HORIZONTAL = True
VERTICAL = False


class CrosswordGenerator:

    def __init__(self, size, words, wordsSet):
        self.size = size
        self.words = words
        self.words_set = wordsSet
        self.initial_solution = [['']*size for _ in range(size)]
        print(f"size is {self.size}")


    def backtracking(self):
        node_puzzle = Node(self.initial_solution, True)
        # call recursivebacktracker
        return self.recursivebacktracker(node_puzzle)


    def recursivebacktracker(self, node):
        # get first variable - gets position
        # get first Value - finds word
        variable = self.getvariable(node.prevsolution, node.direction)
        word = self.getvalue(node.prevsolution, variable, node.direction)

        # base case
        if(word == None):
            return node.prevsolution

        # make partial_solution
        node.makePartial(variable[0], list(word)[0])

        # call recursivebacktracker
        next = Node(node.prevsolution, not node.direction)
        return self.recursivebacktracker(next)

    # get the word
    def getvalue(self, sol, variable, direction):
        word_size = variable[1]
        # print(variable)
        if(word_size > 15 or word_size < 3):
            return None
        word = self.words[word_size-3][1][0].keys()
        return word

    # get the starting position for word and max size
    def getvariable(self, sol, direction):
        pos = (randint(0, self.size-1), randint(0, self.size-1))

        if (direction == HORIZONTAL):
            return [pos, self.size - pos[1]]
        else:
            return [pos, self.size - pos[0]]



class Node:

    def __init__(self, sol, direction):
        self.prevsolution = sol
        self.direction = direction

    def makePartial(self, position, word):
        x = position[0]
        y = position[1]


        for c in word:
            self.prevsolution[x][y] = c

            if (self.direction == HORIZONTAL):
                y += 1
            else:
                x += 1


    # def checkConstraints
