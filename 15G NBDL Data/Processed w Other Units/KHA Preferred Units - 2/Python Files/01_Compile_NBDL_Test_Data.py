
# Import Modules
import os, glob
import pandas as pd
import numpy as np

# Folder Path
# Test = "v01535"
# Test = "v01635"
# Test = "v01636"
# Test = "v01637"
# Test = "v01638"
# Test = "v01639"
# Test = "v01641"
Test = "v01644"

#Test = "v01535 - Integrated Data"
#Test = "v01635 - Integrated Data"
#Test = "v01636 - Integrated Data"
#est = "v01637 - Integrated Data"
#Test = "v01638 - Integrated Data"
#Test = "v01639 - Integrated Data"
#Test = "v01641 - Integrated Data"
#Test = "v01644 - Integrated Data"

#Test = "v01535 - Integrated Rotation Data"
#Test = "v01635 - Integrated Rotation Data"
#Test = "v01636 - Integrated Rotation Data"
#Test = "v01637 - Integrated Rotation Data"
#Test = "v01638 - Integrated Rotation Data"
#Test = "v01639 - Integrated Rotation Data"
#Test = "v01641 - Integrated Rotation Data"
#Test = "v01644 - Integrated Rotation Data"

path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\15G NBDL Data\\"+Test+"\\"
main_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\KHA Preferred Units - 2\\Compiled Test Data\\"
labels_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\KHA Preferred Units - 2\\Labels\\"
# Changing the current working directory
os.chdir(path)

# Getting the FileNames of all txt files in the current dir.
filenames = [i for i in glob.glob(f"*.txt")]

# Creating a List of DataFrames and appending First DataFrame with Time History and Channel 1 Data
df_list = []

first_name = filenames[0]
first_channel_num = int(first_name[-7:-4])
first_file = path+first_name
df_1 = pd.read_csv(first_file, sep='\t', header=None, engine = 'python')

val1 = df_1[1].values[0] #val returns first available Y value at time 0.005 s
row1 = pd.DataFrame([[0,val1]]) #creates a line of data for time 0 s
df_1 = pd.concat([row1, df_1]) #inserts first line of data at time 0 s
df_1.columns = ["Time(s)",first_channel_num] #Names columns
df_1 = df_1.reset_index()
df_1.drop('index', axis=1, inplace=True)
df_list.append(df_1) #Adds DataFrame to DataFrame List

# Reads txt files and stores data within list of DataFrames
for file in filenames[1:]:  # for remaining files...
    text_file = path + file
    # create a DataFrame which returns the first available Y value at time 0.005 s
    userows = [0]
    df_first_row = pd.read_csv(text_file, sep='\t', header=None, engine='python', usecols=[1],
                               skiprows=lambda x: x not in userows)

    df = pd.read_csv(text_file, sep='\t', header=None, engine='python',
                     usecols=[1])  # create DataFrame for each file, reading only the Y values
    df = pd.concat([df_first_row, df])  # inserts first line of data at time 0 s

    channel_num = int(file[-7:-4])
    df.columns = [channel_num]  # name column with Channel Name
    df = df.reset_index()  # Reset index
    df.drop('index', axis=1, inplace=True)
    df_list.append(df)  # Add DataFrame to List of Data Frames
df_concat = pd.concat(df_list, axis=1)

#Read data channel labels and rename text file name
labels = "Data Channel Labels - KHA Preferred Units - 2.txt"
userows = [0]
data_labels = pd.read_csv(labels_path+labels, sep = '\t', header=None, skiprows = 1, engine = 'python')
data_labels.columns = [" ", "Channel", "Location", "Direction", "Measurement", "Units", "Label"] #Names columns

df_concat.rename(columns=dict(zip(data_labels["Channel"], data_labels["Label"])), inplace = True)
df_concat = df_concat.reindex(sorted(df_concat.columns), axis=1)

cols = list(df_concat.columns)
cols = [cols[-1]] + cols[:-1]
df_concat = df_concat[cols]

#Write list of DataFrames to excel
df_concat.to_excel(main_path+"v"+first_name[1:6]+" Compiled Test Data.xlsx")
df_concat.to_csv(main_path+"v"+first_name[1:6]+" Compiled Test Data.csv")