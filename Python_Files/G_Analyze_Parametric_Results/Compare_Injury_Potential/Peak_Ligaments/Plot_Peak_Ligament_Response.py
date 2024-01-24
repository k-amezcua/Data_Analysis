import matplotlib.pyplot as plt
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

def plot_individual_ligament_table(peak_values_dict, title):
    for sim_label, peak_values in peak_values_dict.items():
        # Convert peak_values to a DataFrame with proper formatting
        formatted_values = {}
        for key, val in peak_values.items():
            if isinstance(val, list) and len(val) == 2:
                formatted_values[key] = f"{val[0]}, {val[1]} ms"
            else:
                formatted_values[key] = "N/A"  # Placeholder for missing or improperly formatted data

        df = pd.DataFrame(formatted_values, index=[title]).T
        plot_individual_table(df, sim_label, title)

def plot_individual_table(df, sim_label, title):
    fig, ax = plt.subplots(figsize=(12, 16))
    ax.axis('off')
    table = ax.table(cellText=df.values, rowLabels=df.index, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(0.75, 1.5)
    plt.title(f'{title} for {sim_label}')
    plt.savefig(f'{title.replace(" ", "_")}_{sim_label}.png')
    df.to_excel(f'{title.replace(" ", "_")}_{sim_label}.xlsx')
    plt.show()

def plot_comparison_ligament_table(comparison_dict, title):
    formatted_comparison = format_comparison_data(comparison_dict)
    df = pd.DataFrame(formatted_comparison).T
    df = df.stack().unstack(0)
    plot_comparison_table(df, title)

def plot_comparison_table(df, title):
    fig, ax = plt.subplots(figsize=(16, 20))
    ax.axis('off')
    table = ax.table(cellText=df.values, rowLabels=df.index, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(0.75, 1.5)
    plt.title(title)
    plt.savefig(f'{title.replace(" ", "_")}.png')
    df.to_excel(f'{title.replace(" ", "_")}.xlsx')
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