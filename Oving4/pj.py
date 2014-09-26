from sys import *
import traceback
from collections import deque

class Node():
    def __init__(self):
        self.color = 'w'
        self.nabo = []

def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    noder = 0
    kanter = 0
    d = b(nabomatrise,n)
    q = deque()
    s = d[startnode]
    s.color = 'g'
    q.append(s)
    while q:
        u = q.popleft()
        for v in u.nabo:
            if v.color != 'g':
                v.color = 'g'
                q.append(v)
    for m in d.values():
        if m.color == 'w':
            noder += 1
        for k in m.nabo:
            if k.color == 'w':
                kanter += 1
    if noder == 0:
        return 0.0
    else:
        return float(kanter) / float(noder**2)

def b(nabomatrise,n):
    d = {}
    for i in xrange(n):
        d[i] = Node()
    for j in xrange(n):
        l = nabomatrise[j]
        n = d[j]
        for k in xrange(len(l)):
            if l[k]:
                d[j].nabo.append(d[k])
    return d

def m():
    try:
        n = int(stdin.readline())
        nabomatrise = [None] * n # rader
        for i in range(0, n):
            nabomatrise[i] = [False] * n # kolonner
            linje = stdin.readline()
            for j in range(0, n):
                nabomatrise[i][j] = (linje[j] == '1')
        for linje in stdin:
            start = int(linje)
            print "%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12)
    except:
        traceback.print_exc(file=stderr)

m()
