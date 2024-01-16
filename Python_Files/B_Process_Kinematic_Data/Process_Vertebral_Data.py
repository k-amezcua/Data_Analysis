import re
import pandas as pd
import os
from B_Process_Kinematic_Data.Plot_Vertebral_Data import plot_vertebral_data

def process_vertebrae_rotations(simulation, vert_file_path, panzer_vertebral_data):

    with open(vert_file_path) as data:
        lines = data.readlines()

    #TODO: make sure these tracker read the correct data line based on results.txt export parameters
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

    csv_path = os.path.splitext(vert_file_path)[0] + ".csv"
    data.to_csv(csv_path)

    plot_vertebral_data(data, panzer_vertebral_data)

    return data

