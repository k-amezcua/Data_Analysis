import matplotlib.pyplot as plt
import pandas as pd

def plot_individual_muscle_table(peak_values, title, sim_label):
    # Convert peak_values to a DataFrame with proper formatting
    formatted_values = []
    for muscle, values in peak_values.items():
        formatted_values.append([muscle, f"{values[0]}, {values[1]} ms"])

    df = pd.DataFrame(formatted_values, columns=['Muscle', 'Peak, Time (ms)'])
    plot_table(df, title, sim_label, include_index=False)

def plot_comparison_muscle_table(comparison_dict, title):
    formatted_comparison = format_comparison_data(comparison_dict)
    df = pd.DataFrame(formatted_comparison).T
    df = df.stack().unstack(0)
    plot_table(df, title, None, include_index=True)

def plot_table(df, title, sim_label, include_index):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')
    table = ax.table(cellText=df.values, rowLabels=df.index, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.title(title)

    # Handle the filename differently for comparison tables
    if sim_label is not None:
        filename = f'{title.replace(" ", "_")}_{sim_label}'
    else:
        filename = title.replace(" ", "_")

    plt.savefig(f'{filename}.png')
    df.to_excel(f'{filename}.xlsx', index=include_index)
    plt.show()


def format_comparison_data(comparison_dict):
    formatted_comparison = {}
    for sim_label, values in comparison_dict.items():
        formatted_values = {}
        for key, val in values.items():
            if isinstance(val, list) and len(val) == 2:
                formatted_values[key] = f"{val[0]}, {val[1]} ms"
            else:
                formatted_values[key] = "N/A"
        formatted_comparison[sim_label] = formatted_values
    return formatted_comparison


