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


def q2(a):
    if len(a) <= 1:
        return a
    else:
        p = a[0]
        return q([x for x in a if x < p]) + [x for x in a if x == p] + q([x for x in a if x > p])


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
    s = q(l)
    for linje in stdin:
        o = linje.split()
        r = f(s, int(o[0]), int(o[1]))
        print r[0], r[1]
main()