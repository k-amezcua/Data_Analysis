import matplotlib.pyplot as plt

# Function to format subplots
def format_subplots(axs, title, xlabel, ylabel):
    for ax in axs.flatten():
        ax.set_title(title, fontsize=10)
        ax.set_xlabel(xlabel, fontsize=8)
        ax.set_ylabel(ylabel, fontsize=8)
        ax.legend(fontsize=6)
        ax.grid(True)
def compare_muscle_data(simulations):
    num_simulations = len(simulations)

    # Create figures for flexor and extensor data
    fig_flexor_force, axs_flexor_force = plt.subplots(4, 4, figsize=(20, 20))
    fig_flexor_stretch, axs_flexor_stretch = plt.subplots(4, 4, figsize=(20, 20))
    fig_extensor_force, axs_extensor_force = plt.subplots(4, 4, figsize=(20, 20))
    fig_extensor_stretch, axs_extensor_stretch = plt.subplots(4, 4, figsize=(20, 20))

    for sim_idx, simulation in enumerate(simulations):
        flexor_muscles = [muscle for muscle in simulation.muscles if muscle.muscle_group == 'flexor']
        extensor_muscles = [muscle for muscle in simulation.muscles if muscle.muscle_group == 'extensor']

        # Plot Flexor Muscles
        for i, muscle in enumerate(flexor_muscles):
            row_idx = i // 4
            col_idx = i % 4
            axs_flexor_force[row_idx, col_idx].plot(muscle.data['Sim_Time_s'], muscle.data[f'{muscle.name}_Fres'], label=f'{simulation.label}')
            axs_flexor_stretch[row_idx, col_idx].plot(muscle.data['Sim_Time_s'], muscle.data[f'{muscle.name}_stretch'], label=f'{simulation.label}')

        # Plot Extensor Muscles
        for i, muscle in enumerate(extensor_muscles):
            row_idx = i // 4
            col_idx = i % 4
            axs_extensor_force[row_idx, col_idx].plot(muscle.data['Sim_Time_s'], muscle.data[f'{muscle.name}_Fres'], label=f'{simulation.label}')
            axs_extensor_stretch[row_idx, col_idx].plot(muscle.data['Sim_Time_s'], muscle.data[f'{muscle.name}_stretch'], label=f'{simulation.label}')

    # Add titles, labels, legends, etc. for Flexor Force
    format_subplots(axs_flexor_force, "Flexor Muscle Force", "Time (s)", "Force (N)")

    # Add titles, labels, legends, etc. for Flexor Stretch
    format_subplots(axs_flexor_stretch, "Flexor Muscle Stretch", "Time (s)", "Stretch")

    # Add titles, labels, legends, etc. for Extensor Force
    format_subplots(axs_extensor_force, "Extensor Muscle Force", "Time (s)", "Force (N)")

    # Add titles, labels, legends, etc. for Extensor Stretch
    format_subplots(axs_extensor_stretch, "Extensor Muscle Stretch", "Time (s)", "Stretch")

    # Adjust layout and save figures
    fig_flexor_force.tight_layout()
    fig_flexor_stretch.tight_layout()
    fig_extensor_force.tight_layout()
    fig_extensor_stretch.tight_layout()

    fig_flexor_force.savefig('Flexor_Force_Data_Comparison.png')
    fig_flexor_stretch.savefig('Flexor_Stretch_Data_Comparison.png')
    fig_extensor_force.savefig('Extensor_Force_Data_Comparison.png')
    fig_extensor_stretch.savefig('Extensor_Stretch_Data_Comparison.png')
    plt.close('all')

    # Save the figures
    fig_flexor_force.savefig('Flexor_Force_Data_Comparison.png')
    fig_flexor_stretch.savefig('Flexor_Stretch_Data_Comparison.png')
    fig_extensor_force.savefig('Extensor_Force_Data_Comparison.png')
    fig_extensor_stretch.savefig('Extensor_Stretch_Data_Comparison.png')
    plt.close('all')
