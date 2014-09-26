from sys import *
import traceback
from collections import deque
import gc
gc.disable()

class N():
    def __init__(self):
        self.c = False
        self.n = []

def t(d, r, n):
    for z in d.values():
        z.c = False
    v = 0
    e = 0
    q = deque()
    s = d[r]
    s.c = True
    p = q.popleft
    w = q.append
    w(s)
    while q:
        u = p()
        for h in u.n:
            if not h.c:
                h.c = True
                w(h)
    for m in d.values():
        if not m.c:
            v += 1
        for k in m.n:
            if not k.c:
                e += 1
    if not v:
        return 0.0
    else:
        return e / float(v**2)

def m():
    r = stdin.readline
    try:
        d = {}
        n = int(r())
        m = [None] * n
        for i in xrange(n):
            d[i] = N()
            m[i] = [False] * n
            l = r()
            for j in xrange(n):
                m[i][j] = (l[j] == '1')
        for f in xrange(n):
            w = d[f].n.append
            v = m[f]
            for k in xrange(len(m[i])):
                if v[k]:
                    w(d[k])
        for g in stdin:
            s = int(g)
            print "%.3f" % (t(d, s, n) + 1E-12)
    except:
        traceback.print_exc(file=stderr)

m()
