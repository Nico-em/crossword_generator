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
        self.initial_solution = [[' ']*size for _ in range(size)]
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
        if(word == None or (not list(word))):
            return node.prevsolution

        # make partial_solution
        node.makePartial(variable[0], word)

        # call recursivebacktracker
        next = Node(node.prevsolution, not node.direction)
        return self.recursivebacktracker(next)

    # get the word
    def getvalue(self, sol, variable, direction):
        word = " "
        x = variable[0][0]
        y = variable[0][1]
        word_size = variable[1] - 3
        print(variable)
        if(word_size+3 > 15 or word_size+3 < 3):
            return None

        index = 0
        while( word_size+3 >= 3):
            for i in self.words[word_size][1]:
                word = list(i.keys())[0]
                flag = True
                for j in range(word_size + 3):
                    if (direction == HORIZONTAL):
                        if(sol[x][y+j] != " " and word[j] != sol[x][y+j] ):
                            flag = False
                            break
                    else:
                        if(sol[x+j][y] != " " and word[j] != sol[x+j][y] ):
                            flag = False
                            break
                if flag == True:
                    # del self.words[variable[1]-3][1][0][word]
                    print(word)
                    return word
            word_size -= 1

        print(word)
        # print(self.words[variable[1]-3][1][0][word])
        # del self.words[variable[1]-3][1][0][word]
        return None

    # get the starting position for word and max size
    def getvariable(self, sol, direction):
        pos = (randint(0, self.size-1), randint(0, self.size-1))
        # pos = (0,0)
        # for row in range(len(sol)):
        #     for col in range(len(sol)):
        #         pos = (row, col)
        #         #check constriants
        #         if direction == HORIZONTAL:
        #             if sol[row][col] != " ":
        #                 return [pos, self.size - pos[1]]
        #             if (row -1 != 0 and sol[row-1][col] != " ") or (row + 1 < len(sol) and sol[row+1][col] != " "):
        #                 continue
        #             else:
        #                 return [pos, self.size - pos[1]]
        #         else:
        #             if sol[row][col] != " ":
        #                 return [pos, self.size - pos[1]]
        #             elif (col -1 != 0 and sol[row][col-1] != " ") or (col + 1 < len(sol) and sol[row][col+1] != " "):
        #                 continue
        #             else:
        #                 return [pos, self.size - pos[1]]

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
