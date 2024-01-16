def compare_kinematics(compare_save_path, sim_list,
             average_data, low_data, high_data,
             average_panzer_x_df, average_panzer_y_df, average_panzer_z_df):

    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    print('comparing kinematics')

    os.chdir(compare_save_path)

    ###Variables###
    channelsimt = 'Sim_Time_s'
    channel_Head_Dx_mm = 'Head_Dx'
    channel_Head_Dz_mm = 'Head_Dz'
    channel_Head_Ry_deg= 'Head_Ry'
    channel_Head_aDx_G = 'Head_aDx'
    channel_Head_aDz_G = 'Head_aDz'
    channel_Head_aRy_rad_s_s= 'Head_aRy'
    Sim_Head_vx = 'Head_vx'
    Sim_Head_vz = 'Head_vz'
    Sim_Head_wy= 'Head_wy'
    channel_T1_Dx_mm = 'T1_Dx'
    channel_T1_Ry_deg= 'T1_Ry'
    Sim_Rel_Head_Dx = 'Sim_Rel_Head_Dx'
    Sim_Rel_Head_Ry = 'Sim_Rel_Head_Ry'
    Sim_Rel_Head_Dz = 'Sim_Rel_Head_Dz'

    #######################################################

    channelt = 'Time_s'
    Head_Dx_mm_int_19 = 'Head_Dx_mm_int_19'
    Sled_Dx_mm_int_57 = 'Sled_Dx_mm_int_57'
    Spine_Dx_mm_int_47 = 'Spine_Dx_mm_int_47'
    Head_Dz_mm_int_21 = 'Head_Dz_mm_int_21'
    Spine_Dz_mm_int_49 = 'Spine_Dz_mm_int_49'
    Head_ao_deg_data_22 = 'Head_ao_deg_22'
    Head_ao_deg_23 = 'Head_ao_deg_23'
    Head_ao_deg_data_24 = 'Head_ao_deg_24'
    Spine_ao_deg_data_50 = 'Spine_ao_deg_50'
    Spine_ao_deg_data_51 = 'Spine_ao_deg_51'
    Spine_ao_deg_data_52 = 'Spine_ao_deg_52'
    Head_Ax_G_19 = 'Head_Ax_G_19'
    Head_Az_G_21='Head_Az_G_21'
    Spine_Ax_G_47='Spine_Ax_G_47'
    Head_ao_rad_s_s_23 = 'Head_ao_rad/s^2_23'
    Head_Vx_kph = "Head_Vx_kph_10"
    Head_Vz_kph = "Head_Vz_kph_14"
    Head_wy_rad_s = "Head_wx_rad/s_17"

    Sim_Head_Dx = 'Head_Dx'
    Sim_Head_Dz = 'Head_Dz'
    Sim_Head_Ry = 'Head_Ry'
    Rel_Head_Dx = 'Rel_Head_Dx_mm'
    Rel_Head_Dz = 'Head_Dz_mm_int_21'
    Rel_Head_to_Sled_Dx_mm = 'Rel_Head_to_Sled_Dx_mm'

    #########################################################

    # Plotting loop

    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_Dx_mm], label=sim.label)
        # Add more plots or customizations as needed
    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Dx (mm)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Simulation Results - Head X Displacement (mm)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Parameter - Head X Displacement mm.png')
    plt.close()

    # Plotting loop for Head Z Displacement
    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_Dz_mm], label=sim.label)
    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Dz (mm)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Simulation Results - Head Z Displacement (mm)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Parameter - Head Z Displacement mm.png')
    plt.close()

    # Plotting loop for Head Y Rotation
    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_Ry_deg], label=sim.label)
    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Head Y Rotation (deg)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Parameter - Simulation Results - Head Y Rotation deg.png')
    plt.close()

    # Plotting loop for Head X Acceleration G
    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aDx_G], label=sim.label)
    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ax (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Simulation Results - Head X Acceleration G')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Parameter - Head X Acceleration G.png')
    plt.close()

    # Plotting loop for Compare Results - Head X Acceleration G
    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aDx_G], label=sim.label)
        ax.plot(average_data[channelt], average_data[Head_Ax_G_19], label=Head_Ax_G_19, color="red")
        ax.plot(average_data[channelt], low_data[Head_Ax_G_19], color="lightpink")
        ax.plot(average_data[channelt], high_data[Head_Ax_G_19], color="lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ax (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Compare Results - Head X Acceleration G')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Parameter - Compare Head X Acceleration G.png')
    plt.close()

    # Plotting loop for Simulation Results - Head X Acceleration G
    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aDx_G], label=sim.label)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ax (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Simulation Results - Head X Acceleration G')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Parameter - Head X Acceleration G.png')
    plt.close()

    # Plotting loop for Compare Panzer Results - Head X Acceleration G
    fig, ax = plt.subplots()
    for sim in sim_list:
        if sim.label == 'passive':
            ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aDx_G], label=sim.label)
    ax.plot(average_panzer_x_df["x"]/1000, average_panzer_x_df["Passive X Accel"]*-1, label="Panzer Head X Accel.")

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ax (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Panzer Results - Head X Acceleration G')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Compare Panzer Head X Acceleration G.png')
    plt.close()

    # Plotting loop for Simulation Results - Head Z Acceleration G
    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aDz_G], label=sim.label)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Az (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Simulation Results - Head Z Acceleration G')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Parameter - Head Z Acceleration G.png')
    plt.close()

    # Plotting loop for Compare Results - Head Z Acceleration G
    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aDz_G], label=sim.label)

    ax.plot(average_data[channelt], average_data[Head_Az_G_21], label=Head_Az_G_21, color="red")
    ax.plot(average_data[channelt], low_data[Head_Az_G_21], color="lightpink")
    ax.plot(average_data[channelt], high_data[Head_Az_G_21], color="lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_ylim(-100, 50)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Az (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Results - Head Z Acceleration G')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Parameter - Compare Head Z Acceleration G.png')
    plt.close()

    # Plotting loop for Compare Panzer Results - Head Z Acceleration G
    fig, ax = plt.subplots()
    for sim in sim_list:
        if sim.label == 'passive':
            ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aDz_G], label=sim.label)
    ax.plot(average_panzer_z_df["x"]/1000, average_panzer_z_df["Passive Z Accel"], label="Panzer Head Z Accel.")

    ax.set_xlim(0, 0.25)
    ax.set_ylim(-100, 50)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Az (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Panzer Results - Head Z Acceleration G')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Compare Panzer Head Z Acceleration G.png')
    plt.close()

    # Plotting loop for Head Y Rotation Acceleration (rad/s/s)
    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aRy_rad_s_s], label=sim.label)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (rad-s-s)')
    ax.grid(True)
    ax.legend()
    ax.set_title(f'Head Y Rotation Acceleration (rad/s/s)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig(f'Parameter - Simulation Results - Head Y Rotation Accel.png')
    plt.close()

    # List of data and datalabels
    fig, ax = plt.subplots()
    for i, simulation in enumerate(sim_list, start=1):
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aRy_rad_s_s], label=sim.label)

    ax.plot(average_data[channelt], average_data[Head_ao_rad_s_s_23], label=Head_ao_rad_s_s_23, color="red")
    ax.plot(average_data[channelt], low_data[Head_ao_rad_s_s_23], color="lightpink")
    ax.plot(average_data[channelt], high_data[Head_ao_rad_s_s_23], color="lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_ylim(-2000, 2500)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (rad-s-s)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Head Y Rotation Acceleration (rad/s/s)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Parameter - Compare Head Y Rotation Acceleration rad-s-s.png')
    plt.close()


    # Plotting loop for Compare Panzer Head Y Rotation Acceleration (rad/s/s)
    fig, ax = plt.subplots()
    for sim in sim_list:
        if sim.label == 'passive':
            ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aRy_rad_s_s], label=sim.label)
    ax.plot(average_panzer_y_df["x"]/1000, average_panzer_y_df["Passive Y Rot. Accel"], label="Panzer Head Y Rot Accel.")

    ax.set_xlim(0, 0.25)
    ax.set_ylim(-5000, 2500)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (rad-s-s)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Panzer Head Y Rotation Acceleration (rad/s/s)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Compare Panzer Head Y Rotation Acceleration rad-s-s.png')
    plt.close()

    # Plotting loop for Compare Panzer Head Y Rotation Acceleration (rad/s/s) - NL
    fig, ax = plt.subplots()
    for sim in sim_list:
        if sim.label == 'passive':
            ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aRy_rad_s_s], label=sim.label)
    ax.plot(average_panzer_y_df["x"]/1000, average_panzer_y_df["Passive Y Rot. Accel"], label="Panzer Head Y Rot Accel.")

    ax.set_xlim(0, 0.25)
    # ax.set_ylim(-2000, 2500)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (rad-s-s)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Panzer Head Y Rotation Acceleration (rad/s/s) - NL')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Compare Panzer Head Y Rotation Acceleration rad-s-s - NL.png')
    plt.close()

    fig, ax = plt.subplots()
    for i, simulation in enumerate(sim_list, start=1):
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_T1_Dx_mm], label=sim.label)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Dx (mm)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - T1 X Displacement (mm)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('T1 X Displacement mm.png')
    plt.close()

    fig, ax = plt.subplots()
    for sim in sim_list:
        if sim.label == 'passive':
            ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aRy_rad_s_s], label=sim.label)
    ax.plot(average_panzer_y_df["x"]/1000, average_panzer_y_df["Passive Y Rot. Accel"], label="Panzer Head Y Rot Accel.")

    ax.set_xlim(0, 0.25)
    ax.set_ylim(-5000, 2500)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (rad-s-s)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Panzer Head Y Rotation Acceleration (rad/s/s)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Compare Panzer Head Y Rotation Acceleration rad-s-s.png')
    plt.close()

    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_Head_aRy_rad_s_s], label=sim.label)

    ax.plot(average_panzer_y_df["x"]/1000, average_panzer_y_df["Passive Y Rot. Accel"], label="Panzer Head Y Rot Accel.")

    ax.set_xlim(0, 0.25)
    # ax.set_ylim(-2000, 2500)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (rad-s-s)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Panzer Head Y Rotation Acceleration (rad/s/s) - NL')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Compare Panzer Head Y Rotation Acceleration rad-s-s - NL.png')
    plt.close()

    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_T1_Dx_mm], label=sim.label)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Dx (mm)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - T1 X Displacement (mm)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('T1 X Displacement mm.png')
    plt.close()

    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[channel_T1_Ry_deg], label=sim.label)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('T1 Y Rotation (deg)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Simulation Results - T1 Y Rotation deg.png')
    plt.close()

    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[Sim_Rel_Head_Dx], label=sim.label)

    ax.plot(average_data[channelt], average_data[Rel_Head_Dx], label=Rel_Head_Dx, color="red")
    ax.plot(average_data[channelt], low_data[Rel_Head_Dx], color="lightpink")
    ax.plot(average_data[channelt], high_data[Rel_Head_Dx], color="lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Dx (mm)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - Rel Head X Displacement (mm)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Parameter - Rel Head X Displacement mm.png')
    plt.close()

    # Rel Head Y Rotation (deg)
    fig, ax = plt.subplots()
    for sim in sim_list:
        ax.plot(sim.kin_data[channelsimt], sim.kin_data[Sim_Rel_Head_Ry], label=sim.label)

    ax.plot(average_data[channelt], average_data[Head_ao_deg_23], label='Head_ao_deg_23', color="red")
    ax.plot(average_data[channelt], low_data[Head_ao_deg_23], color="lightpink")
    ax.plot(average_data[channelt], high_data[Head_ao_deg_23], color="lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Rel Head Y Rotation (deg)')
    plt.subplots_adjust(left=0.17, bottom=0.13)
    plt.savefig('Parameter - Rel Head Y Rotation deg.png')
    plt.close()

    #################################################################################################

    # Assuming you have 4 rows and 3 columns for subplots
    fig, ax = plt.subplots(4, 3, figsize=(40, 30))
    plt.rcParams['font.size'] = '20'

    for sim in sim_list:
        print(sim.label)
    def plot_sim_subplot(ax, simulation, simlabel, average_data, low_data, high_data, channelsimt, channelt, expydata, simydata,
                     ylabel, title, color='red'):
        ax.plot(simulation.kin_data[channelsimt], simulation.kin_data[simydata], label=simulation.label)
        ax.set_title(title)
        ax.set_xlim(0, 0.25)
        ax.set_xlabel('Time (s)')
        ax.set_ylabel(ylabel)
        ax.grid(True)
        ax.legend()
    def plot_exp_subplot(ax, simulation, simlabel, average_data, low_data, high_data, channelsimt, channelt, expydata, simydata,
                     ylabel, title, color='red'):
        ax.plot(average_data[channelt], average_data[expydata], label=expydata, color=color)
        ax.plot(low_data[channelt], low_data[expydata], color='lightpink')
        ax.plot(high_data[channelt], high_data[expydata], color='lightpink')

    # Flatten the 2D array of subplots
    ax_flat = ax.flatten()

    average_data['Rel_Head_Ry'] = 0
    low_data['Rel_Head_Ry'] = 0
    high_data['Rel_Head_Ry'] = 0

    # Define different datavariables for each row and column
    simydatalist = [
        [Sim_Rel_Head_Dx, Sim_Rel_Head_Dz, Sim_Rel_Head_Ry],
        [Sim_Head_Dx, Sim_Head_Dz, Sim_Head_Ry],
        [Sim_Head_vx, Sim_Head_vz, Sim_Head_wy],
        ['Head_aDx', 'Head_aDz', 'Head_aRy']
    ]
    expydatalist = [
        [Rel_Head_Dx, Rel_Head_Dz, 'Rel_Head_Ry'],
        ['Head_Dx_mm_int_19', 'Head_Dz_mm_int_21', 'Head_ao_deg_23'],
        [Head_Vx_kph,Head_Vz_kph, Head_wy_rad_s],
        ['Head_Ax_G_19', 'Head_Az_G_21', Head_ao_rad_s_s_23]
    ]
    ylabellist = [
        ['Dx (mm)', 'Dz (mm)', 'Ry (deg)'],
        ['Dx (mm)', 'Dz (mm)', 'Ry (deg)'],
        ['Vx (kph)','Vz (kph)', 'wy (rad/s)'],
        ['Ax (G)', 'Az (G)', 'Y Rot. Acc. (rad/s^2)']
    ]
    titles = [
        ['Rel. Head X Disp.', 'Rel. Head Z Disp.', 'Rel. Head Y Rot.'],
        ['Head X Disp.', 'Head Z Disp. (+Rel.)', 'Head Y Rot.'],
        ['Head X Vel.', 'Head Z Vel.', 'Head Y Rot. Vel.'],
        ['Head X Acc.', 'Head Z Acc.', 'Head Y Rot. Acc.'],
    ]

    # Loop through sim_list in every row and every column
    for i, row in enumerate(ax):
        for j, current_ax in enumerate(row):
            exp_data_plotted = False  # Initialize a flag to track whether experimental data has been plotted
            # Plot all datasets in the current subplot
            for simulation in sim_list:
                simlabel = simulation.label
                expydata = expydatalist[i][j]  # Select the appropriate datavariable
                simydata = simydatalist[i][j]  # Select the appropriate datavariable
                ylabel = ylabellist[i][j]  # Select the appropriate datavariable
                title = titles[i][j]  # Select the appropriate datavariable

                if not exp_data_plotted:
                    # Call plot_exp_subplot() only the first time
                    plot_exp_subplot(current_ax, simulation, simlabel, average_data, low_data, high_data, channelsimt,
                                     channelt,
                                     expydata, simydata, ylabel, title)
                    plot_sim_subplot(current_ax, simulation, simlabel, average_data, low_data, high_data, channelsimt,
                                     channelt,
                                     expydata, simydata, ylabel, title)
                    exp_data_plotted = True
                else:
                    # Call plot_sim_subplot() for subsequent simulations
                    plot_sim_subplot(current_ax, simulation, simlabel, average_data, low_data, high_data, channelsimt,
                                     channelt,
                                     expydata, simydata, ylabel, title)
    plt.tight_layout()
    plt.savefig('Simulation Results Summary.png')
    plt.close()

    print('(completed)\n')

    return