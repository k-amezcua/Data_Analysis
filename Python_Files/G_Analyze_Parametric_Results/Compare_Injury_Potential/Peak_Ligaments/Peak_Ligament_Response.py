def peak_ligament_values(sim):
    peak_force_values = {}
    peak_stretch_values = {}

    for ligament in sim.ligaments:
        ligament_name = ligament.name
        ligament_data = ligament.data

        # Force
        max_force = ligament_data[f'{ligament_name}_Fr'].max()
        time_at_max_force = ligament_data[ligament_data[f'{ligament_name}_Fr'] == max_force].index[0]
        percent_of_failure_force = (max_force / ligament.failure_force) * 100 if ligament.failure_force else None
        peak_force_values[ligament_name] = [round(max_force), round(time_at_max_force), round(percent_of_failure_force, 0) if percent_of_failure_force else "N/A", ligament.failure_force]

        # Stretch
        max_stretch = ligament_data[f'{ligament_name}_stretch'].max()
        time_at_max_stretch = ligament_data[ligament_data[f'{ligament_name}_stretch'] == max_stretch].index[0]
        # Assuming a similar failure_stretch attribute will be available
        percent_of_failure_stretch = (max_stretch / ligament.failure_stretch) * 100 if hasattr(ligament, 'failure_stretch') else None
        peak_stretch_values[ligament_name] = [round(max_stretch, 2), round(time_at_max_stretch), round(percent_of_failure_stretch, 0) if percent_of_failure_stretch else "N/A", ligament.failure_stretch if hasattr(ligament, 'failure_stretch') else "N/A"]

    return peak_force_values, peak_stretch_values


def compare_peak_ligament_values(simulations):
    comparison_force = {}
    comparison_stretch = {}

    for sim in simulations:
        peak_force, peak_stretch = peak_ligament_values(sim)
        comparison_force[sim.label] = peak_force
        comparison_stretch[sim.label] = peak_stretch

    return comparison_force, comparison_stretch
