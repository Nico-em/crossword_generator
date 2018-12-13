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
        self.last_h = [0,0]
        self.last_v = [0,0]
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
        while(word == None):
            variable = self.getvariable(node.prevsolution, node.direction)
            if(variable == None):
                return node.prevsolution
            word = self.getvalue(node.prevsolution, variable, node.direction)

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
        print("in value")
        print(variable)
        if (len(variable[1]) == 0):
            return None
        word_size = variable[1][-1] - 3
        del variable[1][-1]

        if(word_size+3 > 15 or word_size+3 < 3):
            return None

        index = 0
        #while(word_size+3 >= 3):
        while(len(variable[1]) > 0):
            for i in range(0, len(self.words[word_size][1])):
                word = list(self.words[word_size][1][i].keys())[0]
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
                    print(self.words[word_size][1][i])
                    del self.words[word_size][1][i]
                    return word
            word_size = variable[1][-1] - 3
            del variable[1][-1]

        # print(self.words[word_size][1][0])
        # del self.words[word_size][1][0]
        return None

    # get the starting position for word and max size
    def getvariable(self, sol, direction):
        print(f"in variable, {direction}")
        pos =(0,0)

        if direction == HORIZONTAL:
            pos = (self.last_h[0], self.last_h[1])
        else :
            pos = (self.last_v[0], self.last_v[1])
        print(pos)
        sizes = []
        row_start = pos[0]
        col = pos[1]
        for row in range(row_start, len(sol)):
        #for row in range(len(sol)):
            while (col < (len(sol))):
                pos = (row, col)
                # print(pos)
                # self.current_position[0] = pos[0]
                # self.current_position[1] = pos[1]

                if direction == HORIZONTAL:
                    if (pos[1] == self.size - 1):
                        self.last_h[0] = pos[0] + 1
                        self.last_h[1] = 0
                    else:
                        self.last_h[0] = pos[0]
                        self.last_h[1] = pos[1] + 1
                    valid = True
                    # print(f"set prev h: {pos}")
                    if sol[row][col] == " ":
                        # statements for validity
                        if row == 0:
                            if sol[row+1][col] != " ":
                                valid = False
                        elif row == self.size-1:
                            if sol[row-1][col] != " ":
                                valid = False
                        else:
                            if(sol[row-1][col] != " " or sol[row+1][col] != " "):
                                valid = False

                    if(col == 0):
                        if(sol[row][col+1] != " "):
                            valid = False
                    elif(col == self.size-1):
                        if(sol[row][col-1] != " "):
                            valid = False
                    else:
                        if (sol[row][col-1] != " ") or (sol[row][col+1] != " "):
                            valid = False

                    # word size would be < 2 so invalid
                    if(col > self.size-3):
                        valid = False

                    # print(f"H valid: {valid}")
                    if (valid):
                        # if here starting position should be valid
                        for i in range(col+1, self.size):
                            valid2 = True
                            if (sol[row][i] == " "):
                                if (row == 0):
                                    if (sol[row+1][i] != " " ):
                                        valid2 = False
                                        if(len(sizes) != 0):
                                            return [pos, sizes]

                                elif (row == self.size-1):
                                    if (sol[row-1][i] != " " ):
                                        valid2 = False
                                        if(len(sizes) != 0):
                                            return [pos, sizes]

                                else:
                                    if ((sol[row+1][i] != " " or sol[row-1][i] != " ")):
                                        valid2 = False
                                        if(len(sizes) != 0):
                                            return [pos, sizes]
                            # print(f"H valid2: {valid2}")
                            if (valid2):
                                s = i - col +1
                                # everything but last
                                if (i < self.size - 1):
                                    if (sol[row][i+1] == " " and s > 2):
                                        sizes.append(s)
                                # last
                                else:
                                    if (s > 2):
                                        sizes.append(s)
                                        return [pos, sizes]
                            else:
                                break


                else:
                #vertical
                    if (pos[1] == self.size - 1):
                        self.last_v[0] = pos[0] + 1
                        self.last_v[1] = 0
                    else:
                        self.last_v[0] = pos[0]
                        self.last_v[1] = pos[1] + 1
                    valid = True
                    # print(f"set prev v: {pos}")
                    if sol[row][col] == " ":
                        # statements for validity
                        if col == 0:
                            if sol[row][col+1] != " ":
                                valid = False
                        elif col == self.size-1:
                            if sol[row][col-1] != " ":
                                valid = False
                        else:
                            if(sol[row][col-1] != " " or sol[row][col+1] != " "):
                                valid = False

                    if(row == 0):
                        if(sol[row+1][col] != " "):
                            valid = False
                    elif(row == self.size-1):
                        if(sol[row-1][col] != " "):
                            valid = False
                    else:
                        if (sol[row-1][col] != " ") or (sol[row+1][col] != " "):
                            valid = False

                    # word size would be < 2 so invalid
                    if(row > self.size-3):
                        valid = False

                    # print(f"V valid: {valid}")
                    if (valid):
                        # if here starting position should be valid
                        for i in range(row+1, self.size):
                            valid2 = True
                            if (sol[i][col] == " "):
                                if (col == 0):
                                    if (sol[i][col+1] != " "):
                                        valid2 = False
                                        if(len(sizes) != 0):
                                            return [pos, sizes]

                                elif (col == self.size-1):
                                    if (sol[i][col-1] != " "):
                                        valid2 = False
                                        if(len(sizes) != 0):
                                            return [pos, sizes]

                                else:
                                    if ((sol[i][col+1] != " " or sol[i][col-1] != " ")):
                                        valid2 = False
                                        if(len(sizes) != 0):
                                            return [pos, sizes]

                            # print(f"V valid2: {valid2}")
                            if(valid2):
                                s = i - row + 1
                                if (i < self.size - 1):
                                    if (sol[i+1][col] == " " and s > 2):
                                        sizes.append(s)
                                else:
                                    if (s > 2):
                                        sizes.append(s)
                                        return [pos, sizes]
                            else:
                                break
                col += 1
            col = 0
        return None


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
