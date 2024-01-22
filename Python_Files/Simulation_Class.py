
import os
import pandas as pd

from B_Process_Kinematic_Data.Process_Kinematic_Data import process_kinematic_data
from B_Process_Kinematic_Data.Process_Vertebral_Data import process_vertebrae_rotations
from C_Process_Disc_Data.Process_Disc_Data import Disc
from D_Process_Ligament_Data.Process_Ligament_Data import Ligament
from E_Process_Muscle_Data.Process_Muscle_Data import Muscle
from F_Process_Injury_Data.NIJ.Calculate_NIJ import calculate_NIJ
########################################################################################################################
class Simulation:
    def __init__(self, compare_dir_path, dir_path, disc_dict_list, ligament_dict_list, muscle_dict_list, datalabel,
                 exp_kinematic_data):

        self.dir_path = dir_path
        self.compare_dir_path = compare_dir_path
        self.kin_dir_path = os.path.join(dir_path, "Kinematics Data")
        #TODO: Create a separate folder for vertebral rotation data:
        self.vert_dir_path = os.path.join(dir_path, "Kinematics Data")
        self.disc_dir_path = os.path.join(dir_path, "Disc Data")
        self.lig_dir_path = os.path.join(dir_path, "Ligament Data")
        self.musc_dir_path = os.path.join(dir_path, "Muscle Data")
        self.nij_dir_path = os.path.join(dir_path, "Injury Data\\NIJ")

        self.label = datalabel

        self.exp_kinematic_data = exp_kinematic_data
        self.average_data = exp_kinematic_data['NBDL_average']
        self.low_data = exp_kinematic_data['NBDL_STDEV-1']
        self.high_data = exp_kinematic_data['NBDL_STDEV+1']
        self.panzer_kinematic_data = exp_kinematic_data['panzer_kinematic_data']
        self.thunn_data = exp_kinematic_data['thunn_data']

        self.kinematics = self.process_kinematics()
        # self.processed_kinematics = self.load_processed_kinematics()

        self.vertebrae = self.process_vertebrae()

        self.disc_dict_list = disc_dict_list
        self.discs = self.set_disc_paths(self.disc_dir_path, disc_dict_list)

        self.ligament_dict_list = ligament_dict_list
        self.ligaments = self.set_ligament_paths(self.lig_dir_path, ligament_dict_list)

        self.muscle_dict_list = muscle_dict_list
        self.muscles = self.set_muscle_paths(self.musc_dir_path, muscle_dict_list)

    def process_kinematics(self):

        os.chdir(self.kin_dir_path)
        kin_file_path = os.path.join(self.kin_dir_path, 'results.txt')

        self.kinematics = process_kinematic_data(self, kin_file_path, self.average_data, self.low_data, self.high_data,
                                                 self.panzer_kinematic_data, self.thunn_data)
        return self.kinematics

    def process_vertebrae(self):

        os.chdir(self.vert_dir_path)
        vert_file_path = os.path.join(self.kin_dir_path, 'results.txt')
        panzer_vertebral_data =  self.exp_kinematic_data['panzer_vertebral_data']

        self.vertebrae = process_vertebrae_rotations(self, vert_file_path, panzer_vertebral_data)
        return self.vertebrae

    def set_disc_paths(self, disc_dir_path, disc_dict_list):
        discs = []
        for disc_dict in disc_dict_list:
            disc_name = disc_dict['disc_name']
            disc_level = disc_dict['disc_level']
            disc_region = disc_dict['disc_region']
            disc_file_path = os.path.join(disc_dir_path, disc_name + '_results.txt')
            num_elements = disc_dict['disc_elements']
            disc_variables = disc_dict['disc_variables']
            discs.append(Disc(disc_name, disc_level, disc_region, num_elements, disc_file_path, disc_variables))
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
            musc_group = musc_dict['muscle_group']
            musc_file_path = os.path.join(musc_dir_path, musc_name + '_results.txt')
            num_elements = musc_dict['muscle_elements']
            muscles.append(Muscle(musc_name, musc_group, num_elements, musc_file_path))
        return muscles

    def process_discs(self):
        os.chdir(self.disc_dir_path)
        for disc in self.discs:
            disc.process_disc_data()

    def group_ligaments_by_level(self):
        grouped = {}
        for lig in self.ligaments:
            level = lig.name.split('_')[0]
            # Special handling for C01, C02, and C12
            if level in ['C01', 'C02', 'C12']:
                combined_level = 'C01_C02_C12'
                if combined_level not in grouped:
                    grouped[combined_level] = []
                grouped[combined_level].append(lig)
            else:
                if level not in grouped:
                    grouped[level] = []
                grouped[level].append(lig)
        return grouped

    def group_discs_by_level(self):
        grouped = {}
        for disc in self.discs:
            level = disc.name.split('_')[0]
            if level not in grouped:
                grouped[level] = []
            grouped[level].append(disc)
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

    def process_NIJ(self):
        os.chdir(self.nij_dir_path)
        nij_file_path = os.path.join(self.nij_dir_path, 'force_results.txt')
        self.nij, self.nij_injury_criterion = calculate_NIJ(self, nij_file_path)

    # def load_processed_kinematics(self):
    #     load_path = os.path.join(self.kin_dir_path, 'results.csv')
    #     # Add your logic to load data from CSV
    #     if os.path.exists(load_path):
    #         self.processed_kinematics = pd.read_csv(load_path, sep=',', engine='python', index_col=False)
    #         return self.processed_kinematics
    #     else:
    #         return pd.DataFrame()

