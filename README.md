## Automatic Crossword Generator

**Description:**

A description of your project follows. A good description is clear, short, and to the point. Describe the importance of your project, and what it does.
This project generates a crossword with an undefined layout using a wordset, https://github.com/wordset/wordset-dictionary, and a size passed into the terminal by the user. The generated crosswords are square and only contain word of length 3 to 15. This means no adjacent words are allowed and the resulting crossword is grid-like.


**Table of Contents:**

.gitignore: wordset put here, see link in description for wordset.

crosswordgenerator.py: contains the constrain satisfaction problem and generates the crossword.

datasetparser.py: reads the dataset and builds a list of lists, each for unique word size (form 3-15) containing dictionaries of word:list of meanings pairs. This data-structure is pickled.

openfile.py: This file reads in the data, shuffles it and asks the user for a size. It provides crosswordgenerator with necessary information to create the crossword and prints it.

README.md


**Usage:**

First the wordset need to be cloned: https://github.com/wordset/wordset-dictionary in crossword_generator/. Then datasetparser.py should be run then finally openfile.py to create a crossword.


**Credits:**

Nico-em

igriffin415
