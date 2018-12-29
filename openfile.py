from crosswordgenerator import CrosswordGenerator

# load the wordset
def load():
    import pickle
    try:
        file = open("wordbank.bin","rb")
    except IOError as e:
        sys.exit()
    else:
        loadedWords = pickle.load(file)
        file.close()
        return loadedWords

# shuffle the wordset to ensure unique crosswords every program run
def shuffle(words):
    import random
    for l in words:
        random.shuffle(l[1]);
        for w in l[1]:
            wordsSet.add(list(w)[0])

    return words


# get size from user
try:
    size = int(input('Input crossword dimension:'))
except ValueError:
    print("Not a number")

words = load()
wordsSet = set([])
words = shuffle(words)

# run the crossword generator and print the output
crossword_problem = CrosswordGenerator(size, words, wordsSet)
solution = crossword_problem.backtracking()
for line in solution[0]:
    print(line)
for clue in solution[1]:
    print(clue)
