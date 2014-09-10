from sys import stdin

def main():
    ordliste = stdin.readline()
    sok = stdin.read()
    ordbok = {}
    pos = 0
    if len(sok) < 50:
        keys = sok.split('\n')
        if '?' in sok:
            import re

            l = ' %s ' % ordliste.strip()
            for key in filter(None, keys):
                print '%s: %s' % (
                    key, ' '.join(str(a.start()) for a in re.finditer(' %s(?= )' % key.replace('?', '\S'), l)))
        else:
            line = ' %s ' % ordliste.strip()
            for key in filter(None, keys):
                print key + ':',
                key = ' %s ' % key
                n = line.find(key)
                while not n == -1:
                    print n,
                    n = line.find(key, n + 1)
                print
    else:
        ordliste = ordliste.split()
        if '?' in sok:
            ord_tre = ({}, [])
            for t in ordliste:
                if t not in ordbok:
                    n = ord_tre
                    for c in t:
                        if c not in n[0]:
                            n[0][c] = ({},[])
                        n = n[0][c]
                    ordbok[t] = n[1]
                ordbok[t].append(pos)
                pos += len(t) + 1
        else:
            for t in ordliste:
                if t not in ordbok:
                    ordbok[t] = []
                ordbok[t].append(pos)
                pos += len(t) + 1
    
        for ord in sok.split():
            if ord in ordbok:
                posi = ordbok[ord]
            elif '?' in ord:
                noder = [ord_tre]
                for c in ord:
                    nye = []
                    for n in noder:
                        if c == '?':
                            nye.extend(n[0].values())
                        elif c in n[0]:
                            nye.append(n[0][c])
                    noder = nye
                posi = []
                for n in noder:
                    posi.extend(n[1])
                ordbok[ord] = posi
            else:
                posi = []
                ordbok[ord] = posi
            posi.sort()
            print ord + ":",
            for p in posi:
                print p,
            print
main()