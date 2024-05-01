import numpy as np
from scipy.integrate import simps
import pandas as pd
def calculate_HIC_non_constant_time(sim, t_range):
    # Extract acceleration data in g's and time data in seconds from the simulation object
    acceleration_data = (sim.kinematics['Head_aRes'].values) * 9.81  # Convert acceleration to m/s^2
    time_data = sim.kinematics['Sim_Time_s'].values  # Time data in seconds

    # Convert the acceleration and time data into a DataFrame for easier manipulation
    df = pd.DataFrame({'Time': time_data, 'Acceleration': acceleration_data})

    # Filter out rows where time is less than 0.001 seconds, but keep the first row
    filtered_df = df[(df['Time'] >= 0.001) | (df.index == 0)]

    # Update acceleration_data and time_data with filtered values
    acceleration_data_filtered = filtered_df['Acceleration'].values
    time_data_filtered = filtered_df['Time'].values

    # Pass the filtered data to the compute_HIC function
    hic = compute_HIC(acceleration_data_filtered, time_data_filtered, t_range)

    # Create a DataFrame for HIC value
    df_hic = pd.DataFrame({'HIC': [hic]})

    # Save the HIC value to a CSV file
    df_hic.to_csv(f'{sim.label}_HIC_Value.csv', index=False)

    # Save the filtered data used for HIC calculation to a CSV file
    filtered_df.to_csv(f'{sim.label}_HIC_Calc.csv', index=False, columns=['Time', 'Acceleration'])

    print('(saved HIC to file)')

    return hic


def compute_HIC(acceleration, time, t_range):
    max_hic = 0
    for start_idx in range(len(acceleration)):
        for end_idx in range(start_idx + 1, len(acceleration)):
            # Calculate the time interval between the current start and end indices
            t_interval = time[end_idx] - time[start_idx]
            # Ensure the time interval is within the specified range and not too small
            if 0 < t_interval <= t_range:
                # Use absolute values of acceleration to avoid complex numbers
                acc_segment = np.abs(acceleration[start_idx:end_idx + 1])
                # Calculate HIC for the current segment
                hic = (simps(acc_segment ** 2.5, time[start_idx:end_idx + 1]) / t_interval) ** (1 / 2.5) * t_interval
                max_hic = max(max_hic, hic)
    return max_hic


