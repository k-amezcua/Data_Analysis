import matplotlib.pyplot as plt
import pandas as pd

def plot_individual_muscle_table(peak_values, title, sim_label):
    if not peak_values:  # Check if peak_values is empty
        print(f"No data available for {title} in {sim_label}. Skipping plot.")
        return  # Skip plotting if no data

    formatted_values = {key: [f"{val[0]}, {val[1]} ms"] for key, val in peak_values.items()}
    df = pd.DataFrame.from_dict(formatted_values, orient='index', columns=['Peak Value, Time (ms)'])

    if df.empty:  # Check if DataFrame is empty
        print(f"DataFrame is empty for {title} in {sim_label}. Skipping plot.")
        return  # Skip plotting if DataFrame is empty

    plot_table(df, title, sim_label, include_index=False)


def plot_comparison_muscle_table(comparison_dict, title):
    # Adjust the DataFrame creation for comparison
    df = pd.DataFrame.from_dict(comparison_dict, orient='index').stack().unstack(level=0)
    plot_table(df, title, None, include_index=True)

def plot_table(df, title, sim_label, include_index):
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
    plt.close()