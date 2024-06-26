def load_vocab(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        words = sorted (set ([ line . strip () . lower () for line in lines ]) )
    return words
words = load_vocab('./vocab.txt')

