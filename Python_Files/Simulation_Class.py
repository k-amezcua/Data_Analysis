
import os
import pandas as pd

from B_Process_Kinematic_Data.Process_Kinematic_Data import process_kinematic_data
from C_Process_Disc_Data.Process_Disc_Data import Disc
from D_Process_Ligament_Data.Process_Ligament_Data import Ligament
from D_Process_Ligament_Data.Plot_Ligament_Data import plot_ligament_data_summary
from E_Process_Muscle_Data.Process_Muscle_Data import Muscle
from E_Process_Muscle_Data.Plot_Muscle_Data import plot_muscle_data_summary
from F_Process_Injury_Data.NIJ.Calculate_NIJ import calculate_NIJ
from F_Process_Injury_Data.NIJ.Calculate_NIJ import calculate_NIJ
########################################################################################################################
class Simulation:
    def __init__(self, dir_path, disc_dict_list, ligament_dict_list, muscle_dict_list, datalabel,
                 exp_kinematic_data):

        self.dir_path = dir_path
        self.kin_dir_path = os.path.join(dir_path, "Kinematics Data")
        self.disc_dir_path = os.path.join(dir_path, "Disc Data")
        self.lig_dir_path = os.path.join(dir_path, "Ligament Data")
        self.musc_dir_path = os.path.join(dir_path, "Muscle Data")
        self.nij_dir_path = os.path.join(dir_path, "Injury Data\\NIJ")

        self.label = datalabel

        self.exp_kinematic_data = exp_kinematic_data
        self.kinematics = self.process_kinematics()
        self.processed_kinematics = self.load_processed_kinematics()

        self.disc_dict_list = disc_dict_list
        self.discs = self.set_disc_paths(self.disc_dir_path, disc_dict_list)

        self.ligament_dict_list = ligament_dict_list
        self.ligaments = self.set_ligament_paths(self.lig_dir_path, ligament_dict_list)

        self.muscle_dict_list = muscle_dict_list
        self.muscles = self.set_muscle_paths(self.musc_dir_path, muscle_dict_list)

    def process_kinematics(self):

        os.chdir(self.kin_dir_path)
        kin_file_path = os.path.join(self.kin_dir_path, 'results.txt')

        average_data = self.exp_kinematic_data['NBDL_average']
        low_data = self.exp_kinematic_data['NBDL_STDEV-1']
        high_data =  self.exp_kinematic_data['NBDL_STDEV+1']
        panzer_data =  self.exp_kinematic_data['panzer_data']
        thunn_data =  self.exp_kinematic_data['thunn_data']

        process_kinematic_data(self, kin_file_path, average_data, low_data, high_data, panzer_data, thunn_data)

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
    def process_NIJ(self):
        os.chdir(self.nij_dir_path)
        nij_file_path = os.path.join(self.nij_dir_path, 'force_results.txt')
        calculate_NIJ(self, nij_file_path)

    def load_processed_kinematics(self):
        load_path = os.path.join(self.kin_dir_path, 'results.csv')
        # Add your logic to load data from CSV
        if os.path.exists(load_path):
            return pd.read_csv(load_path, sep=',', engine='python', index_col=False)
        else:
            return pd.DataFrame()
