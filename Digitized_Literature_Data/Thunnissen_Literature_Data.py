
def callThunnLit(NBDL_data_path, thunn_data_path):

    import os
    import pandas as pd

    read_path = os.path.join(thunn_data_path, "T1 Rotation - Thunnissen 1995 - Update.csv")
    Spine_Ry_Thunnissen = pd.read_csv(read_path, sep=',', engine = 'python', index_col=False)
    Spine_Ry_Thunnissen['Time_ms'] = Spine_Ry_Thunnissen['Time_ms']/1000
    Spine_Ry_Thunnissen.rename(columns = {'Time_ms':'Time_s'}, inplace = True)
    new_path = os.path.join(NBDL_data_path, "T1 Rotation - Thunnissen 1995 - Average Ry.xlsx")
    Spine_Ry_Thunnissen.to_excel(new_path)

    print("returned Thunnissen data\n")

    return Spine_Ry_Thunnissen