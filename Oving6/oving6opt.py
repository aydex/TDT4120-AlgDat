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
    l = []
    a = l.append
    for x in stdin.readline().split():
        a(int(x))
    s = q(l)
    for linje in stdin:
        o = linje.split()
        m = int(o[0])
        x = int(o[1])
        r = f(s, m, x)
        print str(r[0]) + " " + str(r[1])

main()