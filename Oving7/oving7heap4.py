def percUp(self, i):
    while i // 2 > 0:
        if self[i // 2] > self[i]:
            self[i // 2], self[i] = self[i], self[i // 2]
        i //= 2


def insert(self, i):
    self.append(i)
    percUp(self, len(self)-1)


def percDown(self, i):
    while (i * 2) <= len(self)-1:
        mc = minChild(self, i)
        if self[i] > self[mc]:
            self[i], self[mc] = self[mc], self[i]
        i = mc


def minChild(self, i):
    if i * 2 + 1 > len(self)-1:
        return i*2
    else:
        if self[i*2] < self[i*2+1]:
            return i*2
        else:
            return i*2+1


def delMin(self):
    retval = self[1]
    self[1] = self[len(self)-1]
    self.pop()
    percDown(self, 1)
    return retval


def main():
    from itertools import repeat
    from sys import stdin
    decks = dict()
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        deckr = []
        for i in reversed(deck):
            deckr.append(i)
        decks[deck[0][1]] = deckr
    #print decks
    word = ""
    heap = []
    for deck in decks.values():
        #print "Deck: " + str(decks)
        #print "Inserting " + str(deck[0])
        letter = deck[-1][-1]
        insert(heap, deck.pop())
        if len(deck) < 1:
            decks[letter] = None
    while 1:
        #print "Heap: " + str(heap.heap)
        letter = delMin(heap)[-1]
        word += letter
        deck = decks[letter]
        #print "Letter: " + letter
        if deck:
            insert(heap, decks[letter].pop())
            if len(deck) < 1:
                decks[letter] = None
        if len(heap)-1 == 0:
            print word
            return

main()