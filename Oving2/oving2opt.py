from sys import stdin


class N:
    a = None
    b = None
    c = None
    def __init__(self):
        self.a = []
        self.b = False
        self.c = 0


def d(r):
    e = [r]
    while e:
        f = e.pop()
        if f.b:
            return f.c
        for b in range(len(f.a)-1, -1, -1):
            f.a[b].c = f.c + 1
            e.append(f.a[b])


def b(r):
    q = [r]
    while q:
        n = q.pop(0)
        if n.b:
            return n.c
        for b in n.a:
            b.c = n.c + 1
            q.append(b)

f = stdin.readline().strip()
a = int(stdin.readline())
n = []

for i in range(a):
    n.append(N())

s = n[int(stdin.readline())]
r = n[int(stdin.readline())]
r.b = True

for l in stdin:
    t = l.split()
    x = n[int(t.pop(0))]
    for k in t:
        x.a.append(n[int(k)])

if f == 'dfs':
    print d(s)
elif f == 'bfs':
    print b(s)
elif f == 'velg':
    print d(s)