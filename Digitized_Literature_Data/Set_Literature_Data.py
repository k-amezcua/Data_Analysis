from A_Process_NBDL_Data import NBDL_Compiled_Data as NBDL
from Digitized_Literature_Data import Panzer_Literature_Data as panzer_lit
from Digitized_Literature_Data import Thunnissen_Literature_Data as thunn_lit

def set_literature_data():
    # NBDL data needed for comparison
    NBDL_data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\15G NBDL Data\Processed Data\Compiled Test Data"
    average_data, low_data, high_data = NBDL.callNBDL(NBDL_data_path)

    import pandas as pd

    # Define the file paths for the Excel files
    average_data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\15G NBDL Data\Processed Data\Compiled Test Data\NBDL_average_data.xlsx"
    low_data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\15G NBDL Data\Processed Data\Compiled Test Data\NBDL_low_data.xlsx"
    high_data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\15G NBDL Data\Processed Data\Compiled Test Data\NBDL_high_data.xlsx"

    # Save each DataFrame to its respective Excel file
    average_data.to_excel(average_data_path, index=False)
    low_data.to_excel(low_data_path, index=False)
    high_data.to_excel(high_data_path, index=False)

    # Panzer kinematics literature data needed for comparison
    panzer_data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\Digitized_Literature_Data\Panzer_Accel_Results_Comparison"
    panzer_kinematic_data = panzer_lit.call_panzer_kinematics(panzer_data_path)

    # Panzer kinematics literature data needed for comparison
    panzer_vertebral_data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\Digitized_Literature_Data\Spine_Segment_Flexion_Panzer_2006"
    panzer_vertebral_data = panzer_lit.call_panzer_vertebrae(panzer_vertebral_data_path)

    # Thunnissen literature data needed for comparison
    thunn_data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\Digitized_Literature_Data\Literature_Summary"
    thunn_data = thunn_lit.callThunnLit(NBDL_data_path, thunn_data_path)

    exp_kinematic_data = {'NBDL_average': average_data,
                         'NBDL_STDEV-1': low_data,
                         'NBDL_STDEV+1': high_data,
                         'panzer_kinematic_data': panzer_kinematic_data,
                         'panzer_vertebral_data': panzer_vertebral_data,
                         'thunn_data': thunn_data
    }
    return exp_kinematic_data