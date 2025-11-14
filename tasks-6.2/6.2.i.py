import pandas as pd


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
xmin, xmax = sorted((x1, x2))
ymin, ymax = sorted((y1, y2))

data = pd.read_csv('data.csv')
print(data.loc[data['x'].between(xmin, xmax) & data['y'].between(ymin, ymax)])