from math import floor
#import random

__author__ = 'adrianh'
from sys import stdin


def countingsort(list):
    k = 0
    for i in list:
        if k < i:
            k = i
    counter = [0] * (k+1)
    for i in list:
        counter[i] += 1

    index = 0
    for i in range(len(counter)):
        while 0 < counter[i]:
            list[index] = i
            index += 1
            counter[i] -= 1
    return list


def quicksort(list):
    less = []
    pivot_list = []
    greater = []
    if len(list) <= 1:
        return list
    else:
        pivot = list[-1]
        for i in list:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                pivot_list.append(i)

        less = quicksort(less)
        greater = quicksort(greater)
        return less + pivot_list + greater


def quickquicksort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        return quicksort([x for x in list if x < pivot]) + [x for x in list if x == pivot] + quicksort([x for x in list if x > pivot])


def qsort(list):
    return (qsort([y for y in list[1:] if y < list[0]]) +
            list[:1] +
            qsort([y for y in list[1:] if y >= list[0]])) if len(list) > 1 else list


def finn(list, min, max):
    i = len(list)-1
    if min < list[0]:
        i = 0
        newmin = list[i]
    else:
        while min < list[i]:
            i -= 1
        newmin = list[i]
    if max > list[-1]:
        newmax = list[-1]
    else:
        while max > list[i]:
            i += 1
        newmax = list[i]
    return newmin, newmax


def finn2(list, min, max):
    if min <= list[0]:
        min = list[0]
    else:
        min = [x for x in list if min >= x][-1]
    if max >= list[-1]:
        max = list[-1]
    else:
        max = [x for x in list if max <= x][0]
    return min, max


def main():
    liste = []
    for x in stdin.readline().split():
        liste.append(int(x))

    #print liste
    sortert = quicksort(liste)
    #sortert = qsort(liste)
    #print sortert

    for linje in stdin:
        ord = linje.split()
        minst = int(ord[0])
        maks = int(ord[1])
        resultat = finn(sortert, minst, maks)
        print str(resultat[0]) + " " + str(resultat[1])

main()