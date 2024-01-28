import pandas as pd
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
    df = pd.DataFrame.from_dict(comparison_dict, orient='index').stack().unstack(0)
    plot_comparison_table(df, 'NIJ Comparison')

def plot_comparison_table(df, title):
    fig, ax = plt.subplots(figsize=(16, len(df) * 0.5 + 2))
    ax.axis('off')
    table = ax.table(cellText=df.values, rowLabels=df.index, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.title(title)
    plt.savefig(f'{title.replace(" ", "_")}.png')
    df.to_excel(f'{title.replace(" ", "_")}.xlsx', index=True)
    plt.show()
