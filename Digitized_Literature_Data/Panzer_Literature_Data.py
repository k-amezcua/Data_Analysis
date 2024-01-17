import os
import pandas as pd

def call_panzer_kinematics(panzer_data_path):



    panzer_x_path = os.path.join(panzer_data_path, "Passive X Accel.csv")
    average_panzer_x_df = pd.read_csv(panzer_x_path, sep=',', engine = 'python', index_col=False)

    panzer_y_path = os.path.join(panzer_data_path, "Passive Y Rot Accel.csv")
    average_panzer_y_df = pd.read_csv(panzer_y_path, sep=',', engine = 'python', index_col=False)

    panzer_z_path = os.path.join(panzer_data_path, "Passive Z Accel.csv")
    average_panzer_z_df = pd.read_csv(panzer_z_path, sep=',', engine = 'python', index_col=False)

    panzer_kinematic_data = {'average_panzer_x_df':average_panzer_x_df,
                             'average_panzer_y_df': average_panzer_y_df,
                             'average_panzer_z_df': average_panzer_z_df
    }

    return panzer_kinematic_data

def call_panzer_vertebrae(panzer_data_path):

    path = os.path.join(panzer_data_path,"Panzer 2006 - Spine Segment Flexion.csv")
    panzer_vertebral_data = pd.read_csv(path, sep=',', engine='python', index_col=False)
    panzer_vertebral_data['x'] = panzer_vertebral_data['x'] / 1000
    panzer_vertebral_data.rename(columns = {'x':'Time_s'}, inplace = True)

    print("returned Panzer data")

    return panzer_vertebral_data