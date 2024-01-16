import os, glob
import re
import numpy as np
import pandas as pd
path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\0 15 G Sled Test Validation\\11-8\\Passive\\Baseline\\"
os.chdir(path)

filename= 'rotation_results'
with open(path+filename+'.txt') as data:
    lines = data.readlines()

Head_Ry_tracker = [] # 5
C1_Ry_tracker = []
C2_Ry_tracker = []
C3_Ry_tracker = []
C4_Ry_tracker = []
C5_Ry_tracker = []
C6_Ry_tracker = []
C7_Ry_tracker = []
T1_Ry_tracker = []

time = []

for i,j in enumerate(lines):
    values = []
    if "Time  = " in j:

        start = i+2
        timevalues1 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',lines[start-2])
        linevalues0 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',lines[start])
        linevalues1 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',lines[start+1])
        linevalues2 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',lines[start+2])
        linevalues3 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',lines[start+3])
        linevalues4 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',lines[start+4])
        linevalues5 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',lines[start+5])
        linevalues6 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',lines[start+6])
        linevalues7 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',lines[start+7])
        linevalues8 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?',lines[start+8])
        timevalues1 = float(timevalues1[0])
        timevalues1 = round(timevalues1, 6)

        load0 = float(linevalues0[5])
        load0 = round(load0,6)
        load1 = float(linevalues1[5])
        load1 = round(load1,6)
        load2 = float(linevalues2[5])
        load2 = round(load2,6)
        load3 = float(linevalues3[5])
        load3 = round(load3, 6)
        load4 = float(linevalues4[5])
        load4 = round(load4, 6)
        load5 = float(linevalues5[5])
        load5 = round(load5,6)
        load6 = float(linevalues6[5])
        load6 = round(load6, 6)
        load7 = float(linevalues7[5])
        load7 = round(load7, 6)
        load8 = float(linevalues8[5])
        load8 = round(load8, 6)

        time.append(timevalues1)
        Head_Ry_tracker.append(load0)
        C1_Ry_tracker.append(load1)
        C2_Ry_tracker.append(load2)
        C3_Ry_tracker.append(load3)
        C4_Ry_tracker.append(load4)
        C5_Ry_tracker.append(load5)
        C6_Ry_tracker.append(load6)
        C7_Ry_tracker.append(load7)
        T1_Ry_tracker.append(load8)

data = pd.concat([pd.Series(time, name='Sim_Time_s'),pd.Series(Head_Ry_tracker, name='Head_Ry'), pd.Series(C1_Ry_tracker, name='C1_Ry'),
                  pd.Series(C2_Ry_tracker, name='C2_Ry'), pd.Series(C3_Ry_tracker, name='C3_Ry'),
                  pd.Series(C4_Ry_tracker, name='C4_Ry'), pd.Series(C5_Ry_tracker, name='C5_Ry'),
                  pd.Series(C6_Ry_tracker, name='C6_Ry'), pd.Series(C7_Ry_tracker, name='C7_Ry'),
                  pd.Series(T1_Ry_tracker, name='T1_Ry')], axis=1)

data['Head_Ry'] = data['Head_Ry']*57.2958
data['C1_Ry'] = data['C1_Ry']*57.2958
data['C2_Ry'] = data['C2_Ry']*57.2958
data['C3_Ry'] = data['C3_Ry']*57.2958
data['C4_Ry'] = data['C4_Ry']*57.2958
data['C5_Ry'] = data['C5_Ry']*57.2958
data['C6_Ry'] = data['C6_Ry']*57.2958
data['C7_Ry'] = data['C7_Ry']*57.2958
data['T1_Ry'] = data['T1_Ry']*57.2958

data['C12_Ry'] = data['C1_Ry'] - data['C2_Ry']
data['C23_Ry'] = data['C2_Ry'] - data['C3_Ry']
data['C34_Ry'] = data['C3_Ry'] - data['C4_Ry']
data['C45_Ry'] = data['C4_Ry'] - data['C5_Ry']
data['C56_Ry'] = data['C5_Ry'] - data['C6_Ry']
data['C67_Ry'] = data['C6_Ry'] - data['C7_Ry']
data['C7T1_Ry'] = data['C7_Ry'] - data['T1_Ry']

# data['Head_Ry']  = data['Head_Ry'] - data['Head_Ry'].iloc[[0]].values[0]

# data.loc[-1] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# data = data.sort_index()

print(data)
data.to_csv(path+filename+".csv")

####################################################
data_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Digitized Literature Data\\"

path = data_path + "Panzer 2006 - Spine Segment Flexion.csv"
flexion = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
flexion['Time'] = flexion['Time']/1000
print(flexion)
####################################################

channelt = 'Time'

###########################################################################################################
#Quick Plot
import matplotlib as mpl
import matplotlib.pyplot as plt

channelsimt = 'Sim_Time_s'

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(data[channelsimt],data['Head_Ry'], label ='Head_Ry', color = 'red')
# ax.plot(data[channelsimt],data['C12_Ry'], label ='C12_Ry', color = 'orange')
ax.plot(data[channelsimt],data['C23_Ry'], label ='C23_Ry', color = 'bisque')
ax.plot(data[channelsimt],data['C34_Ry'], label ='C34_Ry', color = 'green')
ax.plot(data[channelsimt],data['C45_Ry'], label ='C45_Ry', color = 'yellowgreen')
ax.plot(data[channelsimt],data['C56_Ry'], label ='C56_Ry', color = 'magenta')
ax.plot(data[channelsimt],data['C67_Ry'], label ='C67_Ry', color = 'purple')
ax.plot(data[channelsimt],data['C7T1_Ry'], label ='C7T1_Ry', color = 'cyan')
# ax.plot(data[channelsimt],data['T1_Ry'], label ='T1_Ry', color = 'pink')

# ax.plot(flexion[channelt],flexion['C12'], label ='C12_Panzer', color = 'navy')
# ax.plot(flexion[channelt],flexion['C23'], label ='C23_Panzer', color = 'bisque')
# ax.plot(flexion[channelt],flexion['C34'], label ='C34_Panzer', color = 'green')
# ax.plot(flexion[channelt],flexion['C45'], label ='C45_Panzer', color = 'yellowgreen')
# ax.plot(flexion[channelt],flexion['C56'], label ='C56_Panzer', color = 'magenta')
# ax.plot(flexion[channelt],flexion['C67'], label ='C67_Panzer', color = 'purple')
# ax.plot(flexion[channelt],flexion['C7T1'], label ='C7T1_Panzer', color = 'cyan')

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Sim Results - Flexion (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Simulation Results - Flexion deg.png')
plt.show()

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(data[channelsimt],data['C23_Ry'], label ='C23_Ry', color = 'blue')
ax.plot(flexion[channelt],flexion['C23'], label ='C23_Panzer', color = 'red')

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Sim Results - C23 Flexion (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Sim Results - C23 Flexion deg.png')
plt.show()

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(data[channelsimt],data['C34_Ry'], label ='C34_Ry', color = 'blue')
ax.plot(flexion[channelt],flexion['C34'], label ='C34_Panzer', color = 'red')

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Sim Results - C34 Flexion (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Sim Results - C34 Flexion deg.png')
plt.show()

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(data[channelsimt],data['C45_Ry'], label ='C45_Ry', color = 'blue')
ax.plot(flexion[channelt],flexion['C45'], label ='C45_Panzer', color = 'red')

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Sim Results - C45 Flexion (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Sim Results - C45 Flexion deg.png')
plt.show()

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(data[channelsimt],data['C56_Ry'], label ='C56_Ry', color = 'blue')
ax.plot(flexion[channelt],flexion['C56'], label ='C56_Panzer', color = 'red')

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Sim Results - C56 Flexion (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Sim Results - C56 Flexion deg.png')
plt.show()

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(data[channelsimt],data['C67_Ry'], label ='C67_Ry', color = 'blue')
ax.plot(flexion[channelt],flexion['C67'], label ='C67_Panzer', color = 'red')

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Sim Results - C67 Flexion (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Sim Results - C67 Flexion deg.png')
plt.show()

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(data[channelsimt],data['C7T1_Ry'], label ='C7T1_Ry', color = 'blue')
ax.plot(flexion[channelt],flexion['C7T1'], label ='C7T1_Panzer', color = 'red')

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Sim Results - C7T1 Flexion (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Sim Results - C7T1 Flexion deg.png')
plt.show()

print("complete")