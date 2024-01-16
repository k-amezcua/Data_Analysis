
def plot_kinematic_data(data, average_data, low_data, high_data, panzer_data, thunn_data):

    import matplotlib.pyplot as plt

    channelt = 'Time_s'
    Head_Dx_mm_int_19 = 'Head_Dx_mm_int_19'
    Sled_Dx_mm_int_57 = 'Sled_Dx_mm_int_57'
    Spine_Dx_mm_int_47 = 'Spine_Dx_mm_int_47'
    Head_Dz_mm_int_21 = 'Head_Dz_mm_int_21'
    Spine_Dz_mm_int_49 = 'Spine_Dz_mm_int_49'
    Head_ao_deg_int_22 = 'Head_ao_deg_22'
    Head_ao_deg_23 = 'Head_ao_deg_23'
    Head_ao_deg_int_24 = 'Head_ao_deg_24'
    Spine_ao_deg_int_50 = 'Spine_ao_deg_50'
    Spine_ao_deg_int_51 = 'Spine_ao_deg_51'
    Spine_ao_deg_int_52 = 'Spine_ao_deg_52'
    Head_Ax_G_19 = 'Head_Ax_G_19'
    Head_Az_G_21 ='Head_Az_G_21'
    Spine_Ax_G_47 ='Spine_Ax_G_47'
    Head_ao_rad_s_s_23 = 'Head_ao_rad/s^2_23' #############
    Head_Vx_kph = "Head_Vx_kph_10" #############
    Head_Vz_kph = "Head_Vz_kph_14" #############
    Head_wy_rad_s = "Head_wx_rad/s_17" #############

    Sim_Head_Dx = 'Head_Dx' #############
    Sim_Head_Dz = 'Head_Dz'
    Sim_Head_Ry = 'Head_Ry' #############
    Rel_Head_Dx = 'Rel_Head_Dx_mm' #############
    Rel_Head_Dz = 'Head_Dz_mm_int_21' #############
    Rel_Head_to_Sled_Dx_mm = 'Rel_Head_to_Sled_Dx_mm'

    ###########################################################################################################

    channelsimt = 'Sim_Time_s'
    channel_Head_Dx_mm = 'Head_Dx' #############
    channel_Head_Dz_mm = 'Head_Dz' #############
    channel_Head_Ry_deg= 'Head_Ry' #############
    channel_Head_aDx_G = 'Head_aDx' #############
    channel_Head_aDz_G = 'Head_aDz' #############
    channel_Head_aRy_rad_s_s= 'Head_aRy' #############
    Sim_Head_vx = 'Head_vx' #############
    Sim_Head_vz = 'Head_vz' #############
    Sim_Head_wy= 'Head_wy' #############
    channel_T1_Dx_mm = 'T1_Dx' #############
    channel_T1_Ry_deg= 'T1_Ry' #############
    Sim_Rel_Head_Dx = 'Sim_Rel_Head_Dx'
    Sim_Rel_Head_Ry = 'Sim_Rel_Head_Ry'
    Sim_Rel_Head_Dz = 'Sim_Rel_Head_Dz'

    ###########################################################################################################

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_Head_Dx_mm], label =channel_Head_Dx_mm)
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Dx (mm)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - Head X Displacement (mm)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Head X Displacement mm.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_Head_Dz_mm], label =channel_Head_Dz_mm)
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Dz (mm)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - Head Z Displacement (mm)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Head Z Displacement mm.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    # ax.plot(average_data[channelt],data[channel_Head_Dx_mm], label =channel_Head_Dx_mm)
    ax.plot(data[channelsimt] ,data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Head Y Rotation (deg)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Simulation Results - Head Y Rotation deg.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_Head_aDx_G], label =channel_Head_aDx_G)
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ax (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - Head X Acceleration G')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Head X Acceleration G.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_Head_aDx_G], label =channel_Head_aDx_G)
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.plot(average_data[channelt] ,average_data[Head_Ax_G_19], label =Head_Ax_G_19, color = "red")
    ax.plot(average_data[channelt] ,low_data[Head_Ax_G_19] ,color = "lightpink")
    ax.plot(average_data[channelt] ,high_data[Head_Ax_G_19] ,color = "lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ax (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Results - Head X Acceleration G')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Compare Head X Acceleration G.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_Head_aDx_G], label =channel_Head_aDx_G)
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ax (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - Head X Acceleration G')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Head X Acceleration G.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_Head_aDx_G], label =channel_Head_aDx_G)
    ax.plot(panzer_data["x" ] /1000 ,panzer_data["Passive X Accel" ] *-1, label ="Panzer Head X Accel.")
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    # ax.plot(average_data[channelt],average_data[Head_Ax_G_19], label =Head_Ax_G_19, color = "red")
    # ax.plot(average_data[channelt],low_data[Head_Ax_G_19],color = "lightpink")
    # ax.plot(average_data[channelt],high_data[Head_Ax_G_19],color = "lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ax (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Panzer Results - Head X Acceleration G')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Compare Panzer Head X Acceleration G.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_Head_aDz_G], label =channel_Head_aDz_G)
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Az (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - Head Z Acceleration G')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Head Z Acceleration G.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_Head_aDz_G], label =channel_Head_aDz_G)
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.plot(average_data[channelt] ,average_data[Head_Az_G_21], label =Head_Az_G_21, color = "red")
    ax.plot(average_data[channelt] ,low_data[Head_Az_G_21] ,color = "lightpink")
    ax.plot(average_data[channelt] ,high_data[Head_Az_G_21] ,color = "lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_ylim(-100, 50)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Az (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Results - Head Z Acceleration G')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Compare Head Z Acceleration G.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_Head_aDz_G], label =channel_Head_aDz_G)
    ax.plot(panzer_data["x" ] /1000 ,panzer_data["Passive Z Accel"], label ="Panzer Head Z Accel.")
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    # ax.plot(average_data[channelt],average_data[Head_Az_G_21], label =Head_Az_G_21, color = "red")
    # ax.plot(average_data[channelt],low_data[Head_Az_G_21],color = "lightpink")
    # ax.plot(average_data[channelt],high_data[Head_Az_G_21],color = "lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_ylim(-100, 50)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Az (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Panzer Results - Head Z Acceleration G')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Compare Panzer Head Z Acceleration G.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    # ax.plot(average_data[channelt],data[channel_Head_Dx_mm], label =channel_Head_Dx_mm)
    ax.plot(data[channelsimt] ,data[channel_Head_aRy_rad_s_s], label =channel_Head_aRy_rad_s_s)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (rad-s-s)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Head Y Rotation Acceleration (rad/s/s)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Simulation Results - Head Y Rotation Accel.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    # ax.plot(average_data[channelt],data[channel_Head_Dx_mm], label =channel_Head_Dx_mm)
    ax.plot(data[channelsimt] ,data[channel_Head_aRy_rad_s_s], label =channel_Head_aRy_rad_s_s)

    ax.plot(average_data[channelt] ,average_data[Head_ao_rad_s_s_23], label =Head_ao_rad_s_s_23, color = "red")
    ax.plot(average_data[channelt] ,low_data[Head_ao_rad_s_s_23] ,color = "lightpink")
    ax.plot(average_data[channelt] ,high_data[Head_ao_rad_s_s_23] ,color = "lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_ylim(-2000, 2500)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (rad-s-s)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Head Y Rotation Acceleration (rad/s/s)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Compare Head Y Rotation Acceleration rad-s-s.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    # ax.plot(average_data[channelt],data[channel_Head_Dx_mm], label =channel_Head_Dx_mm)
    ax.plot(data[channelsimt] ,data[channel_Head_aRy_rad_s_s], label =channel_Head_aRy_rad_s_s)
    ax.plot(panzer_data["x" ] /1000 ,panzer_data["Passive Y Rot. Accel"], label ="Panzer Head Y Rot Accel.")

    # ax.plot(average_data[channelt],average_data[Head_ao_rad_s_s_23], label =Head_ao_rad_s_s_23, color = "red")
    # ax.plot(average_data[channelt],low_data[Head_ao_rad_s_s_23],color = "lightpink")
    # ax.plot(average_data[channelt],high_data[Head_ao_rad_s_s_23],color = "lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_ylim(-5000, 2500)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (rad-s-s)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Panzer Head Y Rotation Acceleration (rad/s/s)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Compare Panzer Head Y Rotation Acceleration rad-s-s.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    # ax.plot(average_data[channelt],data[channel_Head_Dx_mm], label =channel_Head_Dx_mm)
    ax.plot(data[channelsimt] ,data[channel_Head_aRy_rad_s_s], label =channel_Head_aRy_rad_s_s)
    ax.plot(panzer_data["x" ] /1000 ,panzer_data["Passive Y Rot. Accel"], label ="Panzer Head Y Rot Accel.")

    # ax.plot(average_data[channelt],average_data[Head_ao_rad_s_s_23], label =Head_ao_rad_s_s_23, color = "red")
    # ax.plot(average_data[channelt],low_data[Head_ao_rad_s_s_23],color = "lightpink")
    # ax.plot(average_data[channelt],high_data[Head_ao_rad_s_s_23],color = "lightpink")

    ax.set_xlim(0, 0.25)
    # ax.set_ylim(-2000, 2500)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (rad-s-s)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Compare Panzer Head Y Rotation Acceleration (rad/s/s) - NL')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Compare Panzer Head Y Rotation Acceleration rad-s-s - NL.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_T1_Dx_mm], label =channel_T1_Dx_mm)
    # ax.plot(average_data[channelt],data[channel_T1_Ry_deg], label =channel_T1_Ry_deg)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Dx (mm)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - T1 X Displacement (mm)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('T1 X Displacement mm.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    # ax.plot(average_data[channelt],data[channel_T1_Dx_mm], label =channel_T1_Dx_mm)
    ax.plot(data[channelsimt] ,data[channel_T1_Ry_deg], label =channel_T1_Ry_deg)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('T1 Y Rotation (deg)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Simulation Results - T1 Y Rotation deg.png')
    plt.close()
    #######################################################################################################################
    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[Sim_Rel_Head_Dx], label =Sim_Rel_Head_Dx)
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.plot(average_data[channelt] ,average_data[Rel_Head_Dx], label =Rel_Head_Dx, color = "red")
    ax.plot(average_data[channelt] ,low_data[Rel_Head_Dx] ,color = "lightpink")
    ax.plot(average_data[channelt] ,high_data[Rel_Head_Dx] ,color = "lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Dx (mm)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - Rel Head X Displacement (mm)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Rel Head X Displacement mm.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[Sim_Rel_Head_Dz], label =Sim_Rel_Head_Dz)
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.plot(average_data[channelt] ,average_data[Rel_Head_Dz], label ='Rel_Head_Dz', color = "red")
    ax.plot(average_data[channelt] ,low_data[Rel_Head_Dz] ,color = "lightpink")
    ax.plot(average_data[channelt] ,high_data[Rel_Head_Dz] ,color = "lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Dz (mm)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - Rel Head Z Displacement (mm)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Rel Head Z Displacement mm.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    # ax.plot(average_data[channelt],data[channel_Head_Dx_mm], label =channel_Head_Dx_mm)
    ax.plot(data[channelsimt] ,data[Sim_Rel_Head_Ry], label =Sim_Rel_Head_Ry)

    ax.plot(average_data[channelt] ,average_data[Head_ao_deg_23], label ='Head_ao_deg_23', color = "red")
    ax.plot(average_data[channelt] ,low_data[Head_ao_deg_23] ,color = "lightpink")
    ax.plot(average_data[channelt] ,high_data[Head_ao_deg_23] ,color = "lightpink")

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ry (deg)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Rel Head Y Rotation (deg)')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Rel Simulation Results - Head Y Rotation deg.png')
    plt.close()

    # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
    fig ,ax = plt.subplots()
    ax.plot(data[channelsimt] ,data[channel_Head_aDx_G], label =channel_Head_aDx_G)
    # ax.plot(average_data[channelt],data[channel_Head_Ry_deg], label =channel_Head_Ry_deg)

    ax.set_xlim(0, 0.25)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Ax (G)')
    ax.grid(True)
    ax.legend()
    ax.set_title('Simulation Results - Head X Acceleration G')
    plt.subplots_adjust(left = 0.17, bottom = 0.13)
    plt.savefig('Head X Acceleration G.png')
    plt.close()


    # #########################################################################################

    # Create a list of dictionaries to store the subplot information
    subplots = [
        {"row": 0, "col": 0, "title": 'Rel. Head X Disp.', "ylabel": 'Dx (mm)', "data_label": 'Sim_Rel_Head_Dx',
         "data_column": 'Sim_Rel_Head_Dx', "average_data": Rel_Head_Dx},
        {"row": 1, "col": 0, "title": 'Head X Disp.', "ylabel": 'Dx (mm)', "data_label": 'Sim_Head_Dx',
         "data_column": Sim_Head_Dx, "average_data": 'Spine_Dx_mm_int_47'},
        {"row": 0, "col": 1, "title": 'Rel. Head Z Disp.', "ylabel": 'Dz (mm)', "data_label": 'Sim_Rel_Head_Dz',
         "data_column": 'Sim_Rel_Head_Dz', "average_data": 'Head_Dz_mm_int_21'},
        {"row": 1, "col": 1, "title": 'Head Z Disp. (+Rel.)', "ylabel": 'Dz (mm)', "data_label": 'Sim_Rel_Head_Dz',
         "data_column": 'Sim_Rel_Head_Dz', "average_data": 'Head_Dz_mm_int_21'},
        {"row": 0, "col": 2, "title": 'Rel. Head Y Rot.', "ylabel": 'Ry (deg)', "data_label": 'Sim_Rel_Head_Ry',
         "data_column": 'Sim_Rel_Head_Ry', "average_data": None},
        {"row": 1, "col": 2, "title": 'Head Y Rot.', "ylabel": 'Ry (deg)', "data_label": 'Sim_Head_Ry',
         "data_column": Sim_Head_Ry, "average_data": 'Head_ao_deg_23'},
        {"row": 2, "col": 0, "title": 'Head X Vel.', "ylabel": 'Vx (kph)', "data_label": 'Sim_Head_vx',
         "data_column": Sim_Head_vx, "average_data": Head_Vx_kph},
        {"row": 2, "col": 1, "title": 'Head Z Vel.', "ylabel": 'Vz (kph)', "data_label": 'Sim_Head_vz',
         "data_column": Sim_Head_vz, "average_data": Head_Vz_kph},
        {"row": 2, "col": 2, "title": 'Head Y Rot. Vel.', "ylabel": 'wy (rad/s)', "data_label": 'Sim_Head_wy',
         "data_column": Sim_Head_wy, "average_data": Head_wy_rad_s},
        {"row": 3, "col": 0, "title": 'Head X Acc. (G)', "ylabel": 'Ax (G)', "data_label": channel_Head_aDx_G,
         "data_column": channel_Head_aDx_G, "average_data": 'Head_Ax_G_19'},
        {"row": 3, "col": 1, "title": 'Head Z Acc. (G)', "ylabel": 'Az (G)', "data_label": channel_Head_aDz_G,
         "data_column": channel_Head_aDz_G, "average_data": 'Head_Az_G_21'},
        {"row": 3, "col": 2, "title": 'Head Y Rot. Acc. (rad/s/s)', "ylabel": 'Y Rot. Acc. (rad/s/s)',
         "data_label": 'Sim_Head_aRy',
         "data_column": channel_Head_aRy_rad_s_s, "average_data": Head_ao_rad_s_s_23}
    ]

    fig, ax = plt.subplots(4, 3, figsize=(40, 30))
    plt.rcParams['font.size'] = '20'

    for subplot_info in subplots:
        row = subplot_info["row"]
        col = subplot_info["col"]
        title = subplot_info["title"]
        ylabel = subplot_info["ylabel"]
        data_label = subplot_info["data_label"]
        data_column = subplot_info["data_column"]
        average_data_label = subplot_info["average_data"]

        ax[row, col].plot(data[channelsimt], data[data_column], label=data_label)
        if average_data_label:
            ax[row, col].plot(average_data[channelt], average_data[average_data_label], label=average_data_label,
                              color="red")
            ax[row, col].plot(average_data[channelt], low_data[average_data_label], color="lightpink")
            ax[row, col].plot(average_data[channelt], high_data[average_data_label], color="lightpink")

        ax[row, col].set_title(title)
        ax[row, col].set_xlim(0, 0.25)
        ax[row, col].set_xlabel('Time (s)')
        ax[row, col].set_ylabel(ylabel)
        ax[row, col].grid(True)
        ax[row, col].legend()

    plt.tight_layout()
    plt.savefig('Simulation Results Summary - No Limits.png')
    plt.close()

    return