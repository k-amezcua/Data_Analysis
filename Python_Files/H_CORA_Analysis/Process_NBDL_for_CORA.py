def pre_process_NBDL_for_cora(exp_kinematic_data):

    average_data = exp_kinematic_data['NBDL_average']
    low_data = exp_kinematic_data['NBDL_STDEV-1']
    high_data = exp_kinematic_data['NBDL_STDEV+1']

    import pandas as pd
    import os

    # Function to save combined low and high data as .at files
    def save_at_file(low_col, high_col, filename, low_df, high_df):
        combined_data = pd.DataFrame({
            'low': low_df[low_col],
            'high': high_df[high_col]
        })
        combined_data.to_csv(filename, sep='\t', index=False, header=False)

    # Select only the required columns for CORA analysis
    required_columns = ['Time_s', 'Head_Ax_G_19', 'Head_Az_G_21', 'Head_ao_rad/s^2_23']

    # Apply the selection to each DataFrame
    average_data_cora = average_data[required_columns]
    low_data_cora = low_data[required_columns]
    high_data_cora = high_data[required_columns]

    # save data for CORA analysis
    # Rename columns to match CORA control file signal names

    # Create new dataframes with renamed columns for CORA analysis
    average_data_cora = average_data_cora.rename(columns={
        'Head_Ax_G_19': 'head_x_accel',
        'Head_Az_G_21': 'head_z_accel',
        'Head_ao_rad/s^2_23': 'head_y_rot_accel'
    })

    low_data_cora = low_data_cora.rename(columns={
        'Head_Ax_G_19': 'head_x_accel',
        'Head_Az_G_21': 'head_z_accel',
        'Head_ao_rad/s^2_23': 'head_y_rot_accel'
    })

    high_data_cora = high_data_cora.rename(columns={
        'Head_Ax_G_19': 'head_x_accel',
        'Head_Az_G_21': 'head_z_accel',
        'Head_ao_rad/s^2_23': 'head_y_rot_accel'
    })

    # Get the path of the current script
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    current_script_path = os.path.join(current_script_path, r"Simulation_1\data")

    # Define the file names
    exp_head_accel_data_filename = os.path.join(current_script_path, 'exp_head_accel.dat')
    exp_head_x_accel_data_filename = os.path.join(current_script_path, 'exp_head_x_accel.dat')
    exp_head_z_accel_data_filename = os.path.join(current_script_path, 'exp_head_z_accel.dat')
    exp_head_y_rot_accel_data_filename = os.path.join(current_script_path, 'exp_head_y_rot_accel.dat')

    exp_stdev_head_x_accel_filename = os.path.join(current_script_path, 'exp_stdev_head_x_accel_2_curves.at')
    exp_stdev_head_z_accel_filename = os.path.join(current_script_path, 'exp_stdev_head_z_accel_2_curves.at')
    exp_stdev_head_y_rot_accel_filename = os.path.join(current_script_path, 'exp_stdev_head_y_rot_accel_2_curves.at')

    # Save .dat file for CORA analysis with space delimiter
    # with open(exp_head_accel_data_filename, 'w') as f:
    #     f.write("XYDATA, head_x_accel, head_z_accel, head_y_rot_accel\n")
    #     average_data_cora.to_csv(f, sep=' ', index=False, header=False)
    #     f.write("ENDATA\n")

    def save_data_with_time(df, label, filename):
        # Save .dat file with time and corresponding data
        with open(filename, 'w') as f:
            f.write(f"XYDATA, {label}\n")  # Replace (unit) with actual unit
            df.to_csv(f, sep=' ', index=False, header=False)
            f.write("ENDATA\n")

    # Call this function for each required data file
    # save_data_with_time(average_data_cora[['Time_s', 'head_x_accel']], 'head_x_accel', exp_head_x_accel_data_filename)
    # save_data_with_time(average_data_cora[['Time_s', 'head_z_accel']], 'head_z_accel', exp_head_z_accel_data_filename)
    # save_data_with_time(average_data_cora[['Time_s', 'head_y_rot_accel']], 'head_y_rot_accel', exp_head_y_rot_accel_data_filename)

    # low data, high data
    # def save_stdev_data(df_low, df_high, label, filename):
    #     with open(filename, 'w') as f:
    #         # Write header
    #         f.write(f"XYDATA, {label}\n")
    #         # Write low and high data in two columns
    #         for (index_low, value_low), (index_high, value_high) in zip(df_low.iteritems(), df_high.iteritems()):
    #             f.write(f"{value_low}\t{value_high}\n")
    #         # Write 'ENDATA' at the end
    #         f.write("ENDATA\n")
    #
    # # Call this function for each required standard deviation file
    # save_stdev_data(low_data_cora['head_x_accel'], high_data_cora['head_x_accel'], 'head_x_accel', exp_stdev_head_x_accel_filename)
    # save_stdev_data(low_data_cora['head_z_accel'], high_data_cora['head_z_accel'], 'head_z_accel', exp_stdev_head_z_accel_filename)
    # save_stdev_data(low_data_cora['head_y_rot_accel'], high_data_cora['head_y_rot_accel'], 'head_y_rot_accel', exp_stdev_head_y_rot_accel_filename)

    # time, low
    # time, high
    def save_stdev_data_with_time(df_low, df_high, time_col, label, filename):
        with open(filename, 'w') as f:
            # Write header and low data curve with time
            f.write(f"XYDATA, {label}\n")
            for index, row in df_low.iterrows():
                f.write(f"{row[time_col]}\t{row[label]}\n")
            # Write 'ENDATA' to separate curves
            f.write("ENDATA\n")
            # Write header and high data curve with time
            f.write(f"XYDATA, {label}\n")
            for index, row in df_high.iterrows():
                f.write(f"{row[time_col]}\t{row[label]}\n")
            # Write 'ENDATA' at the end
            f.write("ENDATA\n")

            # f.write(f"XYDATA, {label}\n")
            # for index, row in df_low.iterrows():
            #     f.write(f"{row[time_col]}\t{row[label]}\n")
            # # Write 'ENDATA' to separate curves
            # f.write("ENDATA\n")
            # # Write header and high data curve with time
            # f.write(f"XYDATA, {label}\n")
            # for index, row in df_high.iterrows():
            #     f.write(f"{row[time_col]}\t{row[label]}\n")
            # # Write 'ENDATA' at the end
            # f.write("ENDATA\n")

    # Example usage
    save_stdev_data_with_time(low_data_cora, high_data_cora, 'Time_s', 'head_x_accel', exp_stdev_head_x_accel_filename)
    save_stdev_data_with_time(low_data_cora, high_data_cora, 'Time_s', 'head_z_accel', exp_stdev_head_z_accel_filename)
    save_stdev_data_with_time(low_data_cora, high_data_cora, 'Time_s', 'head_y_rot_accel', exp_stdev_head_y_rot_accel_filename)

    return