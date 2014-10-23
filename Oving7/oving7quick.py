def quicksort(list):
    less = []
    pivot_list = []
    greater = []
    if len(list) <= 1:
        return list
    else:
        pivot = list[-1]
        for i in list:
            if i > pivot:
                less.append(i)
            elif i < pivot:
                greater.append(i)
            else:
                pivot_list.append(i)

        less = quicksort(less)
        greater = quicksort(greater)
        return less + pivot_list + greater


def insertionsort(list):
    for i in xrange(0, len(list)):
        x = list[i]
        j = i
        while j > 0 and list[j-1] < x:
            list[j] = list[j-1]
            j -= 1
        list[j] = x

def main():
    from sys import stdin
    from itertools import repeat
    decks = dict()
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        decks[index] = deck
    word = ""
    #print decks
    sorted = []
    for deck in decks.values():
        sorted.append(deck[0])
        del decks[deck[0][-1]][0]
    sorted = quicksort(sorted)
    #print sorted
    while 1:
        letter = sorted.pop()[-1]
        word += letter
        if len(decks[letter]) > 0:
            sorted.append(decks[letter][0])
            del decks[letter][0]
            insertionsort(sorted)
        elif len(sorted) == 0:
            print word
            return
        #print sorted

main()