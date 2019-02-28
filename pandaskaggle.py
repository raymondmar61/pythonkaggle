#https://www.kaggle.com/learn/pandas

#https://www.kaggle.com/residentmario/creating-reading-and-writing-reference
#1. Creating, reading, and writing workbook
import pandas as pd
#A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds with a row (or record) and a column.
yesno = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
"""
	Yes	No
0	50	131
1	21	2
"""
bobsue = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
"""
	Bob	Sue
0	I liked it.	Pretty good.
1	It was awful.	Bland.
"""
#pd.DataFrame constructor generates DataFrame objects. The syntax for declaring a new one is a dictionary whose keys are the column names (Bob and Sue in this example), and whose values are a list of entries.
#A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. 
numberslist = pd.Series([1, 2, 3, 4, 5])
print(numberslist)
"""
0    1
1    2
2    3
3    4
4    5
dtype: int64
"""
#A Series is, in essence, a single column of a DataFrame. So you can assign column values to the Series the same way as before, using an index parameter. However, a Series do not have a column name, it only has one overall name.
productasales = pd.Series([30, 35, 40], index=["2015 Sales", "2016 Sales", "2017 Sales"], name="Product A")
print(productasales)
"""
2015 Sales    30
2016 Sales    35
2017 Sales    40
Name: Product A, dtype: int64
"""
#Think of a DataFrame as actually being just a bunch of Series "glue together".

#Data can be stored in any of a number of different forms and formats. By far the most basic of these is the humble CSV file.
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
print(wine_reviews.shape) #print (129971, 14) 129971 records split across 14 columns.
print(wine_reviews.head()) #prints first five rows
'''
   Unnamed: 0         ...                        winery
0           0         ...                       Nicosia
1           1         ...           Quinta dos Avidagos
2           2         ...                     Rainstorm
3           3         ...                    St. Julian
4           4         ...                  Sweet Cheeks

[5 rows x 14 columns]
'''
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0) #use index_col to specify in-built index.  In this case, first column is index.
print(wine_reviews.head()) #prints first five rows
'''
    country         ...                        winery
0     Italy         ...                       Nicosia
1  Portugal         ...           Quinta dos Avidagos
2        US         ...                     Rainstorm
3        US         ...                    St. Julian
4        US         ...                  Sweet Cheeks
'''
# wine_reviewsexcel = pd.read_excel("winemag-data-130k-v2.csv", index_col=0, sheet_name ="winemag-data-130k-v2") #use index_col to specify in-built index.  In this case, first column is index.
# print(wine_reviewsexcel.head()) #error message.  Excel files are often not formatted as well as CSV files are. Spreadsheets allow (and encourage) creating notes and fields which are human-readable, but not machine-readable.

#SQL databases are where most of the data on the web ultimately gets stored. Connecting to a SQL database requires a lot more thought than reading from an Excel file. For one, you need to create a connector, something that will handle siphoning data from the database.  pandas won't do this for you automatically because there are many, many different types of SQL databases out there, each with its own connector. So for a SQLite database (the only kind supported on Kaggle), you would need to first do the following (using the sqlite3 library that comes with Python).
# import sqlite3
# conn = sqlite3.connect('sqlite')
# conn = sqlite3.connect("fpa_fod_20170508.sqlite")
# fires = pd.read_sql_query("SELECT * FROM fires", conn)
# print(fires.head())
#RM:  sqlite file too big.

#write to .csv file
wine_reviews.head().to_csv("wine_reviews.csv") #creates file wine_reviews.csv in directory
#write to Excel file
# wine_reviewsexcel.to_excel('excelfilename.xlsx', sheet_name='sheetnamehere') #error message.
#write to SQL database
# conn = sqlite3.connect("fires.sqlite")
# fires.head(10).to_sql("fires", conn)

#1. Creating, reading, and writing workbook Exercises
fruits = pd.DataFrame({"Apples":[30], "Bananas":[21]})
print(fruits)
"""
   Apples  Bananas
0      30       21
"""
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'], index=['2017 Sales', '2018 Sales'])
print(fruit_sales)
"""
            Apples  Bananas
2017 Sales      35       21
2018 Sales      41       34
"""
ingredients = pd.Series(["4 cups", "1 cup", "2 large", "1 can"], index=["Flour", "Milk", "Eggs", "Spam"], name="Dinner")
print(ingredients)
"""
Flour     4 cups
Milk       1 cup
Eggs     2 large
Spam       1 can
Name: Dinner, dtype: object
"""
#read the following csv dataset of wine reviews into a DataFrame called reviews
#reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
print(animals.head())
"""
        Cows  Goats
Year 1    12     22
Year 2    20     19
"""
#write to save as csv cows_and_goats.csv
animals.head().to_csv("cows_and_goats.csv")

#https://www.kaggle.com/residentmario/indexing-selecting-assigning-reference
#2. Indexing, Selecting & Assigning
#RM:  start 2.  Indexing, Selecting & Assigning using temppython.py