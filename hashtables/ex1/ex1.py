#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    if length < 2:
        return None
    
    for i in range(length):
        hash_table_insert(ht, weights[i], [i, limit - weights[i]])
    
    lst = []
    for i in ht.storage:
        if i and i.value[1] in weights:
            lst.append(i.value[0])
            lst.sort(reverse=True)

    return lst
    


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
