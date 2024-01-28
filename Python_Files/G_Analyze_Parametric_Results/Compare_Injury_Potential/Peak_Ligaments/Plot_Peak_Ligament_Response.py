import pandas as pd
import matplotlib.pyplot as plt

def plot_individual_ligament_table(peak_values_dict, title):
    for sim_label, peak_values in peak_values_dict.items():
        # Adjust the columns list to exclude failure stretch values
        columns = ['Peak Value', 'Time (ms)', 'Percent of Failure', 'Failure Reference']
        # Create a DataFrame from the peak values dictionary
        df = pd.DataFrame.from_dict(peak_values, orient='index', columns=columns)
        plot_table(df, sim_label, title, include_index=False)

def plot_comparison_ligament_table(comparison_dict, title):
    # Convert the comparison dictionary to a DataFrame for plotting
    df = pd.DataFrame.from_dict(comparison_dict, orient='index').stack().unstack(level=0)
    plot_table(df, None, title, include_index=True)

def plot_table(df, sim_label, title, include_index):
    fig, ax = plt.subplots(figsize=(12, len(df) * 0.5 + 2))  # Adjust height based on number of rows
    ax.axis('off')
    table = ax.table(cellText=df.values, rowLabels=df.index if include_index else None, colLabels=df.columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.title(title)
    if sim_label:
        plt.savefig(f'{title.replace(" ", "_")}_{sim_label}.png')
        df.to_excel(f'{title.replace(" ", "_")}_{sim_label}.xlsx', index=include_index)
    else:
        plt.savefig(f'{title.replace(" ", "_")}.png')
        df.to_excel(f'{title.replace(" ", "_")}.xlsx', index=include_index)
    plt.show()
