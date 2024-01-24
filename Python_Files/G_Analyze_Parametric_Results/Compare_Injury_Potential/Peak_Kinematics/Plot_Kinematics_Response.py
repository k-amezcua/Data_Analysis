import pandas as pd
import matplotlib.pyplot as plt

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
    plt.close()

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
    plt.close()
