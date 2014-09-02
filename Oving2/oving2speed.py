def dfs():
    from sys import stdin
    import gc
    gc.disable()
    r = stdin.readline
    r()
    r()
    rot = int(r())
    goal = int(r())
    s = str.split
    linjer = map(s, stdin.readlines())
    keys = []
    a = keys.append
    for linje in linjer:
        a(linje.pop(0))

    if int(goal) == rot:
        return 0

    dybde = 1

    i = keys.index
    k = keys.remove
    l = linjer.remove
    while 1:
        for key in keys:
            if key != str(goal):
                if str(goal) in set(linjer[i(key)]):
                    goal = key
                    if int(goal) == rot:
                        return dybde
                    dybde += 1
                    l(linjer[i(key)])
                    k(key)
                    break


print dfs()