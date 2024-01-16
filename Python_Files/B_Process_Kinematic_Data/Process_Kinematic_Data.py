import os
import re
import pandas as pd
from B_Process_Kinematic_Data.Plot_Kinematic_Data import plot_kinematic_data

def process_kinematics(simulation,
                        average_data, low_data, high_data,
                         average_panzer_x_df, average_panzer_y_df, average_panzer_z_df,
                         Spine_Ry_Thunnissen):

    print(f"Processing kinematic data for: {simulation.label} ----------------------------------------------------------------")

    os.chdir(simulation.kin_dir_path)
    sim_results_file = simulation.kin_txt_file_path

    with open(sim_results_file) as data:
        lines = data.readlines()

    Head_Dx_tracker = []
    Head_Ry_tracker = []
    T1_Dx_tracker = []
    T1_Ry_tracker = []
    T1_wy_tracker = []
    T1_aRy_tracker = []
    T1_aDx_tracker = []
    T1_vx_tracker = []

    Head_Dx_tracker = []  # 1
    Head_Dz_tracker = []  # 2
    Head_aDx_tracker = []  # 3
    Head_aDz_tracker = []  # 4
    Head_Ry_tracker = []  # 5
    Head_aRy_tracker = []  # 6
    Head_vx_tracker = []  # 7
    Head_vz_tracker = []  # 8
    Head_wy_tracker = []  # 9

    T1_Dx_tracker = []  # 10
    T1_Ry_tracker = []  # 11

    time = []

    for i, j in enumerate(lines):
        values = []
        if "Time  = " in j:
            start = i + 2
            timevalues1 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?', lines[start - 2])
            linevalues1 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?', lines[start])
            linevalues2 = re.findall(r'-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *[-+]?\ *[0-9]+)?', lines[start + 8])
            timevalues1 = float(timevalues1[0])
            timevalues1 = round(timevalues1, 6)
            load1 = float(linevalues1[1])
            load1 = round(load1, 6)
            load2 = float(linevalues1[2])
            load2 = round(load2, 6)
            load3 = float(linevalues1[3])
            load3 = round(load3, 6)
            load4 = float(linevalues1[4])
            load4 = round(load4, 6)
            load5 = float(linevalues1[5])
            load5 = round(load5, 6)
            load6 = float(linevalues1[6])
            load6 = round(load6, 6)
            load7 = float(linevalues1[7])
            load7 = round(load7, 6)
            load8 = float(linevalues1[8])
            load8 = round(load8, 6)
            load9 = float(linevalues1[9])
            load9 = round(load9, 6)

            load10 = float(linevalues2[1])
            load10 = round(load10, 6)
            load11 = float(linevalues2[5])
            load11 = round(load11, 6)
            load12 = float(linevalues2[9])
            load12 = round(load12, 6)
            load13 = float(linevalues2[6])
            load13 = round(load13, 6)
            load14 = float(linevalues2[3])
            load14 = round(load14, 6)
            load15 = float(linevalues2[7])
            load15 = round(load15, 5)
            time.append(timevalues1)
            Head_Dx_tracker.append(load1)
            Head_Dz_tracker.append(load2)
            Head_aDx_tracker.append(load3)
            Head_aDz_tracker.append(load4)
            Head_Ry_tracker.append(load5)
            Head_aRy_tracker.append(load6)
            Head_vx_tracker.append(load7)
            Head_vz_tracker.append(load8)
            Head_wy_tracker.append(load9)
            T1_Dx_tracker.append(load10)
            T1_Ry_tracker.append(load11)
            T1_wy_tracker.append(load12)
            T1_aRy_tracker.append(load13)
            T1_aDx_tracker.append(load14)
            T1_vx_tracker.append(load15)

    data = pd.concat([pd.Series(time, name='Sim_Time_s'), pd.Series(Head_Dx_tracker, name='Head_Dx'),
                      pd.Series(Head_Dz_tracker, name='Head_Dz'),
                      pd.Series(Head_aDx_tracker, name='Head_aDx'), pd.Series(Head_aDz_tracker, name='Head_aDz'),
                      pd.Series(Head_Ry_tracker, name='Head_Ry'), pd.Series(Head_aRy_tracker, name='Head_aRy'),
                      pd.Series(Head_vx_tracker, name='Head_vx'), pd.Series(T1_aDx_tracker, name='T1_aDx'),
                      pd.Series(Head_vz_tracker, name='Head_vz'), pd.Series(Head_wy_tracker, name='Head_wy'),
                      pd.Series(T1_Dx_tracker, name='T1_Dx'), pd.Series(T1_Ry_tracker, name='T1_Ry'),
                      pd.Series(T1_vx_tracker, name='T1_vx'),
                      pd.Series(T1_wy_tracker, name='T1_wy'), pd.Series(T1_aRy_tracker, name='T1_aRy')], axis=1)

    data['Head_Dx'] = data['Head_Dx'] * 1000
    data['Head_Dz'] = data['Head_Dz'] * 1000
    data['Head_aDx'] = data['Head_aDx'] / 9.80665
    data['Head_aDz'] = data['Head_aDz'] / 9.80665
    data['Head_Ry'] = data['Head_Ry'] * 57.2958
    data['Head_aRy'] = data['Head_aRy']
    data['Head_vx'] = data['Head_vx'] * 3.6  # m/s to kph
    data['Head_vz'] = data['Head_vz'] * 3.6
    data['Head_wy'] = data['Head_wy'] * 1  # rad/s

    data['T1_Dx'] = data['T1_Dx'] * 1000
    data['T1_Ry'] = data['T1_Ry'] * -57.2958
    data['T1_wy'] = data['T1_wy'] / 1
    data['T1_aRy'] = data['T1_aRy'] / 1
    data['T1_aDx'] = data['T1_aDx'] / 9.80665
    data['T1_vx'] = data['T1_vx'] * 3.6  # m/s to kph
    data['Head_Dx'] = data['Head_Dx'] - data['Head_Dx'].iloc[[0]].values[0]
    data['Head_Dz'] = data['Head_Dz'] - data['Head_Dz'].iloc[[0]].values[0]
    data['Head_Ry'] = data['Head_Ry'] - data['Head_Ry'].iloc[[0]].values[0]

    data['T1_Dx'] = data['T1_Dx'] - data['T1_Dx'].iloc[[0]].values[0]
    data['T1_Ry'] = data['T1_Ry'] - data['T1_Ry'].iloc[[0]].values[0]
    data.loc[-1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data = data.sort_index()

    data['Sim_Rel_Head_Dx'] = (data['Head_Dx'] - data['T1_Dx']) * -1
    data['Sim_Rel_Head_Dz'] = data['Head_Dz']
    data['Sim_Rel_Head_Ry'] = (data['Head_Ry'] - data['T1_Ry'])

    save_sim_results_file = os.path.join(simulation.kin_csv_file_path)
    data.to_csv(save_sim_results_file)

    plot_kinematic_data(data,
                        average_data, low_data, high_data,
                        average_panzer_x_df, average_panzer_y_df, average_panzer_z_df,
                        Spine_Ry_Thunnissen)

    pass

