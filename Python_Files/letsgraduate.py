from Simulation_Class import Simulation
import os

########################################################################################################################
# Define the path where you want to save the comparison results

compare_dir_path = r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\Troubleshooting\LOA Comparison"

# Define main simulation directories

dir_paths = [
                r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\Troubleshooting\LOA Testing - 0pt2, 74 ms, FE",
                r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\Troubleshooting\LOA Testing - 1pt0, 74 ms, FE",
                r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Active\74 ms delay\Active - Flexors and Extensors"
                # add more paths as needed
]

# Label each simulation to differentiate the results

datalabels = [
                "0.2 mmf - new LOA",
                "1.0 mmf - new LOA",
                "1.0 mmf - prior LOA"
                # Add more datalabels as needed
]

########################################################################################################################
# Create dictionaries for processing tissue and injury data

from Create_Dictionaries import create_dictionaries
disc_dict_list, ligament_dict_list, muscle_dict_list = create_dictionaries()

########################################################################################################################
# Collect NBDL & Literature Data

from Digitized_Literature_Data.Set_Literature_Data import set_literature_data
exp_kinematic_data = set_literature_data()

########################################################################################################################
# Process & Plot Data for Each Simulation
########################################################################################################################

from D_Process_Ligament_Data.Plot_Ligament_Data import plot_ligament_data_summary
from E_Process_Muscle_Data.Plot_Muscle_Data import plot_muscle_data_summary

simulations = [Simulation(compare_dir_path, dir_path, disc_dict_list, ligament_dict_list, muscle_dict_list, datalabel, exp_kinematic_data) for dir_path, datalabel in zip(dir_paths, datalabels)]

for sim in simulations:
    print(f"Processing Kinematic Data for: {sim.label} ---------------------------------------------------------------")
    sim.process_kinematics()
    print("(completed)\n")

    # print(f"Processing Vertebral Rotation Data for: {sim.label}\n")
    # sim.process_vertebrae()
    # print("(completed)\n")

    # print(f"Processing Disc Data for: {sim.label}\n")
    # sim.process_discs()
    # print("(completed)\n")
    #
    # print(f"Processing Ligament Data for: {sim.label}\n")
    # sim.process_ligaments()
    # # plot_ligament_data_summary(sim)
    # print("\n(completed)\n")
    #
    # print(f"Processing Muscle Data for: {sim.label}\n")
    # sim.process_muscles()
    # # plot_muscle_data_summary(sim)
    # print("\n(completed)\n")
    #
    # print(f"Processing NIJ Data for: {sim.label}\n")
    # sim.process_NIJ()
    # print("\n(completed)\n")


from G_Analyze_Parametric_Results.Compare_Kinematics import compare_kinematic_data
from G_Analyze_Parametric_Results.Compare_Vertebral_Data import compare_vertebral_data
os.chdir(compare_dir_path)

print(f"Comparing Kinematic Data")
compare_kinematic_data(simulations, exp_kinematic_data)
print("\n(completed)\n")

print(f"Comparing Vertebral Data")
compare_vertebral_data(simulations, exp_kinematic_data['panzer_vertebral_data'])
print("\n(completed)\n")



