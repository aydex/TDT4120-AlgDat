class Heap:
    def __init__(self):
        self.heap = [0]

    def percUp(self, i):
        while i // 2 > 0:
            if self.heap[i // 2] > self.heap[i]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i //= 2

    def insert(self, i):
        self.heap.append(i)
        self.percUp(len(self.heap)-1)

    def percDown(self, i):
        while (i * 2) <= len(self.heap)-1:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > len(self.heap)-1:
            return i*2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[len(self.heap)-1]
        self.heap.pop()
        self.percDown(1)
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
    heap = Heap()
    for deck in decks.values():
        #print "Deck: " + str(decks)
        #print "Inserting " + str(deck[0])
        letter = deck[-1][-1]
        heap.insert(deck.pop())
        if len(deck) < 1:
            decks[letter] = None
    while 1:
        #print "Heap: " + str(heap.heap)
        letter = heap.delMin()[-1]
        word += letter
        deck = decks[letter]
        #print "Letter: " + letter
        if deck:
            heap.insert(decks[letter].pop())
            if len(deck) < 1:
                decks[letter] = None
        if len(heap.heap)-1 == 0:
            print word
            return

main()