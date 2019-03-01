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
import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 9)
print(reviews)  #print eight columns
"""
         country          ...                         winery
0          Italy          ...                        Nicosia
1       Portugal          ...            Quinta dos Avidagos
2             US          ...                      Rainstorm
3             US          ...                     St. Julian
...          ...          ...                            ...
129967        US          ...                       Citation
129968    France          ...                Domaine Gresser
129969    France          ...           Domaine Marcel Deiss
129970    France          ...               Domaine Schoffit

[129971 rows x 13 columns]
"""
print(reviews.country)  #print eight rows country column because we set pd.set_option("display.max_rows", 9).  Rows printed evenly.
'''
0            Italy
1         Portugal
2               US
3               US
            ...   
129967          US
129968      France
129969      France
129970      France
Name: country, Length: 129971, dtype: object
'''
print(reviews["country"])
'''
0            Italy
1         Portugal
2               US
3               US
            ...   
129967          US
129968      France
129969      France
129970      France
Name: country, Length: 129971, dtype: object
'''
print(reviews["country"][0]) #print Italy
print(reviews["country"][129967]) #print US
#Pandas has its own accessor operators, loc and iloc. For more advanced operations, these are the ones you're supposed to be using.
print(reviews.iloc[0]) #print the first row
"""
country                                                              Italy
description              Aromas include tropical fruit, broom, brimston...
designation                                                   Vulkà Bianco
points                                                                  87
                                               ...                        
taster_twitter_handle                                         @kerinokeefe
title                                    Nicosia 2013 Vulkà Bianco  (Etna)
variety                                                        White Blend
winery                                                             Nicosia
Name: 0, Length: 13, dtype: object
"""
#When choosing or transitioning between loc and iloc, the two methods use slightly different indexing schemes.  iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. 0:10 will select entries 0,...,10.  iloc exclusive.  loc inclusive.
#Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second.  This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns. To get a column with iloc, we can do the following:
print(reviews.iloc[:, 0])  #print the first column.  Remember print eight rows because we set pd.set_option("display.max_rows", 9).  Rows printed evenly.
"""
0            Italy
1         Portugal
2               US
3               US
            ...   
129967          US
129968      France
129969      France
129970      France
Name: country, Length: 129971, dtype: object
"""
print(reviews.iloc[:3, 0])  #print first 3 rows in column 0 index.
'''
0       Italy
1    Portugal
2          US
Name: country, dtype: object
'''
print(reviews.iloc[1:3, 0])  #print row #1 and row #2 in column 0 index.
'''
1    Portugal
2          US
Name: country, dtype: object
'''
print(reviews.iloc[[1, 2, 3, 5, 8], ]) #print row or index 1, 2, 3, 5, 8 show all columns
print(reviews.iloc[[0, 1, 2], 1]) #print row #0, row #1, row #2 in column 1 index.
'''
0    Aromas include tropical fruit, broom, brimston...
1    This is ripe and fruity, a wine that is smooth...
2    Tart and snappy, the flavors of lime flesh and...
Name: description, dtype: object
'''
print(reviews.iloc[-5:]) #print last five rows
"""
        country                    ...                                                       winery
129966  Germany                    ...                     Dr. H. Thanisch (Erben Müller-Burggraef)
129967       US                    ...                                                     Citation
129968   France                    ...                                              Domaine Gresser
129969   France                    ...                                         Domaine Marcel Deiss
129970   France                    ...                                             Domaine Schoffit

[5 rows x 13 columns]
"""
print(reviews.loc[0, 'country']) #print Italy.  The first row in column country.
print(reviews.loc[0:9, 'country']) #print first 10 values in country column.
print(reviews.loc[[0, 1, 10, 100], ["country","province","region_1","region_2"]]) #print row index 0, 1, 10, 100 with country, province, region_1, and region_2 columns
print(reviews.loc[0:99, ["country","variety"]]) #print first 100 rows with country and variety columns
print(reviews.loc[:, ["taster_name","taster_twitter_handle", "points"]]) #print taster_name, taster_twitter_handle, points columns.   Remember print eight rows because we set pd.set_option("display.max_rows", 9).  Rows printed evenly.
'''
               taster_name taster_twitter_handle  points
0            Kerin O’Keefe          @kerinokeefe      87
1               Roger Voss            @vossroger      87
2             Paul Gregutt           @paulgwine       87
3       Alexander Peartree                   NaN      87
...                    ...                   ...     ...
129967        Paul Gregutt           @paulgwine       90
129968          Roger Voss            @vossroger      90
129969          Roger Voss            @vossroger      90
129970          Roger Voss            @vossroger      90

[129971 rows x 3 columns]
'''
#When choosing or transitioning between loc and iloc, the two methods use slightly different indexing schemes.  iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. 0:10 will select entries 0,...,9. loc indexes inclusively. 0:10 will select entries 0,...,10.  iloc exclusively, loc inclusively.

#Label-based selection derives its power from the labels in the index. Critically, the index we use is not immutable. We can manipulate the index in any way we see fit.  #RM:  select a column for set_index.  The example below the title column is the index.
print(reviews.set_index("title"))
"""
                                                  country          ...                         winery
title                                                                 ...                               
Nicosia 2013 Vulkà Bianco  (Etna)                      Italy          ...                        Nicosia
Quinta dos Avidagos 2011 Avidagos Red (Douro)       Portugal          ...            Quinta dos Avidagos
Rainstorm 2013 Pinot Gris (Willamette Valley)             US          ...                      Rainstorm
St. Julian 2013 Reserve Late Harvest Riesling (...        US          ...                     St. Julian
...                                                      ...          ...                            ...
Citation 2004 Pinot Noir (Oregon)                         US          ...                       Citation
Domaine Gresser 2013 Kritt Gewurztraminer (Alsace)    France          ...                Domaine Gresser
Domaine Marcel Deiss 2012 Pinot Gris (Alsace)         France          ...           Domaine Marcel Deiss
Domaine Schoffit 2012 Lieu-dit Harth Cuvée Caro...    France          ...               Domaine Schoffit

[129971 rows x 12 columns]
"""
print(reviews.set_index("winery"))  #winery column is the index.   Remember print eight rows because we set pd.set_option("display.max_rows", 9).  Rows printed evenly.
'''
                       country       ...               variety
winery                               ...                      
Nicosia                  Italy       ...           White Blend
Quinta dos Avidagos   Portugal       ...        Portuguese Red
Rainstorm                   US       ...            Pinot Gris
St. Julian                  US       ...              Riesling
...                        ...       ...                   ...
Citation                    US       ...            Pinot Noir
Domaine Gresser         France       ...        Gewürztraminer
Domaine Marcel Deiss    France       ...            Pinot Gris
Domaine Schoffit        France       ...        Gewürztraminer

[129971 rows x 12 columns]
'''
print(reviews.country=="Italy")
"""
0          True
1         False
2         False
3         False
          ...  
129967    False
129968    False
129969    False
129970    False
Name: country, Length: 129971, dtype: bool
"""
print(reviews.loc[reviews.country=="Italy"])
"""
       country               ...                                          winery
0        Italy               ...                                         Nicosia
6        Italy               ...                                 Terre di Giurfo
13       Italy               ...                             Masseria Setteporte
22       Italy               ...                              Baglio di Pianetto
...        ...               ...                                             ...
129943   Italy               ...                 Baglio del Cristo di Campobello
129947   Italy               ...                        Feudo Principi di Butera
129961   Italy               ...                                             COS
129962   Italy               ...                                        Cusumano

[19540 rows x 13 columns]
"""
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]) #print Italy wines and 90 points and higher.  Remember print eight rows because we set pd.set_option("display.max_rows", 9).  Rows printed evenly.
"""
       country               ...                                          winery
120      Italy               ...                                         Ceretto
130      Italy               ...                                         Ceretto
133      Italy               ...                            Poderi Luigi Einaudi
135      Italy               ...                                 Giacomo Ascheri
...        ...               ...                                             ...
129943   Italy               ...                 Baglio del Cristo di Campobello
129947   Italy               ...                        Feudo Principi di Butera
129961   Italy               ...                                             COS
129962   Italy               ...                                        Cusumano

[6648 rows x 13 columns]
"""
print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]) #print Italy wines or 90 points and higher.  Remember print eight rows because we set pd.set_option("display.max_rows", 9).  Rows printed evenly.
'''
       country          ...                         winery
0        Italy          ...                        Nicosia
6        Italy          ...                Terre di Giurfo
13       Italy          ...            Masseria Setteporte
22       Italy          ...             Baglio di Pianetto
...        ...          ...                            ...
129967      US          ...                       Citation
129968  France          ...                Domaine Gresser
129969  France          ...           Domaine Marcel Deiss
129970  France          ...               Domaine Schoffit

[61937 rows x 13 columns]
'''
#combine & and | and and or use paranthesis ()
print(reviews.loc[((reviews.country == 'Australia') & (reviews.points >= 95)) | ((reviews.country == 'New Zealand') & (reviews.points >= 95))])
#isin is lets you select data whose value "is in" a list of values. For example, here's how we can use it to select wines only from Italy or France:
print(reviews.loc[reviews.country.isin(["Italy","France"])])
'''
       country           ...                              winery
0        Italy           ...                             Nicosia
6        Italy           ...                     Terre di Giurfo
7       France           ...                            Trimbach
9       France           ...                  Jean-Baptiste Adam
...        ...           ...                                 ...
129965  France           ...             Domaine Rieflé-Landmann
129968  France           ...                     Domaine Gresser
129969  France           ...                Domaine Marcel Deiss
129970  France           ...                    Domaine Schoffit

[41633 rows x 13 columns]
'''
#isnull (and its companion notnull) highlight values which are or are not empty (NaN).
print(reviews.loc[reviews.price.notnull()])  #print wines with a price
'''
         country          ...                         winery
1       Portugal          ...            Quinta dos Avidagos
2             US          ...                      Rainstorm
3             US          ...                     St. Julian
4             US          ...                   Sweet Cheeks
...          ...          ...                            ...
129967        US          ...                       Citation
129968    France          ...                Domaine Gresser
129969    France          ...           Domaine Marcel Deiss
129970    France          ...               Domaine Schoffit

[120975 rows x 13 columns]
'''
#Assigning data to a DataFrame is easy. You can assign either a constant value or an iterable of values.
reviews["critic"] = "everyone" #create column named critic and assign a value everyone
print(reviews.loc[:, ["critic"]]) 
"""
          critic
0       everyone
1       everyone
2       everyone
3       everyone
...          ...
129967  everyone
129968  everyone
129969  everyone
129970  everyone

[129971 rows x 1 columns]
"""
reviews["index_backwards"] = range(len(reviews), 0, -1)
print(reviews.loc[:, ["index_backwards"]])
'''
        index_backwards
0                129971
1                129970
2                129969
3                129968
...                 ...
129967                4
129968                3
129969                2
129970                1

[129971 rows x 1 columns]
'''

#2. Indexing, Selecting & Assigning Exercises
#select the description column from reviews
desc = reviews["description"]
#select the first value from the description column of reviews
first_description = desc[0]
#select the first row or first record from reviews
first_row = reviews.iloc[0]
#select the first 10 values from description column in reviews
first_descriptions = reviews.loc[0:11, "description"]
#select rows or recrods with index label 1, 2, 3, 5, and 8.
sample_reviews = reviews.iloc[[1, 2, 3, 5, 8], ]
#select rows or records with index label 0, 1, 10, 100 with country, province, region_1, and region_2 columns
df = reviews.loc[[0, 1, 10, 100], ["country","province","region_1","region_2"]]
#select first 100 records containing country and variety columns
df = reviews.loc[0:99, ["country","variety"]]
#select wines from Italy
italian_wines = reviews.loc[reviews.country=="Italy"]
#select wines from Australia or New Zeland with 95 points or greater
top_oceania_wines = reviews.loc[((reviews.country == 'Australia') & (reviews.points >= 95)) | ((reviews.country == 'New Zealand') & (reviews.points >= 95))]
