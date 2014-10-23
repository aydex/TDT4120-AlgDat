__author__ = 'adrianh'
from sys import stdin, stderr
from collections import deque


def percUp(self, i):
    while i // 2 > 0:
        if self[i // 2] > self[i]:
            self[i // 2], self[i] = self[i], self[i // 2]
        i //= 2


def insert(self, i):
    self.append(i)
    percUp(self, len(self)-1)


def percDown(self, i):
    while (i * 2) <= len(self)-1:
        mc = minChild(self, i)
        if self[i] > self[mc]:
            self[i], self[mc] = self[mc], self[i]
        i = mc


def minChild(self, i):
    if i * 2 + 1 > len(self)-1:
        return i*2
    else:
        if self[i*2] < self[i*2+1]:
            return i*2
        else:
            return i*2+1


def delMin(self):
    retval = self[1]
    self[1] = self[len(self)-1]
    self.pop()
    percDown(self, 1)
    return retval


def bfs(list, heap, sans):
    queue = deque([list[0]])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        print node
        for barn in node:
            if barn > 0 and list[barn] not in visited:
                queue.append(list[barn])
                insert(heap, (list.index(node), list.index(barn)))


def beste_sti(nm, sans):
    heap = []
    bfs(nm, heap)

    return


def main():
    n = int(stdin.readline())
    sannsynligheter = [float(x) for x in stdin.readline().split()]
    nabomatrise = []
    heap = []
    for linje in stdin:
        naborad = [0] * n
        naboer = [int(nabo) for nabo in linje.split()]
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)
    print nabomatrise
    print beste_sti(nabomatrise, sannsynligheter)

main()