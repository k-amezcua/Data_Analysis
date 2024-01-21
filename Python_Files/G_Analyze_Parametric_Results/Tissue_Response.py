import pandas as pd

def peak_vertebra(sim):
    # Assuming sim.vertebrae is a DataFrame with your data
    # Extract peak values and round them to zero decimal places

    peak_rotation_C12 = round(sim.vertebrae['C12_Ry'].max())
    peak_rotation_C23 = round(sim.vertebrae['C23_Ry'].max())
    peak_rotation_C34 = round(sim.vertebrae['C34_Ry'].max())
    peak_rotation_C45 = round(sim.vertebrae['C45_Ry'].max())
    peak_rotation_C56 = round(sim.vertebrae['C56_Ry'].max())
    peak_rotation_C67 = round(sim.vertebrae['C67_Ry'].max())
    peak_rotation_C7T1 = round(sim.vertebrae['C7T1_Ry'].max())

    # Create a dictionary to store these values
    peak_values = {
        'C12_Ry': peak_rotation_C12,
        'C23_Ry': peak_rotation_C23,
        'C34_Ry': peak_rotation_C34,
        'C45_Ry': peak_rotation_C45,
        'C56_Ry': peak_rotation_C56,
        'C67_Ry': peak_rotation_C67,
        'C7T1_Ry': peak_rotation_C7T1
    }

    return peak_values
def compare_peak_vertebra(simulations):
    # Create a dictionary to store peak values for each simulation
    all_peak_values = {}

    # Loop through each simulation and calculate peak values
    for sim in simulations:
        all_peak_values[sim.label] = peak_vertebra(sim)

    # Convert the dictionary to a DataFrame for comparison
    comparison_df = pd.DataFrame(all_peak_values)

    # Transpose the DataFrame to list data vertically
    comparison_df = comparison_df.T

    # Round the values to zero decimal places
    comparison_df = comparison_df.round(0)

    return comparison_df

########################################################################################################################

def peak_disc_values(simulation):
    # Assuming simulation.discs is a list of Disc objects with processed data
    peak_values = []
    for disc in simulation.discs:
        peak_stress = disc.data['stress'].max()
        peak_strain = disc.data['strain'].max()
        peak_values.append({'Disc': disc.name, 'Peak Stress': peak_stress, 'Peak Strain': peak_strain})
    return pd.DataFrame(peak_values)

def peak_ligament_values(simulation):
    # Similar to peak_disc_values, but for ligaments
    peak_values = []
    for ligament in simulation.ligaments:
        peak_stress = ligament.data['stress'].max()
        peak_strain = ligament.data['strain'].max()
        peak_values.append({'Ligament': ligament.name, 'Peak Stress': peak_stress, 'Peak Strain': peak_strain})
    return pd.DataFrame(peak_values)

def peak_muscle_values(simulation):
    # Similar to peak_ligament_values, but for muscles
    peak_values = []
    for muscle in simulation.muscles:
        peak_stress = muscle.data['stress'].max()
        peak_strain = muscle.data['strain'].max()
        peak_values.append({'Muscle': muscle.name, 'Peak Stress': peak_stress, 'Peak Strain': peak_strain})
    return pd.DataFrame(peak_values)

# You can add more functions if needed for other tissues
