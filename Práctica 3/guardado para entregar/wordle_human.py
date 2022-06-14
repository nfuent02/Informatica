import random

LETTER_IN_POS = 0
LETTER_IN_NO_POS = 1
LETTER_NOT_IN = 2
MAX_ATTEMPTS = 6
WORD_LENGTH = 5


def read_words(filename, wlen):
    with open(filename, encoding="utf8") as f:
        lst = []
        r = f.readline()
        while r != '':
            if len(r.strip('\n')) == wlen:
                lst.append(r.strip('\n'))
            r = f.readline()
        return lst


def get_clues(secret, user_word):
    secret = secret.lower()
    user_word = user_word.lower()
    if len(user_word) != len(secret):
        raise Exception(f'Your answer must be {len(secret)} characters long')
    clues = []
    for i in range(len(secret)):
        if secret[i] == user_word[i]:
            clues.append(0)
        elif user_word[i] in secret:
            clues.append(1)
        else:
            clues.append(2)
    return clues


def are_all_in_pos(answer):
    return answer == [0] * len(answer)


'''--------'''

import random

LETTER_IN_POS = 0
LETTER_IN_NO_POS = 1
LETTER_NOT_IN = 2
MAX_ATTEMPTS = 6
WORD_LENGTH = 5


def read_words(filename, wlen):
    with open(filename, encoding="utf8") as f:
        lst = []
        r = f.readline()
        while r != '':
            if len(r.strip('\n')) == wlen:
                lst.append(r.strip('\n'))
            r = f.readline()
        return lst


def get_clues(secret, user_word):
    secret = secret.lower()
    user_word = user_word.lower()
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for a, b in replacements:
        secret = secret.replace(a, b)
        user_word = user_word.replace(a, b)
    if len(user_word) != len(secret):
        raise Exception(f'Debes introducir una palabra de longitud {len(secret)}')
    clues = []
    s = [m for m in secret]
    uw = [n for n in user_word]
    for i in range(len(s)):
        if s[i] == uw[i]:
            clues.append(0)
        elif uw[i] in s:
            clues.append(1)
        else:
            clues.append(2)
    return clues


def are_all_in_pos(answer):
    return answer == [0] * len(answer)


def human(word_file):
    random.seed()
    words = read_words(word_file, WORD_LENGTH)
    secret = words[random.randint(0, len(words) - 1)]
    game_cont = True
    attempts = 0
    while game_cont:
        user_word = input('Your word: ')
        answer = get_clues(secret, user_word)
        print(answer)
        attempts = attempts + 1
        game_cont = not are_all_in_pos(answer) and attempts < MAX_ATTEMPTS
    if user_word == secret:
        print('Congratulations, you have found the secret word')
    else:
        print(f'Sorry, the secret word was: "{secret}"\nTry again!')


def add_answer(storage, candidate, answer):
    candidate = candidate.lower()
    storage.append(tuple((candidate,answer)))
    return storage
    '''
    candidate = candidate.lower()
    wcand = candidate
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    t = [list(h) for h in storage]
    for a, b in replacements:
        wcand = wcand.replace(a, b)
        for i in range(len(t)):
            t[i][0] = t[i][0].replace(a, b)
    a = [tuple(r) for r in t]
    cand = [i for i in wcand]
    k = 0
    l = 0
    while l < len(cand) and k < len(a):
        if l < len(a[k][0]) - 1:
            if a[k][0][l] < cand[l]:
                k += 1
                l = 0
            elif a[k][0][l] > cand[l]:
                a.insert(k, tuple((wcand, answer)))
                return a
            else:
                l += 1

        else:
            if a[k][0][l] > cand[l]:
                a.insert(k, tuple((wcand, answer)))
                return a
            else:
                l = 0
                k += 1
    if k >= len(a):
        a += tuple((wcand, answer))
    else:
        if len(a[k][0]) == len(cand):
            a.insert(k + 1, tuple((wcand, answer)))
        elif len(a[k][0]) > len(cand):
            a.insert(k, tuple((wcand, answer)))
    return a
    '''


'''
print(add_answer([('antojo', [0, 2, 1, 2, 0]), ('frío', [0, 2, 0, 2, 0]), ('panadería', [0, 2, 0, 2, 0])],'friolero',[0,2,1,2,2,1]))
print(add_answer([('avión', [0, 2, 1, 2, 0]), ('jugo', [0, 2, 0, 2, 0]), ('queso', [0, 2, 0, 2, 0])],'zen',[0,2,1,2,2,1]))
print(add_answer([('avión', [0, 2, 1, 2, 0]), ('jugo', [0, 2, 0, 2, 0]), ('queso', [0, 2, 0, 2, 0])],'zancudo',[0,2,1,2,2,1]))
'''


def is_compatible(storage, word):
    k = 0
    for i in range(len(storage)):
        if get_clues(word, storage[i][0]) != storage[i][1]:
            k += 1
    return k == 0


'''
print(is_compatible([('aviones', [1, 2, 0, 1, 0, 2, 2]), ('arbitro', [1, 2, 0, 2, 1, 2, 1]), ('cochazo', [1, 1, 1, 2, 1, 1, 0])],'zancudo'))
print(is_compatible([('aviones', [1, 2, 0, 1, 0, 2, 2]), ('arbitro', [1, 2, 0, 2, 1, 2, 1]), ('cochazo', [2, 0, 1, 2, 1, 1, 0])],'zancudo'))
print(is_compatible([('aviones', [1, 2, 2, 1, 1, 2, 2]), ('arbitro', [1, 2, 2, 2, 2, 2, 0]), ('cochazo', [1, 1, 1, 2, 1, 1, 0])],'zancudo'))
'''


def next_candidate(storage, words, pos):
    w = pos
    if storage:
        while w < len(words) and not is_compatible(storage, words[w]):
            w += 1
        return w
    else:
        return pos + 1


'''
print(next_candidate([('banco', [2, 0, 2, 2, 0]), ('basto', [2, 0, 0, 2, 0]), ('campo', [2, 0, 2, 2, 0]), ('canto', [2, 0, 2, 2, 0]), \
                      ('cauto', [2, 0, 2, 2, 0]), ('dardo', [2, 0, 1, 2, 0]), ('falso', [2, 0, 2, 1, 0]), ('galgo', [1, 0, 2, 0, 0]), \
                      ('gasto', [1, 0, 0, 2, 0]), ('harto', [2, 0, 1, 2, 0]), ('jaleo', [2, 0, 2, 2, 0]), ('labio', [2, 0, 2, 2, 0]), \
                      ('macho', [2, 0, 2, 2, 0]), ('manto', [2, 0, 2, 2, 0]), ('pacto', [2, 0, 2, 2, 0]), ('parto', [2, 0, 1, 2, 0]), \
                      ('pasto', [2, 0, 0, 2, 0]), ('rasgo', [0, 0, 0, 0, 0]), ('sabio', [1, 0, 2, 2, 0]), ('salto', [1, 0, 2, 2, 0]), \
                      ('santo', [1, 0, 2, 2, 0]), ('tacto', [2, 0, 2, 2, 0]), ('vasto', [2, 0, 0, 2, 0]), ('yazco', [2, 0, 2, 2, 0]), \
                      ('zanco', [2, 0, 2, 2, 0])],['banco', 'basto', 'campo', 'canto', 'cauto', 'dardo', 'falso', 'galgo', \
                                                              'gasto', 'harto', 'jaleo', 'labio', 'macho', 'manto', 'pacto', 'parto', \
                                                              'pasto', 'rasgo', 'sabio', 'salto', 'santo', 'tacto', 'vasto', 'yazco', \
                                                              'zanco'],0))
def prueba():
    k=0
    l=[]
    t=[('cacto', [1, 0, 0, 0, 0]), ('canto', [1, 0, 2, 0, 0]), ('capto', [1, 0, 2, 0, 0]), ('casto', [1, 0, 2, 0, 0]), ('cauto', [1, 0, 2, 0, 0])]
    r=['balto', 'basto', 'cacto', 'canto', 'capto', 'casto', 'cauto', 'danto', 'facto', 'falto', 'fasto', 'gasto', 'harto', 'jacto', 'jauto', 'lacto', 'lasto', 'lauto', 'manto', 'masto', 'nanto', 'pacto', 'palto', 'parto', 'pasto', 'pauto', 'rapto', 'saeto', 'salto', 'santo', 'tacto', 'tanto', 'tasto', 'vasto', 'yanto']
    while k<35 and k is not False:
        s=next_candidate(t,r,k)
        if s:
            l.append(s)
        k=s
    for i in range(len(l)):
        print(f'{r[l[i]]} in position {l[i]}')
prueba()
'''


def get_answer(candidate):
    candidate = candidate.lower()
    print(candidate)
    a = input("Your answer: ")
    a = a.lower()
    k=0
    while k<5 and (len(a) != len(candidate) or a == ''):
        print('You have entered an incorrect answer. Please try again')
        a = input("Your answer: ")
        a = a.lower()
        k+=1
    if k==5:
        print('Please, stop cheating. You are a real pain in the ass to deal with.')
        return
    b = get_clues(a, candidate)
    return b

'''
print(get_answer('Maestro'))
print(get_answer('Amigo'))
print(get_answer(' '))
'''


def computer(words_file):
    pos = 0
    words = read_words(words_file, WORD_LENTGH)
    storage = []
    game_cont = True
    while game_cont:
        pos = next_candidate(storage, words, pos)
        if pos < len(words):
            candidate = words[pos]
            answer = get_answer(candidate)
            add_answer(storage, candidate, answer)
            pos += 1
        game_cont = pos < len(words) and not are_all_in_pos(answer)
    if pos == len(words):
        print('You have chosen an illegal word or have given an incorrect answer')
    else:
        print(f'The secret word is {candidate}')


def computer_vs_computer(filename):
    random.seed()
    with open(filename, encoding="utf8") as f:
        r = f.readlines()
        for i in range(len(r)):
            r[i] = r[i].strip('\n')
        words = r
    secret = words[random.randint(0, len(words) - 1)]
    lords = read_words(filename, len(secret))
    firstword = lords[random.randint(0, len(lords) - 1)]
    storage = [(firstword, get_clues(secret, firstword))]
    game_cont = True
    pos = 0
    attempts = 1
    while game_cont:
        pos = next_candidate(storage, lords, pos)
        if pos < len(lords):
            candidate = lords[pos]
            answer = get_clues(secret, candidate)
            storage = add_answer(storage, candidate, answer)
        attempts += 1
        game_cont = pos < len(lords) and not are_all_in_pos(answer) and attempts < MAX_ATTEMPTS
    if pos == len(lords):
        print('The computer just cheated! Or, maybe, the code\'s wrong')
    else:
        return tuple((secret, storage))


k=(computer_vs_computer(
    '../../../../OneDrive - Universidad Complutense de Madrid (UCM)/Escritorio/Estudios/Matemáticas y Estadística/Informática/Prácticas/Práctica 3/wordle/lemario.txt'))
while len(k[1])<7:
    if len(k[1])==6 and k[0] != k[1][-1][0]:
        print('la máquina ha perdido')
        break
    else:
        k = computer_vs_computer(
            '../../../../OneDrive - Universidad Complutense de Madrid (UCM)/Escritorio/Estudios/Matemáticas y Estadística/Informática/Prácticas/Práctica 3/wordle/lemario.txt')
        print(k)
