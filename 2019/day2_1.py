#!/usr/bin/env python3

from collections import Counter

inputFile = 'day2_1.input'
idList = []
two = 0
three = 0

with open(inputFile) as f:
    for line in f:
        alreadyTwo = False
        alreadyThree = False
        word = Counter(line)
        for k in word:
            letter = k
            value = word[letter]
            if value == 2:
                if alreadyTwo == False:
                    two += 1
                    alreadyTwo = True

            if value == 3:
                if alreadyThree == False:
                    three += 1
                    alreadyThree = True

checksum = two * three
print("The checksum is: %s * %s = %s" % (two, three, checksum))
