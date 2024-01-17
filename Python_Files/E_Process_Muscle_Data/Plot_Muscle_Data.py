import matplotlib.pyplot as plt
import pandas as pd

def plot_muscle_data(muscle):
    data = muscle.data

    channelsimt = 'Sim_Time_s'

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig, ax = plt.subplots()
    ax.plot(data[channelsimt], data[f'{muscle.name}_Fres'], label=f'{muscle.name}_Fres', color='red')
    ax.plot(data[channelsimt], data[f'{muscle.name}_Fy'], label=f'{muscle.name}_Fy', color='orange')
    ax.plot(data[channelsimt], data[f'{muscle.name}_Fz'], label=f'{muscle.name}_Fz', color='green')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Force (N)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Muscle Forces (N) - {muscle.name}')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Muscle Forces (N) - {muscle.name}.png')

    plt.close()  # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer

    fig, ax = plt.subplots()
    ax.plot(data[channelsimt], data[f'{muscle.name}_stretch'], label=f'{muscle.name}_stretch', color='blue')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Stretch')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Muscle Stretch - {muscle.name}')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Muscle Stretch - {muscle.name}.png')
    plt.close()

    ###########################################################################################################


import matplotlib.pyplot as plt


def plot_muscle_data_summary(simulation):
    # Assuming simulation.muscles is a list of Muscle objects
    flexor_muscles = [muscle for muscle in simulation.muscles if muscle.muscle_group == 'flexor']
    extensor_muscles = [muscle for muscle in simulation.muscles if muscle.muscle_group == 'extensor']

    # Plot flexor muscles
    fig_flexor_force, axs_flexor_force = plt.subplots(3, 4, figsize=(36, 27))  # Adjust figsize as needed
    fig_flexor_stretch, axs_flexor_stretch = plt.subplots(3, 4, figsize=(36, 27))  # Separate figure for stretch

    for i, muscle in enumerate(flexor_muscles):
        row_idx = i // 4
        col_idx = i % 4

        # Plot Force Data
        ax_force = axs_flexor_force[row_idx, col_idx]
        ax_force.plot(muscle.data['Sim_Time_s'], muscle.data[f'{muscle.name}_Fres'],
                      label=f'{muscle.name}_Fres', color='red')
        ax_force.set_title(f'{muscle.name}')
        ax_force.set_xlabel('Time (s)')
        ax_force.set_ylabel('Force (N)')
        ax_force.legend()
        ax_force.set_xlim(0, 0.25)
        ax_force.grid(True)

        # Plot Stretch Data
        ax_stretch = axs_flexor_stretch[row_idx, col_idx]
        ax_stretch.plot(muscle.data['Sim_Time_s'], muscle.data[f'{muscle.name}_stretch'],
                        label=f'{muscle.name}_Stretch', color='blue')
        ax_stretch.set_title(f'{muscle.name}')
        ax_stretch.set_xlabel('Time (s)')
        ax_stretch.set_ylabel('Stretch')
        ax_stretch.legend()
        ax_stretch.set_xlim(0, 0.25)
        ax_stretch.grid(True)

    plt.tight_layout()
    fig_flexor_force.savefig('Flexor_Muscles_Force_Summary.png')
    plt.close(fig_flexor_force)
    fig_flexor_stretch.savefig('Flexor_Muscles_Stretch_Summary.png')
    plt.close(fig_flexor_stretch)

    # Plot extensor muscles
    fig_extensor_force, axs_extensor_force = plt.subplots(4, 4, figsize=(36, 36))  # Adjust figsize as needed
    fig_extensor_stretch, axs_extensor_stretch = plt.subplots(4, 4, figsize=(36, 36))  # Separate figure for stretch

    for i, muscle in enumerate(extensor_muscles):
        row_idx = i // 4
        col_idx = i % 4

        # Plot Force Data
        ax_force = axs_extensor_force[row_idx, col_idx]
        ax_force.plot(muscle.data['Sim_Time_s'], muscle.data[f'{muscle.name}_Fres'],
                      label=f'{muscle.name}_Fres', color='red')
        ax_force.set_title(f'{muscle.name}')
        ax_force.set_xlabel('Time (s)')
        ax_force.set_ylabel('Force (N)')
        ax_force.legend()
        ax_force.set_xlim(0, 0.25)
        ax_force.grid(True)

        # Plot Stretch Data
        ax_stretch = axs_extensor_stretch[row_idx, col_idx]
        ax_stretch.plot(muscle.data['Sim_Time_s'], muscle.data[f'{muscle.name}_stretch'],
                        label=f'{muscle.name}_Stretch', color='blue')
        ax_stretch.set_title(f'{muscle.name}')
        ax_stretch.set_xlabel('Time (s)')
        ax_stretch.set_ylabel('Stretch')
        ax_stretch.legend()
        ax_stretch.set_xlim(0, 0.25)
        ax_stretch.grid(True)

    plt.tight_layout()
    fig_extensor_force.savefig('Extensor_Muscles_Force_Summary.png')
    plt.close(fig_extensor_force)
    fig_extensor_stretch.savefig('Extensor_Muscles_Stretch_Summary.png')
    plt.close(fig_extensor_stretch)
