# Import Modules
import os, glob
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

main_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\Original Units\\Compiled Test Data\\"
plot_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\Original Units\\Acceleration Data\\"
# Changing the current working directory
os.chdir(main_path)

path = main_path + "Average.csv"
average_df = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
print(average_df)

path = main_path + "Standard Deviation.csv"
stdev_df = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
# average_df.drop(0, axis=1, inplace=True)
print(stdev_df)

low = average_df-stdev_df
print(low)
# low = low.add_suffix('_low')
high = average_df+stdev_df
# high = high.add_suffix('_high')


channelt = 'Time_s'
channel_Head_Dx_mm_1 = 'Head_Dx_mm_1'#km    #plotted
channel_Head_Dx_mm_2 = 'Head_Dx_mm_2'#km    #plotted
channel_Head_Dy_mm_3 = 'Head_Dy_mm_3'
channel_Head_Dy_mm_4 = 'Head_Dy_mm_4'
channel_Head_Dz_mm_5 = 'Head_Dz_mm_5' #km    #plotted
channel_Head_Dz_mm_6 = 'Head_Dz_mm_6' #km    #plotted
channel_Head_Ro_rad_7 = 'Head_Ro_rad_7' #km    #plotted
channel_Head_Ro_rad_8 = 'Head_Ro_rad_8' #km    #plotted
channel_Head_Ro_rad_9 = 'Head_Ro_rad_9' #km    #plotted
channel_Head_Vx_kph_10 = 'Head_Vx_kph_10'
channel_Head_Vx_kph_11 = 'Head_Vx_kph_11'
channel_Head_Vy_kph_12 = 'Head_Vy_kph_12'
channel_Head_Vy_kph_13 = 'Head_Vy_kph_13'
channel_Head_Vz_kph_14 = 'Head_Vz_kph_14'
channel_Head_Vz_kph_15 = 'Head_Vz_kph_15'
channel_Head_wx_rad_s_16 = 'Head_wx_rad/s_16'
channel_Head_wx_rad_s_17 = 'Head_wx_rad/s_17'
channel_Head_wx_rad_s_18 = 'Head_wx_rad/s_18'
channel_Head_Ax_G_19 = 'Head_Ax_G_19' #km
channel_Head_Ay_G_20 = 'Head_Ay_G_20' #km
channel_Head_Az_G_21 = 'Head_Az_G_21' #km
channel_Head_ao_rad_s_s_22 = 'Head_ao_rad/s^2_22' #km
channel_Head_ao_rad_s_s_23 = 'Head_ao_rad/s^2_23' #km
channel_Head_ao_rad_s_s_24 = 'Head_ao_rad/s^2_24' #km
channel_Head_oo_N_A_25 = 'Head_oo_N/A_25' #km
channel_Head_oo_N_A_26 = 'Head_oo_N/A_26' #km
channel_Head_oo_N_A_27 = 'Head_oo_N/A_27' #km
channel_Head_oo_N_A_28 = 'Head_oo_N/A_28' #km
channel_Spine_Dx_mm_29 = 'Spine_Dx_mm_29' #bc-      #plotted
channel_Spine_Dx_mm_30 = 'Spine_Dx_mm_30'#bc-      #plotted
channel_Spine_Dy_mm_31 = 'Spine_Dy_mm_31'
channel_Spine_Dy_mm_32 = 'Spine_Dy_mm_32'
channel_Spine_Dz_mm_33 = 'Spine_Dz_mm_33'#bc-      #plotted
channel_Spine_Dz_mm_34 = 'Spine_Dz_mm_34'#bc-      #plotted
channel_Spine_Ro_rad_35 = 'Spine_Ro_rad_35' #bc-    #plotted
channel_Spine_Ro_rad_36 = 'Spine_Ro_rad_36'#bc-    #plotted
channel_Spine_Ro_rad_37 = 'Spine_Ro_rad_37'#bc-    #plotted
channel_Spine_Vx_kph_38 = 'Spine_Vx_kph_38'
channel_Spine_Vx_kph_39 = 'Spine_Vx_kph_39'
channel_Spine_Vy_kph_40 = 'Spine_Vy_kph_40'
channel_Spine_Vy_kph_41 = 'Spine_Vy_kph_41'
channel_Spine_Vz_kph_42 = 'Spine_Vz_kph_42'
channel_Spine_Vz_kph_43 = 'Spine_Vz_kph_43'
channel_Spine_wo_rad_s_44 = 'Spine_wo_rad/s_44'
channel_Spine_wo_rad_s_45 = 'Spine_wo_rad/s_45'
channel_Spine_wo_rad_s_46 = 'Spine_wo_rad/s_46'
channel_Spine_Ax_G_47 = 'Spine_Ax_G_47' #bc-
channel_Spine_Ay_G_48 = 'Spine_Ay_G_48'
channel_Spine_Az_G_49 = 'Spine_Az_G_49' #bc-
channel_Spine_ao_rad_s_s_50 = 'Spine_ao_rad/s^2_50' #bc-
channel_Spine_ao_rad_s_s_51 = 'Spine_ao_rad/s^2_51' #bc-
channel_Spine_ao_rad_s_s_52 = 'Spine_ao_rad/s^2_52' #bc-
channel_Spine_oo_N_A_53 = 'Spine_oo_N/A_53' #bc-
channel_Spine_oo_N_A_54 = 'Spine_oo_N/A_54' #bc-
channel_Spine_oo_N_A_55 = 'Spine_oo_N/A_55' #bc-
channel_Spine_oo_N_A_56 = 'Spine_oo_N/A_56' #bc-
channel_Sled_Ax_G_57 = 'Sled_Ax_G_57' #sled
channel_Sled_Vx_kph_58 = 'Sled_Vx_kph_58' #sled
channel_Sled_Dx_mm_59 = 'Sled_Dx_mm_59' #sled
channel_Head_Dx_mm_60 = 'Head_Dx_mm_60' #km     #plotted
channel_Head_Dy_mm_61 = 'Head_Dy_mm_61'
channel_Head_Dz_mm_62 = 'Head_Dz_mm_62' #km    #plotted
channel_Head_Ro_rad_63 = 'Head_Ro_rad_63' #km    #plotted
channel_Head_Ro_rad_64 = 'Head_Ro_rad_64'#km    #plotted
channel_Head_Ro_rad_65 = 'Head_Ro_rad_65'#km    #plotted
channel_Head_Vx_kph_66 = 'Head_Vx_kph_66'
channel_Head_Vy_kph_67 = 'Head_Vy_kph_67'
channel_Head_Vz_kph_68 = 'Head_Vz_kph_68'
channel_Head_wx_rad_s_69 = 'Head_wx_rad/s_69'
channel_Head_wx_rad_s_70 = 'Head_wx_rad/s_70'
channel_Head_wx_rad_s_71 = 'Head_wx_rad/s_71'
channel_Head_oo_N_A_72 = 'Head_oo_N/A_72'
channel_Head_oo_N_A_73 = 'Head_oo_N/A_73'
channel_Head_oo_N_A_74 = 'Head_oo_N/A_74'
channel_Head_oo_N_A_75 = 'Head_oo_N/A_75'
channel_Spine_Dx_mm_76 = 'Spine_Dx_mm_76' #bc-      #plotted
channel_Spine_Dy_mm_77 = 'Spine_Dy_mm_77'
channel_Spine_Dz_mm_78 = 'Spine_Dz_mm_78'#bc-      #plotted
channel_Spine_Ro_rad_79 = 'Spine_Ro_rad_79'#bc-     #plotted
channel_Spine_Ro_rad_80 = 'Spine_Ro_rad_80'#bc-    #plotted
channel_Spine_Ro_rad_81 = 'Spine_Ro_rad_81'#bc-    #plotted
channel_Spine_Vx_kph_82 = 'Spine_Vx_kph_82'
channel_Spine_Vy_kph_83 = 'Spine_Vy_kph_83'
channel_Spine_Vz_kph_84 = 'Spine_Vz_kph_84'
channel_Spine_wo_rad_s_s_85 = 'Spine_wo_rad/s^2_85'
channel_Spine_wo_rad_s_s_86 = 'Spine_wo_rad/s^2_86'
channel_Spine_wo_rad_s_s_87 = 'Spine_wo_rad/s^2_87'
channel_Spine_oo_N_A_88 = 'Spine_oo_N/A_88' #bc-
channel_Spine_oo_N_A_89 = 'Spine_oo_N/A_89'#bc-
channel_Spine_oo_N_A_90 = 'Spine_oo_N/A_90'#bc-
channel_Spine_oo_N_A_91 = 'Spine_oo_N/A_91'#bc-

os.chdir(plot_path)
import matplotlib as mpl
import matplotlib.pyplot as plt

##############################################################################################################

#Plot Head Acceleration (G) - C19-20-21

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ax_G_19], label =channel_Head_Ax_G_19)
ax.plot(average_df[channelt],average_df[channel_Head_Ay_G_20], label =channel_Head_Ay_G_20)
ax.plot(average_df[channelt],average_df[channel_Head_Az_G_21], label =channel_Head_Az_G_21)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (G)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Y Z Acceleration (G)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Y Z Acceleration G - Summary - C19-20-21.png')
plt.show()

#Plot Head X Acceleration (G) - C19

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ax_G_19], label =channel_Head_Ax_G_19)

ax.plot(average_df[channelt],low[channel_Head_Ax_G_19], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ax_G_19], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (G)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Acceleration (G)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Acceleration G - C19.png')
plt.show()

#Plot Head Y Acceleration (G) - C20

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ay_G_20], label =channel_Head_Ay_G_20)

ax.plot(average_df[channelt],low[channel_Head_Ay_G_20], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ay_G_20], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (G)')
ax.grid(True)
ax.legend()
ax.set_title('Head Y Acceleration (G)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Y Acceleration G - C20.png')
plt.show()


#Plot Head Z Acceleration (G) - C21

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Az_G_21], label =channel_Head_Az_G_21)

ax.plot(average_df[channelt],low[channel_Head_Az_G_21], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Az_G_21], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (G)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Acceleration (G)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Acceleration G - C21.png')
plt.show()

##############################################################################################################

#Plot Head Angular Acceleration (rad/s/s) - C22-23-24

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_ao_rad_s_s_22], label =channel_Head_ao_rad_s_s_22)
ax.plot(average_df[channelt],average_df[channel_Head_ao_rad_s_s_23], label =channel_Head_ao_rad_s_s_23)
ax.plot(average_df[channelt],average_df[channel_Head_ao_rad_s_s_24], label =channel_Head_ao_rad_s_s_24)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Acceleration (rad/S^2)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Angular Acceleration (rad/s^2)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Angular Acceleration rad_s_s - Summary - C22-23-24.png')
plt.show()

#Plot Head Angular Acceleration (rad/s/s) - C22

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_ao_rad_s_s_22], label =channel_Head_ao_rad_s_s_22)

ax.plot(average_df[channelt],low[channel_Head_ao_rad_s_s_22], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_ao_rad_s_s_22], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Acceleration (rad/S^2)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Angular Acceleration (rad/s^2)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Angular Acceleration rad_s_s - C22.png')
plt.show()

#Plot Head Angular Acceleration (rad/s/s) - C23

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_ao_rad_s_s_23], label =channel_Head_ao_rad_s_s_23)

ax.plot(average_df[channelt],low[channel_Head_ao_rad_s_s_23], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_ao_rad_s_s_23], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Acceleration (rad/S^2)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Angular Acceleration (rad/s^2)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Angular Acceleration rad_s_s - C23.png')
plt.show()

#Plot Head Angular Acceleration (rad/s/s) - C24

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_ao_rad_s_s_24], label =channel_Head_ao_rad_s_s_24)

ax.plot(average_df[channelt],low[channel_Head_ao_rad_s_s_24], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_ao_rad_s_s_24], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Acceleration (rad/S^2)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Angular Acceleration (rad/s^2)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Angular Acceleration rad_s_s - C24.png')
plt.show()

##############################################################################################################

#Plot Head Other N/A (N/A) - C25-26-27-28

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_oo_N_A_25], label =channel_Head_oo_N_A_25)
ax.plot(average_df[channelt],average_df[channel_Head_oo_N_A_26], label =channel_Head_oo_N_A_26)
ax.plot(average_df[channelt],average_df[channel_Head_oo_N_A_27], label =channel_Head_oo_N_A_27)
ax.plot(average_df[channelt],average_df[channel_Head_oo_N_A_28], label =channel_Head_oo_N_A_28)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('N/A (N/A)')
ax.grid(True)
ax.legend()
ax.set_title('Head Other N/A (N/A)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Other N-A - Summary - C25-26-27-28.png')
plt.show()

##############################################################################################################
##############################################################################################################

#Plot Spine Acceleration (G) - C47-48-49

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ax_G_47], label =channel_Spine_Ax_G_47)
ax.plot(average_df[channelt],average_df[channel_Spine_Ay_G_48], label =channel_Spine_Ay_G_48)
ax.plot(average_df[channelt],average_df[channel_Spine_Az_G_49], label =channel_Spine_Az_G_49)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (G)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Y Z Acceleration (G)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Y Z Acceleration G - Summary - C47-48-49.png')
plt.show()

#Plot Spine X Acceleration (G) - C47

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ax_G_47], label =channel_Spine_Ax_G_47)

ax.plot(average_df[channelt],low[channel_Spine_Ax_G_47], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ax_G_47], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (G)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Acceleration (G)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Acceleration G - C47.png')
plt.show()


#Plot Spine Y Acceleration (G) - C48

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ay_G_48], label =channel_Spine_Ay_G_48)

ax.plot(average_df[channelt],low[channel_Spine_Ay_G_48], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ay_G_48], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (G)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Y Acceleration (G)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Y Acceleration G - C48.png')
plt.show()


#Plot Spine Z Acceleration (G) - C49

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Az_G_49], label =channel_Spine_Az_G_49)

ax.plot(average_df[channelt],low[channel_Spine_Az_G_49], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Az_G_49], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (G)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Acceleration (G)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Acceleration G - C49.png')
plt.show()

##############################################################################################################

#Plot Spine Angular Acceleration (rad/s/s) - C50-51-52

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_ao_rad_s_s_50], label =channel_Spine_ao_rad_s_s_50)
ax.plot(average_df[channelt],average_df[channel_Spine_ao_rad_s_s_51], label =channel_Spine_ao_rad_s_s_51)
ax.plot(average_df[channelt],average_df[channel_Spine_ao_rad_s_s_52], label =channel_Spine_ao_rad_s_s_52)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Acceleration (rad/S^2)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Angular Acceleration (rad/s^2)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Angular Acceleration rad_s_s - Summary - C50-51-52.png')
plt.show()

#Plot Spine Angular Acceleration (rad/s/s) - C50

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_ao_rad_s_s_50], label =channel_Spine_ao_rad_s_s_50)

ax.plot(average_df[channelt],low[channel_Spine_ao_rad_s_s_50], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_ao_rad_s_s_50], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Acceleration (rad/S^2)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Angular Acceleration (rad/s^2)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Angular Acceleration rad_s_s - C50.png')
plt.show()

#Plot Spine Angular Acceleration (rad/s/s) - C51

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_ao_rad_s_s_51], label =channel_Spine_ao_rad_s_s_51)

ax.plot(average_df[channelt],low[channel_Spine_ao_rad_s_s_51], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_ao_rad_s_s_51], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Acceleration (rad/S^2)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Angular Acceleration (rad/s^2)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Angular Acceleration rad_s_s - C51.png')
plt.show()

#Plot Spine Angular Acceleration (rad/s/s) - C52

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_ao_rad_s_s_52], label =channel_Spine_ao_rad_s_s_52)

ax.plot(average_df[channelt],low[channel_Spine_ao_rad_s_s_52], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_ao_rad_s_s_52], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Acceleration (rad/S^2)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Angular Acceleration (rad/s^2)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Angular Acceleration rad_s_s - C52.png')
plt.show()

##############################################################################################################

#Plot Spine Other N/A (N/A) - C53-54-55-56

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_oo_N_A_53], label =channel_Spine_oo_N_A_53)
ax.plot(average_df[channelt],average_df[channel_Spine_oo_N_A_54], label =channel_Spine_oo_N_A_54)
ax.plot(average_df[channelt],average_df[channel_Spine_oo_N_A_55], label =channel_Spine_oo_N_A_55)
ax.plot(average_df[channelt],average_df[channel_Spine_oo_N_A_56], label =channel_Spine_oo_N_A_56)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('N/A (N/A)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Other N/A (N/A)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Other N-A - Summary - C53-54-55-56.png')
plt.show()

#Plot Spine Other N/A (N/A) - C88-89-90-91

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_oo_N_A_88], label =channel_Spine_oo_N_A_88)
ax.plot(average_df[channelt],average_df[channel_Spine_oo_N_A_89], label =channel_Spine_oo_N_A_89)
ax.plot(average_df[channelt],average_df[channel_Spine_oo_N_A_90], label =channel_Spine_oo_N_A_90)
ax.plot(average_df[channelt],average_df[channel_Spine_oo_N_A_91], label =channel_Spine_oo_N_A_91)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('N/A (N/A)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Other N/A (N/A)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Other N-A - Summary - C88-89-90-91.png')
plt.show()
##############################################################################################################
##############################################################################################################

#Plot Sled X Acceleration (G) - C57

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Sled_Ax_G_57], label =channel_Sled_Ax_G_57)

ax.plot(average_df[channelt],low[channel_Sled_Ax_G_57], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Sled_Ax_G_57], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (G)')
ax.grid(True)
ax.legend()
ax.set_title('Sled X Acceleration (G)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Sled X Acceleration G - C57.png')
plt.show()

#Plot Sled X Velocity (kph) - C58

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Sled_Vx_kph_58], label =channel_Sled_Vx_kph_58)

ax.plot(average_df[channelt],low[channel_Sled_Vx_kph_58], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Sled_Vx_kph_58], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Velocity (kph)')
ax.grid(True)
ax.legend()
ax.set_title('Sled X Velocity (kph)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Sled X Velocity kph - C58.png')
plt.show()

#Plot Sled X Displacement (mm) - C59

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Sled_Dx_mm_59], label =channel_Sled_Dx_mm_59)

ax.plot(average_df[channelt],low[channel_Sled_Dx_mm_59], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Sled_Dx_mm_59], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Displacement (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Sled X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Sled X Displacement mm - C59.png')
plt.show()

##############################################################################################################
##############################################################################################################

#Plot Sled Acceleration (G) - C57-47-19

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Sled_Ax_G_57], label =channel_Sled_Ax_G_57)
ax.plot(average_df[channelt],average_df[channel_Spine_Ax_G_47], label =channel_Spine_Ax_G_47)
ax.plot(average_df[channelt],average_df[channel_Head_Ax_G_19], label =channel_Head_Ax_G_19)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (G)')
ax.grid(True)
ax.legend()
ax.set_title('Sled, Spine, & Head X Acceleration (G)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('X Acceleration G - Summary - C57-47-19.png')
plt.show()