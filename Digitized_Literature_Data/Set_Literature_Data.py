from A_Process_NBDL_Data import NBDL_Compiled_Data as NBDL
from Digitized_Literature_Data import Panzer_Literature_Data as panzer_lit
from Digitized_Literature_Data import Thunnissen_Literature_Data as thunn_lit

def set_literature_data():
    # NBDL data needed for comparison
    NBDL_data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\15G NBDL Data\Processed Data\Compiled Test Data"
    average_data, low_data, high_data = NBDL.callNBDL(NBDL_data_path)

    # Panzer literature data needed for comparison
    panzer_data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\Digitized_Literature_Data\Panzer_Accel_Results_Comparison"
    panzer_data = panzer_lit.callPanzerLit(panzer_data_path)

    # Thunnissen literature data needed for comparison
    thunn_data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\Digitized_Literature_Data\Literature_Summary"
    thunn_data = thunn_lit.callThunnLit(NBDL_data_path, thunn_data_path)

    exp_kinematic_data = {'NBDL_average': average_data,
                         'NBDL_STDEV-1': low_data,
                         'NBDL_STDEV+1': high_data,
                         'panzer_data': panzer_data,
                         'thunn_data': thunn_data
    }
    return exp_kinematic_data