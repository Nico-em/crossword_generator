import time
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

def space_filled(solution):
    size = len(solution[0]) ** 2
    full = 0
    for row in range(len(solution[0])):
        for col in range(len(solution[0])):
            if solution[0][row][col] != " ":
                full += 1

    answer = (full * 100) / size
    return answer


words = load()
wordsSet = set([])
words = shuffle(words)

for size in range(3,16):
    start = time.time()
    crossword_problem = CrosswordGenerator(size, words, wordsSet)
    solution = crossword_problem.backtracking()
    end = time.time()
    perc_filled = space_filled(solution)
    print("\nsize:",size, "\ttime:",end - start, "s\tpercent filled:",perc_filled)
