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