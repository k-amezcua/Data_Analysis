import os
import pandas as pd
from C_Process_Disc_Data.Process_Disc_Data import Disc
from D_Process_Ligament_Data.Process_Ligament_Data import Ligament
from D_Process_Ligament_Data.Plot_Ligament_Data import plot_ligament_data_summary
from E_Process_Muscle_Data.Process_Muscle_Data import Muscle
from E_Process_Muscle_Data.Plot_Muscle_Data import plot_muscle_data_summary
########################################################################################################################

class Simulation:
    def __init__(self, dir_path, disc_dict_list, ligament_dict_list, muscle_dict_list,
                 datalabel):
        self.dir_path = dir_path
        self.kin_dir_path = os.path.join(dir_path, "Kinematics Data")
        self.disc_dir_path = os.path.join(dir_path, "Disc Data")
        self.lig_dir_path = os.path.join(dir_path, "Ligament Data")
        self.musc_dir_path = os.path.join(dir_path, "Muscle Data")
        self.nij_dir_path = os.path.join(dir_path, "NIJ\\Injury Data")

        self.kin_txt_file_path = os.path.join(self.kin_dir_path, 'results.txt')
        self.kin_csv_file_path = os.path.join(self.kin_dir_path, 'results.csv')

        self.label = datalabel
        self.kin_data = self.read_kinematics(self.kin_csv_file_path)

        self.disc_dict_list = disc_dict_list
        self.discs = self.set_disc_paths(self.disc_dir_path, disc_dict_list)

        self.ligament_dict_list = ligament_dict_list
        self.ligaments = self.set_ligament_paths(self.lig_dir_path, ligament_dict_list)

        self.muscle_dict_list = muscle_dict_list
        self.muscles = self.set_muscle_paths(self.musc_dir_path, muscle_dict_list)

    def read_kinematics(self, kin_csv_file_path):
        # Add your logic to load data from CSV
        if os.path.exists(kin_csv_file_path):
            return pd.read_csv(kin_csv_file_path, sep=',', engine='python', index_col=False)
        else:
            return pd.DataFrame()

    def set_disc_paths(self, disc_dir_path, disc_dict_list):
        discs = []
        for disc_dict in disc_dict_list:
            disc_name = disc_dict['disc_name']
            disc_file_path = os.path.join(disc_dir_path, disc_name + '_results.txt')
            num_elements = disc_dict['disc_elements']
            disc_variables = disc_dict['disc_variables']
            discs.append(Disc(disc_name, num_elements, disc_file_path, disc_variables))
        return discs

    def set_ligament_paths(self, lig_dir_path, ligament_dict_list):
        ligaments = []
        for lig_dict in ligament_dict_list:
            lig_name = lig_dict['ligament_name']
            lig_file_path = os.path.join(lig_dir_path, lig_name + '_results.txt')
            num_elements = lig_dict['ligament_elements']
            ligaments.append(Ligament(lig_name, num_elements, lig_file_path))
        return ligaments

    def set_muscle_paths(self, musc_dir_path, muscle_dict_list):
        muscles = []
        for musc_dict in muscle_dict_list:
            musc_name = musc_dict['muscle_name']
            musc_file_path = os.path.join(musc_dir_path, musc_name + '_results.txt')
            num_elements = musc_dict['muscle_elements']
            muscles.append(Muscle(musc_name, num_elements, musc_file_path))
        return muscles

    def process_discs(self):
        os.chdir(self.disc_dir_path)
        for disc in self.discs:
            disc.process_disc_data()
            disc.plot_disc_data()

    def group_ligaments_by_level(self):
        grouped = {}
        for lig in self.ligaments:
            level = lig.name.split('_')[0]
            if level not in grouped:
                grouped[level] = []
            grouped[level].append(lig)
        return grouped

    def process_ligaments(self):
        os.chdir(self.lig_dir_path)
        for lig in self.ligaments:
            lig.process_ligament_data()
            lig.plot_ligament_data()
    def process_muscles(self):
        os.chdir(self.musc_dir_path)
        for muscle in self.muscles:
            muscle.process_muscle_data()
            muscle.plot_muscle_data()

########################################################################################################################

# Define the path where you want to save the comparison results
compare_save_path = r"C:\Users\kryst\Desktop\THESIS\Data Analysis\00 Parameter Study\Troubleshooting\LOA Comparison"

#Define main simulation directories
dir_paths = [
                # r"C:\Users\kryst\Desktop\THESIS\Data Analysis\00 Parameter Study\Troubleshooting\LOA Testing - 0pt2, 74 ms, FE",
                r"C:\Users\kryst\Desktop\THESIS\Data Analysis\00 Parameter Study\Troubleshooting\LOA Testing - 1pt0, 74 ms, FE",
                r"C:\Users\kryst\Desktop\THESIS\Data Analysis\00 Parameter Study\1pt0 max muscle force\Active\74 ms delay\Active - Flexors and Extensors"
                # add more paths as needed
]

#  Label each simulation to differentiate the results
datalabels = [
                # "0.2 mmf - new LOA",
                "1.0 mmf - new LOA",
                "1.0 mmf - prior LOA"
                # Add more datalabels as needed
]

disc_variables = ['Time', 's1', 's2', 's3', 'E1', 'E2', 'E3']

disc_dict_list = [
    {'disc_name': 'C23_Anterior_Disc', 'disc_elements': 120},
    {'disc_name': 'C23_Posterior_Disc', 'disc_elements': 120},
    {'disc_name': 'C23_Middle_Disc', 'disc_elements': 240},
    {'disc_name': 'C34_Anterior_Disc', 'disc_elements': 144},
    {'disc_name': 'C34_Posterior_Disc', 'disc_elements': 144},
    {'disc_name': 'C34_Middle_Disc', 'disc_elements': 288},
    {'disc_name': 'C45_Anterior_Disc', 'disc_elements': 168},
    {'disc_name': 'C45_Posterior_Disc', 'disc_elements': 168},
    {'disc_name': 'C45_Middle_Disc', 'disc_elements': 336},
    {'disc_name': 'C56_Anterior_Disc', 'disc_elements': 144},
    {'disc_name': 'C56_Posterior_Disc', 'disc_elements': 144},
    {'disc_name': 'C56_Middle_Disc', 'disc_elements': 288},
    {'disc_name': 'C67_Anterior_Disc', 'disc_elements': 120},
    {'disc_name': 'C67_Posterior_Disc', 'disc_elements': 120},
    {'disc_name': 'C67_Middle_Disc', 'disc_elements': 240},
    {'disc_name': 'C7T1_Anterior_Disc', 'disc_elements': 144},
    {'disc_name': 'C7T1_Posterior_Disc', 'disc_elements': 144},
    {'disc_name': 'C7T1_Middle_Disc', 'disc_elements': 288}
]

for disc_dict in disc_dict_list:
    disc_dict['disc_variables'] = disc_variables

# Define ligament information
ligament_dict_list = [
    {'ligament_name': 'C01_AAOM', 'ligament_elements': 4},
    {'ligament_name': 'C01_JC', 'ligament_elements': 26},
    {'ligament_name': 'C01_PAOM', 'ligament_elements': 4},
    {'ligament_name': 'C02_ALAR', 'ligament_elements': 2},
    {'ligament_name': 'C02_APICAL', 'ligament_elements': 1},
    {'ligament_name': 'C02_TM', 'ligament_elements': 1},
    {'ligament_name': 'C02_TM_VC', 'ligament_elements': 4},
    {'ligament_name': 'C12_AAAM', 'ligament_elements': 6},
    {'ligament_name': 'C12_ISL', 'ligament_elements': 4},
    {'ligament_name': 'C12_JC', 'ligament_elements': 16},
    {'ligament_name': 'C12_PAAM', 'ligament_elements': 8},
    {'ligament_name': 'C12_TL', 'ligament_elements': 4},
    {'ligament_name': 'C23_ALL', 'ligament_elements': 4},
    {'ligament_name': 'C23_ISL', 'ligament_elements': 4},
    {'ligament_name': 'C23_JC', 'ligament_elements': 16},
    {'ligament_name': 'C23_LF', 'ligament_elements': 8},
    {'ligament_name': 'C23_PLL', 'ligament_elements': 4},
    {'ligament_name': 'C34_ALL', 'ligament_elements': 4},
    {'ligament_name': 'C34_ISL', 'ligament_elements': 4},
    {'ligament_name': 'C34_JC', 'ligament_elements': 16},
    {'ligament_name': 'C34_LF', 'ligament_elements': 8},
    {'ligament_name': 'C34_PLL', 'ligament_elements': 4},
    {'ligament_name': 'C45_ALL', 'ligament_elements': 4},
    {'ligament_name': 'C45_ISL', 'ligament_elements': 4},
    {'ligament_name': 'C45_JC', 'ligament_elements': 16},
    {'ligament_name': 'C45_LF', 'ligament_elements': 8},
    {'ligament_name': 'C45_PLL', 'ligament_elements': 4},
    {'ligament_name': 'C56_ALL', 'ligament_elements': 4},
    {'ligament_name': 'C56_ISL', 'ligament_elements': 4},
    {'ligament_name': 'C56_JC', 'ligament_elements': 16},
    {'ligament_name': 'C56_LF', 'ligament_elements': 8},
    {'ligament_name': 'C56_PLL', 'ligament_elements': 4},
    {'ligament_name': 'C67_ALL', 'ligament_elements': 4},
    {'ligament_name': 'C67_ISL', 'ligament_elements': 4},
    {'ligament_name': 'C67_JC', 'ligament_elements': 16},
    {'ligament_name': 'C67_LF', 'ligament_elements': 8},
    {'ligament_name': 'C67_PLL', 'ligament_elements': 4},
    {'ligament_name': 'C7T1_ALL', 'ligament_elements': 4},
    {'ligament_name': 'C7T1_ISL', 'ligament_elements': 4},
    {'ligament_name': 'C7T1_JC', 'ligament_elements': 16},
    {'ligament_name': 'C7T1_LF', 'ligament_elements': 8},
    {'ligament_name': 'C7T1_PLL', 'ligament_elements': 4}
    # Add more ligament information as needed
]

for disc_dict in disc_dict_list:
    disc_dict['disc_variables'] = disc_variables

# Define ligament information
muscle_dict_list = [
    {'muscle_name': 'Anterior_Scalene', 'muscle_elements': 8},
    {'muscle_name': 'Iliocostalis_Cervicis', 'muscle_elements': 6},
    {'muscle_name': 'Levator_Scapulae', 'muscle_elements': 8},
    {'muscle_name': 'Longissimus_Capitis', 'muscle_elements': 16},
    {'muscle_name': 'Longissimus_Cervicis', 'muscle_elements': 18},
    {'muscle_name': 'Longus_Capitis', 'muscle_elements': 12},
    {'muscle_name': 'Longus_Colli_Inferior', 'muscle_elements': 8},
    {'muscle_name': 'Longus_Colli_Superior', 'muscle_elements': 8},
    {'muscle_name': 'Longus_Colli_Vertical', 'muscle_elements': 16},
    {'muscle_name': 'Middle_Scalene', 'muscle_elements': 12},
    {'muscle_name': 'Minor_Rhomboid', 'muscle_elements': 4},
    {'muscle_name': 'Multifidus', 'muscle_elements': 12},
    {'muscle_name': 'Oblique_Capitis_Inferior', 'muscle_elements': 2},
    {'muscle_name': 'Oblique_Capitis_Superior', 'muscle_elements': 2},
    {'muscle_name': 'Omohyoid', 'muscle_elements': 2},
    {'muscle_name': 'Posterior_Scalene', 'muscle_elements': 6},
    {'muscle_name': 'RCPM', 'muscle_elements': 2},
    {'muscle_name': 'RCPminor', 'muscle_elements': 2},
    {'muscle_name': 'Rectus_Capitis_Anterior', 'muscle_elements': 2},
    {'muscle_name': 'Rectus_Capitis_Lateralis', 'muscle_elements': 2},
    {'muscle_name': 'SCM', 'muscle_elements': 2},
    {'muscle_name': 'Semispinalis_Capitis', 'muscle_elements': 20},
    {'muscle_name': 'Semispinalis_Cervicis', 'muscle_elements': 12},
    {'muscle_name': 'Splenius_Capitis', 'muscle_elements': 2},
    {'muscle_name': 'Splenius_Cervicis', 'muscle_elements': 12},
    {'muscle_name': 'Sternohyoid', 'muscle_elements': 2},
    {'muscle_name': 'Trapezius', 'muscle_elements': 16},
]

# Create a list of Simulation objects
simulations = [Simulation(dir_path, disc_dict_list, ligament_dict_list, muscle_dict_list, datalabel) for dir_path, datalabel in zip(dir_paths, datalabels)]

########################################################################################################################
# Collect NBDL & Literature Data

from A_Process_NBDL_Data import NBDL_Compiled_Data as NBDL
from Digitized_Literature_Data import Panzer_Literature_Data as panzer_lit
from Digitized_Literature_Data import Thunnissen_Literature_Data as thunn_lit

# NBDL data needed for comparison
NBDL_data_path = r"C:\Users\kryst\Desktop\THESIS\Data Analysis\15G NBDL Data\Processed Data\Compiled Test Data"
average_data, low_data, high_data = NBDL.callNBDL(NBDL_data_path)

# Panzer literature data needed for comparison
panzer_data_path = r"C:\Users\kryst\Desktop\THESIS\Data Analysis\Digitized_Literature_Data\Panzer_Accel_Results_Comparison"
average_panzer_x_df, average_panzer_y_df, average_panzer_z_df = panzer_lit.callPanzerLit(panzer_data_path)

# Thunnissen literature data needed for comparison
thunn_data_path = r"C:\Users\kryst\Desktop\THESIS\Data Analysis\Digitized_Literature_Data\Literature_Summary"
Spine_Ry_Thunnissen = thunn_lit.callThunnLit(NBDL_data_path, thunn_data_path)

########################################################################################################################
# Process Kinematic Data for Each Simulation
########################################################################################################################

from B_Process_Kinematic_Data import Process_Kinematic_Data as kd

# for sim in simulations:
#     kd.process_kinematics(sim,
#                          average_data, low_data, high_data,
#                          average_panzer_x_df, average_panzer_y_df, average_panzer_z_df,
#                          Spine_Ry_Thunnissen)

########################################################################################################################
# COMPARE Kinematic Data
########################################################################################################################

from G_Analyze_Parametric_Results import Compare_Kinematics as ck

simulations = [Simulation(dir_path, disc_dict_list, ligament_dict_list, muscle_dict_list, datalabel) for dir_path, datalabel in zip(dir_paths, datalabels)]

# Compare simulation results
# ck.compare_kinematics(compare_save_path, simulations,
#             average_data, low_data, high_data,
#             average_panzer_x_df, average_panzer_y_df, average_panzer_z_df)

########################################################################################################################
# Process Disc Data for Each Simulation
########################################################################################################################

# Process disc data for each simulation
for sim in simulations:

    # print(f"Processing Disc Data for: {sim.label}\n")
    # sim.process_discs()
    # print("(completed)\n")

    print(f"Processing Ligament Data for: {sim.label}\n")
    sim.process_ligaments()
    plot_ligament_data_summary(sim)
    print("\n(completed)\n")

    print(f"Processing Muscle Data for: {sim.label}\n")
    sim.process_muscles()
    plot_muscle_data_summary(sim)
    print("\n(completed)\n")

########################################################################################################################
# COMPARE Disc Data for Each Simulation
########################################################################################################################


