def pre_process_sim_for_cora(sim):

    data = sim.kinematics

    import pandas as pd
    import os

    # Select only the required columns for CORA analysis
    required_columns = ['Sim_Time_s', 'Head_aDx', 'Head_aDz', 'Head_aRy']

    # Apply the selection to each DataFrame
    data_cora = data[required_columns]

    # save data for CORA analysis
    # Rename columns to match CORA control file signal names

    # Create new dataframes with renamed columns for CORA analysis
    data_cora = data_cora.rename(columns={
        'Head_aDx': 'head_x_accel',
        'Head_aDz': 'head_z_accel',
        'Head_aRy': 'head_y_rot_accel'
    })

    # Get the path of the current script
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    current_script_path = os.path.join(current_script_path, r"Simulation_1\data")

    # Define the file names
    sim_head_accel_data_filename = os.path.join(current_script_path, 'sim_head_accel.dat')
    sim_head_x_accel_data_filename = os.path.join(current_script_path, 'sim_head_x_accel.dat')
    sim_head_z_accel_data_filename = os.path.join(current_script_path, 'sim_head_z_accel.dat')
    sim_head_y_rot_accel_data_filename = os.path.join(current_script_path, 'sim_head_y_rot_accel.dat')


    # sim_stdev_head_x_accel_data_filename = os.path.join(current_script_path, 'sim_stdev_head_x_accel.at')
    # sim_stev_head_z_accel_data_filename = os.path.join(current_script_path, 'sim_stdev_head_z_accel.at')
    # sim_stdev_head_y_rot_accel_data_filename = os.path.join(current_script_path, 'sim_stdev_head_y_rot_accel.at')

    # Save .dat files for CORA analysis
    # Save .dat file for CORA analysis with space delimiter
    with open(sim_head_accel_data_filename, 'w') as f:
        f.write("XYDATA,\thead_x_accel / (G),\thead_z_accel / (G),\thead_y_rot_accel / (G)\n")
        data_cora.to_csv(f, sep='\t', index=False, header=False)
    
    def save_data_with_time(df, label, filename):
        # Save .dat file with time and corresponding data
        with open(filename, 'w') as f:
            f.write(f"XYDATA,\t{label} / (G)\n")  # Replace (unit) with actual unit
            df.to_csv(f, sep='\t', index=False, header=False)

    # Call this function for each required data file
    save_data_with_time(data_cora[['Sim_Time_s', 'head_x_accel']], 'head_x_accel', sim_head_x_accel_data_filename)
    save_data_with_time(data_cora[['Sim_Time_s', 'head_z_accel']], 'head_z_accel', sim_head_z_accel_data_filename)
    save_data_with_time(data_cora[['Sim_Time_s', 'head_y_rot_accel']], 'head_y_rot_accel', sim_head_y_rot_accel_data_filename)

    # def save_stdev_data(df, label, filename):
    #     # Repeat the data column
    #     repeated_data = pd.concat([df, df], axis=1)
    #     # Save .dat file with repeated data
    #     with open(filename, 'w') as f:
    #         f.write(f"{label} / (G),\t{label} / (G)\n")  # Replace (unit) with actual unit
    #         repeated_data.to_csv(f, sep='\t', index=False, header=False)
    #
    # # Call this function for each required simulation 'standard deviation' file
    # save_stdev_data(data_cora['head_x_accel'], 'head_x_accel', sim_stdev_head_x_accel_data_filename)
    # save_stdev_data(data_cora['head_z_accel'], 'head_z_accel', sim_stev_head_z_accel_data_filename)
    # save_stdev_data(data_cora['head_y_rot_accel'], 'head_y_rot_accel', sim_stdev_head_y_rot_accel_data_filename)

    return