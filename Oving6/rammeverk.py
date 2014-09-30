__author__ = 'adrianh'
from sys import stdin


def sorter(A):
    # Merk: den sorterte lista ma returneres
    ma = []
    return ma


def finn(A, nedre, ovre):
    # Merk: resultatet ma returneres
    ma = []
    return ma


def main():
    liste = []
    for x in stdin.readline().split():
        liste.append(int(x))

    sortert = sorter(liste)

    for linje in stdin:
        ord = linje.split()
        minst = int(ord[0])
        maks = int(ord[1])
        resultat = finn(sortert, minst, maks)
        print str(resultat[0]) + " " + str(resultat[1])

main()