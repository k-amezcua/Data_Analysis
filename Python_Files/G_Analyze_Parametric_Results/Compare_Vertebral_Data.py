def compare_vertebral_data(sim_list, panzer_vertebral_data):


    import matplotlib.pyplot as plt

    channelsimt = 'Sim_Time_s'
    channelt = 'Time_s'

    # Assuming sim_list is your list of simulations
    num_sims = len(sim_list)

    # Define the number of rows and columns for the subplot grid
    # Adjust these numbers based on your requirements
    num_rows = 1
    num_cols = num_sims

    fig, axs = plt.subplots(num_rows, num_cols, figsize=(30, 10))
    plt.rcParams['font.size'] = '20'
    # Check if axs is a single axis or an array of axes
    if num_sims == 1:
        axs = [axs]

    for ax, sim in zip(axs, sim_list):
        data = sim.vertebrae
        # ax.plot(data[channelsimt],data['Head_Ry'], label ='Head_Ry', color = 'red')
        # ax.plot(data[channelsimt],data['C12_Ry'], label ='C12_Ry', color = 'orange')
        ax.plot(data[channelsimt], data['C23_Ry'], label=f'C23_Ry', color='red')
        ax.plot(data[channelsimt], data['C34_Ry'], label=f'C34_Ry', color='green')
        ax.plot(data[channelsimt], data['C45_Ry'], label=f'C45_Ry', color='yellowgreen')
        ax.plot(data[channelsimt], data['C56_Ry'], label=f'C56_Ry', color='magenta')
        ax.plot(data[channelsimt], data['C67_Ry'], label=f'C67_Ry', color='purple')
        ax.plot(data[channelsimt], data['C7T1_Ry'], label=f'C7T1_Ry', color='cyan')
        # ax.plot(data[channelsimt],data['T1_Ry'], label ='T1_Ry', color = 'pink')
        ax.set_title(f'Simulation: {sim.label}')
        ax.legend()
        ax.set_xlim(0, 0.25)
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Ry (deg)')
        ax.grid(True)

    plt.tight_layout()
    plt.savefig('Simulation Results - Flexion deg.png')
    plt.close()