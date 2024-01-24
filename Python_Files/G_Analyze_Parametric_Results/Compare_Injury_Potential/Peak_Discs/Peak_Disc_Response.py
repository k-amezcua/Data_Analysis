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