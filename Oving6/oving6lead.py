from sys import stdin


def q(a):
    l = []
    p = []
    g = []
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        e = l.append
        f = g.append
        h = p.append
        for i in a:
            if i < pivot:
                e(i)
            elif i > pivot:
                f(i)
            else:
                h(i)
        l = q(l)
        g = q(g)
        return l + p + g


def o(A, v):
    l = 0
    h = len(A)-1
    while l <= h:
        m = (l+h)//2
        if A[m] < v:
            l = m+1
        elif A[m] > v:
            if A[m-1] < v:
                return A[m]
            else:
                h = m - 1
        else:
            return A[m]
    return A[m]


def u(A, v):
    l = 0
    h = len(A)-1
    while l <= h:
        m = (l+h)//2
        if A[m] > v:
            h = m-1
        elif A[m] < v:
            if A[m+1] > v:
                return A[m]
            else:
                l = m + 1
        else:
            return A[m]
    return A[m]


def main():
    l = (map(int, stdin.readline().split()))
    s = q(l)
    i = 0
    a = dict()
    b = dict()
    for linje in stdin:
        w = linje.split()
        m = int(w[0])
        if m not in a:
            a[m] = u(s, m)

        x = int(w[1])
        if x not in b:
            b[x] = o(s, x)

        print a[m], b[x]
main()