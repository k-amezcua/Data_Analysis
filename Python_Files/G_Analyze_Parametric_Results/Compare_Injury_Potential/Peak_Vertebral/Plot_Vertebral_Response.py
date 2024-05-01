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
    plt.close()