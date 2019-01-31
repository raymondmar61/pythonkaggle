#https://www.kaggle.com/learn/machine-learning

#3. Exercise:  Explore Your Data
import pandas as pd
from datetime import datetime
#Path to csv file
iowafilepath = "/home/mar/python/kaggle/train.csv"
#Read csv file
iowadata = pd.read_csv(iowafilepath)
print(iowadata.describe())
#print(dir(pd))
averagelotsize = iowadata.LotArea.mean()
print("Average lot size from LotArea column {:.0f}".format(averagelotsize)) #print Average lot size from LotArea column 10517
maxyearsold = iowadata.YrSold.max()
print(maxyearsold) #print 2010
print(datetime.now().year - maxyearsold) #print 9

#5. Exercise: Your Machine Learning Model
print(iowadata.columns)
"""
Index(['Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',
       'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig',
       'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType',
       'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
       'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',
       'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
       'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
       'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
       'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF',
       'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
       'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual',
       'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType',
       'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual',
       'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF',
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC',
       'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType',
       'SaleCondition', 'SalePrice'],
      dtype='object')
"""
#Predict SalePrice assign to y variable
y = iowadata.SalePrice
#Create DataFreame holding predictive features assign to X variable.  RM:  X is capitalized.
iowadatafeatures = ["LotArea","YearBuilt","1stFlrSF","2ndFlrSF","FullBath","BedroomAbvGr","TotRmsAbvGrd"]
X = iowadata[iowadatafeatures]
print(X.describe())
"""
             LotArea    YearBuilt      ...       BedroomAbvGr  TotRmsAbvGrd
count    1460.000000  1460.000000      ...        1460.000000   1460.000000
mean    10516.828082  1971.267808      ...           2.866438      6.517808
std      9981.264932    30.202904      ...           0.815778      1.625393
min      1300.000000  1872.000000      ...           0.000000      2.000000
25%      7553.500000  1954.000000      ...           2.000000      5.000000
50%      9478.500000  1973.000000      ...           3.000000      6.000000
75%     11601.500000  2000.000000      ...           3.000000      7.000000
max    215245.000000  2010.000000      ...           8.000000     14.000000

[8 rows x 7 columns]
"""
from sklearn.tree import DecisionTreeRegressor
iowamodel = DecisionTreeRegressor(random_state=1)
print(iowamodel.fit(X,y))
"""
DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=None,
           max_leaf_nodes=None, min_impurity_decrease=0.0,
           min_impurity_split=None, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           presort=False, random_state=1, splitter='best')
"""
print("Making predictions for the following five hourses:")
print(X.head())
"""   LotArea  YearBuilt      ...       BedroomAbvGr  TotRmsAbvGrd
0     8450       2003      ...                  3             8
1     9600       1976      ...                  3             6
2    11250       2001      ...                  3             6
3     9550       1915      ...                  3             7
4    14260       2000      ...                  4             9

[5 rows x 7 columns]
"""
print("The predictions are")
print(iowamodel.predict(X)) #print [208500. 181500. 223500. ... 266500. 142125. 147500.]
print("Actual target values for those homes I commented out below because print entire list")
#print(y.tolist()) #print [208500, 181500, 223500, ...  ,266500, 142125, 147500]  RM:  actually printed all prices in one list

#7. Exercise:  Model Validation
#Split data.  Features loaded in DataFrame X variable and target loaded in y variable.
from sklearn.model_selection import train_test_split
trainX, validateX, trainy, validatey = train_test_split(X, y, random_state=1) #Give random_state equal to one
#Create DecisionTreeRegressor.  Set random_state equal to one.
iowamodel = DecisionTreeRegressor(random_state=1)
#Fit with training data.  Print, too.
print(iowamodel.fit(trainX, trainy))
"""
DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=None,
           max_leaf_nodes=None, min_impurity_decrease=0.0,
           min_impurity_split=None, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           presort=False, random_state=1, splitter='best')
"""
#Predict all validation observations
validatepredictions = iowamodel.predict(validateX)
#print top few validation predictions
print(iowamodel.predict(X.head())) #print [208500. 181500. 223500. 128000. 250000.]
#print top few actual prices from validation data
print(y.head().tolist()) #print [208500, 181500, 223500, 140000, 250000]
#calculate the mean absolute error
from sklearn.metrics import mean_absolute_error
validatepredictions = iowamodel.predict(validateX)
print(mean_absolute_error(validatey, validatepredictions)) #print 29652.931506849316