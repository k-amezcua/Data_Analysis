import matplotlib.pyplot as plt

def compare_ligament_data(simulations, level):
    num_simulations = len(simulations)
    # Create subplots with a single row and multiple columns
    fig_force, axs_force = plt.subplots(1, num_simulations, figsize=(num_simulations * 40, 20), squeeze=False)
    fig_stretch, axs_stretch = plt.subplots(1, num_simulations, figsize=(num_simulations * 40, 20), squeeze=False)

    for sim_idx, sim in enumerate(simulations):
        grouped_ligaments = sim.group_ligaments_by_level()
        ligaments = grouped_ligaments.get(level, [])

        # Plot force data for each simulation
        for lig in ligaments:
            data = lig.data
            axs_force[0, sim_idx].plot(data['Sim_Time_s'], data[f'{lig.name}_Fres'], label=f'{lig.name}_Fres')
            axs_force[0, sim_idx].set_title(f'{sim.label} - {level} - Force')
            axs_force[0, sim_idx].set_xlabel('Time (s)')
            axs_force[0, sim_idx].set_ylabel('Force (N)')
            axs_force[0, sim_idx].legend()

        # Plot stretch data for each simulation
        for lig in ligaments:
            data = lig.data
            axs_stretch[0, sim_idx].plot(data['Sim_Time_s'], data[f'{lig.name}_stretch'], label=f'{lig.name}_stretch')
            axs_stretch[0, sim_idx].set_title(f'{sim.label} - {level} - Stretch')
            axs_stretch[0, sim_idx].set_xlabel('Time (s)')
            axs_stretch[0, sim_idx].set_ylabel('Stretch')
            axs_stretch[0, sim_idx].legend()

    plt.tight_layout()
    fig_force.savefig(f'{level}_Ligament_Force_Comparison.png')
    plt.close(fig_force)
    fig_stretch.savefig(f'{level}_Ligament_Stretch_Comparison.png')
    plt.close(fig_stretch)
