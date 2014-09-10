from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    toppnode = Node()
    for ord in ordliste.keys():
        tempnode = toppnode
        last = ord[-1]
        for i in ord:
            if i not in tempnode.barn.keys():
                node = Node()
                tempnode.barn[i] = node
                if i == last:
                    node.posi.extend(ordliste.get(ord))
                tempnode = node
            elif i == last:
                tempnode.barn[i].posi.extend(ordliste.get(ord))
            else:
                tempnode = tempnode.barn[i]
    return toppnode


def posisjoner(ord, indeks, node):
    retlist = []
    if indeks == len(ord):
        retlist.extend(node.posi)
        return retlist
    if ord[indeks] == '?':
        for node in node.barn.values():
            retlist.extend(posisjoner(ord, indeks + 1, node))
    if ord[indeks] in node.barn.keys():
        retlist.extend(posisjoner(ord, indeks + 1, node.barn[ord[indeks]]))
    return retlist

try:
    ord = stdin.readline().split()
    ordliste = {}
    pos = 0
    for o in ord:
        if o not in ordliste:
            ordliste[o] = [pos]
        else:
            ordliste[o].append(pos)
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)
