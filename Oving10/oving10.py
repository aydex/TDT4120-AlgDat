__author__ = 'adrianh'
from sys import stdin


def korteste_rute(rekkefolge, nb, byer):
    dist = dict()
    for i in xrange(1, byer+1):
        for j in xrange(1, byer+1):
            dist.setdefault((i, j), float(1e3000))
    for v in range(byer):
        dist[(v, v)] = 0
    for u in xrange(byer):
        for v in xrange(byer):
            if nb[u][v] == -1:
                dist[(u, v)] = float(1e3000)
            else:
                dist[(u, v)] = nb[u][v]
    for k in xrange(0, byer):
        for i in xrange(0, byer):
            for j in xrange(0, byer):
                if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]
    retval = 0
    for x in xrange(0, len(rekkefolge)-1):
        retval += dist[(rekkefolge[x], rekkefolge[x+1])]
        if dist[(rekkefolge[x], rekkefolge[x+1])] == float("inf"):
            return "umulig"
    return retval


def main():
    testcases = int(stdin.readline())
    for test in range(testcases):
        byer = int(stdin.readline())
        rekkefolge = [int(by) for by in stdin.readline().split()]
        rekkefolge.append(rekkefolge[0])
        nabomatrise = []
        for by in range(byer):
            nabomatrise.append([int(x) for x in stdin.readline().split()])
        print korteste_rute(rekkefolge, nabomatrise, byer)

main()