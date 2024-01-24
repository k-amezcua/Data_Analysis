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