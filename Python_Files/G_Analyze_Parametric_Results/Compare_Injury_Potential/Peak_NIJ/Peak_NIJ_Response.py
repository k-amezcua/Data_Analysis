def determine_NIJ(simulation, injury_criteria):
    nij_values = {}

    for column in ['Fz', 'My', 'NIJ']:
        max_value = round(simulation.nij[column].max(), 1)
        min_value = round(simulation.nij[column].min(), 1)
        time_at_max = round(simulation.nij.loc[simulation.nij[column].idxmax(), 'Sim_Time_s'] * 1000)
        time_at_min = round(simulation.nij.loc[simulation.nij[column].idxmin(), 'Sim_Time_s'] * 1000)

        unit = "(N)" if column == "Fz" else "(Nm)"
        if column == 'Fz':
            # Tension
            percent_of_ref_tension = (max_value / injury_criteria.get(column + "_tension", 1)) * 100
            label_tension = f'{column} Max (tension) {unit}'
            nij_values[label_tension] = [max_value, time_at_max, round(percent_of_ref_tension, 0), injury_criteria.get(column + "_tension", "N/A")]

            # Compression
            percent_of_ref_compression = (abs(min_value) / injury_criteria.get(column + "_compression", 1)) * 100
            label_compression = f'{column} Min (compression) {unit}'
            nij_values[label_compression] = [min_value, time_at_min, round(percent_of_ref_compression, 0), injury_criteria.get(column + "_compression", "N/A")]

        elif column == 'My':
            # Flexion
            percent_of_ref_flexion = (max_value / injury_criteria.get(column + "_flexion", 1)) * 100
            label_flexion = f'{column} Max (flexion) {unit}'
            nij_values[label_flexion] = [max_value, time_at_max, round(percent_of_ref_flexion, 0), injury_criteria.get(column + "_flexion", "N/A")]

            # Extension
            percent_of_ref_extension = (abs(min_value) / injury_criteria.get(column + "_extension", 1)) * 100
            label_extension = f'{column} Min (extension) {unit}'
            nij_values[label_extension] = [min_value, time_at_min, round(percent_of_ref_extension, 0), injury_criteria.get(column + "_extension", "N/A")]

        else:  # For NIJ
            percent_of_ref_nij = (max_value / injury_criteria.get(column, 1)) * 100
            nij_values[column] = [max_value, time_at_max, round(percent_of_ref_nij, 0), injury_criteria.get(column, "N/A")]

    return nij_values


def compare_NIJ(simulations, injury_criteria):
    comparison = {}
    for sim in simulations:
        comparison[sim.label] = determine_NIJ(sim, injury_criteria)
    return comparison