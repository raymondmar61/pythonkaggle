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

#3.  Summary Functions and Maps
import pandas as pd
pd.set_option('max_rows', 5)
import numpy as np
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(reviews.head())  #print first 5 rows starting index 0
'''
    country         ...                        winery
0     Italy         ...                       Nicosia
1  Portugal         ...           Quinta dos Avidagos
2        US         ...                     Rainstorm
3        US         ...                    St. Julian
4        US         ...                  Sweet Cheeks

[5 rows x 13 columns]
'''
#One of the most important summarization functions is the describe method.   The describe method used for points column.
print(reviews.points.describe())
'''
count    129971.000000
mean         88.447138
             ...      
75%          91.000000
max         100.000000
Name: points, Length: 8, dtype: float64
'''
#Using describe method for string data.  The describe method used for taster_name column.
print(reviews.taster_name.describe())
'''
count         103727
unique            19
top       Roger Voss
freq           25514
Name: taster_name, dtype: object
'''
#There are functions that return more specific information. For example, you can see the points allotted using the mean function.
print(reviews.points.mean()) #print 88.44713820775404
#To see a list of unique values we can use the unique function.  For example, you can see the tasters using the unique function.
print(reviews.taster_name.unique()) #print ['Kerin O’Keefe' 'Roger Voss' 'Paul Gregutt' 'Alexander Peartree' 'Michael Schachner' 'Anna Lee C. Iijima' 'Virginie Boone' 'Matt Kettmann' nan 'Sean P. Sullivan' 'Jim Gordon' 'Joe Czerwinski' 'Anne Krebiehl\xa0MW' 'Lauren Buzzeo' 'Mike DeSimone' 'Jeff Jenssen' 'Susan Kostrzewa' 'Carrie Dykes' 'Fiona Adams' 'Christina Pickard']
print(list(reviews.taster_name.unique())) #print ['Kerin O’Keefe', 'Roger Voss', 'Paul Gregutt', 'Alexander Peartree', 'Michael Schachner', 'Anna Lee C. Iijima', 'Virginie Boone', 'Matt Kettmann', nan, 'Sean P. Sullivan', 'Jim Gordon', 'Joe Czerwinski', 'Anne Krebiehl\xa0MW', 'Lauren Buzzeo', 'Mike DeSimone', 'Jeff Jenssen', 'Susan Kostrzewa', 'Carrie Dykes', 'Fiona Adams', 'Christina Pickard']
#To see a list of unique values and how often they occur in the dataset, we can use the value_counts method.
print(reviews.taster_name.value_counts())
'''
Roger Voss           25514
Michael Schachner    15134
                     ...  
Fiona Adams             27
Christina Pickard        6
Name: taster_name, Length: 19, dtype: int64
'''

#A "map" is a term for a function that takes one set of values and "maps" them to another set of values. In data science we often have a need for creating new representations from existing data, or for transforming data from the format it is in now to the format that we want it to be in later.
#There are two mapping method that you will use often. Series.map is the first, and slightly simpler one. For example, suppose that we wanted to remean the scores the wines recieved to 0.  #RM:  I don't see the remean the scores the wines received to 0.  I believe the Series.map is reviews from reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0) and points is the column name to remean the scores the wines received to 0.
review_points_mean = reviews.points.mean()
print(reviews.points.map(lambda p: p - review_points_mean))
'''
0        -1.447138
1        -1.447138
            ...   
129969    1.552862
129970    1.552862
Name: points, Length: 129971, dtype: float64
'''
#The function you pass to map should expect a single value from the Series (a point value, in the above example), and return a transformed version of that value. map returns a new Series where all the values have been transformed by your function.
#DataFrame.apply is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.  #RM:  I think the method DataFrame.apply below remean the scores the wines received to 0.  The DataFrame is the reviews from reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0).
def remean_points(row):
    row.points = row.points - review_points_mean
    return row
print(reviews.apply(remean_points, axis='columns'))
'''
Name: points, Length: 129971, dtype: float64
         country          ...                         winery
0          Italy          ...                        Nicosia
1       Portugal          ...            Quinta dos Avidagos
...          ...          ...                            ...
129969    France          ...           Domaine Marcel Deiss
129970    France          ...               Domaine Schoffit

[129971 rows x 13 columns]
'''
#Note that Series.map and DataFrame.apply return new, transformed Series and DataFrames, respectively. They don't modify the original data they're called on.  Please note #RM:  It's the two python code above.
#Pandas provides many common mapping operations as built-ins. For example, here's a faster way of remeaning our points column.  We are performing an operation between a lot of values on the left-hand side (everything in the Series) and a single value on the right-hand side (the mean value). pandas looks at this expression and figures out that we must mean to subtract that mean value from every value in the dataset.
review_points_mean = reviews.points.mean()
print(reviews.points - review_points_mean)
'''
0        -1.447138
1        -1.447138
            ...   
129969    1.552862
129970    1.552862
Name: points, Length: 129971, dtype: float64
'''
#pandas will also understand what to do if we perform these operations between Series of equal length. For example, an easy way of combining country and region information in the dataset would be to do the following.
print(reviews.country + " - " + reviews.region_1)
'''
0            Italy - Etna
1                     NaN
               ...       
129969    France - Alsace
129970    France - Alsace
Length: 129971, dtype: object
'''

#3.  Summary Functions and Maps Exercises
import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
#What is the median of the "points" column in the "reviews" DataFrame?
print(reviews.points.median()) #print 88.0
#What countries are represented in the dataset? (Your answer should not include any duplicates.)
print(reviews.country.unique()) #print ['Italy' 'Portugal' 'US' 'Spain' 'France' 'Germany' 'Argentina' 'Chile' 'Australia' 'Austria' 'South Africa' 'New Zealand' 'Israel' 'Hungary' 'Greece' 'Romania' 'Mexico' 'Canada' nan 'Turkey' 'Czech Republic' 'Slovenia' 'Luxembourg' 'Croatia' 'Georgia' 'Uruguay' 'England' 'Lebanon' 'Serbia' 'Brazil' 'Moldova' 'Morocco' 'Peru' 'India' 'Bulgaria' 'Cyprus' 'Armenia' 'Switzerland' 'Bosnia and Herzegovina' 'Ukraine' 'Slovakia' 'Macedonia' 'China' 'Egypt']
#How often does each country appear in the dataset? Create a Series "reviews_per_country" mapping countries to the count of reviews of wines from that country.
print(reviews.country.value_counts())
'''
US          54504
France      22093
            ...  
Slovakia        1
Egypt           1
Name: country, Length: 43, dtype: int64
'''
#Create variable "centered_price" containing a version of the "price" column with the mean price subtracted.  (Note: this 'centering' transformation is a common preprocessing step before applying various machine learning algorithms.) 
print(reviews.price - reviews.price.mean())
'''
0               NaN
1        -20.363389
            ...    
129969    -3.363389
129970   -14.363389
Name: price, Length: 129971, dtype: float64
'''
#I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable "bargain_wine" with the title of the wine with the highest points-to-price ratio in the dataset.
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
print(bargain_wine) #print Bandit NV Merlot (California)
#There are only so many words you can use when describing a bottle of wine. Is a wine more likely to be "tropical" or "fruity"? Create a Series "descriptor_counts" counting how many times each of these two words appears in the "description" column in the dataset.
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
print(descriptor_counts)
'''
tropical    3607
fruity      9090
dtype: int64
'''
#We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.
#Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.
#Create a series "star_ratings" with the number of stars corresponding to each review in the dataset.
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
star_ratings = reviews.apply(stars, axis='columns')
print(star_ratings)
'''
0         2
1         2
         ..
129969    2
129970    2
Length: 129971, dtype: int64
'''
#4.   Grouping and Sorting
import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)
#We can replicate what value_counts does using groupby by doing the following.  groupby created groups of reviews with the same point values. Then, for each group, it counted the size of the group.
print(reviews.groupby("points").points.count())
'''
points
80     397
81     692
      ... 
99      33
100     19
Name: points, Length: 21, dtype: int64
'''
#count was the aggregation for each group.  There are others.  For example, to get the cheapest wine in each point value category, we can do the following:
print(reviews.groupby("points").price.min())
'''
points
80      5.0
81      5.0
       ... 
99     44.0
100    80.0
Name: price, Length: 21, dtype: float64
'''
#You can think of each group we generate as being a slice of our DataFrame containing only data with values that match. This DataFrame is accessible to us directly using the apply method, and we can then manipulate the data in any way we see fit. For example, here's one way of selecting the name of the first wine reviewed from each winery in the dataset:
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))
'''
winery
1+1=3                          1+1=3 NV Rosé Sparkling (Cava)
10 Knots                 10 Knots 2010 Viognier (Paso Robles)
                                  ...                        
àMaurice    àMaurice 2013 Fred Estate Syrah (Walla Walla V...
Štoka                         Štoka 2009 Izbrani Teran (Kras)
Length: 16757, dtype: object
'''
#For even more fine-grained control, you can also group by more than one column. For an example, here's how we would pick out the best wine by country and province:
print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.argmax()]))
'''
temppython.py:38: FutureWarning: 'argmax' is deprecated, use 'idxmax' instead. The behavior of 'argmax'
will be corrected to return the positional maximum in the future.
Use 'series.values.argmax' to get the position of the maximum now.
  print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.argmax()]))
                              country          ...                         winery
country   province                             ...                               
Argentina Mendoza Province  Argentina          ...           Bodega Catena Zapata
          Other             Argentina          ...                         Colomé
...                               ...          ...                            ...
Uruguay   San Jose            Uruguay          ...                 Castillo Viejo
          Uruguay             Uruguay          ...                        Narbona

[425 rows x 13 columns]
'''
#Another groupby method worth mentioning is agg, which lets you run a bunch of different functions on your DataFrame simultaneously. For example, we can generate a simple statistical summary of the dataset as follows:
print(reviews.groupby(['country']).price.agg([len, min, max]))
'''
              len   min    max
country                       
Argentina  3800.0   4.0  230.0
Armenia       2.0  14.0   15.0
...           ...   ...    ...
Ukraine      14.0   6.0   13.0
Uruguay     109.0  10.0  130.0

[43 rows x 3 columns]
'''
#groupby sometimes result in a "multi-index."  A multi-index has multiple levels. For example:
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)
'''
                             len
country   province              
Argentina Mendoza Province  3264
          Other              536
...                          ...
Uruguay   San Jose             3
          Uruguay             24

[425 rows x 1 columns]
'''
#Multi-indices have several methods for dealing with their tiered structure which are absent for single-level indices. They also require two levels of labels to retrieve a value, an operation that looks something like this.
#There are detailed instructions using MultiIndex in the pandas documentation https://pandas.pydata.org/pandas-docs/stable/advanced.html
#The MultiIndex method you will use most often is the one for converting back to a regular index, the reset_index method:
print(countries_reviewed.reset_index())
'''
       country          province   len
0    Argentina  Mendoza Province  3264
1    Argentina             Other   536
..         ...               ...   ...
423    Uruguay          San Jose     3
424    Uruguay           Uruguay    24

[425 rows x 3 columns]
'''
#Grouping returns data in index order, not in value order. That is to say, when outputting the result of a groupby, the order of the rows is dependent on the values in the index, not the data.  But you can sort the data with the sort_values method.
countries_reviewed = countries_reviewed.reset_index()
print(countries_reviewed.sort_values(by='len'))
'''
    country               province    len
179  Greece  Muscat of Kefallonian      1
192  Greece          Sterea Ellada      1
..      ...                    ...    ...
415      US             Washington   8639
392      US             California  36247

[425 rows x 3 columns]
'''
#sort_values defaults to an ascending sort, where the lowest values go first. Most of the time we want a descending sort however, where the higher numbers go first.
print(countries_reviewed.sort_values(by='len', ascending=False))
'''
    country    province    len
392      US  California  36247
415      US  Washington   8639
..      ...         ...    ...
63    Chile     Coelemu      1
149  Greece      Beotia      1

[425 rows x 3 columns]
'''
#To sort by index values, use the companion method sort_index. This method has the same arguments and default order:
print(countries_reviewed.sort_index())
'''
       country          province   len
0    Argentina  Mendoza Province  3264
1    Argentina             Other   536
..         ...               ...   ...
423    Uruguay          San Jose     3
424    Uruguay           Uruguay    24

[425 rows x 3 columns]
'''
#Finally, know that you can sort by more than one column at a time:
print(countries_reviewed.sort_values(by=['country', 'len']))
'''
       country          province   len
1    Argentina             Other   536
0    Argentina  Mendoza Province  3264
..         ...               ...   ...
424    Uruguay           Uruguay    24
419    Uruguay         Canelones    43

[425 rows x 3 columns]
'''

#4.  Grouping and Sorting Exercises
#Who are the most common wine reviewers in the dataset? Create a `Series` whose index is the `taster_twitter_handle` category from the dataset, and whose values count how many reviews each person wrote.
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
#or
reviews_written = reviews.groupby('taster_twitter_handle').size()
#What is the best wine I can buy for a given amount of money? Create a `Series` whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review. Sort the values by price, ascending (so that `4.0` dollars is at the top and `3300.0` dollars is at the bottom).
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
#What are the minimum and maximum prices for each `variety` of wine? Create a `DataFrame` whose index is the `variety` category from the dataset and whose values are the `min` and `max` values thereof.
price_extremes = reviews.groupby(['variety']).price.agg([min, max])
#What are the most expensive wine varieties? Create a variable `sorted_varieties` containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price, then on maximum price (to break ties).
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
#Create a `Series` whose index is reviewers and whose values is the average review score given out by that reviewer. Hint: you will need the `taster_name` and `points` columns.
reviewer_mean_ratings = reviews.groupby("taster_name").points.mean()
#What combination of countries and varieties are most common? Create a `Series` whose index is a `MultiIndex`of `{country, variety}` pairs. For example, a pinot noir produced in the US should map to `{"US", "Pinot Noir"}`. Sort the values in the `Series` in descending order based on wine count.
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)

#5 Data Types And Missing Data