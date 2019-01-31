#https://www.kaggle.com/learn/machine-learning

import pandas as pd
from datetime import datetime
melbournefilepath = "/home/mar/python/kaggle/melb_data.csv"
melbournedata = pd.read_csv(melbournefilepath)
print(melbournedata.describe())
print(melbournedata.columns) #print Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG', 'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car','Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'], dtype='object')
# dropna drops missing values (think of na as "not available")
melbournedata = melbournedata.dropna(axis=0)
#We'll use the dot notation to select the column we want to predict, which is called the prediction target. By convention, the prediction target is called y.
y = melbournedata.Price
#The columns that are inputted into our model (and later used to make predictions) are called "features." In our case, those would be the columns used to determine the home price.
melbournefeatures = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']\
#By convention, this data is called x.
x = melbournedata[melbournefeatures]
print(x.describe())
print(x.head()) #print default first 5 rows


# iowafilepath = "/home/mar/python/kaggle/train.csv"
# iowadata = pd.read_csv(iowafilepath)
# print(iowadata.describe())
# #print(dir(pd))
# averagelotsize = iowadata.LotArea.mean()
# print("Average lot size from LotArea column {:.0f}".format(averagelotsize)) #print Average lot size from LotArea column 10517
# maxyearsold = iowadata.YrSold.max()
# print(maxyearsold) #print 2010
# print(datetime.now().year - maxyearsold) #print 9
