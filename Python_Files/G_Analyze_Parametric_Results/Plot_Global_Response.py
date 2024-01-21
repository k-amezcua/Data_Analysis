import matplotlib.pyplot as plt
import pandas as pd

def plot_peak_global_response_table(peak_values):
    df = pd.DataFrame(peak_values)
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(0.25, 1.5)
    plt.savefig(f'Peak_Global_Response.png')
    df.to_excel('peak_global_response.xlsx')  # Save to Excel
    plt.show()

def plot_peak_global_comparison_table(comparison_dict):
    df = pd.DataFrame(comparison_dict)
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(0.75, 1.5)
    plt.savefig(f'Global_Response_Comparison.png')
    df.to_excel('global_response_comparison.xlsx')  # Save to Excel
    plt.show()

################################################################################

import matplotlib.pyplot as plt

def plot_NIJ_table(nij_values_dict):
    for sim_label, nij_values in nij_values_dict.items():
        # Create a DataFrame with formatted values
        formatted_values = {}
        for key, val in nij_values.items():
            if key == 'NIJ':
                formatted_values[key] = [f"{round(val[0], 1)}", f"{int(val[1])}"]
            else:
                formatted_values[key] = [f"{int(val[0])}", f"{int(val[1])}"]

        df = pd.DataFrame(formatted_values, index=['Peak', 'Time (ms)']).T

        fig, ax = plt.subplots(figsize=(12, 8))
        ax.axis('off')
        table = ax.table(cellText=df.values, rowLabels=df.index, colLabels=df.columns, loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(.5, 1.5)
        plt.title(f'NIJ Values for {sim_label}')
        plt.savefig(f'{sim_label}_NIJ_Values.png')
        df.to_excel(f'{sim_label}_NIJ_Values.xlsx')
        plt.show()

def plot_NIJ_comparison_table(comparison_dict):
    df = pd.DataFrame(comparison_dict).T
    df = df.stack().unstack(0)
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.axis('off')
    table = ax.table(cellText=df.values, rowLabels=df.index, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(.5, 1.5)
    plt.title('NIJ Comparison Across Simulations')
    plt.savefig('NIJ_Comparison_Across_Simulations.png')
    df.to_excel('NIJ_Comparison_Across_Simulations.xlsx')
    plt.show()
