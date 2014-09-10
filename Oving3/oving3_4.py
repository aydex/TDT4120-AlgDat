from sys import stdin
import sys

l = ' %s ' % stdin.readline().strip()

for k in stdin:
    k = k.strip()
    s = '%s:' % k
    if '?' in k:
        k = k.split('?')
        k0 = k.pop(0)
        pos = []
        n = 0
        while 1:
            f = 0
            m = l.find(' %s' % k0, n)
            if m == -1:
                break
            n = m + len(k0) + 2
            for i in k:
                if not l.find(i, n) == n:
                    break
                n += len(i)
                if i == k[-1] and l[n] == ' ':
                    f = 1
            if f == 1:
                s = '%s %s' % (s, str(m))
    else:
        k = ' %s ' % k
        n = l.find(k)
        while not n == -1:
            s = '%s %s' % (s, str(n))
            n = l.find(k, n + 1)
    print s
