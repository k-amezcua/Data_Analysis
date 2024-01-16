import os
from C_Process_Disc_Data.Plot_Disc_Data import plot_data

class Disc:
    def __init__(self, name, num_elements, file_path, disc_variables):
        import pandas as pd
        self.name = name
        self.num_elements = num_elements
        self.file_path = file_path
        self.disc_variables = disc_variables
        self.data = pd.DataFrame()

    def process_disc_data(self):

        import pandas as pd
        from collections import defaultdict

        print(f"{self.name}")

        # Create a dictionary to store the data for each variable
        data = defaultdict(list)

        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()

                if line.startswith('*Time'):
                    # Extract the time value and store it in the 'Time' variable
                    time_value = float(line.split('=')[1].strip())
                    data['Sim_Time_s'].append(time_value)  # Include the element number in the column name
                elif line.startswith('*Data'):
                    current_variable = None
                elif line and not line.startswith('*'):
                    parts = line.split(',')
                    element_number = int(parts[0])
                    values = list(map(float, parts[1:]))
                    current_element_number = element_number

                    for i, var in enumerate(self.disc_variables[1:]):  # Skip 'Time' in variables list
                        data[f'{var}_{current_element_number}'].append(values[i])  # Include the element number in the column name

            # Convert the dictionary to a DataFrame
            self.data = pd.DataFrame(data)

            # Define the number of elements, associated variables, and rows
            num_variables = len(self.disc_variables)-1

            # Get the number of rows dynamically
            num_rows = self.data.shape[0]

            # Create an empty DataFrame to store the results
            sr_df = pd.DataFrame()
            Er_df = pd.DataFrame()

            # Define the calc_element function
            def calc_sr(element_variables):
                s1_value = element_variables.iloc[:, 0]
                s2_value = element_variables.iloc[:, 1]
                s3_value = element_variables.iloc[:, 2]
                fun1 = (s1_value-s2_value)**2
                fun2 = (s2_value-s3_value)**2
                fun3 = (s3_value-s1_value)**2
                sr_value = round(((0.5*(fun1+fun2+fun3))**0.5),1)
                return sr_value

            def calc_Er(element_variables):
                E1_value = element_variables.iloc[:, 3]
                E2_value = element_variables.iloc[:, 4]
                E3_value = element_variables.iloc[:, 5]
                fun1 = (E1_value-E1_value)**2
                fun2 = (E2_value-E3_value)**2
                fun3 = (E3_value-E1_value)**2
                sr_value = round(((0.5*(fun1+fun2+fun3))**0.5),2)
                return sr_value

            sr_results = []
            Er_results = []

            # Loop through each element
            for element in range(self.num_elements):
                # Extract the 6 associated variables for the current element
                element_variables = self.data.iloc[:, (element * num_variables) + 1:((element + 1) * num_variables) + 1]
                # Perform the calculation using the calc_element function
                sr_result = calc_sr(element_variables)
                Er_result = calc_Er(element_variables)

                # Append the individual element result to the list
                sr_results.append(pd.Series(sr_result, name=f'Element_{element + 1}_sr'))
                Er_results.append(pd.Series(Er_result, name=f'Element_{element + 1}_Er '))


            sr_df = pd.concat(sr_results, axis=1)
            Er_df = pd.concat(Er_results, axis=1)
            # Set the time column from the original DataFrame as the index of the result_df
            # sr_df.index = df.iloc[:, 0]
            # Er_df.index = df.iloc[:, 0]
            # sr_df.columns.values[0] = 'Sim_Time_s'
            # Er_df.columns.values[0] = 'Sim_Time_s'


            sr_df['Sim_Time_s'] = self.data['Sim_Time_s']
            Er_df['Sim_Time_s'] = self.data['Sim_Time_s']

            # Define the name of the column you want to move to the first position
            column_to_move = 'Sim_Time_s'

            # Reorder the columns
            new_order = [column_to_move] + [col for col in sr_df.columns if col != column_to_move]
            sr_df = sr_df[new_order]

            # Reorder the columns
            new_order = [column_to_move] + [col for col in Er_df.columns if col != column_to_move]
            Er_df = Er_df[new_order]

            # Find the column with the greatest value
            max_column_sr = sr_df.iloc[:, 1:].max().idxmax()
            # Get the maximum value in the DataFrame
            max_value_sr = sr_df.iloc[:, 1:].max().max()
            # Make a copy of the column with the greatest value and assign a new column name
            # print(max_column_sr)
            sr_df['max_sr'] = sr_df[max_column_sr]
            # Find the index of the maximum value in the 'Data' column
            max_index_sr = sr_df['max_sr'].idxmax()
            # Get the corresponding time value
            # print(sr_df.head())
            # print(sr_df.columns)
            time_at_max_sr = sr_df.at[max_index_sr, 'Sim_Time_s']
            # print("sr_df:")
            # print(sr_df)

            # Print the results
            print(f"Element w/Maximum Value: {max_column_sr}")
            print(f"Maximum sr Value: {round(max_value_sr/(10**6))}e06")
            print(f"Time at Maximum sr Value: {round(time_at_max_sr,3)}")

            # Find the column with the greatest value
            max_column_Er = Er_df.iloc[:, 1:].max().idxmax()
            # Get the maximum value in the DataFrame
            max_value_Er = Er_df.iloc[:, 1:].max().max()
            # Make a copy of the column with the greatest value and assign a new column name
            # print(max_column_Er)
            Er_df['max_Er'] = Er_df[max_column_Er]
            # Find the index of the maximum value in the 'Data' column
            max_index_Er = Er_df['max_Er'].idxmax()
            # Get the corresponding time value
            # print(Er_df.head())
            # print(Er_df.columns)
            time_at_max_Er = Er_df.at[max_index_Er, 'Sim_Time_s']
            # print("Er_df:")
            # print(Er_df)

            # Print the results
            print(f"Element w/Maximum Value: {max_column_Er}")
            print(f"Maximum Er Value: {max_value_Er}")
            print(f"Time at Maximum Er Value: {round(time_at_max_Er,3)}\n")

            # Calculate the average of the first variable (variable 1) across all elements for each row
            s1_average = round((self.data.iloc[:, 1::6].mean(axis=1)),1)
            # s1_average.index = sr_df.index
            sr_df['s1_average'] = s1_average
            s2_average = round((self.data.iloc[:, 2::6].mean(axis=1)),1)
            # s2_average.index = sr_df.index
            sr_df['s2_average'] = s2_average
            s3_average = round((self.data.iloc[:, 3::6].mean(axis=1)),1)
            # s3_average.index = sr_df.index
            sr_df['s3_average'] = s3_average

            E1_average = round((self.data.iloc[:, 4::6].mean(axis=1)),2)
            # E1_average.index = sr_df.index
            Er_df['E1_average'] = E1_average
            E2_average = round((self.data.iloc[:, 5::6].mean(axis=1)),2)
            # E2_average.index = sr_df.index
            Er_df['E2_average'] = E2_average
            E3_average = round((self.data.iloc[:, 6::6].mean(axis=1)),2)
            # E3_average.index = sr_df.index
            Er_df['E3_average'] = E3_average

            #TODO: just assign the above to self.data instead of merging.

            ###########################################################################################################
            # Merge the calculated data with the original data
            self.data = self.data.merge(sr_df, on='Sim_Time_s', how='left')
            self.data = self.data.merge(Er_df, on='Sim_Time_s', how='left')

            # Add additional calculated columns (averages, max values, etc.) to self.data
            self.data['max_sr'] = sr_df['max_sr']
            self.data['max_Er'] = Er_df['max_Er']
            self.data['s1_average'] = sr_df['s1_average']
            self.data['s2_average'] = sr_df['s2_average']
            self.data['s3_average'] = sr_df['s3_average']
            self.data['E1_average'] = Er_df['E1_average']
            self.data['E2_average'] = Er_df['E2_average']
            self.data['E3_average'] = Er_df['E3_average']

            # Save the processed data to a CSV file
            csv_file_path = self.file_path.replace('.txt', '.csv')
            self.data.to_csv(csv_file_path, float_format='%.9f')

            # plot_data(self)

        pass

    def plot_disc_data(self):
        plot_data(self)