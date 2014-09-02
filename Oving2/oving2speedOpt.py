def d():
    from sys import stdin
    import gc
    gc.disable()
    r = stdin.readline
    r()
    r()
    a = r().strip()
    g = r().strip()
    s = stdin.readlines
    m = map(str.split, s())
    d = 1
    if g == a:
        return 0
    while 1:
        for l in m:
            if l[0] != g:
                if g in set(l):
                    g = l[0]
                    if g == a:
                        return d
                    d += 1
                    break
print d()