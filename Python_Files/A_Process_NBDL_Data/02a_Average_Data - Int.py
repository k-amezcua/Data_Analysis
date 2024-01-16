# Import Modules
import os, glob
import pandas as pd
import numpy as np

# Folder Path
# Test = "v01535"


main_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\Original Units\\Compiled Test Data\\"
# averaged_path = "C:\\Users\\kamezcua\\Desktop\\NBDL Data Analysis - Python\\Averaged Test Data\\"
# Changing the current working directory
os.chdir(main_path)

Test = "v01535"
v01535 = main_path + Test + " Compiled Test Data - Integrated.csv"
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
df_v01535['Rel_Head_Dx_mm'] = df_v01535['Head_Ax_G_19'] - df_v01535['Spine_Ax_G_47']
df_v01535['Rel_Head_Dz_mm'] = df_v01535['Head_Az_G_21'] - df_v01535['Spine_Az_G_49']
df_v01535['Rel_Head_to_Sled_Dx_mm'] = df_v01535['Head_Ax_G_19'] - df_v01535['Sled_Ax_G_57']
# print(df_v01535)
# df_v01535.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01635"
v01635 = main_path + Test + " Compiled Test Data - Integrated.csv"
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
df_v01635['Rel_Head_Dx_mm'] = df_v01635['Head_Ax_G_19'] - df_v01635['Spine_Ax_G_47']
df_v01635['Rel_Head_Dz_mm'] = df_v01635['Head_Az_G_21'] - df_v01635['Spine_Az_G_49']
df_v01635['Rel_Head_to_Sled_Dx_mm'] = df_v01635['Head_Ax_G_19'] - df_v01635['Sled_Ax_G_57']
#print(df_v01635)
# df_v01635.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01636"
v01636 = main_path + Test + " Compiled Test Data - Integrated.csv"
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
df_v01636['Rel_Head_Dx_mm'] = df_v01636['Head_Ax_G_19'] - df_v01636['Spine_Ax_G_47']
df_v01636['Rel_Head_Dz_mm'] = df_v01636['Head_Az_G_21'] - df_v01636['Spine_Az_G_49']
df_v01636['Rel_Head_to_Sled_Dx_mm'] = df_v01636['Head_Ax_G_19'] - df_v01636['Sled_Ax_G_57']
#print(df_v01636)
# df_v01636.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01637"
v01637 = main_path + Test + " Compiled Test Data - Integrated.csv"
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
df_v01637['Rel_Head_Dx_mm'] = df_v01637['Head_Ax_G_19'] - df_v01637['Spine_Ax_G_47']
df_v01637['Rel_Head_Dz_mm'] = df_v01637['Head_Az_G_21'] - df_v01637['Spine_Az_G_49']
df_v01637['Rel_Head_to_Sled_Dx_mm'] = df_v01637['Head_Ax_G_19'] - df_v01637['Sled_Ax_G_57']
#print(df_v01637)
# df_v01637.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01638"
v01638 = main_path + Test + " Compiled Test Data - Integrated.csv"
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
df_v01638['Rel_Head_Dx_mm'] = df_v01638['Head_Ax_G_19'] - df_v01638['Spine_Ax_G_47']
df_v01638['Rel_Head_Dz_mm'] = df_v01638['Head_Az_G_21'] - df_v01638['Spine_Az_G_49']
df_v01638['Rel_Head_to_Sled_Dx_mm'] = df_v01638['Head_Ax_G_19'] - df_v01638['Sled_Ax_G_57']
#print(df_v01638)
# df_v01638.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01639"
v01639 = main_path + Test + " Compiled Test Data - Integrated.csv"
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
df_v01639['Rel_Head_Dx_mm'] = df_v01639['Head_Ax_G_19'] - df_v01639['Spine_Ax_G_47']
df_v01639['Rel_Head_Dz_mm'] = df_v01639['Head_Az_G_21'] - df_v01639['Spine_Az_G_49']
df_v01639['Rel_Head_to_Sled_Dx_mm'] = df_v01639['Head_Ax_G_19'] - df_v01639['Sled_Ax_G_57']
#print(df_v01639)
# df_v01639.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01641"
v01641 = main_path + Test + " Compiled Test Data - Integrated.csv"
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
df_v01641['Rel_Head_Dx_mm'] = df_v01641['Head_Ax_G_19'] - df_v01641['Spine_Ax_G_47']
df_v01641['Rel_Head_Dz_mm'] = df_v01641['Head_Az_G_21'] - df_v01641['Spine_Az_G_49']
df_v01641['Rel_Head_to_Sled_Dx_mm'] = df_v01641['Head_Ax_G_19'] - df_v01641['Sled_Ax_G_57']
# print(df_v01641)
# df_v01641.to_excel(main_path+Test+" Test.xlsx", header=False, index=False)

Test = "v01644"
v01644 = main_path + Test + " Compiled Test Data - Integrated.csv"
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
df_v01644['Rel_Head_Dx_mm'] = df_v01644['Head_Ax_G_19'] - df_v01644['Spine_Ax_G_47']
df_v01644['Rel_Head_Dz_mm'] = df_v01644['Head_Az_G_21'] - df_v01644['Spine_Az_G_49']
df_v01644['Rel_Head_to_Sled_Dx_mm'] = df_v01644['Head_Ax_G_19'] - df_v01644['Sled_Ax_G_57']

average = (df_v01535 + df_v01635+ df_v01636+ df_v01637+ df_v01638+ df_v01639+ df_v01641+ df_v01644)/8

df_stdev = ((df_v01535-average)**2)+((df_v01635-average)**2)+ ((df_v01636-average)**2)+ ((df_v01637-average)**2)+ ((df_v01638-average)**2)+ ((df_v01639-average)**2)+ ((df_v01641-average)**2)+ ((df_v01644-average)**2)
df_stdev = df_stdev/8
df_stdev = df_stdev**0.5

average = average*9.80665*1000
df_stdev = df_stdev*9.80665*1000
average['Time_s'] = average['Time_s']/9.80665/1000
df_stdev['Time_s'] = df_stdev['Time_s']/9.80665/1000
average.columns = ['Time_s', 'Head_Dx_mm_int_19', 'Head_Dz_mm_int_21', 'Sled_Dx_mm_int_57', 'Spine_Dx_mm_int_47',  'Spine_Dz_mm_int_49', 'Rel_Head_Dx_mm', 'Rel_Head_Dz_mm', 'Rel_Head_to_Sled_Dx_mm']
df_stdev.columns = ['Time_s', 'Head_Dx_mm_int_19', 'Head_Dz_mm_int_21', 'Sled_Dx_mm_int_57', 'Spine_Dx_mm_int_47',  'Spine_Dz_mm_int_49', 'Rel_Head_Dx_mm', 'Rel_Head_Dz_mm', 'Rel_Head_to_Sled_Dx_mm']

average.to_excel(main_path+"Average - Integrated.xlsx")
average.to_csv(main_path+"Average - Integrated.csv")
df_stdev.to_excel(main_path+"Standard Deviation - Integrated.xlsx")
df_stdev.to_csv(main_path+"Standard Deviation - Integrated.csv")
print('complete')