from sys import stdin
from itertools import repeat


def merge_sort(decks):
    if len(decks) <= 1:
        return decks

    mid = len(decks)/2
    left = decks[:mid]
    right = decks[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


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
    decks = []
    for line in stdin:
        (index, list) = line.split(':')
        deck = zip(map(int, list.split(',')), repeat(index))
        decks.append(deck)
    print decks
    print merge_sort(decks)

main()