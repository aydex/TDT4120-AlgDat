__author__ = 'adrianh'
from sys import stdin, stderr


def beste_sti(nm, sans):
    return


def main():
    n = int(stdin.readline())
    sannsynligheter = [float(x) for x in stdin.readline().split()]
    nabomatrise = []
    for linje in stdin:
        naborad = [0] * n
        naboer = [int(nabo) for nabo in linje.split()]
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)
    print nabomatrise
    print beste_sti(nabomatrise, sannsynligheter)

main()