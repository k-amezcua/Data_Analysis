import pandas as pd

def peak_vertebra(sim):
    peak_values = {}
    for column in sim.vertebrae.columns:
        max_value = sim.vertebrae[column].max()
        time_at_max = sim.vertebrae[sim.vertebrae[column] == max_value].index[0]
        peak_values[column + " (degrees)"] = [round(max_value), round(time_at_max)]
    return peak_values

def compare_peak_vertebra(simulations):
    comparison = {}
    for sim in simulations:
        peak_values = peak_vertebra(sim)
        comparison[sim.label] = peak_values
    # Convert the dictionary to a DataFrame for easier manipulation and plotting
    comparison_df = pd.DataFrame.from_dict(comparison, orient='index')
    return comparison_df


########################################################################################################################
def peak_disc_values(sim):
    peak_stress_values = {}
    peak_strain_values = {}

    for disc in sim.discs:
        disc_level = disc.level
        disc_region = disc.region
        disc_data = disc.data

        # Stress
        max_sr = disc_data['max_sr'].max() / 1e6  # Convert to MPa
        time_at_max_sr = disc_data[disc_data['max_sr'] == disc_data['max_sr'].max()].index[0]
        peak_stress_values[f'{disc_level}_{disc_region}'] = [f"{round(max_sr)} MPa, {time_at_max_sr} ms"]

        # Strain
        max_er = disc_data['max_Er'].max()
        time_at_max_er = disc_data[disc_data['max_Er'] == disc_data['max_Er'].max()].index[0]
        peak_strain_values[f'{disc_level}_{disc_region}'] = [f"{round(max_er, 2)} mm/mm, {time_at_max_er} ms"]

    return peak_stress_values, peak_strain_values

def compare_peak_disc_values(simulations):
    comparison_stress = {}
    comparison_strain = {}

    for sim in simulations:
        peak_stress, peak_strain = peak_disc_values(sim)
        comparison_stress[sim.label] = peak_stress
        comparison_strain[sim.label] = peak_strain

    return comparison_stress, comparison_strain

########################################################################################################################

def peak_ligament_values(sim):
    peak_force_values = {}
    peak_stretch_values = {}

    for ligament in sim.ligaments:
        ligament_name = ligament.name
        ligament_data = ligament.data

        # Force
        max_force = ligament_data[f'{ligament_name}_Fr'].max()
        time_at_max_force = ligament_data[ligament_data[f'{ligament_name}_Fr'] == max_force].index[0]
        peak_force_values[ligament_name] = [round(max_force), round(time_at_max_force)]

        # Stretch
        max_stretch = ligament_data[f'{ligament_name}_stretch'].max()
        time_at_max_stretch = ligament_data[ligament_data[f'{ligament_name}_stretch'] == max_stretch].index[0]
        peak_stretch_values[ligament_name] = [round(max_stretch, 2), round(time_at_max_stretch)]

    return peak_force_values, peak_stretch_values

def compare_peak_ligament_values(simulations):
    comparison_force = {}
    comparison_stretch = {}

    for sim in simulations:
        peak_force, peak_stretch = peak_ligament_values(sim)
        comparison_force[sim.label] = peak_force
        comparison_stretch[sim.label] = peak_stretch

    return comparison_force, comparison_stretch

#################################################################################

def peak_muscle_values(sim):
    peak_force_values = {}
    peak_stretch_values = {}

    for muscle in sim.muscles:
        muscle_name = muscle.name
        muscle_data = muscle.data

        # Force
        max_force = muscle_data[f'{muscle_name}_Fres'].max()
        time_at_max_force = muscle_data[muscle_data[f'{muscle_name}_Fres'] == max_force].index[0]
        peak_force_values[muscle_name] = [round(max_force), round(time_at_max_force)]

        # Stretch
        max_stretch = muscle_data[f'{muscle_name}_stretch'].max()
        time_at_max_stretch = muscle_data[muscle_data[f'{muscle_name}_stretch'] == max_stretch].index[0]
        peak_stretch_values[muscle_name] = [round(max_stretch, 2), round(time_at_max_stretch)]

    return peak_force_values, peak_stretch_values


def compare_peak_muscle_values(simulations):
    comparison_force = {}
    comparison_stretch = {}

    for sim in simulations:
        peak_force, peak_stretch = peak_muscle_values(sim)
        comparison_force[sim.label] = peak_force
        comparison_stretch[sim.label] = peak_stretch

    return comparison_force, comparison_stretch


