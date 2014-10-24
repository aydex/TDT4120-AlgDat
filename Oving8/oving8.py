__author__ = 'adrianh'
from sys import stdin, stderr


def percUp(self, i):
    while i // 2 > 0:
        if self[i // 2] < self[i]:
            self[i // 2], self[i] = self[i], self[i // 2]
        i //= 2


def insert(self, i):
    self.append(i)
    percUp(self, len(self)-1)


def percDown(self, i):
    while (i * 2) <= len(self)-1:
        mc = minChild(self, i)
        if self[i] < self[mc]:
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


def beste_sti(nm, sans):
    heap = [0]
    heap.append((sans[0], 0))
    val = [0]*(len(nm)+1)
    val[0] = 1
    sti = {0: [0]}
    while len(heap) > 1:
        edge = delMin(heap)
        node = nm[edge[1]]
        #sti.append(edge[1])
        for i in xrange(0, len(node)):
            b = 0
            #print str(node[i]) + "(" + str(i) + ")" + "=" + "1"
            if node[i] == 1:
                #print "true"
                print heap
                print "Val: " + str(val)
                print "Node " + str(nm.index(node)) + ": " + str(node)
                print "Edge:" + str(edge)
                print val[edge[1]],
                print " * ",
                print sans[edge[1]],
                print "(" + str(i) + ")"
                new = val[edge[1]]*sans[edge[1]]
                print new,
                print " - ",
                print val[i]
                if new > val[i]:
                    val[i] = new
                    b = 1
                print heap
                print "------------"
            if b:
                sti[i] = list(sti[edge[1]]) + ['-'] + [i]
                edge = (val[i], i)
                insert(heap, edge)
            #if node[i] == 1 and nm[i] not in visited:
             #   edge = (sans[i], i)
              #  insert(heap, edge)
    print "***" + str(val[-1])
    print val
    return sti[len(nm)-1]



def main():
    n = int(stdin.readline())
    sannsynligheter = [float(x) for x in stdin.readline().split()]
    nabomatrise = []
    for linje in stdin:
        naborad = [0] * n
        naboer = [int(nabo) for nabo in linje.split()]
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)
    result = beste_sti(nabomatrise, sannsynligheter)
    s = ''
    for w in result:
        s += str(w)
    if not result:
        s += "0"
    print s
    return s

main()