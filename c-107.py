import csv
import pandas as pa
import plotly.graph_objects as pg

df = pa.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())
fig=pg.Figure(pg.Bar(x=df.groupby("level")["attempt"].mean(),y=["level1","level2","level3","level4"],orientation='h'))
fig.show()