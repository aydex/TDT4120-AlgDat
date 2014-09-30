__author__ = 'adrianh'
from sys import stdin
from heapq import *


def Inf():
    return float(1e3000)


def mst(nm):
    heap = []
    visited = []
    high = 0
    next_node = 0
    root = -Inf()
    while len(visited) != len(nm):
        for e in xrange(0, len(nm[next_node])):
            current_weight = nm[next_node][e]
            if current_weight < Inf() and nm[next_node] not in visited:
                heappush(heap, (current_weight, next_node, e))
                if root > high:
                    high = root
        current_edge = heappop(heap)
        visited.append(nm[current_edge[1]])
        next_node = current_edge[2]
        root = current_edge[0]
    return high


def main():
    linjer = []
    for line in stdin:
        linjer.append(line)
    n = len(linjer)
    nabomatrise = [None] * n
    node = 0
    for linje in linjer:
        nabomatrise[node] = [Inf()] * n
        for k in linje.split():
            data = k.split(':')
            nabo = int(data[0])
            vekt = int(data[1])
            nabomatrise[node][nabo] = vekt
        node += 1
    print mst(nabomatrise)

main()