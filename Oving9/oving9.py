from sys import stdin
from collections import deque


def edmonds_karp(N, s, t):
    n = len(N)
    F = [[0] * n for i in xrange(n)]
    while 1:
        P = bfs(N, F, s, t)
        if not P:
            break
        flow = min(N[u][v] - F[u][v] for u, v in P)
        for u, v in P:
            F[u][v] += flow
            F[v][u] -= flow
    return sum(F[s][i] for i in xrange(n))


def bfs(N, F, s, t):
    queue = deque([s])
    paths = {s: []}
    while queue:
        u = queue.popleft()
        for v in xrange(len(N)):
            if N[u][v] - F[u][v] > 0 and v not in paths :
                paths[v] = paths[u] + [(u, v)]
                if v == t:
                    return paths[v]
                queue.append(v)
    return None


def main():
    noder, _, _ = [int(x) for x in stdin.readline().split()]
    startrom = [int(x) for x in stdin.readline().split()]
    utganger = [int(x) for x in stdin.readline().split()]
    nabomatrise = [1]
    noder *= 2
    noder += 2
    nabomatrise[0] = [0]*noder
    for node in startrom:
        nabomatrise[0][node*2+1] = 1
    i = 2
    for linje in stdin:
        v1 = [0] * (noder-1)
        v1.insert(i, 1)
        v2 = [0]
        for node in linje:
            if node == '1' or node == '0':
                v2.append(int(node))
                v2.append(0)
        v2.append(0)
        for x in utganger:
            if (i/2)-1 == x:
                v2[-1] = 1
        nabomatrise.append(v1)
        nabomatrise.append(v2)
        i += 2
    nabomatrise.append([0] * noder)

    print edmonds_karp(nabomatrise, 0, noder-1)
main()