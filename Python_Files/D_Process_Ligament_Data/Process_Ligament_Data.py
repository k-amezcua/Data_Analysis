import os
import re
import pandas as pd

from D_Process_Ligament_Data.Plot_Ligament_Data import plot_ligament_data, plot_ligament_data_summary

class Ligament:
    def __init__(self, name, num_elements, file_path):
        self.name = name
        self.num_elements = num_elements
        self.file_path = file_path
        self.data = pd.DataFrame()

    def process_ligament_data(self):
        print(f"{self.name}")
        with open(self.file_path) as data:
            lines = data.readlines()

        # Initialize dictionaries for data storage
        data_dict = {f'E{i}_{metric}': [] for i in range(1, self.num_elements + 1) for metric in
                     ['Fr', 'Fy', 'Fz', 'stretch']}
        data_dict['Sim_Time_s'] = []  # Ensure 'Sim_Time_s' is the last column in the dictionary

        for i, line in enumerate(lines):
            if "Time  = " in line:
                start = i + 2
                time_match = re.search(r'-?\d+(\.\d+)?(e[-+]?\d+)?', lines[start - 2], re.IGNORECASE)
                if time_match:
                    time_value = float(time_match.group())
                    data_dict['Sim_Time_s'].append(time_value)
                else:
                    continue  # Skip this iteration if time value is not found

                for j in range(self.num_elements):
                    element_line = lines[start + j]
                    element_data = re.findall(r'-?\d+(\.\d+)?(e[-+]?\d+)?', element_line, re.IGNORECASE)
                    element_data = [float(''.join(e)) if e[0] else 0 for e in
                                    element_data]  # Convert tuples to floats or 0

                    # Ensure each metric list is populated
                    for metric, idx in zip(['Fr', 'Fy', 'Fz', 'stretch'], [1, 3, 4, 5]):
                        if idx < len(element_data):
                            value = abs(round(element_data[idx], 6))
                        else:
                            value = 0  # Default value if data is missing
                        data_dict[f'E{j + 1}_{metric}'].append(value)

        # Create the DataFrame with 'Sim_Time_s' as the first column
        self.data = pd.DataFrame(data_dict,
                                 columns=['Sim_Time_s'] + [f'E{i}_{metric}' for i in range(1, self.num_elements + 1) for
                                                           metric in ['Fr', 'Fy', 'Fz', 'stretch']])
        # Calculate aggregate metrics
        for metric in ['Fr', 'Fy', 'Fz']:
            self.data[f'{self.name}_{metric}'] = self.data[
                [f'E{i}_{metric}' for i in range(1, self.num_elements + 1)]].sum(axis=1)
            self.data[f'{self.name}_stretch'] = self.data[
                [f'E{i}_stretch' for i in range(1, self.num_elements + 1)]].mean(axis=1)
        self.data[f'{self.name}_Fres'] = (self.data[f'{self.name}_Fy'] ** 2 + self.data[f'{self.name}_Fz'] ** 2) ** 0.5

        # Save to CSV
        csv_path = os.path.splitext(self.file_path)[0] + ".csv"
        self.data.to_csv(csv_path)

        return self.data

    def plot_ligament_data(self):
        plot_ligament_data(self)
    def plot_ligament_data_summary(sim):
        plot_ligament_data_summary(sim)
