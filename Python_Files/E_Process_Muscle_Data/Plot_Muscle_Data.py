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
def plot_muscle_data_summary(muscle):
    #TODO: probably plot flexor muscles and extensor muscle in separate mltiplots. Will need to update the dictionary.
    return