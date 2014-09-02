from sys import stdin
from collections import deque

class Node:
    barn = None
    ratatosk = None
    dybde = None
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.dybde = 0


def dfs(rot):
    stack = [rot]
    while stack:
        node = stack.pop()
        if node.ratatosk:
            return node.dybde
        for barn in range(len(node.barn)-1, -1, -1):
            node.barn[barn].dybde = node.dybde + 1
            stack.append(node.barn[barn])


def bfs(rot):
    queue = deque([rot])
    while queue:
        node = queue.popleft()
        if node.ratatosk:
            return node.dybde
        for barn in node.barn:
            barn.dybde = node.dybde + 1
            queue.append(barn)

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []

for i in range(antall_noder):
    noder.append(Node())

start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True

for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print dfs(start_node)