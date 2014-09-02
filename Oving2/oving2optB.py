from sys import stdin

y = stdin.readline

class N:
    a = None
    b = None
    c = None
    def __init__(self):
        self.a = []
        self.b = False
        self.c = 0


def b(r):
    q = [r]
    while q:
        n = q.pop(0)
        if n.b:
            return n.c
        for b in n.a:
            b.c = n.c + 1
            q.append(b)

f = y().strip()
a = int(y())
n = []

for i in range(a):
    n.append(N())

s = n[int(y())]
r = n[int(y())]
r.b = True

for l in stdin:
    t = l.split()
    x = n[int(t.pop(0))]
    for k in t:
        x.a.append(n[int(k)])


print b(s)
