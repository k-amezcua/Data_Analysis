def determine_peak_global_response(simulation):
    peak_values = {}
    columns_to_process = [
        "Head_Dx (mm)", "Sim_Head_Dx (mm)", "Sim_Rel_Head_Dz (mm)", "Sim_Rel_Head_Ry (degrees)",
        "Head_Ry (degrees)", "Head_vx (kph)", "Head_vz (kph)", "Head_wy (rad/s)",
        "Head_aDx (G)", "Head_aDz (G)", "Head_aRy (rad/s^2)"
    ]
    original_columns = [
        "Head_Dx", "Sim_Head_Dx", "Sim_Rel_Head_Dz", "Sim_Rel_Head_Ry",
        "Head_Ry", "Head_vx", "Head_vz", "Head_wy",
        "Head_aDx", "Head_aDz", "Head_aRy"
    ]

    for original, new in zip(original_columns, columns_to_process):
        if original in simulation.kinematics.columns:
            # Find the maximum absolute value in the column
            max_abs_value = simulation.kinematics[original].abs().max()
            # Determine if the original max or min value is closer to this absolute value
            original_max = simulation.kinematics[original].max()
            original_min = simulation.kinematics[original].min()
            peak_value = original_max if abs(original_max) == max_abs_value else original_min
            # Round and store the value
            peak_values[new] = round(peak_value)
    return peak_values

def compare_peak_global_response(simulations):
    comparison = {}
    for sim in simulations:
        peak_values = determine_peak_global_response(sim)
        comparison[sim.label] = peak_values
    return comparison

#############################################################################

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

