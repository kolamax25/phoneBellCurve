import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

list = []

df = pd.read_csv("phoneBell.csv")

bmi = ff.create_distplot([df["Avg Rating"].tolist()], ["Ratings from different certain phone brands"])
bmi.show()
