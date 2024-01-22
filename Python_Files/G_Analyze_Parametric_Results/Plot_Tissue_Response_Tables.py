import matplotlib.pyplot as plt
import pandas as pd

def plot_peak_vertebra_table(peak_values_dict):
    # Iterate through each simulation in the dictionary
    for sim_label, peak_values in peak_values_dict.items():
        # Ensure peak_values is a DataFrame with appropriate index
        if not isinstance(peak_values, pd.DataFrame):
            peak_values = pd.DataFrame([peak_values])

        # Transpose the DataFrame to get vertebral levels as rows
        transposed_peak_values = peak_values.transpose()

        # Create a figure and axis to plot the table
        fig, ax = plt.subplots(figsize=(16, 8))

        # Hide the axes
        ax.axis('off')

        # Create the table
        table = ax.table(cellText=transposed_peak_values.values,
                         rowLabels=transposed_peak_values.index,
                         colLabels=[sim_label],
                         loc='center')

        # Adjust font size
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(0.2, 1.2)  # Adjust table scale

        plt.title(f'Peak Vertebral Values for {sim_label} (degrees)')

        # Save the figure
        plt.savefig(f'Peak_Vertebral_Values.png')
        transposed_peak_values.to_excel(f'Peak_Vertebral_Values.xlsx')
        plt.close()

def plot_vertebra_comparison_table(comparison_df):
    # Transpose the DataFrame to list vertebral levels vertically and simulations horizontally
    transposed_df = comparison_df.T

    fig, ax = plt.subplots(figsize=(16, 8))  # Adjust the figure size as needed
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=transposed_df.values, colLabels=transposed_df.columns, rowLabels=transposed_df.index, cellLoc='center', loc='center')

    # Adjust table scale
    table.scale(1.0, 2.0)  # Increase scaley for more vertical space

    # Adjust font size
    plt.rcParams.update({'font.size': 14})  # Adjust font size as needed

    plt.savefig(f'Vertebral_Comparison.png')
    transposed_df.to_excel('Vertebra_Comparison_Table.xlsx')
    plt.show()

########################################################################################################################

def plot_disc_stress_table(peak_stress_values_dict):
    for sim_label, peak_stress_values in peak_stress_values_dict.items():
        df = pd.DataFrame(peak_stress_values, index=['Stress (MPa)', 'Time (ms)']).T
        plot_table(df, sim_label, 'Peak Disc Stress Values')

def plot_disc_strain_table(peak_strain_values_dict):
    for sim_label, peak_strain_values in peak_strain_values_dict.items():
        df = pd.DataFrame(peak_strain_values, index=['Strain (mm/mm)', 'Time (ms)']).T
        plot_table(df, sim_label, 'Peak Disc Strain Values')

def plot_table(df, sim_label, title):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    table = ax.table(cellText=df.values, rowLabels=df.index, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.title(f'{title} for {sim_label}')
    plt.savefig(f'{title.replace(" ", "_")}.png')
    df.to_excel(f'{title.replace(" ", "_")}.xlsx')
    plt.close()

def plot_disc_comparison_table(comparison_dict, title):
    formatted_comparison = {}
    for sim_label, values in comparison_dict.items():
        formatted_values = {}
        for key, val in values.items():
            # Check if val is a list with one string element
            if isinstance(val, list) and len(val) == 1:
                formatted_values[key] = val[0]  # Use the string directly
            else:
                formatted_values[key] = "N/A"  # Placeholder if data is missing or not in expected format
        formatted_comparison[sim_label] = formatted_values

    df = pd.DataFrame(formatted_comparison).T
    df = df.stack().unstack(0)
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.axis('off')
    table = ax.table(cellText=df.values, rowLabels=df.index, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.title(f'Disc {title} Comparison')
    plt.savefig(f'Disc {title} Comparison.png')
    df.to_excel(f'Disc {title} Comparison.xlsx')
    plt.show()

########################################################################################################################
def plot_ligament_table(peak_values_dict, title):
    for sim_label, peak_values in peak_values_dict.items():
        df = pd.DataFrame(peak_values, index=['Value', 'Time (ms)']).T
        plot_table(df, sim_label, title)

def plot_ligament_comparison_table(comparison_dict, title):
    formatted_comparison = format_comparison_data(comparison_dict)
    df = pd.DataFrame(formatted_comparison).T
    df = df.stack().unstack(0)
    plot_table(df, 'Comparison', title)

def plot_table(df, sim_label, title):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    table = ax.table(cellText=df.values, rowLabels=df.index, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.title(f'{title} for {sim_label}')
    plt.savefig(f'{title.replace(" ", "_")}_{sim_label}.png')
    df.to_excel(f'{title.replace(" ", "_")}_{sim_label}.xlsx')
    plt.close()

def format_comparison_data(comparison_dict):
    formatted_comparison = {}
    for sim_label, values in comparison_dict.items():
        formatted_values = {}
        for key, val in values.items():
            formatted_values[key] = val[0] if isinstance(val, list) and len(val) == 1 else "N/A"
        formatted_comparison[sim_label] = formatted_values
    return formatted_comparison
