import matplotlib.pyplot as plt

def plot_vertebral_data(data, panzer_vertebral_data):

    channelsimt = 'Sim_Time_s'
    channelt = 'Time_s'

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig,ax = plt.subplots()
    # ax.plot(data[channelsimt],data['Head_Ry'], label ='Head_Ry', color = 'red')
    # ax.plot(data[channelsimt],data['C12_Ry'], label ='C12_Ry', color = 'orange')
    ax.plot(data[channelsimt],data['C23_Ry'], label ='C23_Ry', color = 'bisque')
    ax.plot(data[channelsimt],data['C34_Ry'], label ='C34_Ry', color = 'green')
    ax.plot(data[channelsimt],data['C45_Ry'], label ='C45_Ry', color = 'yellowgreen')
    ax.plot(data[channelsimt],data['C56_Ry'], label ='C56_Ry', color = 'magenta')
    ax.plot(data[channelsimt],data['C67_Ry'], label ='C67_Ry', color = 'purple')
    ax.plot(data[channelsimt],data['C7T1_Ry'], label ='C7T1_Ry', color = 'cyan')
    # ax.plot(data[channelsimt],data['T1_Ry'], label ='T1_Ry', color = 'pink')

    # ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C12'], label ='C12_Panzer', color = 'navy')
    # ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C23'], label ='C23_Panzer', color = 'bisque')
    # ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C34'], label ='C34_Panzer', color = 'green')
    # ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C45'], label ='C45_Panzer', color = 'yellowgreen')
    # ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C56'], label ='C56_Panzer', color = 'magenta')
    # ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C67'], label ='C67_Panzer', color = 'purple')
    # ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C7T1'], label ='C7T1_Panzer', color = 'cyan')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Sim Results - Flexion (deg)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Simulation Results - Flexion deg.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig,ax = plt.subplots()
    ax.plot(data[channelsimt],data['C23_Ry'], label ='C23_Ry', color = 'blue')
    ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C23'], label ='C23_Panzer', color = 'red')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Sim Results - C23 Flexion (deg)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Sim Results - C23 Flexion deg.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig,ax = plt.subplots()
    ax.plot(data[channelsimt],data['C34_Ry'], label ='C34_Ry', color = 'blue')
    ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C34'], label ='C34_Panzer', color = 'red')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Sim Results - C34 Flexion (deg)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Sim Results - C34 Flexion deg.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig,ax = plt.subplots()
    ax.plot(data[channelsimt],data['C45_Ry'], label ='C45_Ry', color = 'blue')
    ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C45'], label ='C45_Panzer', color = 'red')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Sim Results - C45 Flexion (deg)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Sim Results - C45 Flexion deg.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig,ax = plt.subplots()
    ax.plot(data[channelsimt],data['C56_Ry'], label ='C56_Ry', color = 'blue')
    ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C56'], label ='C56_Panzer', color = 'red')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Sim Results - C56 Flexion (deg)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Sim Results - C56 Flexion deg.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig,ax = plt.subplots()
    ax.plot(data[channelsimt],data['C67_Ry'], label ='C67_Ry', color = 'blue')
    ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C67'], label ='C67_Panzer', color = 'red')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Sim Results - C67 Flexion (deg)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Sim Results - C67 Flexion deg.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig,ax = plt.subplots()
    ax.plot(data[channelsimt],data['C7T1_Ry'], label ='C7T1_Ry', color = 'blue')
    ax.plot(panzer_vertebral_data[channelt],panzer_vertebral_data['C7T1'], label ='C7T1_Panzer', color = 'red')

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Sim Results - C7T1 Flexion (deg)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Sim Results - C7T1 Flexion deg.png')
    plt.close()