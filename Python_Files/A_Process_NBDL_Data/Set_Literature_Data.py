from A_Process_NBDL_Data import NBDL_Compiled_Data as NBDL
from Digitized_Literature_Data import Panzer_Literature_Data as panzer_lit
from Digitized_Literature_Data import Thunnissen_Literature_Data as thunn_lit

import os

def set_literature_data():
    # Get the path of the current script
    current_script_path = os.path.dirname(os.path.realpath(__file__))

    # Construct the relative path to the data directory
    NBDL_data_base_path  = os.path.join(current_script_path, '..', '..', '15G NBDL Data', 'Processed Data', 'Compiled Test Data', 'Average')

    # Call the function with the relative path
    average_data, low_data, high_data = NBDL.callNBDL(NBDL_data_base_path )

    # Define the file paths for the Excel files
    average_data_path = os.path.join(NBDL_data_base_path, 'NBDL_average_data.xlsx')
    low_data_path = os.path.join(NBDL_data_base_path, 'NBDL_low_data.xlsx')
    high_data_path = os.path.join(NBDL_data_base_path, 'NBDL_high_data.xlsx')

    # Save each DataFrame to its respective Excel file
    average_data.to_excel(average_data_path, index=False)
    low_data.to_excel(low_data_path, index=False)
    high_data.to_excel(high_data_path, index=False)

    # Define the base path for digitized literature data files
    literature_data_base_path = os.path.join(current_script_path, '..', '..', 'Digitized_Literature_Data')

    # Define file paths for Panzer and Thunnissen data
    panzer_data_path = os.path.join(literature_data_base_path, 'Panzer_Accel_Results_Comparison')
    panzer_vertebral_data_path = os.path.join(literature_data_base_path, 'Spine_Segment_Flexion_Panzer_2006')
    thunn_data_path = os.path.join(literature_data_base_path, 'Literature_Summary')

    # Call functions with the updated paths
    panzer_kinematic_data = panzer_lit.call_panzer_kinematics(panzer_data_path)
    panzer_vertebral_data = panzer_lit.call_panzer_vertebrae(panzer_vertebral_data_path)
    thunn_data = thunn_lit.callThunnLit(NBDL_data_base_path, thunn_data_path)

    exp_kinematic_data = {'NBDL_average': average_data,
                         'NBDL_STDEV-1': low_data,
                         'NBDL_STDEV+1': high_data,
                         'panzer_kinematic_data': panzer_kinematic_data,
                         'panzer_vertebral_data': panzer_vertebral_data,
                         'thunn_data': thunn_data
    }
    return exp_kinematic_data