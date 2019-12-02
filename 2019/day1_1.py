#!/usr/bin/env python3

inputFile = 'day1_1.input'
frequency = 0

with open(inputFile) as f:
     for line in f:
         frequency = frequency + ( int(line) )

print(frequency)
