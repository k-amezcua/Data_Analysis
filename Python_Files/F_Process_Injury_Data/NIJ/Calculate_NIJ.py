import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict
import os

def calculate_NIJ(sim, nij_file_path):
    # Define the injury criterion values in a dictionary
    nij_injury_criterion = {
        'Fcrit_tension': 6806,
        'Fcrit_compression': -6160,
        'Mcrit_flexion': 310,
        'Mcrit_extension': -135
    }

    def calculate_NIJ_values(Fz, My):
        # Extract critical values from the dictionary
        Fcrit_tension = nij_injury_criterion['Fcrit_tension']
        Fcrit_compression = nij_injury_criterion['Fcrit_compression']
        Mcrit_flexion = nij_injury_criterion['Mcrit_flexion']
        Mcrit_extension = nij_injury_criterion['Mcrit_extension']

        # Initialize an empty Series for NIJ values
        Nij_values = pd.Series(index=Fz.index)

        # Calculate Nij for each condition
        condition1 = (Fz >= 0) & (My >= 0)
        Nij_values[condition1] = (Fz[condition1] / Fcrit_tension) + (My[condition1] / Mcrit_flexion)

        condition2 = (Fz >= 0) & (My < 0)
        Nij_values[condition2] = (Fz[condition2] / Fcrit_tension) + (My[condition2] / Mcrit_extension)

        condition3 = (Fz < 0) & (My >= 0)
        Nij_values[condition3] = (Fz[condition3] / Fcrit_compression) + (My[condition3] / Mcrit_flexion)

        condition4 = (Fz < 0) & (My < 0)
        Nij_values[condition4] = (Fz[condition4] / Fcrit_compression) + (My[condition4] / Mcrit_extension)

        # Round the values
        Nij_values = Nij_values.round(3)

        return round(Nij_values, 3)

    ###########################################################################################################

    # Define the list of variables you want to extract
    variables = ['Time', 'Fx', 'Fy', 'Fz', 'Mx', 'My', 'Mz']

    # Create a dictionary to store the data for each variable, with the rigid_body number included in the column names
    data = defaultdict(list)

    with open(nij_file_path, 'r') as file:
        current_rigid_body = None  # Track the current rigid_body number

        for line in file:
            line = line.strip()

            if line.startswith('*Time'):
                # Extract the time value and store it in the 'Time' variable
                time_value = float(line.split('=')[1].strip())
                data['Sim_Time_s'].append(time_value)  # Include the rigid_body number in the column name
            elif line.startswith('*Data'):
                current_variable = None
            elif line and not line.startswith('*'):
                parts = line.split(',')
                rigid_body = int(parts[0])
                values = list(map(float, parts[1:]))
                current_rigid_body = rigid_body

                for i, var in enumerate(variables[1:]):  # Skip 'Time' in variables list
                    data[f'{var}_{current_rigid_body}'].append(values[i])  # Include the rigid_body number in the column name

    # Create a DataFrame from the data
    # print(data)
    df = pd.DataFrame(data)
    # print(f"Neck Force Results:\n{df}\n")

    OC_data = df[['Sim_Time_s', 'Fz_31', 'Mx_31']].copy()
    OC_data = OC_data.rename(columns={'Fz_31': 'Fz', 'Mx_31': 'My'})
    Sim_Time_s = OC_data['Sim_Time_s']
    df['Fz'] = OC_data['Fz']
    df['My'] = OC_data['My']
    Fz_min = min(df['Fz'])
    Fz_max = max(df['Fz'])
    My_min = min(df['My'])
    My_max = max(df['My'])

    Nij_results = calculate_NIJ_values(df['Fz'], df['My'])

    df['NIJ'] = Nij_results
    # print(f"NIJ results:\n{Nij_results}\n")


    print(f"Minimum Fz: {round((Fz_min),2)}")
    print(f"Maxmimum Fz: {round((Fz_max),2)}")
    print(f"Minimum My: {round((My_min),2)}")
    print(f"Maxmimum My: {round((My_max),2)}\n")

    max_NIJ = df['NIJ'].max()
    max_index_NIJ = df['NIJ'].idxmax()
    # # Get the corresponding time value
    time_at_max_NIJ = df.at[max_index_NIJ, 'Sim_Time_s']
    print(f"Maximum NIJ Value: {round(max_NIJ,3)}")
    print(f"Time at Maximum NIJ Value: {round(time_at_max_NIJ,3)}")
    min_NIJ = df['NIJ'].min()
    min_index_NIJ = df['NIJ'].idxmin()
    # # Get the corresponding time value
    time_at_min_NIJ = df.at[min_index_NIJ, 'Sim_Time_s']
    print(f"Minimum NIJ Value: {round(min_NIJ,3)}")
    print(f"Time at Minimum NIJ Value: {round(time_at_min_NIJ,3)}")

    # Now you should have the data in a pandas DataFrame.

    csv_path = os.path.splitext(nij_file_path)[0] + ".csv"
    df.to_csv(csv_path, float_format='%.9f')
    # df_test = pd.read_csv(path + filename + ".csv", sep=',', engine = 'python', index_col=False, dtype='float64')

    Fcrit_tension = 6806
    Fcrit_compression = -6160
    Mcrit_flexion = 310
    Mcrit_extension = -135
    axial_load_zero = 0

    x = [Mcrit_extension, 0, Mcrit_flexion]
    y_upper = [0, Fcrit_tension,0]
    y_lower = [0, Fcrit_compression,0]

    # Plot the Nij values over time
    plt.plot(df['My'], df['Fz'], marker='o', linestyle=' ', color='g', label='Nij')
    plt.plot(x, y_upper, marker='o', linestyle='--', color='b')
    plt.plot(x, y_lower, marker='o', linestyle='--', color='b')

    plt.title('Neck Injury Criterion (Nij)')
    plt.xlabel('My (Nm)')
    plt.ylabel('Fz (N)')
    plt.legend()
    plt.grid(True)
    plt.savefig('NIJ.png')
    plt.show()

    # #######################################################################################################################
    #
    # # Define the number of rigid_bodies, associated variables, and rows
    # num_rigid_bodies = 9
    # num_variables = 6
    #
    # # Get the number of rows dynamically
    # num_rows = df.shape[0]
    #
    # # Create an empty DataFrame to store the results
    # Fr_df = pd.DataFrame()
    # Mr_df = pd.DataFrame()
    #
    # # Define the calc_rigid_body function
    # def calc_Fr(rb_variables):
    #     Fx = rb_variables.iloc[:, 0]
    #     Fy = rb_variables.iloc[:, 1]
    #     Fz = rb_variables.iloc[:, 2]
    #     Fr_value = round((((Fx**2)+(Fy**2)+(Fz**2))**0.5),1)
    #     return Fr_value
    #
    # def calc_Mr(rb_variables):
    #     Mx = rb_variables.iloc[:, 3]
    #     My = rb_variables.iloc[:, 4]
    #     Mz = rb_variables.iloc[:, 5]
    #     Mr_value = round((((Mx**2)+(My**2)+(Mz**2))**0.5),1)
    #     return Mr_value
    #
    # Fr_results = []
    # Mr_results = []
    #
    # # Loop through each rigid_body
    # for rigid_body in range(num_rigid_bodies):
    #     # Extract the 6 associated variables for the current rigid_body
    #     rb_variables = df.iloc[:, (rigid_body * num_variables) + 1:((rigid_body + 1) * num_variables) + 1]
    #     # Perform the calculation using the calc_rigid_body function
    #     Fr_result = calc_Fr(rb_variables)
    #     Mr_result = calc_Mr(rb_variables)
    #
    #     # Append the individual rigid_body result to the list
    #     Fr_results.append(pd.Series(Fr_result, name=f'Rigid_Body_{rigid_body + 1}_Fr'))
    #     Mr_results.append(pd.Series(Mr_result, name=f'Rigid_Body_{rigid_body + 1}_Mr '))
    #
    #
    # Fr_df = pd.concat(Fr_results, axis=1)
    # Mr_df = pd.concat(Mr_results, axis=1)
    # # Set the time column from the original DataFrame as the index of the result_df
    # # Fr_df.index = df.iloc[:, 0]
    # # Mr_df.index = df.iloc[:, 0]
    # # Fr_df.columns.values[0] = 'Sim_Time_s'
    # # Mr_df.columns.values[0] = 'Sim_Time_s'
    #
    # Fr_df['Sim_Time_s'] = df['Sim_Time_s']
    # Mr_df['Sim_Time_s'] = df['Sim_Time_s']
    #
    # # Define the name of the column you want to move to the first position
    # column_to_move = 'Sim_Time_s'
    #
    # # Reorder the columns
    # new_order = [column_to_move] + [col for col in Fr_df.columns if col != column_to_move]
    # Fr_df = Fr_df[new_order]
    #
    # # Reorder the columns
    # new_order = [column_to_move] + [col for col in Mr_df.columns if col != column_to_move]
    # Mr_df = Mr_df[new_order]


    # # Find the column with the greatest value
    # max_column_Fr = Fr_df.iloc[:, 1:].max().idxmax()
    # # Get the maximum value in the DataFrame
    # max_value_Fr = Fr_df.iloc[:, 1:].max().max()
    # # Make a copy of the column with the greatest value and assign a new column name
    # # print(max_column_Fr)
    # Fr_df['max_Fr'] = Fr_df[max_column_Fr]
    # # Find the index of the maximum value in the 'Data' column
    # max_index_Fr = Fr_df['max_Fr'].idxmax()
    # # Get the corresponding time value
    # # print(Fr_df.head())
    # # print(Fr_df.columns)
    # time_at_max_Fr = Fr_df.at[max_index_Fr, 'Sim_Time_s']
    # print("Fr_df:")
    # print(Fr_df)
    #
    # # Print the results
    # print(f"rigid_body w/Maximum Value: {max_column_Fr}")
    # print(f"Maximum Fr Value: {max_value_Fr}")
    # print(f"Time at Maximum Fr Value: {round(time_at_max_Fr,3)}")
    #
    # # Find the column with the greatest value
    # max_column_Mr = Mr_df.iloc[:, 1:].max().idxmax()
    # # Get the maximum value in the DataFrame
    # max_value_Mr = Mr_df.iloc[:, 1:].max().max()
    # # Make a copy of the column with the greatest value and assign a new column name
    # # print(max_column_Mr)
    # Mr_df['max_Mr'] = Mr_df[max_column_Mr]
    # # Find the index of the maximum value in the 'Data' column
    # max_index_Mr = Mr_df['max_Mr'].idxmax()
    # # Get the corresponding time value
    # # print(Mr_df.head())
    # # print(Mr_df.columns)
    # time_at_max_Mr = Mr_df.at[max_index_Mr, 'Sim_Time_s']
    # print("Mr_df:")
    # print(Mr_df)
    #
    # # Print the results
    # print(f"rigid_body w/Maximum Value: {max_column_Mr}")
    # print(f"Maximum Mr Value: {max_value_Mr}")
    # print(f"Time at Maximum Mr Value: {round(time_at_max_Mr,3)}")

    # # Calculate the average of the first variable (variable 1) across all rigid_bodies for each row
    # Fx_average = round((df.iloc[:, 1::6].mean(axis=1)),1)
    # # Fx_average.index = Fr_df.index
    # Fr_df['Fx_average'] = Fx_average
    # Fy_average = round((df.iloc[:, 2::6].mean(axis=1)),1)
    # # Fy_average.index = Fr_df.index
    # Fr_df['Fy_average'] = Fy_average
    # Fz_average = round((df.iloc[:, 3::6].mean(axis=1)),1)
    # # Fz_average.index = Fr_df.index
    # Fr_df['Fz_average'] = Fz_average
    #
    # Mx_average = round((df.iloc[:, 4::6].mean(axis=1)),2)
    # # Mx_average.index = Fr_df.index
    # Mr_df['Mx_average'] = Mx_average
    # My_average = round((df.iloc[:, 5::6].mean(axis=1)),2)
    # # My_average.index = Fr_df.index
    # Mr_df['My_average'] = My_average
    # Mz_average = round((df.iloc[:, 6::6].mean(axis=1)),2)
    # # Mz_average.index = Fr_df.index
    # Mr_df['Mz_average'] = Mz_average

    # print(Fr_df)
    # print(Mr_df)

    ###########################################################################################################

    return df, nij_injury_criterion


