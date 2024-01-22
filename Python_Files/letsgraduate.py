from Simulation_Class import Simulation
import os

########################################################################################################################
# Define the path where you want to save the comparison results

compare_dir_path = r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\Troubleshooting\LOA Comparison"

# Define main simulation directories

dir_paths = [
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\Troubleshooting\LOA Testing - 0pt2, 74 ms, FE",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\Troubleshooting\LOA Testing - 1pt0, 74 ms, FE",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Active\74 ms delay\Active - Flexors and Extensors",
                r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Passive",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Active\74 ms delay\Active - Flexors and Extensors\smaller_time_step",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Active\74 ms delay\Active - Flexors and Extensors\smaller_time_step\slightly_large_step"
                # add more paths as needed
]

# Label each simulation to differentiate the results

datalabels = [
                # "0pt2_mmf_new_LOA",
                # "1pt0_mmf_new_LOA",
                # "1pt0_mmf_prior_LOA",
                "passive",
                # "1pt0_mmf_prior_LOA_small_step",
                # "1pt0_mmf_prior_LOA_larger_step"
                # Add more datalabels as needed
]

########################################################################################################################
# Create dictionaries for processing tissue and injury data

from Create_Dictionaries import create_dictionaries
disc_dict_list, ligament_dict_list, muscle_dict_list = create_dictionaries()

########################################################################################################################
# Collect NBDL & Literature Data

from Python_Files.A_Process_NBDL_Data.Set_Literature_Data import set_literature_data
from H_CORA_Analysis.Process_NBDL_for_CORA import pre_process_NBDL_for_cora
exp_kinematic_data = set_literature_data()
# pre_process_NBDL_for_cora(exp_kinematic_data)
# print('processed NBDL data for CORA\n')


########################################################################################################################
# Process & Plot Data for Each Simulation
########################################################################################################################
from G_Analyze_Parametric_Results.Compare_Kinematics import compare_kinematic_data
from C_Process_Disc_Data.Plot_Disc_Data import plot_disc_data, plot_disc_data_summary
from G_Analyze_Parametric_Results.Tissue_Response import peak_ligament_values, compare_peak_ligament_values
from G_Analyze_Parametric_Results.Plot_Tissue_Response_Tables import plot_individual_ligament_table, plot_comparison_ligament_table
from G_Analyze_Parametric_Results.Tissue_Response import compare_peak_muscle_values, peak_muscle_values
from G_Analyze_Parametric_Results.Plot_Tissue_Response_Tables import plot_comparison_muscle_table, plot_individual_muscle_table
from H_CORA_Analysis.Process_Simulations_for_CORA import pre_process_sim_for_cora
from G_Analyze_Parametric_Results.Global_Response import determine_NIJ, compare_NIJ
from G_Analyze_Parametric_Results.Plot_Global_Response import plot_NIJ_table, plot_NIJ_comparison_table
from G_Analyze_Parametric_Results.Tissue_Response import peak_vertebra, compare_peak_vertebra, peak_disc_values, compare_peak_disc_values
from G_Analyze_Parametric_Results.Plot_Tissue_Response_Tables import plot_peak_vertebra_table, plot_vertebra_comparison_table, plot_disc_stress_table, plot_disc_strain_table, plot_disc_comparison_table
from G_Analyze_Parametric_Results.Global_Response import determine_peak_global_response, compare_peak_global_response
from G_Analyze_Parametric_Results.Plot_Global_Response import plot_peak_global_response_table, plot_peak_global_comparison_table

simulations = [Simulation(compare_dir_path, dir_path, disc_dict_list, ligament_dict_list, muscle_dict_list, datalabel, exp_kinematic_data) for dir_path, datalabel in zip(dir_paths, datalabels)]

nij_values_dict = {}
peak_vertebra_values_dict = {}
peak_global_response_dict = {}
peak_disc_values_dict = {}
peak_muscle_stress_values_dict = {}
peak_muscle_strain_values_dict = {}
peak_lig_force_values_dict = {}
peak_lig_stretch_values_dict = {}
peak_muscle_force_values_dict = {}
peak_muscle_stretch_values_dict = {}

for sim in simulations:

    # print(f"Processing Kinematic Data for: {sim.label} ---------------------------------------------------------------")
    # sim.process_kinematics()
    # pre_process_sim_for_cora(sim)
    # print(f"Processing data for CORA")
    #
    # print(f"Processing NIJ Data")
    # sim.process_NIJ()
    #
    # print(f"Calculating Peak Global Response")
    #
    # peak_global_response = determine_peak_global_response(sim)
    # peak_global_response_dict[sim.label] = peak_global_response
    # plot_peak_global_response_table(peak_global_response_dict)
    #
    # nij_values_dict[sim.label] = determine_NIJ(sim)
    # plot_NIJ_table(nij_values_dict)
    # print(f"Completed\n")

    # ###################################################################
    #
    # print(f"Processing Vertebral Rotation Data for: {sim.label}")
    # sim.process_vertebrae()
    #
    # print(f"Calculating Peak Vertebral Rotations")
    # peak_vertebra_values_dict[sim.label] = peak_vertebra(sim)
    # # plot_peak_vertebra_table(peak_vertebra_values_dict)
    # print("(completed)\n")

    ###################################################################

    # print(f"Processing Disc Data for: {sim.label}\n")
    # sim.process_discs()
    # grouped_discs = sim.group_discs_by_level()
    #
    # for level, discs in grouped_discs.items():
    #     plot_disc_data(level, discs)
    # # plot_disc_data_summary(grouped_discs, 'stress')
    # # plot_disc_data_summary(grouped_discs, 'strain')
    # print("(completed)\n")
    #
    # peak_stress, peak_strain = peak_disc_values(sim)
    # peak_muscle_stress_values_dict[sim.label] = peak_stress
    # peak_muscle_strain_values_dict[sim.label] = peak_strain

    # plot_disc_stress_table(peak_muscle_stress_values_dict)
    # plot_disc_strain_table(peak_muscle_strain_values_dict)

    ###################################################################
    #
    # print(f"Processing Ligament Data for: {sim.label}\n")
    # sim.process_ligaments()
    # sim.grouped_ligaments = sim.group_ligaments_by_level()
    # # plot_ligament_data_summary(sim)
    #
    # peak_force, peak_stretch = peak_ligament_values(sim)
    # peak_lig_force_values_dict[sim.label] = peak_force
    # peak_lig_stretch_values_dict[sim.label] = peak_stretch
    #
    # plot_individual_ligament_table(peak_lig_force_values_dict, "Ligament Force")
    # plot_individual_ligament_table(peak_lig_stretch_values_dict, "Ligament Stretch")
    #
    # print("\n(completed)\n")

    ###################################################################

    print(f"Processing Muscle Data for: {sim.label}\n")
    sim.process_muscles()
    # plot_muscle_data_summary(sim)
    print("\n(completed)\n")

    peak_force, peak_stretch = peak_muscle_values(sim)
    peak_muscle_force_values_dict[sim.label] = peak_force
    peak_muscle_stretch_values_dict[sim.label] = peak_stretch
    plot_individual_muscle_table(peak_force, "Muscle Force", sim.label)
    plot_individual_muscle_table(peak_stretch, "Muscle Stretch", sim.label)

os.chdir(compare_dir_path)

#########################################################################################

# print(f"Comparing Kinematic Data")
# compare_kinematic_data(simulations, exp_kinematic_data)
# print("\n(completed)\n")

# print(f"Comparing Peak Global Response")
#
# nij_comparison = compare_NIJ(simulations)
# plot_NIJ_comparison_table(nij_comparison)
#
# global_comparison = compare_peak_global_response(simulations)
# plot_peak_global_comparison_table(global_comparison)

#########################################################################################

# print(f"Comparing Vertebral Data")
# compare_vertebral_data(simulations, exp_kinematic_data['panzer_vertebral_data'])
# print("\n(completed)\n")

# print(f"Comparing Peak Vertebral Rotations")
# vertebral_comparison_df = compare_peak_vertebra(simulations)
# plot_vertebra_comparison_table(vertebral_comparison_df)

#########################################################################################

# print(f"Comparing Disc Data")
# compare_disc_data(simulations)
# print("\n(completed)\n")

# print(f"Comparing Peak Disc Data")
# disc_stress_comparison, disc_strain_comparison = compare_peak_disc_values(simulations)
# plot_disc_comparison_table(disc_stress_comparison, "Stress")
# plot_disc_comparison_table(disc_strain_comparison, "Strain")

#########################################################################################

# print(f"Comparing Ligament Data")
# # Call the function in your main script
# for level in ['C01_C02_C12', 'C23', 'C34', 'C45', 'C56', 'C67', 'C7T1']:  # Add other levels as needed
#     compare_ligament_data(simulations, level)
# print("\n(completed)\n")

# print(f"Comparing Peak Ligament Data")
# lig_force_comparison, lig_stretch_comparison = compare_peak_ligament_values(simulations)
# plot_comparison_ligament_table(lig_force_comparison, "Ligament Force Comparison")
# plot_comparison_ligament_table(lig_stretch_comparison, "Ligament Stretch Comparison")
#########################################################################################

# print(f"Comparing Muscle Data")
# # Call the function in your main script
# compare_muscle_data(simulations)
# print("\n(completed)\n")

muscle_force_comparison, muscle_stretch_comparison = compare_peak_muscle_values(simulations)
plot_comparison_muscle_table(muscle_force_comparison, "Muscle Force Comparison")
plot_comparison_muscle_table(muscle_stretch_comparison, "Muscle Stretch Comparison")
#########################################################################################

# print(f"Comparing NIJ Data")
# # Call the function in your main script
# compare_nij_data(simulations)
# print("\n(completed)\n")

# #########################################################################################






