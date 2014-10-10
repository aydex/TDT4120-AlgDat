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


def newqs(list, left, right):
    if left < right:
        pivotIndex = left
        pivotValue = list[pivotIndex]
        list[right], list[pivotIndex] = list[pivotIndex], list[right]
        storeIndex = left
        for i in xrange(left, right):
            if list[i] <= pivotValue:
                list[storeIndex], list[i] = list[i], list[storeIndex]
                storeIndex += 1
        list[right], list[storeIndex] = list[storeIndex], list[right]
        newqs(list, left, storeIndex - 1)
        newqs(list, storeIndex + 1, right)


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


def binover(list, val):
    low = 0
    high = len(list)-1
    while low <= high:
        #print low,
        #print " // ",
        #print high
        mid = (low+high)//2
        if list[mid] < val:
            #print str(list[mid]) + " < " + str(val)
            low = mid+1
        elif list[mid] > val:
            #print str(list[mid]) + " > " + str(val)
            if list[mid-1] < val:
                return list[mid]
            else:
                high = mid - 1
        else:
            return list[mid]
    return list[mid]


def binunder(list, val):
    low = 0
    high = len(list)-1
    while low <= high:
        #print low,
        #print " // ",
        #print high
        mid = (low+high)//2
        if list[mid] > val:
            #print str(list[mid]) + " > " + str(val)
            high = mid-1
        elif list[mid] < val:
            #print str(list[mid]) + " < " + str(val)
            if list[mid+1] > val:
                #print str(list[mid])
                return list[mid]
            else:
                low = mid + 1
        else:
            return list[mid]
    return list[mid]


def main():
    list = []
    for x in stdin.readline().split():
        list.append(int(x))

    #print list
    newqs(list, 0, len(list) - 1)
    #print list
    #sortert = quicksort(liste)
    #sortert = qsort(liste)
    #print sortert
    under = dict()
    over = dict()

    for linje in stdin:
        ord = linje.split()

        minst = int(ord[0])
        if minst not in under:
            under[minst] = binunder(list, minst)

        maks = int(ord[1])
        if maks not in over:
            over[maks] = binover(list, maks)

        print under[minst], over[maks]


main()