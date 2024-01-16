import matplotlib.pyplot as plt
import os

def plot_data(disc):
    data = disc.data

    channelsimt = 'Sim_Time_s'

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig, ax = plt.subplots()
    ax.plot(data[channelsimt], data['s1_average'], label=f'{disc.name}: Avg s1', color='red')
    ax.plot(data[channelsimt], data['s2_average'], label=f'{disc.name}: Avg s2', color='orange')
    ax.plot(data[channelsimt], data['s3_average'], label=f'{disc.name}: Avg s3', color='green')
    ax.plot(data[channelsimt], data['max_sr'], label=f'{disc.name}: Max sr', color='blue')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Average Disc Stress (Pa)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Average Disc Stress - {disc.name}')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Average Disc Stress - {disc.name}.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig, ax = plt.subplots()
    ax.plot(data[channelsimt], data['E1_average'], label=f'{disc.name}: Avg E1', color='red')
    ax.plot(data[channelsimt], data['E2_average'], label=f'{disc.name}: Avg E2', color='orange')
    ax.plot(data[channelsimt], data['E3_average'], label=f'{disc.name}: Avg E3', color='green')
    ax.plot(data[channelsimt], data['max_Er'], label=f'{disc.name}: Max Er', color='blue')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Average Disc Strain')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Average Disc Strain - {disc.name}')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Average Disc Strain - {disc.name}.png')
    plt.close()

    ###########################################################################################################

    # Extract the column names for the variables (excluding "Time")
    sr_columns = ['s1_average', 's2_average', 's3_average']

    # Create a single plot for all variables
    plt.figure()

    # Iterate through the variable columns and plot each one
    for column in sr_columns:
        plt.plot(data[channelsimt], data[column], label=column)

    plt.title('Effective Stress for Each Element')
    plt.xlabel('Time (s)')
    plt.xlim(0,0.25)
    plt.ylabel('Effective Stress (Pa)')
    plt.grid(True)
    plt.legend(loc='best')
    plt.savefig(f'Effective Disc Stress - {disc.name}.png')
    plt.close()

    ###########################################################################################################

    # Extract the column names for the variables (excluding "Time")
    Er_columns = ['E1_average', 'E2_average', 'E3_average']

    # Create a single plot for all variables
    plt.figure()

    # Iterate through the variable columns and plot each one
    for column in Er_columns:
        plt.plot(data[channelsimt], data[column], label=column)

    plt.title('Effective Strain for Each Element')
    plt.xlabel('Time (s)')
    plt.xlim(0,0.25)
    plt.ylabel('Effective Strain')
    plt.grid(True)
    plt.legend(loc='best')
    plt.savefig(f'Effective Disc Strain - {disc.name}.png')
    plt.close()

    ###########################################################################################################
