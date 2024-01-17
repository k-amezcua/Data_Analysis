import matplotlib.pyplot as plt

def compare_ligament_data(simulations, level):
    num_simulations = len(simulations)
    fig_force, axs_force = plt.subplots(num_simulations, 1, figsize=(10, num_simulations * 5), squeeze=False)
    fig_stretch, axs_stretch = plt.subplots(num_simulations, 1, figsize=(10, num_simulations * 5), squeeze=False)

    for sim_idx, sim in enumerate(simulations):
        grouped_ligaments = sim.group_ligaments_by_level()
        ligaments = grouped_ligaments.get(level, [])

        # Plot force data for each simulation
        for lig in ligaments:
            data = lig.data
            print(data)
            axs_force[sim_idx, 0].plot(data['Sim_Time_s'], data[f'{lig.name}_Fres'], label=f'{lig.name}_Fres')
            # axs_force[sim_idx, 0].plot(data['Sim_Time_s'], data[f'{lig.name}_Fy'], label=f'{lig.name}_Fy')
            # axs_force[sim_idx, 0].plot(data['Sim_Time_s'], data[f'{lig.name}_Fz'], label=f'{lig.name}_Fz')
            axs_force[sim_idx, 0].set_title(f'{sim.label} - {level} - Force')
            axs_force[sim_idx, 0].set_xlabel('Time (s)')
            axs_force[sim_idx, 0].set_ylabel('Force (N)')
            axs_force[sim_idx, 0].legend()

        # Plot stretch data for each simulation
        for lig in ligaments:
            data = lig.data
            axs_stretch[sim_idx, 0].plot(data['Sim_Time_s'], data[f'{lig.name}_stretch'], label=f'{lig.name}_stretch')
            axs_stretch[sim_idx, 0].set_title(f'{sim.label} - {level} - Stretch')
            axs_stretch[sim_idx, 0].set_xlabel('Time (s)')
            axs_stretch[sim_idx, 0].set_ylabel('Stretch')
            axs_stretch[sim_idx, 0].legend()

    plt.tight_layout()
    fig_force.savefig(f'{level}_Ligament_Force_Comparison.png')
    plt.close(fig_force)
    fig_stretch.savefig(f'{level}_Ligament_Stretch_Comparison.png')
    plt.close(fig_stretch)


