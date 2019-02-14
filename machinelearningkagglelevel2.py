#https://www.kaggle.com/learn/machine-learning

#1. Handling Missing Values
#We will see am example predicting housing prices from the Melbourne Housing data. To master missing value handling, fork this notebook and repeat the same steps with the Iowa Housing data.
import pandas as pd

#Load data
#Save filepath to variable
melbournefilepath = "/home/mar/python/kaggle/melb_data.csv"
#read data and store data in DataFrame variable melb_data
melb_data = pd.read_csv(melbournefilepath)
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

melb_target = melb_data.Price
melb_predictors = melb_data.drop(['Price'], axis=1)
# For the sake of keeping the example simple, we'll use only numeric predictors. 
melb_numeric_predictors = melb_predictors.select_dtypes(exclude=['object'])
#We divide our data into training and test.
#We've loaded a function score_dataset(X_train, X_test, y_train, y_test) to compare the quality of diffrent approaches to missing values. This function reports the out-of-sample MAE score from a RandomForest.
X_train, X_test, y_train, y_test = train_test_split(melb_numeric_predictors, melb_target, train_size=0.7, test_size=0.3, random_state=0)
def score_dataset(X_train, X_test, y_train, y_test):
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    return mean_absolute_error(y_test, preds)
#Get Model Score from Dropping Columns with Missing Values
cols_with_missing = [col for col in X_train.columns 
                                 if X_train[col].isnull().any()]
reduced_X_train = X_train.drop(cols_with_missing, axis=1)
reduced_X_test  = X_test.drop(cols_with_missing, axis=1)
print("Mean Absolute Error from dropping columns with Missing Values:")
print(score_dataset(reduced_X_train, reduced_X_test, y_train, y_test)) #print Mean Absolute Error from dropping columns with Missing Values:  189582.30368188513
#Get Model Score from Imputation
from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()
imputed_X_train = my_imputer.fit_transform(X_train)
imputed_X_test = my_imputer.transform(X_test)
print("Mean Absolute Error from Imputation:")
print(score_dataset(imputed_X_train, imputed_X_test, y_train, y_test)) #print Mean Absolute Error from Imputation:  182752.85395189002
#Get Score from Imputation with Extra Columns Showing What Was Imputed
imputed_X_train_plus = X_train.copy()
imputed_X_test_plus = X_test.copy()
cols_with_missing = (col for col in X_train.columns 
                                 if X_train[col].isnull().any())
for col in cols_with_missing:
    imputed_X_train_plus[col + '_was_missing'] = imputed_X_train_plus[col].isnull()
    imputed_X_test_plus[col + '_was_missing'] = imputed_X_test_plus[col].isnull()
# Imputation
my_imputer = SimpleImputer()
imputed_X_train_plus = my_imputer.fit_transform(imputed_X_train_plus)
imputed_X_test_plus = my_imputer.transform(imputed_X_test_plus)
print("Mean Absolute Error from Imputation while Track What Was Imputed:")
print(score_dataset(imputed_X_train_plus, imputed_X_test_plus, y_train, y_test)) #print Mean Absolute Error from Imputation while Track What Was Imputed:  183565.47610281227
#As is common, imputing missing values allowed us to improve our model compared to dropping those columns. We got an additional boost by tracking what values had been imputed.

#2. Using Categorical Data with One Hot Encoding
# Read the data
import pandas as pd
train_data = pd.read_csv('/home/mar/python/kaggle/train.csv')
test_data = pd.read_csv('/home/mar/python/kaggle/test.csv')
# Drop houses where the target is missing
train_data.dropna(axis=0, subset=['SalePrice'], inplace=True)
target = train_data.SalePrice
# Since missing values isn't the focus of this tutorial, we use the simplest
# possible approach, which drops these columns. 
# For more detail (and a better approach) to missing values, see
# https://www.kaggle.com/dansbecker/handling-missing-values
cols_with_missing = [col for col in train_data.columns 
                                 if train_data[col].isnull().any()]                                  
candidate_train_predictors = train_data.drop(['Id', 'SalePrice'] + cols_with_missing, axis=1)
candidate_test_predictors = test_data.drop(['Id'] + cols_with_missing, axis=1)
# "cardinality" means the number of unique values in a column.
# We use it as our only way to select categorical columns here. This is convenient, though
# a little arbitrary.
low_cardinality_cols = [cname for cname in candidate_train_predictors.columns if 
                                candidate_train_predictors[cname].nunique() < 10 and
                                candidate_train_predictors[cname].dtype == "object"]
numeric_cols = [cname for cname in candidate_train_predictors.columns if 
                                candidate_train_predictors[cname].dtype in ['int64', 'float64']]
my_cols = low_cardinality_cols + numeric_cols
train_predictors = candidate_train_predictors[my_cols]
test_predictors = candidate_test_predictors[my_cols]
#Pandas assigns a data type (called a dtype) to each column or Series. Let's see a random sample of dtypes from our prediction data:
print(train_predictors.dtypes.sample(10))
"""
YearRemodAdd      int64
OverallCond       int64
CentralAir       object
HouseStyle       object
BldgType         object
LandContour      object
KitchenQual      object
3SsnPorch         int64
MSSubClass        int64
SaleCondition    object
dtype: object
"""
#Object indicates a column has text (there are other things it could be theoretically be, but that's unimportant for our purposes). It's most common to one-hot encode these "object" columns, since they can't be plugged directly into most models. Pandas offers a convenient function called get_dummies to get one-hot encodings. Call it like this:
one_hot_encoded_training_predictors = pd.get_dummies(train_predictors)
"""
Alternatively, you could have dropped the categoricals. To see how the approaches compare, we can calculate the mean absolute error of models built with two alternative sets of predictors:

1. One-hot encoded categoricals as well as numeric predictors
2. Numerical predictors, where we drop categoricals.

One-hot encoding usually helps, but it varies on a case-by-case basis. In this case, there doesn't appear to be any meaningful benefit from using the one-hot encoded variables.
"""
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
def get_mae(X, y):
    # multiple by -1 to make positive MAE score instead of neg value returned as sklearn convention
    return -1 * cross_val_score(RandomForestRegressor(50), X, y, scoring = 'neg_mean_absolute_error').mean()
predictors_without_categoricals = train_predictors.select_dtypes(exclude=['object'])
mae_without_categoricals = get_mae(predictors_without_categoricals, target)
mae_one_hot_encoded = get_mae(one_hot_encoded_training_predictors, target)
print('Mean Absolute Error when Dropping Categoricals: ' + str(int(mae_without_categoricals))) #print Mean Absolute Error when Dropping Categoricals: 18444
print('Mean Abslute Error with One-Hot Encoding: ' + str(int(mae_one_hot_encoded))) #print Mean Abslute Error with One-Hot Encoding: 17923
#So far, you've one-hot-encoded your training data. What about when you have multiple files (e.g. a test dataset, or some other data that you'd like to make predictions for)? Scikit-learn is sensitive to the ordering of columns, so if the training dataset and test datasets get misaligned, your results will be nonsense. This could happen if a categorical had a different number of values in the training data vs the test data.
#Ensure the test data is encoded in the same manner as the training data with the align command:
one_hot_encoded_training_predictors = pd.get_dummies(train_predictors)
one_hot_encoded_test_predictors = pd.get_dummies(test_predictors)
final_train, final_test = one_hot_encoded_training_predictors.align(one_hot_encoded_test_predictors, join='left', axis=1)
#The align command makes sure the columns show up in the same order in both datasets (it uses column names to identify which columns line up in each dataset.) The argument join='left' specifies that we will do the equivalent of SQL's left join. That means, if there are ever columns that show up in one dataset and not the other, we will keep exactly the columns from our training data. The argument join='inner' would do what SQL databases call an inner join, keeping only the columns showing up in both datasets. That's also a sensible choice.
