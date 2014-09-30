__author__ = 'adrianh'
from sys import stdin

def qsort(list):
    return (qsort([y for y in list[1:] if y < list[0]]) +
            list[:1] +
            qsort([y for y in list[1:] if y >= list[0]])) if len(list) > 1 else list


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


def finn(list, min, max):
    if min <= list[0]:
        min = list[0]
    else:
        min = [x for x in list if min >= x][-1]
    if max >= list[-1]:
        max = list[-1]
    else:
        max = [x for x in list if max <= x][0]
    return min, max


def finn2(list, min, max):
    # Merk: resultatet ma returneres
    i = len(list)-1
    if min < list[0]:
        i = 0
        min = list[i]
    else:
        while min < list[i]:
            i -= 1
        min = list[i]
    if max > list[-1]:
        max = list[-1]
    else:
        i = 0
        while max > list[i]:
            i += 1
        max = list[i]
    return min, max


def main():
    list = [int(x) for x in stdin.readline().split()]
    #print list
    list = qsort(list)
    #print list
    for linje in stdin:
        ord = linje.split()
        min = int(ord[0])
        max = int(ord[1])
        res = finn2(list, min, max)
        print str(res[0]) + " " + str(res[1])

main()