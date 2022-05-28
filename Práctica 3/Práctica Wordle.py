LETTER_IN_POS = 0
LETTER_IN_NO_POS = 1
LETTER_NOT_IN = 2
MAX_ATTEMPTS = 6
WORD_LENGTH = 5


def read_words(filename, length):
    """
    This function reads the filename. Each line contains a word.
    This function returns a list with the words with the indicated length
    """
    lst = []
    with open(filename, "r", encoding='utf8') as fwords:
        line = fwords.readline()
        while line != "":
            if len(line) == length+1:
                lst.append(line.strip())
            line = fwords.readline()
    return lst
