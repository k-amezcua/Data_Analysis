# Import Modules
import os, glob
import pandas as pd
import numpy as np

# Folder Path
# Test = "v01535"


main_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\KHA Preferred Units\\Compiled Test Data\\"
# averaged_path = "C:\\Users\\kamezcua\\Desktop\\NBDL Data Analysis - Python\\Averaged Test Data\\"
# Changing the current working directory
os.chdir(main_path)

Test = "v01535"
v01535 = main_path + Test + " Compiled Test Data.csv"
df_v01535 = pd.read_csv(v01535, sep=',', header=None,engine = 'python')
df_v01535.drop(0, axis=1, inplace=True)
new_header = df_v01535.iloc[0] #grab the first row for the header
df_v01535 = df_v01535[1:] #take the data less the header row
df_v01535.columns = new_header #set the header row as the df header
df_v01535 = df_v01535.replace(np.NaN,0)

df_v01535 = df_v01535.dropna()
df_v01535 = df_v01535.astype(float)

first_row = df_v01535.iloc[[0]].values[0]
df_v01535 = df_v01535.apply(lambda row: row - first_row, axis=1)
df_v01535.rename(columns = {'Time(s)':'Time_s'}, inplace = True)
# print(df_v01535)
df_v01535.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01635"
v01635 = main_path + Test + " Compiled Test Data.csv"
df_v01635 = pd.read_csv(v01635, sep=',', header=None,engine = 'python')
df_v01635.drop(0, axis=1, inplace=True)
new_header = df_v01635.iloc[0] #grab the first row for the header
df_v01635 = df_v01635[1:] #take the data less the header row
df_v01635.columns = new_header #set the header row as the df header
#df_v01635 = df_v01635.replace(np.NaN,0)
df_v01635 = df_v01635.dropna()
df_v01635 = df_v01635.astype(float)

first_row = df_v01635.iloc[[0]].values[0]
df_v01635 = df_v01635.apply(lambda row: row - first_row, axis=1)
df_v01635.rename(columns = {'Time(s)':'Time_s'}, inplace = True)
#print(df_v01635)
df_v01635.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01636"
v01636 = main_path + Test + " Compiled Test Data.csv"
df_v01636 = pd.read_csv(v01636, sep=',', header=None,engine = 'python')
df_v01636.drop(0, axis=1, inplace=True)
new_header = df_v01636.iloc[0] #grab the first row for the header
df_v01636 = df_v01636[1:] #take the data less the header row
df_v01636.columns = new_header #set the header row as the df header
#df_v01636 = df_v01636.replace(np.NaN,0)
df_v01636 = df_v01636.dropna()
df_v01636 = df_v01636.astype(float)

first_row = df_v01636.iloc[[0]].values[0]
df_v01636 = df_v01636.apply(lambda row: row - first_row, axis=1)
df_v01636.rename(columns = {'Time(s)':'Time_s'}, inplace = True)
#print(df_v01636)
df_v01636.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01637"
v01637 = main_path + Test + " Compiled Test Data.csv"
df_v01637 = pd.read_csv(v01637, sep=',', header=None,engine = 'python')
df_v01637.drop(0, axis=1, inplace=True)
new_header = df_v01637.iloc[0] #grab the first row for the header
df_v01637 = df_v01637[1:] #take the data less the header row
df_v01637.columns = new_header #set the header row as the df header
#df_v01637 = df_v01637.replace(np.NaN,0)
df_v01637 = df_v01637.dropna()
df_v01637 = df_v01637.astype(float)


first_row = df_v01637.iloc[[0]].values[0]
df_v01637 = df_v01637.apply(lambda row: row - first_row, axis=1)
df_v01637.rename(columns = {'Time(s)':'Time_s'}, inplace = True)
#print(df_v01637)
df_v01637.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01638"
v01638 = main_path + Test + " Compiled Test Data.csv"
df_v01638 = pd.read_csv(v01638, sep=',', header=None,engine = 'python')
df_v01638.drop(0, axis=1, inplace=True)
new_header = df_v01638.iloc[0] #grab the first row for the header
df_v01638 = df_v01638[1:] #take the data less the header row
df_v01638.columns = new_header #set the header row as the df header
#df_v01638 = df_v01638.replace(np.NaN,0)
df_v01638 = df_v01638.dropna()
df_v01638 = df_v01638.astype(float)

first_row = df_v01638.iloc[[0]].values[0]
df_v01638 = df_v01638.apply(lambda row: row - first_row, axis=1)
df_v01638.rename(columns = {'Time(s)':'Time_s'}, inplace = True)
#print(df_v01638)
df_v01638.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01639"
v01639 = main_path + Test + " Compiled Test Data.csv"
df_v01639 = pd.read_csv(v01639, sep=',', header=None,engine = 'python')
df_v01639.drop(0, axis=1, inplace=True)
new_header = df_v01639.iloc[0] #grab the first row for the header
df_v01639 = df_v01639[1:] #take the data less the header row
df_v01639.columns = new_header #set the header row as the df header
#df_v01639 = df_v01639.replace(np.NaN,0)
df_v01639 = df_v01639.dropna()
df_v01639 = df_v01639.astype(float)

first_row = df_v01639.iloc[[0]].values[0]
df_v01639 = df_v01639.apply(lambda row: row - first_row, axis=1)
df_v01639.rename(columns = {'Time(s)':'Time_s'}, inplace = True)
#print(df_v01639)
df_v01639.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01641"
v01641 = main_path + Test + " Compiled Test Data.csv"
df_v01641 = pd.read_csv(v01641, sep=',', header=None,engine = 'python')
df_v01641.drop(0, axis=1, inplace=True)
new_header = df_v01641.iloc[0] #grab the first row for the header
df_v01641 = df_v01641[1:] #take the data less the header row
df_v01641.columns = new_header #set the header row as the df header
#df_v01641 = df_v01641.replace(np.NaN,0)
df_v01641 = df_v01641.dropna()
df_v01641 = df_v01641.astype(float)

first_row = df_v01641.iloc[[0]].values[0]
df_v01641 = df_v01641.apply(lambda row: row - first_row, axis=1)
df_v01641.rename(columns = {'Time(s)':'Time_s'}, inplace = True)
# print(df_v01641)
df_v01641.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01644"
v01644 = main_path + Test + " Compiled Test Data.csv"
df_v01644 = pd.read_csv(v01644, sep=',', header=None,engine = 'python')
df_v01644.drop(0, axis=1, inplace=True)
new_header = df_v01644.iloc[0] #grab the first row for the header
df_v01644 = df_v01644[1:] #take the data less the header row
df_v01644.columns = new_header #set the header row as the df header
#df_v01644 = df_v01644.replace(np.NaN,0)
df_v01644 = df_v01644.dropna()
df_v01644 = df_v01644.astype(float)

first_row = df_v01644.iloc[[0]].values[0]
df_v01644 = df_v01644.apply(lambda row: row - first_row, axis=1)
df_v01644.rename(columns = {'Time(s)':'Time_s'}, inplace = True)
#print(df_v01644.head())
df_v01644.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

average = (df_v01535 + df_v01635+ df_v01636+ df_v01637+ df_v01638+ df_v01639+ df_v01641+ df_v01644)/8
print(average)

df_stdev = ((df_v01535-average)**2)+((df_v01635-average)**2)+ ((df_v01636-average)**2)+ ((df_v01637-average)**2)+ ((df_v01638-average)**2)+ ((df_v01639-average)**2)+ ((df_v01641-average)**2)+ ((df_v01644-average)**2)
df_stdev = df_stdev/8
df_stdev = df_stdev**0.5
print(df_stdev)

#convert mm to in
#convert kph to mph
#convert rad to deg
# average[average.columns[pd.Series(average.columns).str.contains('_m/s/s_')]] = average[average.columns[pd.Series(average.columns).str.contains('_m/s/s_')]].multiply(9.80665, axis='index')
average[average.columns[pd.Series(average.columns).str.contains('_in_')]] = average[average.columns[pd.Series(average.columns).str.contains('_in_')]].multiply(0.0393701, axis='index')
average[average.columns[pd.Series(average.columns).str.contains('_mph_')]] = average[average.columns[pd.Series(average.columns).str.contains('_mph_')]].multiply(0.621371, axis='index')
average[average.columns[pd.Series(average.columns).str.contains('deg')]] = average[average.columns[pd.Series(average.columns).str.contains('deg')]].multiply(57.2958, axis='index')

average = average.astype(float)
average.to_excel(main_path+"Average.xlsx")
average.to_csv(main_path+"Average.csv")

#convert mm to in
#convert kph to mph
#convert rad to deg
# df_stdev[df_stdev.columns[pd.Series(df_stdev.columns).str.contains('_m/s/s_')]] = df_stdev[df_stdev.columns[pd.Series(df_stdev.columns).str.contains('_m/s/s_')]].multiply(9.80665, axis='index')
df_stdev[df_stdev.columns[pd.Series(df_stdev.columns).str.contains('_in_')]] = df_stdev[df_stdev.columns[pd.Series(df_stdev.columns).str.contains('_in_')]].multiply(0.0393701, axis='index')
df_stdev[df_stdev.columns[pd.Series(df_stdev.columns).str.contains('_mph_')]] = df_stdev[df_stdev.columns[pd.Series(df_stdev.columns).str.contains('_mph_')]].multiply(0.621371, axis='index')
df_stdev[df_stdev.columns[pd.Series(df_stdev.columns).str.contains('deg')]] = df_stdev[df_stdev.columns[pd.Series(df_stdev.columns).str.contains('deg')]].multiply(57.2958, axis='index')

df_stdev = df_stdev.astype(float)
df_stdev.to_excel(main_path+"Standard Deviation.xlsx")
df_stdev.to_csv(main_path+"Standard Deviation.csv")

print(average)
print(df_stdev)