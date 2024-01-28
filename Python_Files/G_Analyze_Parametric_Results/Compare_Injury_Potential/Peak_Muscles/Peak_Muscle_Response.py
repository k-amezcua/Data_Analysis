def peak_muscle_values(sim):
    peak_force_values = {}
    peak_strain_values = {}

    for muscle in sim.muscles:
        muscle_name = muscle.name
        muscle_data = muscle.data

        # Force
        max_force = muscle_data[f'{muscle_name}_Fres'].max()
        time_at_max_force = muscle_data[muscle_data[f'{muscle_name}_Fres'] == max_force].index[0]
        peak_force_values[muscle_name] = [round(max_force), round(time_at_max_force)]

        # Strain (calculated from stretch)
        max_stretch = muscle_data[f'{muscle_name}_stretch'].max()
        max_strain = max_stretch - 1  # Strain calculation
        time_at_max_strain = muscle_data[muscle_data[f'{muscle_name}_stretch'] == max_stretch].index[0]
        percent_of_failure_strain = (max_strain / muscle.failure_strain * 100) if muscle.failure_strain else None
        peak_strain_values[muscle_name] = [round(max_strain, 2), round(time_at_max_strain), round(percent_of_failure_strain, 0) if percent_of_failure_strain else "N/A", muscle.failure_strain]
    
    return peak_force_values, peak_strain_values

def compare_peak_muscle_values(simulations):
    comparison_force = {}
    comparison_strain = {}

    for sim in simulations:
        peak_force, peak_strain = peak_muscle_values(sim)
        comparison_force[sim.label] = peak_force
        comparison_strain[sim.label] = peak_strain

    return comparison_force, comparison_strain