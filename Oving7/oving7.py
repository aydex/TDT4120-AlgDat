def merge2(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [n1 + 1]
    R = [n2 + 1]
    for i in xrange(0, n1):
        L[i] = A[p + i - 1]
    for j in range(0, n2):
        R[j] = A[q + j]
    L[n1 + 1] = float(1e3000)
    R[n2 + 1] = float(1e3000)
    i = 1
    j = 1
    for k in xrange(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        elif A[k] == R[j]:
            j += 1


def merge(left, right):
    result = []
    left_i, right_i = 0, 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1

    if left:
        result.extend(left[left_i:])
    if right:
        result.extend(right[right_i:])
    return result


def main():
    from sys import stdin
    from itertools import repeat
    decks = []
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        decks.append(deck)
    word = ""
    sorted = []
    for i in xrange(0, len(decks)):
        sorted = (merge(sorted, decks[i]))
        #sorted = (merge2(sorted + decks[i], 0, len(sorted), len(sorted) + len(decks[i])))
    for x in sorted:
        word += x[-1]
    print word

main()