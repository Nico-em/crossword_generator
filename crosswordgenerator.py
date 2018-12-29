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
        self.clues = []
        print(f"size is {self.size}")


    def backtracking(self):
        node_puzzle = Node(self.initial_solution, True)
        # call recursivebacktracker
        return (self.recursivebacktracker(node_puzzle), self.clues)


    def recursivebacktracker(self, node):
        # getVariable call to find a valid slot to insert word
        variable = self.getvariable(node.prevsolution, node.direction)

        # if no slot found swap direction and look again
        if(variable == None):
            node.direction = not node.direction
            variable = self.getvariable(node.prevsolution, node.direction)
            # both directions failed. return current crossword
            if(variable == None):
                return node.prevsolution
        # get a word for the slot
        word = self.getvalue(node.prevsolution, variable, node.direction)

        # if no word found find a new slot
        while(word == None):
            variable = self.getvariable(node.prevsolution, node.direction)
            if(variable == None):
                node.direction = not node.direction
                variable = self.getvariable(node.prevsolution, node.direction)
                if(variable == None):
                    return node.prevsolution
            word = self.getvalue(node.prevsolution, variable, node.direction)

        # make partial_solution
        node.makePartial(variable[0], word)

        # call recursivebacktracker
        next = Node(node.prevsolution, not node.direction)
        return self.recursivebacktracker(next)

    # getValue finds a word that will not break constraints: does not modify exsisting words
    def getvalue(self, sol, variable, direction):
        word = " "
        x = variable[0][0]
        y = variable[0][1]

        if (len(variable[1]) == 0):
            return None


        while(len(variable[1]) > 0):
            # get largest word size:
            word_size = variable[1][-1] - 3
            del variable[1][-1]
            # get smallest word size:
            # word_size = variable[1][0] -3
            # del variable[1][0]

            # if word size is invalid - no word found
            if(word_size+3 > 15 or word_size+3 < 3):
                return None


            for i in range(0, len(self.words[word_size][1])):
                word = list(self.words[word_size][1][i].keys())[0]
                flag = True
                # check each character against the characters in the crossword
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
                    if (direction == HORIZONTAL):
                        self.clues.append([variable[0], list(self.words[word_size][1][i].values())[0][0], "Horizontal"])
                    else:
                        self.clues.append([variable[0], list(self.words[word_size][1][i].values())[0][0], "Vertical"])
                    del self.words[word_size][1][i]
                    return word

        return None

    # getVariable gets a starting position for word and a size list
    def getvariable(self, sol, direction):
        pos =(0,0)

        if direction == HORIZONTAL:
            pos = (self.last_h[0], self.last_h[1])
        else :
            pos = (self.last_v[0], self.last_v[1])
        sizes = []
        row_start = pos[0]
        col = pos[1]

        # loop through possible row, col starting positions
        for row in range(row_start, len(sol)):
            while (col < (len(sol))):
                pos = (row, col)

                if direction == HORIZONTAL:
                    if (pos[1] == self.size - 1):
                        self.last_h[0] = pos[0] + 1
                        self.last_h[1] = 0
                    else:
                        self.last_h[0] = pos[0]
                        self.last_h[1] = pos[1] + 1
                    valid = True

                    # if starting position is empty check vertical positions for characters - invalid
                    if sol[row][col] == " ":
                        if row == 0:
                            if sol[row+1][col] != " ":
                                valid = False
                        elif row == self.size-1:
                            if sol[row-1][col] != " ":
                                valid = False
                        else:
                            if(sol[row-1][col] != " " or sol[row+1][col] != " "):
                                valid = False
                    # check horizontal positions for characters - invalid
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

                    # if starting position is valid - find valid sizes
                    if (valid):
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
                                    # position adjacent to exsisting word.
                                    if ((sol[row+1][i] != " " or sol[row-1][i] != " ")):
                                        valid2 = False
                                        if(len(sizes) != 0):
                                            return [pos, sizes]

                            # at least one size exists
                            if (valid2):
                                s = i - col + 1
                                # everything but last - append valid size
                                if (i < self.size-1):
                                    if (sol[row][i+1] == " " and s > 2):
                                        sizes.append(s)
                                # last
                                else:
                                    if (s > 2):
                                        sizes.append(s)
                                        return [pos, sizes]
                            else:
                                break

                # similar constraints to horizontal
                else:
                    if (pos[1] == self.size - 1):
                        self.last_v[0] = pos[0] + 1
                        self.last_v[1] = 0
                    else:
                        self.last_v[0] = pos[0]
                        self.last_v[1] = pos[1] + 1
                    valid = True

                    # if starting position is empty check vertical positions for characters - invalid
                    if sol[row][col] == " ":
                        if col == 0:
                            if sol[row][col+1] != " ":
                                valid = False
                        elif col == self.size-1:
                            if sol[row][col-1] != " ":
                                valid = False
                        else:
                            if(sol[row][col-1] != " " or sol[row][col+1] != " "):
                                valid = False
                    # check horizontal positions for characters - invalid
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

                    # if starting position is valid - find valid sizes
                    if (valid):
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
                                    # position adjacent to exsisting word.
                                    if ((sol[i][col+1] != " " or sol[i][col-1] != " ")):
                                        valid2 = False
                                        if(len(sizes) != 0):
                                            return [pos, sizes]

                            # at least one size exists
                            if(valid2):
                                s = i - row + 1
                                # everything but last - append valid size
                                if (i < self.size - 1):
                                    if (sol[i+1][col] == " " and s > 2):
                                        sizes.append(s)
                                # last
                                else:
                                    if (s > 2):
                                        sizes.append(s)
                                        return [pos, sizes]
                            else:
                                break
                col += 1
            col = 0
        # if exsits loops no variable found
        return None

# Node class keeps track of current crossword and word direction
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
