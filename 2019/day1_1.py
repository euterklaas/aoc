#!/bin/env python3

input = 'day1_1.input'

total = 0

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

with open(input) as f:
    for mass in f:
        fuel = int(mass) / 3
        roundedFuel = truncate(fuel)
        finalFuel = roundedFuel - 2
        total += finalFuel

print(total)
