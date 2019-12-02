#!/usr/bin/env python3

import re
import numpy as np

inputFile = 'day3_1.input'
claims = []
fabric = []
overlap = 0

with open(inputFile) as f:
    for line in f:
        claims.append(line)

# Die "Karte" erzeugen mit 1000 Zeilen und 1000 Spalten als Liste von Listen
fabric = np.zeros( [1000,1000],dtype=int)

# Die Anweisungen zerlegen und einzeln speichern
parseClaims = re.compile(r'#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)')

for claim in claims:
    mo = parseClaims.search(claim)
    if mo:
        claimId = mo.group(1)
        xOffset = int(mo.group(2))
        yOffset = int(mo.group(3))
        width = int(mo.group(4))
        height = int(mo.group(5))
# Zur jeweiligen Koordinate navigieren und +1 rechnen
    for i in range(height):
        y = yOffset + i - 1
        for j in range(width):
            x = xOffset + j - 1
            fabric[y][x] += 1
# Alle Koordinaten, die Inhalt > 1 haben, überlappen
for i in range(1000):
    for j in range(1000):
        if fabric[i][j] > 1:
            overlap += 1

print(overlap)
