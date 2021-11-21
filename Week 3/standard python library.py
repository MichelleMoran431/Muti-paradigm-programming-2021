#reference https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/#


import pandas as pd
df = pd.read_csv (r'C:\Users\User\Desktop\repo\Muti-paradigm-programming-2021\example week 3.csv') 

# block 1 - simple stats
mean1 = df['Score'].mean()
sum1 = df['Score'].sum()
max1 = df['Score'].max()
min1 = df['Score'].min()
count1 = df['Score'].count()
median1 = df['Score'].median() 
std1 = df['Score'].std() 
var1 = df['Score'].var()  



# print block 1
print ('Mean score: ' + str(mean1))
print ('Sum of score: ' + str(sum1))
print ('Max score: ' + str(max1))
print ('Min score: ' + str(min1))
print ('Count of score: ' + str(count1))
print ('Median score: ' + str(median1))
print ('Std of score: ' + str(std1))
print ('Var of score: ' + str(var1))
