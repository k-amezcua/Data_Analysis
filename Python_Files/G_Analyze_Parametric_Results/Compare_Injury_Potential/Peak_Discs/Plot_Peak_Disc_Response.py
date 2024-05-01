import matplotlib.pyplot as plt
import pandas as pd

def plot_disc_table(df, sim_label, title):
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

def plot_disc_stress_table(peak_stress_values_dict):
    for sim_label, peak_stress_values in peak_stress_values_dict.items():
        df = pd.DataFrame(peak_stress_values, index=['Stress (MPa)', 'Time (ms)']).T
        plot_disc_table(df, sim_label, 'Peak Disc Stress Values')

def plot_disc_strain_table(peak_strain_values_dict):
    for sim_label, peak_strain_values in peak_strain_values_dict.items():
        df = pd.DataFrame(peak_strain_values, index=['Strain (mm/mm)', 'Time (ms)']).T
        plot_disc_table(df, sim_label, 'Peak Disc Strain Values')

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
    plt.close()
