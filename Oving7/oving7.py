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
    for x in ([x[1] for x in sorted]):
        word += x
    print word

main()