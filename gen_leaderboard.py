import os
import pandas as pd

df = pd.read_csv('board.csv')
print(len(df))
print(df.head())
# read the title of dataFrame
header = df.columns.values.tolist()
print(header)

with open('test.html', 'w') as f:
    for i in range(len(df)):
        print(df[header[0]][i])
        print(df[header[1]][i])
        print(df[header[2]][i])
        print(df[header[3]][i])
        print(df[header[4]][i])
        print(df[header[5]][i])

        f.writelines('<tr>\n')
        f.writelines('<td align="center">{}</td>\n'.format(df[header[0]][i]))
        f.writelines('<td align="center">{}</td>\n'.format(df[header[1]][i]))
        f.writelines('<td align="center">{}</td>\n'.format(df[header[2]][i]))
        f.writelines('<td align="center">{}</td>\n'.format(df[header[3]][i]))
        f.writelines('<td align="center">{}%</td>\n'.format(round(df[header[4]][i], 2)))
        f.writelines('<td align="center">{}</td>\n'.format(df[header[5]][i]))
        f.writelines('</tr>\n')