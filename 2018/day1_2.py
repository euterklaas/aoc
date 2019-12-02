#!/usr/bin/env python3

inputFile = 'day1_2.input'
frequency = 0
frequencyList = []
frequencyDuplicateList = []
duplicateFound = False
listRuns = 0

print('Saving frequencies as list...')
with open(inputFile) as f:
    for line in f:
        frequencyList.append(line)

#print('Add 0-Frequency to list...')
#frequencyList.append(frequency)

while duplicateFound == False:
    listRuns += 1
    print('Number of list runs: %s' % listRuns)
    for i in frequencyList:
        frequency = frequency + ( int(i) )
        if frequency in frequencyDuplicateList:
            print('Duplicate frequency: %s' % frequency)
            duplicateFound = True
            break
        frequencyDuplicateList.append(frequency)

print('The duplicate frequency is: %s' % frequency)
