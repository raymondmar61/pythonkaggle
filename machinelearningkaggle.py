#https://www.kaggle.com/learn/machine-learning

#2. Explore Your Data
import pandas as pd
#save filepath to variable
melbournefilepath = "/home/mar/python/kaggle/melb_data.csv"
#read data and store data in DataFrame variable melbournedata
melbournedata = pd.read_csv(melbournefilepath)
#print a summary of the data which includes count, mean, std for each column
print(melbournedata.describe())

#4 Your First Machine Learning Model
#print list of all columns in the dataset
print(melbournedata.columns) #print Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG', 'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car','Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'], dtype='object')
# dropna drops missing values (think of na as "not available")
melbournedata = melbournedata.dropna(axis=0)
#We'll use the dot notation to select the column we want to predict, which is called the prediction target. By convention, the prediction target is called y.
y = melbournedata.Price
#The columns that are inputted into our model (and later used to make predictions) are called "features." In our case, those would be the columns used to determine the home price.
melbournefeatures = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
#By convention, the features data is called X.
X = melbournedata[melbournefeatures]
print(X.describe())
print(X.head()) #print default first 5 rows
"""
You will use the scikit-learn library to create your models. When coding, this library is written as sklearn, as you will see in the sample code. Scikit-learn is easily the most popular library for modeling the types of data typically stored in DataFrames.

The steps to building and using a model are:
Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
Fit: Capture patterns from provided data. This is the heart of modeling.
Predict: Just what it sounds like
Evaluate: Determine how accurate the model's predictions are.
"""
from sklearn.tree import DecisionTreeRegressor
#print(dir(DecisionTreeRegressor))
# Define model. Specify a number for random_state to ensure same results each run
melbournemodel = DecisionTreeRegressor(random_state=1)
#Fit model
print(melbournemodel.fit(X,y)) #print DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=None, max_leaf_nodes=None, min_impurity_decrease=0.0,min_impurity_split=None, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, presort=False, random_state=1, splitter='best')
#In practice, you'll want to make predictions for new houses coming on the market rather than the houses we already have prices for. But we'll make predictions for the first few rows of the training data to see how the predict function works.
print("Making predictions for the following five hourses:")
print(X.head()) 
"""
   Rooms  Bathroom  Landsize  Lattitude  Longtitude
1      2       1.0     156.0   -37.8079    144.9934
2      3       2.0     134.0   -37.8093    144.9944
4      4       1.0     120.0   -37.8072    144.9941
6      3       2.0     245.0   -37.8024    144.9993
7      2       1.0     256.0   -37.8060    144.9954
"""
print("The predictions are")
print(melbournemodel.predict(X.head())) #print [1035000. 1465000. 1600000. 1876000. 1636000.]

#6. Model Validation
#calculate the mean absolute error
from sklearn.metrics import mean_absolute_error
predictedhomeprices = melbournemodel.predict(X)
print(mean_absolute_error(y, predictedhomeprices)) #print 1115.7467183128902
"""
The 1115.7467183128902 measure we just computed can be called an "in-sample" score. We used a single "sample" of houses for both building the model and evaluating it.  It's bad.  Since models' practical value come from making predictions on new data, we measure performance on data that wasn't used to build the model. The most straightforward way to do this is to exclude some data from the model-building process, and then use those to test the model's accuracy on data it hasn't seen before. This data is called validation data.
"""
#The scikit-learn library has a function train_test_split to break up the data into two pieces. We'll use some of that data as training data to fit the model, and we'll use the other data as validation data to calculate mean_absolute_error.
from sklearn.model_selection import train_test_split
#split data into training and validation data, for both features and target.  The split is based on a random number generator. Supplying a numeric value to the random_state argument guarantees we get the same split every time we run this script.
trainX, validateX, trainy, validatey = train_test_split(X, y, random_state = 0)
#define model
melbournemodel = DecisionTreeRegressor()
#Fit model
print(melbournemodel.fit(trainX, trainy))
"""
DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=None,
           max_leaf_nodes=None, min_impurity_decrease=0.0,
           min_impurity_split=None, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           presort=False, random_state=None, splitter='best')
"""
#get predicted prices on validation data
from sklearn.metrics import mean_absolute_error
validatepredictions = melbournemodel.predict(validateX)
print(mean_absolute_error(validatey, validatepredictions)) #print 274081.70109748223

#8.  Underfitting and Overfitting
#The max_leaf_nodes argument provides a very sensible way to control overfitting vs underfitting. The more leaves we allow the model to make, the more we move from the underfitting area in the above graph to the overfitting area.  We can use a utility function to help compare MAE scores from different values for max_leaf_nodes.
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
def get_mae(max_leaf_nodes, trainX, validateX, trainy, validatey):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(trainX, trainy)
    preds_val = model.predict(validateX)
    mae = mean_absolute_error(validatey, preds_val)
    return(mae)
#compare MAE Mean Average Error with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, trainX, validateX, trainy, validatey)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
"""
Max leaf nodes: 5  		 Mean Absolute Error:  385696
Max leaf nodes: 50  		 Mean Absolute Error:  279794
Max leaf nodes: 500  		 Mean Absolute Error:  261718
Max leaf nodes: 5000  		 Mean Absolute Error:  271996
"""
#Of the options listed, 500 is the optimal number of leaves.
best_tree_size = 500
from sklearn.tree import DecisionTreeRegressor
finalmodel = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)
print(finalmodel.fit(X,y))
"""
DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=None,
           max_leaf_nodes=500, min_impurity_decrease=0.0,
           min_impurity_split=None, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           presort=False, random_state=1, splitter='best')
"""

#10. Random Forests
#The random forest uses many trees, and it makes a prediction by averaging the predictions of each component tree.
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(trainX, trainy)
melb_preds = forest_model.predict(validateX)
print(mean_absolute_error(validatey, melb_preds)) #print 218482.25517538196


