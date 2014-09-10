from sys import stdin

line = stdin.readline().split()
keys = stdin.read()

if '?' in keys:
    def build(line):
        ll = len
        pos = 0
        dict = {}
        r = 0
        for w in line:
            r = dict
            l = ll(w)
            if w in r:
                r[w].append(pos)
                r = r[l]
                for l in w:
                    r = r[l]
                r[0].append(pos)
            else:
                r[w] = []
                r[w].append(pos)
                if l not in dict:
                    r = dict[l] = {}
                r = dict[l]
                for l in w:
                    if l not in r:
                        r[l] = {}
                    r = r[l]
                r[0] = []
                r[0].append(pos)
            pos += ll(w) + 1
        return dict

    dict = build(line)
    ll = len
    for key in keys.split('\n'):
        l = ll(key)
        if '?' in key and key not in dict and l in dict:
            next = [dict[l]]
            for l in key:
                nodes = next
                next = []
                e = next.extend
                a = next.append
                for node in nodes:
                    if l == '?':
                        e(node.values())
                    elif l in node:
                        a(node[l])
            pos = []
            e = pos.extend
            for n in next:
                e(n[0])
            pos.sort()
            dict[key] = pos
            print '%s: %s' % (key, ' '.join(str(i) for i in pos))
        elif not key == '':
            if key in dict:
                print '%s: %s' % (key, ' '.join(str(i) for i in dict[key]))
            else:
                print '%s: ' % key
else:
    def build(line):
        pos = 0
        dict = {}
        for w in line:
            try:
                dict[w].append(pos)
            except:
                dict[w] = []
                dict[w].append(pos)
            pos += len(w) + 1
        return dict

    dict = build(line)
    for key in filter(None, keys.split('\n')):
        if key in dict:
            print '%s: %s' % (key, ' '.join(str(i) for i in dict[key]))
        else:
            print '%s: ' % key
