elements = ["hi", "JOhn", "eliee", "wonderful"]

#word_list = []
#word_list_opp = []

def list_word(arr):
    word_list = []
    for ele in elements:
        for word in ele:
            word_list.append(word)
    return word_list

def list_opposite_word(arr):
    word_list_opp = []
    for i in reversed(elements):
        for word in reversed(i):
            word_list_opp.append(word)
    return word_list_opp

print(list_word(elements))
print(list_opposite_word(elements))



