import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(np.sum([1,2,3]))
print(np.random.randint(1,10))

poke_data = open("Aulas Data Science - Firmino/Tarefa Pokemon/pokemon.csv")

header = poke_data.readline().split(",")

dados = []
for line in poke_data:
    dado = line.split(",")
    print(dado)
    break

poke_csv = csv.reader(poke_data, delimiter = ',', quotechar = '"')

header = next(poke_csv)
header_position = {}

for i in range(len(header)):
    header_position[header[i]] = i

print(header_position)

for line in poke_csv:
    print(line)
    break
