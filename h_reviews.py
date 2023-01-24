import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# I have used apple_products.csv file downloaded from kaggle.com for the dataset analysis

datafr = pd.read_csv('location of apple_products.csv')  # store dataset in dataframe

# for initial null value and descriptive analysis ... 

# describe the aggregate data of each column for count, max, min, mean, etc
# << print(datafr.describe) >> 

# check for null vales in each column
# << print(datafr.isnull().sum()) >>

#----------------------------------------------------------------------------------------------------

# DA : FINDING THE TOP 10 HIGHEST REVIEWED (acccording to ratings) IPHONES IN INDIA
h_rated = datafr.sort_values(by = ['Star Rating'], ascending= False)
h_rated = h_rated.head(10)
# print(h_rated['Product Name'])

cnt = h_rated['Product Name'].value_counts()
label = cnt.index
counts = h_rated['Number Of Reviews']
fig = px.bar(h_rated, x = label, y = counts, title = "Number of reviews for highest Rated Iphones")
fig.show()

# << DA : Apple Iphone 8 Plus Gold 64GB has the highest number of reviews