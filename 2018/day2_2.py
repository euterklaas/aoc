#!/usr/bin/env python3

from itertools import combinations

inputFile = 'day2_2.input'
boxIds = []
lineCounter = 0


with open(inputFile) as f:
    for line in f:
        boxIds.append(line)

for firstLine in boxIds:
    lineCounter += 1
    secondLineCounter = 0
    for secondLine in boxIds:
        differences = 0
        secondLineCounter += 1
        if firstLine == secondLine:
            continue
        for x, y in zip(firstLine, secondLine):
            if x != y:
                if differences > 1:
                    break
                differences += 1
        if differences == 1:
            print('Line %s: %s, Line %s: %s' % (lineCounter, firstLine, secondLineCounter, secondLine))

#with open(inputFile) as f:
#    for line in f:
#        lineCounter +=1
#        compareLineCounter = 0
#        for compareLine in f:
#            compareLineCounter +=1
#            print('Comparing line %s with line %s' % (lineCounter, compareLineCounter))
#            different = 0
#            if line == compareLine:
#                continue
#            for x, y in zip(line, compareLine):
#                if x != y:
#                    print('Difference detected: %s %s' % (x, y))
#                    if different > 1:
#                        print('More than one difference. Going on...')
#                        print('%s %s' % (line, compareLine))
#                        break
#                    different += 1
#            if different == 1:
#                print('%s\n%s' % (line, compareLine))


#with open(inputFile) as f:
#    for firstBoxId, secondBoxId in combinations(f.splitlines(), 2):
#        print('%s %s' % (firstBoxId, secondBoxId))

        # Check if more than 1 differing letter is contained
#        differingLetters = 0
#        for firstIdLetter, secondIdLetter in zip(firstBoxId, secondBoxId):
#            if firstIdLetter != secondIdLetter:
#                differingLetters += 1

#            if differingLetters > 1:
#                break
#            else:
            # FOUND!
            # Return only same letters:
#            return str().join(letter1 for letter1, letter2 in zip(firstBoxId, secondBoxId) if letter1 == letter2)
#                print('%s %s' % (fistBoxId, secondBoxId))
