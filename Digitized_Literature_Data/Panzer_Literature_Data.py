
def callPanzerLit(panzer_data_path):

    import os
    import pandas as pd

    panzer_x_path = os.path.join(panzer_data_path, "Passive X Accel.csv")
    average_panzer_x_df = pd.read_csv(panzer_x_path, sep=',', engine = 'python', index_col=False)

    panzer_y_path = os.path.join(panzer_data_path, "Passive Y Rot Accel.csv")
    average_panzer_y_df = pd.read_csv(panzer_y_path, sep=',', engine = 'python', index_col=False)

    panzer_z_path = os.path.join(panzer_data_path, "Passive Z Accel.csv")
    average_panzer_z_df = pd.read_csv(panzer_z_path, sep=',', engine = 'python', index_col=False)


    merge_data = pd.merge(average_panzer_x_df, average_panzer_y_df, on='x')
    panzer_data = pd.merge(merge_data, average_panzer_z_df, on='x')

    print("returned Panzer data")

    return panzer_data