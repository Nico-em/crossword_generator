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
    # for list in words:
    #     random.shuffle(list[1]);
    return words

# get size from user
try:
    size = int(input('Input crossword dimension:'))
except ValueError:
    print("Not a number")
words = load()
words = shuffle(words)
#print(words[4])

crossword_problem = CrosswordGenerator(size, words)
