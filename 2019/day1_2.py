#!/bin/env python3

input = 'day1_1.input'

total = 0

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

with open(input) as f:
    for mass in f:
        fuel = int(mass) / 3
        fuel = truncate(fuel)
        fuel = fuel - 2
        total += fuel
        if fuel > 0:
            while fuel > 0:
                fuel = int(fuel) / 3
                fuel = truncate(fuel)
                fuel = fuel - 2
                if fuel > 0:
                    total += fuel
                print(fuel)
print(total)
