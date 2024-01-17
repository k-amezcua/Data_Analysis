import matplotlib.pyplot as plt
import os

def plot_disc_data(level, discs):
    fig, axs = plt.subplots(2, 3, figsize=(30, 10))  # 2 rows (stress, strain), 3 columns (anterior, middle, posterior)

    for i, section in enumerate(['Anterior', 'Middle', 'Posterior']):
        section_discs = [disc for disc in discs if section in disc.name]

        for disc in section_discs:
            data = disc.data  # Assuming 'data' contains the stress and strain data

            # Stress plots
            axs[0, i].plot(data['Sim_Time_s'], data['s1_average'], label=f'{disc.name}: Avg s1', color='red')
            axs[0, i].plot(data['Sim_Time_s'], data['s2_average'], label=f'{disc.name}: Avg s2', color='orange')
            axs[0, i].plot(data['Sim_Time_s'], data['s3_average'], label=f'{disc.name}: Avg s3', color='green')

            # Strain plots
            axs[1, i].plot(data['Sim_Time_s'], data['E1_average'], label=f'{disc.name}: Avg E1', color='blue')
            axs[1, i].plot(data['Sim_Time_s'], data['E2_average'], label=f'{disc.name}: Avg E2', color='purple')
            axs[1, i].plot(data['Sim_Time_s'], data['E3_average'], label=f'{disc.name}: Avg E3', color='brown')

        axs[0, i].set_title(f'{level} {section} - Stress')
        axs[1, i].set_title(f'{level} {section} - Strain')

    for ax in axs.flat:
        ax.set_xlim(0, 0.25)
        ax.set(xlabel='Time (s)', ylabel='Value')
        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    plt.savefig(f'{level}_Disc_Data.png')
    plt.close()

def plot_disc_data_summary(grouped_discs, data_type):
    levels = ['C23', 'C34', 'C45', 'C56', 'C67', 'C7T1']
    fig, axs = plt.subplots(2, 3, figsize=(40, 20))  # 2 rows, 3 columns

    stress_colors = {'Anterior': 'red', 'Posterior': 'orange', 'Middle': 'green'}
    strain_colors = {'Anterior': 'blue', 'Posterior': 'purple', 'Middle': 'brown'}

    for i, level in enumerate(levels):
        row_idx = i // 3
        col_idx = i % 3

        for disc in grouped_discs.get(level, []):
            data = disc.data
            section = 'Anterior' if 'Anterior' in disc.name else 'Middle' if 'Middle' in disc.name else 'Posterior'

            if data_type == 'stress':
                color = stress_colors[section]
                axs[row_idx, col_idx].plot(data['Sim_Time_s'], data['max_sr'], label=f'{section}: max_sr', color=color)
                # axs[row_idx, col_idx].plot(data['Sim_Time_s'], data['s1_average'], label=f'{section}: Avg s1', color='red')
                # axs[row_idx, col_idx].plot(data['Sim_Time_s'], data['s2_average'], label=f'{section}: Avg s2', color='orange')
                # axs[row_idx, col_idx].plot(data['Sim_Time_s'], data['s3_average'], label=f'{section}: Avg s3', color='green')
            elif data_type == 'strain':
                color = strain_colors[section]
                axs[row_idx, col_idx].plot(data['Sim_Time_s'], data['max_Er'], label=f'{section}: max_Er', color=color)
                # axs[row_idx, col_idx].plot(data['Sim_Time_s'], data['E1_average'], label=f'{section}: Avg E1', color='blue')
                # axs[row_idx, col_idx].plot(data['Sim_Time_s'], data['E2_average'], label=f'{section}: Avg E2', color='purple')
                # axs[row_idx, col_idx].plot(data['Sim_Time_s'], data['E3_average'], label=f'{section}: Avg E3', color='brown')

            axs[row_idx, col_idx].set_title(f'{level} - {data_type.capitalize()}')
            axs[row_idx, col_idx].set_xlim(0, 0.25)
            axs[row_idx, col_idx].grid(True)
            axs[row_idx, col_idx].set_xlabel('Time (s)')
            axs[row_idx, col_idx].set_ylabel('Value')
            axs[row_idx, col_idx].legend()

    plt.tight_layout()
    plt.savefig(f'Summary_{data_type.capitalize()}.png')
    plt.close()