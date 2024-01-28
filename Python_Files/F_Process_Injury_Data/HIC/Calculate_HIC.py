import numpy as np
from scipy.integrate import simps
import pandas as pd
def calculate_HIC_non_constant_time(sim, t_range):
    # Extract acceleration data in g's and time data in seconds from the simulation object
    acceleration_data = sim.kinematics['Head_aDx'].values  # Assuming acceleration is in g's
    time_data = sim.kinematics['Sim_Time_s'].values  # Assuming time is in seconds

    # Pass t_range to the compute_HIC function
    hic = compute_HIC(acceleration_data, time_data, t_range)

    df_hic = pd.DataFrame({'HIC': [hic]})
    df_hic.to_csv(f'{sim.label}_HIC_Value.csv', index=False)

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


