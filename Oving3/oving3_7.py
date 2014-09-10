from sys import stdin

line = stdin.readline()
keys = stdin.read()

x = 0
if '?' in keys:
    x = 1
#keys = keys.split('\n')

if len(keys) < 50:
    keys = keys.split('\n')
    if x:
        import re

        l = ' %s ' % line.strip()
        for key in filter(None, keys):
            print '%s: %s' % (
                key, ' '.join(str(a.start()) for a in re.finditer(' %s(?= )' % key.replace('?', '\S'), l)))
    else:
        line = ' %s ' % line.strip()
        for key in filter(None, keys):
            print key + ':',
            key = ' %s ' % key
            n = line.find(key)
            while not n == -1:
                print n,
                n = line.find(key, n + 1)
            print
else:
    line = line.split()
    if x:
        ordbok = {}
        pos = 0
                        
        # Bygger ordlisten. Dersom det finnes '?' blant oppslagene, lager vi ogsa et tre utfra bokstavene i hvert ord.
        if '?' in keys:
            ord_tre = ({}, [])
            for t in line:
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
            for t in line:
                if t not in ordbok:
                    ordbok[t] = []
                ordbok[t].append(pos)
                pos += len(t) + 1
    
        # Gjennomforer oppslagene, ord for ord. Der vi har mulighet, slaar vi direkte opp i ordboken.
        # Skriver ut svarene underveis.
        for ord in keys.split():
            if ord in ordbok:
                posi = ordbok[ord]
            elif '?' in ord:
                # Der det dukker opp '?', maa vi huske paa alle mulighetene
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
    else:
        keys = keys.split('\n')
        def build(line):
            dict = {}
            pos = 0
            for w in line:
                try:
                    dict[w].append(pos)
                except:
                    dict[w] = []
                    dict[w].append(pos)
                pos += len(w) + 1
            return dict

        dict = build(line)
        for key in filter(None, keys):
            print key + ':',
            if key in dict:
                for i in dict[key]:
                    print str(i),
            print
