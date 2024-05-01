from Simulation_Class import Simulation
import os

########################################################################################################################
# Define the path where you want to save the comparison results

compare_dir_path = r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\Troubleshooting\LOA Comparison"

# Define main simulation directories

dir_paths = [
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Active\74 ms delay\Active - Flexors and Extensors\smaller_time_step",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Active\74 ms delay\Active - Flexors Only",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Active\74 ms delay\Active - Extensors Only",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\74 ms delay\Active - Flexors and Extensors",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\74 ms delay\Active - Flexors Only",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\74 ms delay\Active - Extensors Only",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Active\00 ms delay\Active - Flexors and Extensors",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Active\00 ms delay\Active - Flexors Only",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Active\00 ms delay\Active - Extensors Only",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors and Extensors",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors Only",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors Only\Mid",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors Only\Increment",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors Only\febio3_rerun",
                # r"E:\K\FeBioRuns\kevin\febio3\Kevin\main"
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors Only"
                r"E:\thesis\flexors_1e05_1e03"
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors Only\5e06_5e05"
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors Only\must point\opt_iter_5000_06_5e05"
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors Only\must point\opt_iter_1000"
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Extensors Only",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Passive",
                # r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\1pt0 max muscle force\Passive",

                # add more paths as needed
]

# Label each simulation to differentiate the results

datalabels = [
                # "100_FE_74ms",
                # "100_FO_74ms",
                # "100_EO_74ms",
                # "020_FE_74ms",
                # "020_FO_74ms",
                # "020_EO_74ms",
                # "100_FE_00ms",
                # "100_FO_00ms",
                # "100_EO_00ms",
                # "020_FE_00ms",
                "020_FO_00ms_1e05_1e_03",
                # "020_FO_00ms_5e06_5e05",
                # "020_FO_00ms_opt_iter_5000",
                # "020_FO_00ms_MID",
                # "020_FO_00ms_INCREMENT",
                # "020_FO_00ms_FEBIO3_RERUN",
                # "must_point_opt_iter_1000"
                # "020_EO_00ms",
                # "000_FE_74ms (0.2)",
                # "000_FE_74ms (1.0)"
]

########################################################################################################################
# Create dictionaries for processing tissue and injury data

from Create_Dictionaries import create_dictionaries
disc_dict_list, ligament_dict_list, muscle_dict_list = create_dictionaries()
from H_CORA_Analysis.Process_Simulations_for_CORA import pre_process_sim_for_cora
from H_CORA_Analysis.Process_NBDL_for_CORA import pre_process_NBDL_for_cora
########################################################################################################################
# Collect NBDL & Literature Data

from Python_Files.A_Process_NBDL_Data.Set_Literature_Data import set_literature_data

exp_kinematic_data = set_literature_data()
pre_process_NBDL_for_cora(exp_kinematic_data)
print('processed NBDL data for CORA\n')


########################################################################################################################
# Process & Plot Data for Each Simulation
########################################################################################################################

from C_Process_Disc_Data.Plot_Disc_Data import plot_disc_data, plot_disc_data_summary
from D_Process_Ligament_Data.Plot_Ligament_Data import plot_ligament_data, plot_ligament_data_summary
from E_Process_Muscle_Data.Plot_Muscle_Data import plot_muscle_data, plot_muscle_data_summary

from G_Analyze_Parametric_Results.Compare_Data.Discs.Compare_Disc_Data import compare_disc_data
from G_Analyze_Parametric_Results.Compare_Data.Kinematics.Compare_Kinematics import compare_kinematic_data
from G_Analyze_Parametric_Results.Compare_Data.Ligaments.Compare_Ligament_Data import compare_ligament_data
from G_Analyze_Parametric_Results.Compare_Data.Muscles.Compare_Muscle_Data import compare_muscle_data
from G_Analyze_Parametric_Results.Compare_Data.NIJ.Compare_NIJ_Data import compare_nij_data
from G_Analyze_Parametric_Results.Compare_Data.Vertebral.Compare_Vertebral_Data import compare_vertebral_data

from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_Ligaments.Peak_Ligament_Response import peak_ligament_values, compare_peak_ligament_values
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_Ligaments.Plot_Peak_Ligament_Response import plot_individual_ligament_table, plot_comparison_ligament_table
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_Muscles.Peak_Muscle_Response import compare_peak_muscle_values, peak_muscle_values
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_Muscles.Plot_Peak_Muscle_response import plot_comparison_muscle_table, plot_individual_muscle_table
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_Kinematics.Peak_Kinematics_Response import determine_peak_global_response, compare_peak_global_response
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_Kinematics.Plot_Kinematics_Response import plot_peak_global_response_table, plot_peak_global_comparison_table
from G_Analyze_Parametric_Results.Compare_Data.HIC.Compare_HIC_Data import plot_HIC_comparison, plot_individual_HIC, compare_HIC
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_Discs.Peak_Disc_Response import peak_disc_values, compare_peak_disc_values
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_Discs.Plot_Peak_Disc_Response import plot_disc_strain_table, plot_disc_stress_table, plot_disc_comparison_table
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_NIJ.Peak_NIJ_Response import compare_NIJ, determine_NIJ
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_NIJ.Plot_NIJ_Response import plot_NIJ_table, plot_NIJ_comparison_table
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_Vertebral.Peak_Vertebral_Response import peak_vertebra,compare_peak_vertebra
from G_Analyze_Parametric_Results.Compare_Injury_Potential.Peak_Vertebral.Plot_Vertebral_Response import plot_peak_vertebra_table,plot_vertebra_comparison_table


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

nij_injury_criteria = {
    'Fz_tension': 6806,  # Reference value for Fz in Newtons
    'Fz_compression': -6160,
    'My_extension': -135,   # Reference value for My in Newton-meters
    'My_flexion': 310,
    'NIJ': 1.0   # Reference value for NIJ
}

hic_injury_criteria = 1000

for sim in simulations:

    print(f"Processing Kinematic Data for: {sim.label} ---------------------------------------------------------------")
    sim.process_kinematics()
    pre_process_sim_for_cora(sim)
    print(f"Processing data for CORA")

    # print(f"Processing HIC Data")
    # sim.process_HIC()
    # plot_individual_HIC(sim, hic_injury_criteria)

    # print(f"Processing NIJ Data")
    # sim.process_NIJ()

    print(f"Calculating Peak Global Response")

    peak_global_response = determine_peak_global_response(sim)
    peak_global_response_dict[sim.label] = peak_global_response
    plot_peak_global_response_table(peak_global_response_dict)

    # nij_values_dict[sim.label] = determine_NIJ(sim, nij_injury_criteria)
    # plot_NIJ_table(nij_values_dict)
    print(f"Completed\n")

    # ###################################################################

    print(f"Processing Vertebral Rotation Data for: {sim.label}")
    sim.process_vertebrae()

    print(f"Calculating Peak Vertebral Rotations")
    peak_vertebra_values_dict[sim.label] = peak_vertebra(sim)
    plot_peak_vertebra_table(peak_vertebra_values_dict)
    print("(completed)\n")

    ###################################################################

    print(f"Processing Disc Data for: {sim.label}\n")
    sim.process_discs()
    grouped_discs = sim.group_discs_by_level()

    for level, discs in grouped_discs.items():
        plot_disc_data(level, discs)
    plot_disc_data_summary(grouped_discs, 'stress')
    plot_disc_data_summary(grouped_discs, 'strain')
    print("(completed)\n")

    peak_stress, peak_strain = peak_disc_values(sim)
    peak_muscle_stress_values_dict[sim.label] = peak_stress
    peak_muscle_strain_values_dict[sim.label] = peak_strain

    plot_disc_stress_table(peak_muscle_stress_values_dict)
    plot_disc_strain_table(peak_muscle_strain_values_dict)

    ###################################################################

    print(f"Processing Ligament Data for: {sim.label}\n")
    sim.process_ligaments()
    sim.grouped_ligaments = sim.group_ligaments_by_level()
    plot_ligament_data_summary(sim)

    peak_force, peak_stretch = peak_ligament_values(sim)
    peak_lig_force_values_dict[sim.label] = peak_force
    peak_lig_stretch_values_dict[sim.label] = peak_stretch

    plot_individual_ligament_table(peak_lig_force_values_dict, "Ligament Force")
    plot_individual_ligament_table(peak_lig_stretch_values_dict, "Ligament Stretch")

    print("\n(completed)\n")

    ###################################################################

    print(f"Processing Muscle Data for: {sim.label}\n")
    sim.process_muscles()
    plot_muscle_data_summary(sim)
    print("\n(completed)\n")

    peak_force, peak_stretch = peak_muscle_values(sim)
    peak_muscle_force_values_dict[sim.label] = peak_force
    peak_muscle_stretch_values_dict[sim.label] = peak_stretch
    plot_individual_muscle_table(peak_force, "Muscle Force", sim.label)
    plot_individual_muscle_table(peak_stretch, "Muscle Strain", sim.label)

os.chdir(compare_dir_path)

#########################################################################################

print(f"Comparing Kinematic Data")
compare_kinematic_data(simulations, exp_kinematic_data)
print("\n(completed)\n")

print(f"Comparing Peak Global Response")

global_comparison = compare_peak_global_response(simulations)
plot_peak_global_comparison_table(global_comparison)

# comparison_data = compare_HIC(simulations, hic_injury_criteria)
# plot_HIC_comparison(comparison_data, hic_injury_criteria)

# nij_comparison = compare_NIJ(simulations, nij_injury_criteria)
# plot_NIJ_comparison_table(nij_comparison)

# ########################################################################################

print(f"Comparing Vertebral Data")
compare_vertebral_data(simulations, exp_kinematic_data['panzer_vertebral_data'])
print("\n(completed)\n")

print(f"Comparing Peak Vertebral Rotations")
vertebral_comparison_df = compare_peak_vertebra(simulations)
plot_vertebra_comparison_table(vertebral_comparison_df)

#########################################################################################

print(f"Comparing Disc Data")
compare_disc_data(simulations)
print("\n(completed)\n")

print(f"Comparing Peak Disc Data")
disc_stress_comparison, disc_strain_comparison = compare_peak_disc_values(simulations)
plot_disc_comparison_table(disc_stress_comparison, "Stress")
plot_disc_comparison_table(disc_strain_comparison, "Strain")

#########################################################################################

print(f"Comparing Ligament Data")
# Call the function in your main script
for level in ['C01_C02_C12', 'C23', 'C34', 'C45', 'C56', 'C67', 'C7T1']:  # Add other levels as needed
    compare_ligament_data(simulations, level)
print("\n(completed)\n")

print(f"Comparing Peak Ligament Data")
lig_force_comparison, lig_stretch_comparison = compare_peak_ligament_values(simulations)
plot_comparison_ligament_table(lig_force_comparison, "Ligament Force Comparison")
plot_comparison_ligament_table(lig_stretch_comparison, "Ligament Stretch Comparison")
# #########################################################################################

print(f"Comparing Muscle Data")
# Call the function in your main script
compare_muscle_data(simulations)
print("\n(completed)\n")

muscle_force_comparison, muscle_stretch_comparison = compare_peak_muscle_values(simulations)
plot_comparison_muscle_table(muscle_force_comparison, "Muscle Force Comparison")
plot_comparison_muscle_table(muscle_stretch_comparison, "Muscle Strain Comparison")
#########################################################################################

# print(f"Comparing NIJ Data")
# compare_nij_data(simulations)
print("\n(completed)\n")

# #########################################################################################






