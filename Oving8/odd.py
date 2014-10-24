from sys import stdin, stderr

def he(A,i,j):
    m = i
    l = 2*i + 1
    r = 2*i + 2
    if l < j and A[l] > A[m]:
        m = l
    if r < j and A[r] > A[m]:
        m = r
    if m != i:
        A[i],A[m] = A[m],A[i]
        he(A,m,j)


def dj(d, p, sans,n):
    val = [0]*(n+1)
    val[0] = 1
    h = [(sans[0],0)]
    j = 1
    s = set([])
    s.add(0)
    while j > 0:
        u = h[0]
        h[0] = h[j-1]
        j -= 1
        h.pop()
        he(h,0,j)
        for g in d[u[1]]:
            b = 0
            print "true"
            print h
            print "Val: " + str(val)
            print "Node " + str(u[1]) + ": " + str(d[u[1]])
            print "Edge:" + str(u)
            print val[u[1]],
            print " * ",
            print sans[u[1]],
            print "(" + str(g) + ")"
            new = val[u[1]]*sans[u[1]]
            print new,
            print " - ",
            print val[g]
            if new > val[g]:
                val[g] = new
                b = 1
            print h
            print "----------"
            if b:
                p[g] = list(p[u[1]]) + ['-'] + [g]
                j += 1
                h.append((val[g],g))
                i = j - 1
                k = (val[g],g)
                while k > 0 and h[i/2] < h[i]:
                    h[i],h[i/2] = h[i/2],h[i]
                    i = i/2
            s.add(g)
    print val
    return p[n-1]

def ma():
    re = stdin.readline
    n = int(re())
    sans = map(float,re().split())
    nm = []
    i = 0
    d = {}
    p = {}
    for linje in stdin:
        d[i] = map(int,linje.split())
        p[i] = []
        i += 1
    p[0] = [0]
    w = dj(d,p,sans,n)
    s = ''
    for v in w:
        s += str(v)
    if not w:
        s += str(0)
    return s

print ma()