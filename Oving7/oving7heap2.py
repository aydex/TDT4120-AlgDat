from sys import stdin


class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heap[i // 2] > self.heap[i]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i //= 2

    def insert(self, i):
        self.heap.append(i)
        self.size += 1
        self.percUp(self.size)

    def percDown(self, i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i*2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.percDown(1)
        return retval


def main():
    from itertools import repeat
    decks = dict()
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        decks[deck[0][1]] = deck
    #print decks
    word = ""
    heap = Heap()
    for deck in decks.values():
        #print "Deck: " + str(decks)
        #print "Inserting " + str(deck[0])
        heap.insert(deck[0])
        if len(deck) > 1:
            #print "Removing " + str(deck[0]) + " from " + str(decks[deck[0][-1]])
            decks[deck[0][-1]][0] = None
        else:
            decks[deck[0][-1]] = None
    while 1:
        #print "Heap: " + str(heap.heap)
        letter = heap.delMin()[-1]
        word += letter
        deck = decks[letter]
        #print "Letter: " + letter
        #print "Deck: " + str(deck)
        if deck:
            i = 0
            for d in deck:
                if d:
         #           print "Inserting " + str(d)
                    heap.insert(d)
                    if len(deck) > 1:
                        decks[letter][i] = None
                    else:
                        decks[letter] = None
                    break
                else:
                    i += 1
        #print word
        if heap.size == 0:
            print word
            return

main()