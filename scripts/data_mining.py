import csv
import os
import pandas as pd

print("Before:",os.getcwd()) #check current directory
os.chdir(r'C:\Users\Sia\Documents\quantium_tech_interview\quantium-starter-repo\data') #move to where files are
print("After:",os.getcwd()) #check the changed directory
print("Files in directory:", os.listdir())

#import csv files as dataframes
ds_0 =pd.read_csv('daily_sales_data_0.csv')
print(ds_0.head(n = 5))
#print(len(ds_0))
ds_1 = pd.read_csv('daily_sales_data_1.csv')
print(ds_1.head(n = 5))
#print(len(ds_0))
ds_2 = pd.read_csv('daily_sales_data_2.csv')
#print(ds_2.head(n = 5))
print(len(ds_0))

#remove rows that are not pink morsels
#merge quantity and price by times to create a new column sales
#then remove product as not necessary

#ds_0
print(ds_0.dtypes)
#remove dollar from the price column and make a sales column
ds_0['price'] = ds_0['price'].astype(str)
ds_0['price'] = ds_0['price'].str.replace('$','')
ds_0['price'] = pd.to_numeric(ds_0['price'], errors='coerce')
ds_0['sales'] = ds_0['price']*ds_0['quantity']

#filter for pink morsel
print(len(ds_0))
ds_0 = ds_0[ds_0['product'].str.contains('pink morsel', na = False)]
print(len(ds_0))

#select the required columns
ds_0_processed = ds_0[['sales','date','region']]
print(ds_0.head(n = 5))
print(ds_0_processed.head(n = 5))


#ds_1
#remove dollar from the price column and make a sales column
print(ds_1.dtypes)
ds_1['price'] = ds_1['price'].astype(str)
ds_1['price'] = ds_1['price'].str.replace('$','')
ds_1['price'] = pd.to_numeric(ds_1['price'], errors='coerce')
ds_1['sales'] = ds_1['price']*ds_1['quantity']

#filter for pink morsel
print(len(ds_1))
ds_1 = ds_1[ds_1['product'].str.contains('pink morsel', na = False)]
print(len(ds_1))

#select the required columns
ds_1_processed = ds_1[['sales','date','region']]
print(ds_1.head(n = 5))
print(ds_1_processed.head(n = 5))

#ds_2
#remove dollar from the price column and make a sales column
print(ds_2.dtypes)
ds_2['price'] = ds_2['price'].astype(str)
ds_2['price'] = ds_2['price'].str.replace('$','')
ds_2['price'] = pd.to_numeric(ds_2['price'], errors='coerce')
ds_2['sales'] = ds_2['price']*ds_2['quantity']

#filter for pink morsel
print(len(ds_2))
ds_2 = ds_2[ds_2['product'].str.contains('pink morsel', na = False)]
print(len(ds_2))

#select the required columns
ds_2_processed = ds_2[['sales','date','region']]
print(ds_2.head(n = 5))
print(ds_2_processed.head(n = 5))
