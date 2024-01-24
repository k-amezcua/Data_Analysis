
def determine_NIJ(simulation):
    nij_values = {}
    for column in ['Fz', 'My', 'NIJ']:
        if column in ['Fz', 'My']:
            max_value = round(simulation.nij[column].max())
            min_value = round(simulation.nij[column].min())
            time_at_max = round(simulation.nij.loc[simulation.nij[column].idxmax(), 'Sim_Time_s'] * 1000)
            time_at_min = round(simulation.nij.loc[simulation.nij[column].idxmin(), 'Sim_Time_s'] * 1000)

            unit = "(N)" if column == "Fz" else "(Nm)"
            tension_compression = "tension" if column == "Fz" else "flexion"
            compression_extension = "compression" if column == "Fz" else "extension"
            nij_values[f'{column} Max ({tension_compression}) {unit}, Time (ms)'] = [max_value, time_at_max]
            nij_values[f'{column} Min ({compression_extension}) {unit}, Time (ms)'] = [min_value, time_at_min]
        else:  # For NIJ
            max_value = round(simulation.nij[column].max(), 1)
            time_at_max = round(simulation.nij.loc[simulation.nij[column].idxmax(), 'Sim_Time_s'] * 1000)
            nij_values[f'{column}'] = [max_value, time_at_max]

    return nij_values

def compare_NIJ(simulations):
    comparison = {}
    for sim in simulations:
        comparison[sim.label] = determine_NIJ(sim)
    return comparison