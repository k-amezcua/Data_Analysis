import pandas as pd
import matplotlib.pyplot as plt

def determine_HIC(sim, hic_injury_criteria):
    # Assuming sim.HIC is already calculated and stored in each simulation object
    hic = round(sim.hic)
    percent_of_criteria = (hic / hic_injury_criteria) * 100
    return hic, percent_of_criteria

def compare_HIC(simulations, hic_injury_criteria):
    comparison_data = []
    for sim in simulations:
        hic, percent_of_criteria = determine_HIC(sim, hic_injury_criteria)
        comparison_data.append([sim.label, hic, percent_of_criteria, hic_injury_criteria])
    return comparison_data

def plot_individual_HIC(sim, hic_injury_criteria):
    hic, percent_of_criteria = determine_HIC(sim, hic_injury_criteria)
    data = [[sim.label, hic, percent_of_criteria, hic_injury_criteria]]
    df = pd.DataFrame(data, columns=['Simulation', 'HIC', 'Percent of Injury Criteria', f'Injury Criteria (HIC={hic_injury_criteria})'])
    plot_table(df, f'HIC for {sim.label}')

def plot_HIC_comparison(comparison_data, hic_injury_criteria):
    df = pd.DataFrame(comparison_data, columns=['Simulation', 'HIC', 'Percent of Injury Criteria', f'Injury Criteria (HIC={hic_injury_criteria})'])
    plot_table(df, 'HIC Comparison')

def plot_table(df, title):
    fig, ax = plt.subplots(figsize=(10, len(df) * 0.5 + 1))
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.title(title)
    plt.savefig(f'{title.replace(" ", "_")}.png')
    df.to_excel(f'{title.replace(" ", "_")}.xlsx', index=False)
    plt.show()

