from random import *

line = set()
for x in range(0, 2001):
    nextInt = randint(0, 1000001)
    line.add(str(nextInt))
print line
with open("input.txt", "w") as f:
    for tall in line:
        f.write(tall)
        f.write(" ")
    f.write("\n")
    for x in range(0, 20000):
        num1 = randint(0, 1000001)
        num2 = randint(num1, 1000001)
        f.write(str(num1) + " " + str(num2) + "\n")
f.close()