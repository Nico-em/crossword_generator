import json

# a list for each size
words = [[3,[]], [4,[]], [5,[]], [6,[]], [7,[]], [8,[]], [9,[]], [10,[]], [11,[]], [12,[]], [13,[]], [14,[]], [15,[]]]

def save():
    import pickle
    try:
        file = open("wordbank.bin","wb")
    except IOError as e:
        print(fileName+" does not exist.\n"+e)
        sys.exit()
    else:
        pickle.dump(words, file)
        file.close()

def parseFile(filename):
    import re

    # read the json file from memory: only want word: definition + POS pairs {word: [(definition, POS)], ...}
    # filename example: "wordset-dictionary/data/a.json"
    with open(filename, "r", encoding="utf8") as read_file:
        # data is a dictionary
        data = json.load(read_file)
        read_file.close()

    for word, info in data.items():
        # only care about words between 3 and 15 in length
        word_len = len(word)

        if ((word_len < 3) or (word_len > 15)):
            continue

        # list of meanings from data
        data_definitions = info.get("meanings", None)
        if (data_definitions != None):

            # list for our data - iterate through and append to list
            definitions = []
            for d in data_definitions:
                definition = d.get("def", None)
                pos = d.get("speech_part", None)
                # if there is no definition or pos, get next definition
                if (definition == None or definition.find("slur") >= 0 or definition.find("(offensive") >= 0):
                    continue
                definitions.append((definition, pos))

            # if there are no valid definitions, move onto next word
            if (len(definitions) == 0):
                continue

            # add the word to the words list, size 3 is index 0
            words[word_len - 3][1].append({word: definitions})


# data
def readData():
    print("Reading ...")
    parseFile("wordset-dictionary/data/a.json")
    parseFile("wordset-dictionary/data/b.json")
    parseFile("wordset-dictionary/data/c.json")
    parseFile("wordset-dictionary/data/d.json")
    parseFile("wordset-dictionary/data/e.json")
    parseFile("wordset-dictionary/data/f.json")
    parseFile("wordset-dictionary/data/g.json")
    parseFile("wordset-dictionary/data/h.json")
    parseFile("wordset-dictionary/data/i.json")
    parseFile("wordset-dictionary/data/j.json")
    parseFile("wordset-dictionary/data/k.json")
    parseFile("wordset-dictionary/data/l.json")
    parseFile("wordset-dictionary/data/m.json")
    parseFile("wordset-dictionary/data/n.json")
    parseFile("wordset-dictionary/data/o.json")
    parseFile("wordset-dictionary/data/p.json")
    parseFile("wordset-dictionary/data/q.json")
    parseFile("wordset-dictionary/data/r.json")
    parseFile("wordset-dictionary/data/s.json")
    parseFile("wordset-dictionary/data/t.json")
    parseFile("wordset-dictionary/data/u.json")
    parseFile("wordset-dictionary/data/v.json")
    parseFile("wordset-dictionary/data/w.json")
    parseFile("wordset-dictionary/data/x.json")
    parseFile("wordset-dictionary/data/y.json")
    parseFile("wordset-dictionary/data/z.json")
    print("Finished!")

readData()
