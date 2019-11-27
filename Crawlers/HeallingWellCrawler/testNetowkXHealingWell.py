import networkx as nx
import json

with open("bs4Test/testHealingWell2.json", 'r') as f:
    dataset = json.load(f)

for i in dataset:
    print(i['author'])
    i['postContent']

dataset[0]