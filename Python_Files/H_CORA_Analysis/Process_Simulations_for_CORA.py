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
    sim_head_accel_data_filename = os.path.join(current_script_path, f'{sim.label}_sim_head_accel.dat')
    sim_head_x_accel_data_filename = os.path.join(current_script_path, f'{sim.label}_sim_head_x_accel.dat')
    sim_head_z_accel_data_filename = os.path.join(current_script_path, f'{sim.label}_sim_head_z_accel.dat')
    sim_head_y_rot_accel_data_filename = os.path.join(current_script_path, f'{sim.label}_sim_head_y_rot_accel.dat')


    sim_stdev_head_x_accel_data_filename = os.path.join(current_script_path, f'{sim.label}_sim_stdev_head_x_accel.at')
    sim_stdev_head_z_accel_data_filename = os.path.join(current_script_path, f'{sim.label}_sim_stdev_head_z_accel.at')
    sim_stdev_head_y_rot_accel_data_filename = os.path.join(current_script_path, f'{sim.label}_sim_stdev_head_y_rot_accel.at')

    # Save .dat files for CORA analysis
    # Save .dat file for CORA analysis with space delimiter
    # with open(sim_head_accel_data_filename, 'w') as f:
    #     f.write("XYDATA, head_x_accel, head_z_accel, head_y_rot_accel\n")
    #     data_cora.to_csv(f, sep=' ', index=False, header=False)
    #     f.write("ENDATA\n")

    def save_data_with_time(df, label, filename):
        with open(filename, 'w') as f:
            f.write(f"XYDATA, {label}\n")
            for index, row in df.iterrows():
                line = ' '.join([str(row[col]) for col in df.columns])
                f.write(line + '\n')
            f.write("ENDATA\n")

    data_cora['head_z_accel'] = data_cora['head_z_accel']*-1
    data_cora['head_y_rot_accel'] = data_cora['head_y_rot_accel']*-1

    # Call this function for each required data file
    save_data_with_time(data_cora[['Sim_Time_s', 'head_x_accel']], 'head_x_accel', sim_head_x_accel_data_filename)
    save_data_with_time(data_cora[['Sim_Time_s', 'head_z_accel']], 'head_z_accel', sim_head_z_accel_data_filename)
    save_data_with_time(data_cora[['Sim_Time_s', 'head_y_rot_accel']], 'head_y_rot_accel', sim_head_y_rot_accel_data_filename)

    def save_stdev_data(df, time_col, label, filename):
        # Repeat the data column
        repeated_data = pd.concat([df[time_col], df[label], df[label]], axis=1)
        # Save .dat file with repeated data
        with open(filename, 'w') as f:
            f.write(f"XYDATA, {label}\n")
            for index, row in repeated_data.iterrows():
                f.write(f"{row[0]}\t{row[1]}\t{row[2]}\n")
            f.write("ENDATA\n")

    # Call this function for each required simulation 'standard deviation' file
    # save_stdev_data(data_cora, 'Sim_Time_s', 'head_x_accel', sim_stdev_head_x_accel_data_filename)
    # save_stdev_data(data_cora, 'Sim_Time_s', 'head_z_accel', sim_stdev_head_z_accel_data_filename)
    # save_stdev_data(data_cora, 'Sim_Time_s', 'head_y_rot_accel', sim_stdev_head_y_rot_accel_data_filename)

    return