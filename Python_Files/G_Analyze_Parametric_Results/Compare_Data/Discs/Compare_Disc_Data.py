import matplotlib.pyplot as plt

def compare_disc_data(simulations):
    levels = ['C23', 'C34', 'C45', 'C56', 'C67', 'C7T1']
    num_simulations = len(simulations)
    fig_force, axs_force = plt.subplots(num_simulations, len(levels), figsize=(40, num_simulations * 8), squeeze=False)  # Adjust figsize as needed
    fig_strain, axs_strain = plt.subplots(num_simulations, len(levels), figsize=(40, num_simulations * 8), squeeze=False)  # Adjust figsize as needed

    for sim_idx, sim in enumerate(simulations):
        grouped_discs = sim.group_discs_by_level()

        for level_idx, level in enumerate(levels):
            for disc in grouped_discs.get(level, []):
                data = disc.data
                section = 'Anterior' if 'Anterior' in disc.name else 'Middle' if 'Middle' in disc.name else 'Posterior'

                # Plot stress data (you can add strain data similarly)
                axs_force[sim_idx, level_idx].plot(data['Sim_Time_s'], data['max_sr'], label=f'{section}: max_sr')
                # axs_force[sim_idx, level_idx].plot(data['Sim_Time_s'], data['s1_average'], label=f'{section}: Avg s1')
                # axs_force[sim_idx, level_idx].plot(data['Sim_Time_s'], data['s2_average'], label=f'{section}: Avg s2')
                # axs_force[sim_idx, level_idx].plot(data['Sim_Time_s'], data['s3_average'], label=f'{section}: Avg s3')

                axs_force[sim_idx, level_idx].set_title(f'{sim.label} - {level} - Stress')
                axs_force[sim_idx, level_idx].set_xlabel('Time (s)')
                axs_force[sim_idx, level_idx].set_ylabel('Stress (Pa)')
                axs_force[sim_idx, level_idx].legend()

            for disc in grouped_discs.get(level, []):
                data = disc.data
                section = 'Anterior' if 'Anterior' in disc.name else 'Middle' if 'Middle' in disc.name else 'Posterior'

                # Plot stress data (you can add strain data similarly)
                axs_strain[sim_idx, level_idx].plot(data['Sim_Time_s'], data['max_sr'], label=f'{section}: max_sr')
                # axs_strain[sim_idx, level_idx].plot(data['Sim_Time_s'], data['s1_average'], label=f'{section}: Avg s1')
                # axs_strain[sim_idx, level_idx].plot(data['Sim_Time_s'], data['s2_average'], label=f'{section}: Avg s2')
                # axs_strain[sim_idx, level_idx].plot(data['Sim_Time_s'], data['s3_average'], label=f'{section}: Avg s3')

                axs_strain[sim_idx, level_idx].set_title(f'{sim.label} - {level} - Stress')
                axs_strain[sim_idx, level_idx].set_xlabel('Time (s)')
                axs_strain[sim_idx, level_idx].set_ylabel('Stress (Pa)')
                axs_strain[sim_idx, level_idx].legend()

    plt.tight_layout()
    fig_force.savefig('Disc_Force_Data_Comparison.png')
    plt.close(fig_force)
    fig_strain.savefig('Disc_Strain_Data_Comparison.png')
    plt.close(fig_strain)
