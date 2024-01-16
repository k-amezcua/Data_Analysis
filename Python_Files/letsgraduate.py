from Simulation_Class import Simulation

########################################################################################################################
# Define the path where you want to save the comparison results

compare_save_path = r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\Troubleshooting\LOA Comparison"

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

simulations = [Simulation(dir_path, disc_dict_list, ligament_dict_list, muscle_dict_list, datalabel, exp_kinematic_data) for dir_path, datalabel in zip(dir_paths, datalabels)]

for sim in simulations:
    print(f"Processing Kinematic Data for: {sim.label} ---------------------------------------------------------------")
    sim.process_kinematics()
    print("(completed)\n")

    # print(f"Processing Disc Data for: {sim.label}\n")
    # sim.process_discs()
    # print("(completed)\n")

    # print(f"Processing Ligament Data for: {sim.label}\n")
    # sim.process_ligaments()
    # plot_ligament_data_summary(sim)
    # print("\n(completed)\n")
    #
    # print(f"Processing Muscle Data for: {sim.label}\n")
    # sim.process_muscles()
    # plot_muscle_data_summary(sim)
    # print("\n(completed)\n")

    # print(f"Processing NIJ Data for: {sim.label}\n")
    # sim.process_NIJ()
    # print("\n(completed)\n")

    print(f"Processing Vertebral Rotation Data for: {sim.label}\n")
    sim.process_vertebrae()
    print("(completed)\n")

########################################################################################################################
# COMPARE Data
########################################################################################################################

from G_Analyze_Parametric_Results import Compare_Kinematics as ck

# simulations = [Simulation(dir_path, disc_dict_list, ligament_dict_list, muscle_dict_list, datalabel) for dir_path, datalabel in zip(dir_paths, datalabels)]

# Compare simulation results
# ck.compare_kinematics(compare_save_path, simulations,
#             average_data, low_data, high_data,
#             average_panzer_x_df, average_panzer_y_df, average_panzer_z_df)



