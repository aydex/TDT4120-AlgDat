from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    toppnode = Node()
    for ord in ordliste:
        print ord[0]
        print ord[1]
        tempnode = Node()
        #if toppnode.barn.has_key(ord[0]):
            #toppnode.barn.update(ord[0], (toppnode.barn[ord[0]], toppnode.)
        toppnode.barn[ord[0]] = tempnode
        for letter in ord:
            pass


def posisjoner(ord, indeks, node):
    pass

try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o, pos) )
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
