__author__ = 'adrianh'
from sys import stdin

def main():
    o = stdin.readline()
    s = stdin.read()
    b = {}
    d = 0
    if len(s) < 50:
        keys = s.split('\n')
        if '?' in s:
            import re

            l = ' %s ' % o.strip()
            for key in filter(None, keys):
                print '%s: %s' % (
                    key, ' '.join(str(a.start()) for a in re.finditer(' %s(?= )' % key.replace('?', '\S'), l)))
        else:
            line = ' %s ' % o.strip()
            for key in filter(None, keys):
                print key + ':',
                key = ' %s ' % key
                n = line.find(key)
                while not n == -1:
                    print n,
                    n = line.find(key, n + 1)
                print
    else:
        o = o.split()
        if '?' in s:
            i = ({}, [])
            for t in o:
                if t not in b:
                    n = i
                    for c in t:
                        if c not in n[0]:
                            n[0][c] = ({},[])
                        n = n[0][c]
                    b[t] = n[1]
                b[t].append(d)
                d += len(t) + 1
        else:
            for t in o:
                if t not in b:
                    b[t] = []
                b[t].append(d)
                d += len(t) + 1
        for r in s.split():
            if r in b:
                y = b[r]
            elif '?' in r:
                noder = [i]
                for c in r:
                    nye = []
                    e = nye.extend
                    a = nye.append
                    for n in noder:
                        if c == '?':
                            e(n[0].values())
                        elif c in n[0]:
                            a(n[0][c])
                    noder = nye
                y = []
                p = y.extend
                for n in noder:
                    p(n[1])
                b[r] = y
            else:
                y = []
                b[r] = y
            y.sort()
            print r + ":",
            for p in y:
                print p,
            print
main()
