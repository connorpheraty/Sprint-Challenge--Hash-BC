#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    temp = hash_table_retrieve(hashtable, "NONE")
    route[0] = temp

    for i in range(length -1):
        j = route[i]
        val = hash_table_retrieve(hashtable, j)
        route[i+1] = val

    return route
