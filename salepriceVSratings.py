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

# DA : FINDING THE TOP 10 HIGHEST RATED IPHONES IN INDIA
h_rated = datafr.sort_values(by = ['Star Rating'], ascending= False)
h_rated = h_rated.head(10)
# print(h_rated['Product Name'])

#----SCATTER PLOT

fig = px.scatter(data_frame= datafr, x = "Number Of Ratings", 
                y = "Sale Price", size = "Discount Percentage",trendline="ols",
                title="SALE PRICE VS NO. OF RATINGS for IPHONE")
fig.show()


# DA : WITH DECREASING SALES PRICE THE NUMBER OF RATINGS INCREASES