def determine_peak_global_response(simulation):
    peak_values = {}
    columns_to_process = [
        "Sim_Head_Dx (mm)", "Sim_Rel_Head_Dz (mm)", "Sim_Rel_Head_Ry (degrees)",
        "Head_Ry (degrees)", "Head_vx (kph)", "Head_vz (kph)", "Head_wy (rad/s)",
        "Head_aDx (G)", "Head_aDz (G)", "Head_aRy (rad/s^2)"
    ]
    original_columns = [
        "Sim_Head_Dx", "Sim_Rel_Head_Dz", "Sim_Rel_Head_Ry",
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
            time_at_peak = simulation.kinematics[simulation.kinematics[original] == peak_value].index[0]
            # Round and store the value and time
            peak_values[new] = [round(peak_value), round(time_at_peak)]
    return peak_values


def compare_peak_global_response(simulations):
    comparison = {}
    for sim in simulations:
        peak_values = determine_peak_global_response(sim)
        comparison[sim.label] = peak_values
    return comparison