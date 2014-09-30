__author__ = 'adrianh'
from sys import stdin


def main():
    word = ""
    lines = dict()
    j = 0
    for line in stdin:
        split = line.split(":")
        lines[split[0]] = map(int, split[1].split(","))
        j += len(lines[split[0]])

    i = 0
    while i <= j:
        for key in lines.keys():
            if i in lines[key]:
                word += key
        i += 1

    print str(word)

main()