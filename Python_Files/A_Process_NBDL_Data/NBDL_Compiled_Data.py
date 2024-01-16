
def callNBDL(NBDL_data_path):

    import os
    import pandas as pd

    path = os.path.join(NBDL_data_path, "Average.csv")
    average_df = pd.read_csv(path, sep=',', engine='python', index_col=False)

    path = os.path.join(NBDL_data_path, "Standard Deviation.csv")
    stdev_df = pd.read_csv(path, sep=',', engine='python', index_col=False)

    low = average_df - stdev_df
    high = average_df + stdev_df

    path = os.path.join(NBDL_data_path, "Average - Integrated.csv")
    average_df_int = pd.read_csv(path, sep=',', engine = 'python', index_col=False)

    path = os.path.join(NBDL_data_path, "Standard Deviation - Integrated.csv")
    stdev_df_int = pd.read_csv(path, sep=',', engine = 'python', index_col=False)

    low_int = average_df_int-stdev_df_int
    high_int = average_df_int+stdev_df_int

    path = os.path.join(NBDL_data_path, "Average - Integrated Rotation.csv")
    average_df_int_rot = pd.read_csv(path, sep=',', engine = 'python', index_col=False)

    path = os.path.join(NBDL_data_path, "Standard Deviation - Integrated Rotation.csv")
    stdev_df_int_rot = pd.read_csv(path, sep=',', engine = 'python', index_col=False)

    low_int_rot = average_df_int_rot-stdev_df_int_rot
    high_int_rot = average_df_int_rot+stdev_df_int_rot

    #########################################################

    import pandas as pd

    # Merge average_df and average_df_int based on the 'channelt' column
    average_data = pd.merge(average_df, average_df_int, on='Time_s')
    average_data = pd.merge(average_data, average_df_int_rot, on='Time_s')
    low_data = pd.merge(low, low_int, on='Time_s')
    low_data = pd.merge(low_data, low_int_rot, on='Time_s')
    high_data = pd.merge(high, high_int, on='Time_s')
    high_data = pd.merge(high_data, high_int_rot, on='Time_s')

    average_data['Spine_Dx_mm_int_47'] = average_data['Spine_Dx_mm_int_47'] * -1
    average_data['Head_Dx_mm_int_19'] = average_data['Head_Dx_mm_int_19'] / (-1)
    average_data['Head_Vx_kph_10'] = average_data['Head_Vx_kph_10'] * (-1)
    average_data['Head_Ax_G_19'] = average_data['Head_Ax_G_19'] * (-1)

    low_data['Spine_Dx_mm_int_47'] = low_data['Spine_Dx_mm_int_47'] * -1
    low_data['Head_Dx_mm_int_19'] = low_data['Head_Dx_mm_int_19'] / (-1)
    low_data['Head_Vx_kph_10'] = low_data['Head_Vx_kph_10'] * (-1)
    low_data['Head_Ax_G_19'] = low_data['Head_Ax_G_19'] * (-1)

    high_data['Spine_Dx_mm_int_47'] = high_data['Spine_Dx_mm_int_47'] * -1
    high_data['Head_Dx_mm_int_19'] = high_data['Head_Dx_mm_int_19'] / (-1)
    high_data['Head_Vx_kph_10'] = high_data['Head_Vx_kph_10'] * (-1)
    high_data['Head_Ax_G_19'] = high_data['Head_Ax_G_19'] * (-1)

    print("\nreturned NBDL data")

    return (average_data, low_data, high_data)