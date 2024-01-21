import os
import pandas as pd

main_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\15G NBDL Data\Processed Data\Compiled Test Data\Processed_Individual_Test_Data"
data_path = r"C:\Users\kryst\Desktop\THESIS\Data_Analysis\Python_Files\H_CORA_Analysis\Simulation_1\data"
tests = ["v01535", "v01635", "v01636", "v01637", "v01638", "v01639", "v01641", "v01644"]
required_columns = ['Time(s)', 'Head_Ax_G_19', 'Head_Az_G_21', 'Head_ao_rad/s^2_23']
column_mapping = {
    'Head_Ax_G_19': 'head_x_accel',
    'Head_Az_G_21': 'head_z_accel',
    'Head_ao_rad/s^2_23': 'head_y_rot_accel'
}
def process_data(test):
    file_path = os.path.join(main_path, test + " Compiled Test Data.csv")

    if os.path.isfile(file_path):
        df = pd.read_csv(file_path, usecols=lambda c: c in required_columns)

        # Calculate zeroed data by subtracting the first row from each row
        first_row = df.iloc[0]
        df = df.apply(lambda row: row - first_row, axis=1)

        df.rename(columns={'Time(s)': 'Time_s'}, inplace=True)

        # Rename the columns using the mapping dictionary
        df.rename(columns=column_mapping, inplace=True)

        # Filter data to include only up to 0.25 seconds
        df = df[df['Time_s'] <= 0.25]

        # Multiply each column by -1 except for 'Time_s'
        for col in df.columns:
            if col != 'Time_s':
                df[col] = df[col] * -1

        # Save the zeroed data with the specified column names
        save_data_with_time(df, test, data_path)

def save_data_with_time(df, test, data_path):
    for col in ['head_x_accel', 'head_z_accel', 'head_y_rot_accel']:
        save_path = os.path.join(data_path, f'{test}_{col}.dat')

        # Drop rows with NaN values in the specified column
        df_filtered = df.dropna(subset=[col])

        with open(save_path, 'w') as f:
            f.write(f"XYDATA, {col}\n")
            for index, row in df_filtered[['Time_s', col]].iterrows():
                f.write(f"{row['Time_s']} {row[col]}\n")
            f.write("ENDATA\n")

for test in tests:
    process_data(test)
