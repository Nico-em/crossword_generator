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

words = load()
words = shuffle(words)
print(words[4])
