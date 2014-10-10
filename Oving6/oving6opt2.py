from sys import stdin


def q(a, l, r):
    if l < r:
        v = a[l]
        a[r], a[l] = a[l], a[r]
        s = l
        for i in xrange(l, r):
            if a[i] < v:
                a[s], a[i] = a[i], a[s]
                s += 1
        a[r], a[s] = a[s], a[r]
        q(a, l, s - 1)
        q(a, s + 1, r)


def f(l, m, x):
    i = len(l)-1
    if m < l[0]:
        i = 0
        w = l[i]
    else:
        while m < l[i]:
            i -= 1
        w = l[i]
    if x > l[-1]:
        e = l[-1]
    else:
        while x > l[i]:
            i += 1
        e = l[i]
    return w, e


def main():
    l = (map(int, stdin.readline().split()))
    q(l, 0, len(l)-1)
    for linje in stdin:
        o = linje.split()
        r = f(l, int(o[0]), int(o[1]))
        print r[0], r[1]

main()