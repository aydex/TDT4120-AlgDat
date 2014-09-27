__author__ = 'adrianh'
from sys import stdin

Inf = float(1e3000)


def mst(nm):
    return


def main():
    linjer = []
    for str in stdin:
        linjer.append(str)
    n = len(linjer)
    nabomatrise = [None] * n
    node = 0
    for linje in linjer:
        nabomatrise[node] = [Inf] * n
        for k in linje.split():
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            nabomatrise[node][nabo] = vekt
        node += 1
    print mst(nabomatrise)

main()