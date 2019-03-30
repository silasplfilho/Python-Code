import pandas as pd

gender_df = pd.read_csv('gender_purchase.csv')
print(gender_df.head(3))

table = pd.crosstab(gender_df['Gender'], gender_df['Purchase'])
table

random = []
xlist = []
for i in range(100):
    x = uniform(0, 10)
    xlist.append(x)
    random.append(math.log(x))