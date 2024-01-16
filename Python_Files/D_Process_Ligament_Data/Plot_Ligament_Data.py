import matplotlib.pyplot as plt
import pandas as pd

def plot_ligament_data(ligament):
    data = ligament.data
    
    channelsimt = 'Sim_Time_s'
    
    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig, ax = plt.subplots()
    ax.plot(data[channelsimt], data[f'{ligament.name}_Fres'], label=f'{ligament.name}_Fres', color='red')
    ax.plot(data[channelsimt], data[f'{ligament.name}_Fy'], label=f'{ligament.name}_Fy', color='orange')
    ax.plot(data[channelsimt], data[f'{ligament.name}_Fz'], label=f'{ligament.name}_Fz', color='green')
    
    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Force (N)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Ligament Forces (N) - {ligament.name}')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Ligament Forces (N) - {ligament.name}.png')
    
    plt.close()  # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer

    fig, ax = plt.subplots()
    ax.plot(data[channelsimt], data[f'{ligament.name}_stretch'], label=f'{ligament.name}_stretch', color='blue')
    
    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Stretch')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Ligament Stretch - {ligament.name}')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Ligament Stretch - {ligament.name}.png')
    plt.close()

###########################################################################################################

# Function to aggregate data for a vertebral level
def aggregate_data(ligaments):
    # Initialize empty DataFrame for aggregated data
    aggregated_data = pd.DataFrame()
    for lig in ligaments:
        if aggregated_data.empty:
            aggregated_data = lig.data.copy()
        else:
            # Aggregate Fres, Fy, Fz
            for col in ['Fres', 'Fy', 'Fz']:
                aggregated_data[f'{lig.name}_{col}'] = lig.data[f'{lig.name}_{col}']
    return aggregated_data

import matplotlib.pyplot as plt

def plot_ligament_subplot(ax, ligament, data_type):
    channelsimt = 'Sim_Time_s'
    metrics = ['Fr', 'Fy', 'Fz'] if data_type == 'force' else ['stretch']

    for metric in metrics:
        ax.plot(ligament.data[channelsimt], ligament.data[f'{ligament.name}_{metric}'], label=f'{metric}')

    ax.set_title(f'{ligament.name} - {data_type.capitalize()}')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Value')
    ax.grid(True)
    ax.legend()

def plot_ligaments(level, ligaments):
    # Create two figures: one for force and one for strain
    fig_force, axs_force = plt.subplots(3, 4, figsize=(20, 15))
    fig_stretch, axs_strain = plt.subplots(3, 4, figsize=(20, 15))

    for i, ligament in enumerate(ligaments):
        row_idx = i // 4
        col_idx = i % 4

        # Plot force data
        plot_ligament_subplot(axs_force[row_idx, col_idx], ligament, 'force')

        # Plot strain data
        plot_ligament_subplot(axs_strain[row_idx, col_idx], ligament, 'stretch')

        fig_force.tight_layout()
        fig_force.savefig(f'{level}_Ligament_Force_Summary.png')
        plt.close(fig_force)

        fig_stretch.tight_layout()
        fig_stretch.savefig(f'{level}_Ligament_Stretch_Summary.png')
        plt.close(fig_stretch)


# Function to plot data for a vertebral level
def plot_level_data(level, ligaments):
    # Assuming each ligament has 3 force metrics (Fr, Fy, Fz) and 3 strain metrics (Er, Ey, Ez)
    num_metrics = 3
    num_ligaments = len(ligaments)
    figure, axes = plt.subplots(2, num_ligaments, figsize=(num_ligaments * 5, 10))  # 2 rows, num_ligaments columns
    plt.rcParams['font.size'] = '10'

    for i, ligament in enumerate(ligaments):
        data = ligament.data
        channelsimt = 'Sim_Time_s'

        # Plot force data (Fr, Fy, Fz) in the first row
        # for j, metric in enumerate(['Fr', 'Fy', 'Fz']):
        for j, metric in enumerate(['Fr']):
            axes[0, i].plot(data[channelsimt], data[f'{ligament.name}_{metric}'], label=f'{ligament.name}_{metric}')
            axes[0, i].set_title(f'{ligament.name} - {metric}')
            axes[0, i].set_xlabel('Time (s)')
            axes[0, i].set_ylabel('Force (N)')
            axes[0, i].grid(True)
            axes[0, i].legend()

        # Plot strain data (Er, Ey, Ez) in the second row
        for j, metric in enumerate(['stretch']):
            axes[1, i].plot(data[channelsimt], data[f'{ligament.name}_{metric}'], label=f'{ligament.name}_{metric}')
            axes[1, i].set_title(f'{ligament.name} - {metric}')
            axes[1, i].set_xlabel('Time (s)')
            axes[1, i].set_ylabel('Stretch')
            axes[1, i].grid(True)
            axes[1, i].legend()

    plt.tight_layout()
    plt.savefig(f'{level}_Ligament_Summary.png')
    plt.close()
    
def plot_ligament_data_summary(simulation):
    grouped_ligaments = simulation.group_ligaments_by_level()

    # Aggregate ligaments from C01, C02, and C12
    ligaments_to_plot = []
    for level in ['C01', 'C02', 'C12']:
        if level in grouped_ligaments:
            ligaments_to_plot.extend(grouped_ligaments[level])
            # Plot the aggregated ligaments
            plot_ligaments("C01_C02_C12", ligaments_to_plot)

    # Plot other levels
    for level, ligaments in grouped_ligaments.items():
        if level not in ['C01', 'C02', 'C12']:
            plot_level_data(level, ligaments)

