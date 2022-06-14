def next_candidate():

def add_answer():


def get_answer(candidate):
    a=input("Introduce tu respuesta: ")
    l=[]
    for i in range(len(a)):
        if a[i]!=' ':
            l.append(a[i])
    return l

print(get_answer(almohada))

def computer(words_file):
    pos = 0
    words = read_words(words_file, WORD_LENTGH)
    storage = []
    game_cont = True
    while game_cont:
        pos = next_candidate(storage, words, pos)
        if pos<len(words):
            candidate = words[pos]
            answer = get_answer(candidate)
            add_answer(storage, candidate, answer)
            pos += 1
        game_cont = pos<len(words) and not are_all_in_pos(answer)
    if pos==len(words):
        print('You have chosen an illegal word or have given an incorrect answer')
    else:
        print(f'The secret word is {candidate}')

