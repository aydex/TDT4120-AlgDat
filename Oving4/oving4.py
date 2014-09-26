#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'adrianh'
from sys import *
import traceback

class Node:
    def __init__(self):
        self.visited = False
        self.nr = None

def bygg(nabomatrise):
    p = dict()
    nr = 0
    for linje in nabomatrise:
        n = Node()
        n.nr = nr
        a = []
        for i in xrange(0, len(linje)):
            if linje[i]:
                a.append(i)
        p[n] = a
        nr += 1
    return p

def bfs(p, startnode):
    queue = [startnode]
    visited = set()
    while queue:
        current_node = queue.pop(0)
        for node in p.keys():
            if node.nr == current_node and not node.visited:
                node.visited = True
                visited.add(node.nr)
                for barn in p.get(node):
                    if barn not in visited:
                        queue.append(barn)
                continue
    return visited

def sok(p, node, reachable):
    kanter = 0
    for kant in p.get(node):
        if kant not in reachable:
            kanter += 1
    return kanter


def subgraftetthet(p, startnode):
    noder = 0
    kanter = 0
    reachable = bfs(p, startnode)
    for node in p.keys():
        if node.visited:
            p.pop(node)
    for node in p.keys():
        if not node.visited:
            kanter += sok(p, node, reachable)
            noder += 1
    if noder == 0:
        return 0.0
    else:
        return float(kanter) / float(noder**2)


def main():
    try:
        n = int(stdin.readline())
        nabomatrise = [None] * n  # rader
        for i in range(0, n):
            nabomatrise[i] = [False] * n  # kolonner
            linje = stdin.readline()
            for j in range(0, n):
                nabomatrise[i][j] = (linje[j] == '1')
        for linje in stdin:
            p = bygg(nabomatrise)
            start = int(linje)
            print "%.3f" % (subgraftetthet(p, start) + 1E-12)
    except:
        traceback.print_exc(file=stderr)

main()