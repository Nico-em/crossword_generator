from crosswordgenerator import CrosswordGenerator

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
print(wordsSet)

#print(words[4])

crossword_problem = CrosswordGenerator(size, words)
