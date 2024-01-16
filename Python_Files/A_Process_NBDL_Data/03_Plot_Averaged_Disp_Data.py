# Import Modules
import os, glob
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

main_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\Original Units\\Compiled Test Data\\"
plot_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\Original Units\\Displacement Data\\"
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

#Plot Head X Displacement (mm) - C1-2-60

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_1], label =channel_Head_Dx_mm_1)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_2], label =channel_Head_Dx_mm_2)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_60], label =channel_Head_Dx_mm_60)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement mm - Summary - C1-2-60.png')
plt.show()

#Plot Head X Displacement (mm) - C1-2

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_1], label =channel_Head_Dx_mm_1)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_2], label =channel_Head_Dx_mm_2)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_60], label =channel_Head_Dx_mm_60)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement mm - Compare - C1-2.png')
plt.show()

#Plot Head X Displacement (mm) - C1-60

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_1], label =channel_Head_Dx_mm_1)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_2], label =channel_Head_Dx_mm_2)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_60], label =channel_Head_Dx_mm_60)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement mm - Compare - C1-60.png')
plt.show()

#Plot Head X Displacement (mm) - C2-60

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_1], label =channel_Head_Dx_mm_1)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_2], label =channel_Head_Dx_mm_2)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_60], label =channel_Head_Dx_mm_60)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement mm - Compare - C2-60.png')
plt.show()

#Plot Head X Displacement (mm) - C1

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_1], label =channel_Head_Dx_mm_1)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_2], label =channel_Head_Dx_mm_2)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_60], label =channel_Head_Dx_mm_60)

ax.plot(average_df[channelt],low[channel_Head_Dx_mm_1],color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dx_mm_1],color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement mm - C1.png')
plt.show()

#Plot Head X Displacement (mm) - C2

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_1], label =channel_Head_Dx_mm_1)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_2], label =channel_Head_Dx_mm_2)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_60], label =channel_Head_Dx_mm_60)

ax.plot(average_df[channelt],low[channel_Head_Dx_mm_2],color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dx_mm_2],color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement mm - C2.png')
plt.show()

#Plot Head X Displacement (mm) - C60

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_1], label =channel_Head_Dx_mm_1)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_2], label =channel_Head_Dx_mm_2)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_mm_60], label =channel_Head_Dx_mm_60)

ax.plot(average_df[channelt],low[channel_Head_Dx_mm_60], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dx_mm_60], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement mm - C60.png')
plt.show()

##############################################################################################################


#Plot Head Z Displacement (mm) - C5-6-62

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_5], label =channel_Head_Dz_mm_5)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_6], label =channel_Head_Dz_mm_6)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_62], label =channel_Head_Dz_mm_62)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement mm - Summary - C5-6-62.png')
plt.show()

#Plot Head Z Displacement (mm) - C5-6

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_5], label =channel_Head_Dz_mm_5)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_6], label =channel_Head_Dz_mm_6)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_62], label =channel_Head_Dz_mm_62)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement mm - Compare - C5-6.png')
plt.show()

#Plot Head Z Displacement (mm) - C5-62

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_5], label =channel_Head_Dz_mm_5)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_6], label =channel_Head_Dz_mm_6)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_62], label =channel_Head_Dz_mm_62)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement mm - Compare - C5-62.png')
plt.show()

#Plot Head Z Displacement (mm) - C6-62

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_5], label =channel_Head_Dz_mm_5)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_6], label =channel_Head_Dz_mm_6)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_62], label =channel_Head_Dz_mm_62)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement mm - Compare - C6-62.png')
plt.show()

#Plot Head Z Displacement (mm) - C5

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_5], label =channel_Head_Dz_mm_5)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_6], label =channel_Head_Dz_mm_6)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_62], label =channel_Head_Dz_mm_62)

ax.plot(average_df[channelt],low[channel_Head_Dz_mm_5], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dz_mm_5], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement mm - C5.png')
plt.show()

#Plot Head Z Displacement (mm) - C6

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_5], label =channel_Head_Dz_mm_5)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_6], label =channel_Head_Dz_mm_6)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_62], label =channel_Head_Dz_mm_62)

ax.plot(average_df[channelt],low[channel_Head_Dz_mm_6], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dz_mm_6], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement mm - C6.png')
plt.show()

#Plot Head Z Displacement (mm) - C62

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_5], label =channel_Head_Dz_mm_5)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_6], label =channel_Head_Dz_mm_6)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_mm_62], label =channel_Head_Dz_mm_62)

ax.plot(average_df[channelt],low[channel_Head_Dz_mm_62], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dz_mm_62], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement mm - C62.png')
plt.show()

##############################################################################################################
##############################################################################################################

#Plot Spine X Displacement (mm) - C29-30-76

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_29], label =channel_Spine_Dx_mm_29)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_30], label =channel_Spine_Dx_mm_30)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_76], label =channel_Spine_Dx_mm_76)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement mm - Summary - C29-30-76.png')
plt.show()

#Plot Spine X Displacement (mm) - C29-30

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_29], label =channel_Spine_Dx_mm_29)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_30], label =channel_Spine_Dx_mm_30)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_76], label =channel_Spine_Dx_mm_76)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement mm - Compare - C29-30.png')
plt.show()

#Plot Spine X Displacement (mm) - C29-76

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_29], label =channel_Spine_Dx_mm_29)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_30], label =channel_Spine_Dx_mm_30)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_76], label =channel_Spine_Dx_mm_76)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement mm - Compare - C29-76.png')
plt.show()

#Plot Spine X Displacement (mm) - C30-76

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_29], label =channel_Spine_Dx_mm_29)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_30], label =channel_Spine_Dx_mm_30)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_76], label =channel_Spine_Dx_mm_76)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement mm - Compare - C30-76.png')
plt.show()

#Plot Spine X Displacement (mm) - C29

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_29], label =channel_Spine_Dx_mm_29)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_30], label =channel_Spine_Dx_mm_30)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_76], label =channel_Spine_Dx_mm_76)

ax.plot(average_df[channelt],low[channel_Spine_Dx_mm_29], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dx_mm_29], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement mm - C29')
plt.show()

#Plot Spine X Displacement (mm) - C30

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_29], label =channel_Spine_Dx_mm_29)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_30], label =channel_Spine_Dx_mm_30)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_76], label =channel_Spine_Dx_mm_76)

ax.plot(average_df[channelt],low[channel_Spine_Dx_mm_30], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dx_mm_30], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement mm - C30.png')
plt.show()

#Plot Spine X Displacement (mm) - C76

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_29], label =channel_Spine_Dx_mm_29)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_30], label =channel_Spine_Dx_mm_30)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_mm_76], label =channel_Spine_Dx_mm_76)

ax.plot(average_df[channelt],low[channel_Spine_Dx_mm_76], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dx_mm_76], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement mm - C76.png')
plt.show()

##############################################################################################################


#Plot Spine Z Displacement (mm) - C33-34-78

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_33], label =channel_Spine_Dz_mm_33)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_34], label =channel_Spine_Dz_mm_34)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_78], label =channel_Spine_Dz_mm_78)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement mm - Summary - C33-34-78.png')
plt.show()

#Plot Spine Z Displacement (mm) - C33-34

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_33], label =channel_Spine_Dz_mm_33)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_34], label =channel_Spine_Dz_mm_34)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_78], label =channel_Spine_Dz_mm_78)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement mm - Compare - C33-34.png')
plt.show()

#Plot Spine Z Displacement (mm) - C33-78

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_33], label =channel_Spine_Dz_mm_33)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_34], label =channel_Spine_Dz_mm_34)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_78], label =channel_Spine_Dz_mm_78)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement mm - Compare - C33-78.png')
plt.show()

#Plot Spine Z Displacement (mm) - C34-78

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_33], label =channel_Spine_Dz_mm_33)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_34], label =channel_Spine_Dz_mm_34)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_78], label =channel_Spine_Dz_mm_78)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement mm - Compare - C34-78.png')
plt.show()

#Plot Spine Z Displacement (mm) - C33

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_33], label =channel_Spine_Dz_mm_33)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_34], label =channel_Spine_Dz_mm_34)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_78], label =channel_Spine_Dz_mm_78)

ax.plot(average_df[channelt],low[channel_Spine_Dz_mm_33], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dz_mm_33], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement mm - C33.png')
plt.show()

#Plot Spine Z Displacement (mm) - C34

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_33], label =channel_Spine_Dz_mm_33)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_34], label =channel_Spine_Dz_mm_34)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_78], label =channel_Spine_Dz_mm_78)

ax.plot(average_df[channelt],low[channel_Spine_Dz_mm_34], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dz_mm_34], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement mm - C34.png')
plt.show()

#Plot Spine Z Displacement (mm) - C78

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_33], label =channel_Spine_Dz_mm_33)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_34], label =channel_Spine_Dz_mm_34)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_mm_78], label =channel_Spine_Dz_mm_78)

ax.plot(average_df[channelt],low[channel_Spine_Dz_mm_78], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dz_mm_78], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement mm - C78.png')
plt.show()

##############################################################################################################
##############################################################################################################
##############################################################################################################

#Plot Head NA Rotation (rad) - C7-8-9

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_7], label =channel_Head_Ro_rad_7)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_8], label =channel_Head_Ro_rad_8)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_9], label =channel_Head_Ro_rad_9)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - Summary - C7-8-9.png')
plt.show()

#Plot Head NA Rotation (rad) - C7-8

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_7], label =channel_Head_Ro_rad_7)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_8], label =channel_Head_Ro_rad_8)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_9], label =channel_Head_Ro_rad_9)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - Compare - C7-8.png')
plt.show()

#Plot Head NA Rotation (rad) - C7-9

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_7], label =channel_Head_Ro_rad_7)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_8], label =channel_Head_Ro_rad_8)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_9], label =channel_Head_Ro_rad_9)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - Compare - C7-9.png')
plt.show()

#Plot Head NA Rotation (rad) - C8-9

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_7], label =channel_Head_Ro_rad_7)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_8], label =channel_Head_Ro_rad_8)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_9], label =channel_Head_Ro_rad_9)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - Compare - C8-9.png')
plt.show()

#Plot Head NA Rotation (rad) - C7

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_7], label =channel_Head_Ro_rad_7)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_8], label =channel_Head_Ro_rad_8)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_9], label =channel_Head_Ro_rad_9)

ax.plot(average_df[channelt],low[channel_Head_Ro_rad_7], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_rad_7], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - C7.png')
plt.show()

#Plot Head NA Rotation (rad) - C8

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_7], label =channel_Head_Ro_rad_7)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_8], label =channel_Head_Ro_rad_8)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_9], label =channel_Head_Ro_rad_9)

ax.plot(average_df[channelt],low[channel_Head_Ro_rad_8], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_rad_8], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - C8.png')
plt.show()

#Plot Head NA Rotation (rad) - C9

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_7], label =channel_Head_Ro_rad_7)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_8], label =channel_Head_Ro_rad_8)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_9], label =channel_Head_Ro_rad_9)

ax.plot(average_df[channelt],low[channel_Head_Ro_rad_9], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_rad_9], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - C9.png')
plt.show()

##############################################################################################################

#Plot Head NA Rotation (rad) - C63-64-65

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_63], label =channel_Head_Ro_rad_63)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_64], label =channel_Head_Ro_rad_64)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_65], label =channel_Head_Ro_rad_65)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - Summary - C63-64-65.png')
plt.show()

#Plot Head NA Rotation (rad) - C63-64

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_63], label =channel_Head_Ro_rad_63)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_64], label =channel_Head_Ro_rad_64)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_65], label =channel_Head_Ro_rad_65)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - Compare - C63-64.png')
plt.show()

#Plot Head NA Rotation (rad) - C63-65

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_63], label =channel_Head_Ro_rad_63)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_64], label =channel_Head_Ro_rad_64)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_65], label =channel_Head_Ro_rad_65)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - Compare - C63-65.png')
plt.show()

#Plot Head NA Rotation (rad) - C64-65

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_63], label =channel_Head_Ro_rad_63)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_64], label =channel_Head_Ro_rad_64)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_65], label =channel_Head_Ro_rad_65)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - Compare - C64-65.png')
plt.show()

#Plot Head NA Rotation (rad) - C63

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_63], label =channel_Head_Ro_rad_63)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_64], label =channel_Head_Ro_rad_64)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_65], label =channel_Head_Ro_rad_65)

ax.plot(average_df[channelt],low[channel_Head_Ro_rad_63], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_rad_63], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - C63.png')
plt.show()

#Plot Head NA Rotation (rad) - C64

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_63], label =channel_Head_Ro_rad_63)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_64], label =channel_Head_Ro_rad_64)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_65], label =channel_Head_Ro_rad_65)

ax.plot(average_df[channelt],low[channel_Head_Ro_rad_64], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_rad_64], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - C64.png')
plt.show()

#Plot Head NA Rotation (rad) - C65

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_63], label =channel_Head_Ro_rad_63)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_64], label =channel_Head_Ro_rad_64)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_rad_65], label =channel_Head_Ro_rad_65)

ax.plot(average_df[channelt],low[channel_Head_Ro_rad_65], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_rad_65], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation rad - C65.png')
plt.show()

##############################################################################################################
##############################################################################################################


#Plot Spine NA Rotation (rad) - C35-36-37

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_35], label =channel_Spine_Ro_rad_35)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_36], label =channel_Spine_Ro_rad_36)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_37], label =channel_Spine_Ro_rad_37)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - Summary - C35-36-37.png')
plt.show()

#Plot Spine NA Rotation (rad) - C35-36

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_35], label =channel_Spine_Ro_rad_35)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_36], label =channel_Spine_Ro_rad_36)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_37], label =channel_Spine_Ro_rad_37)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - Compare - C35-36.png')
plt.show()

#Plot Spine NA Rotation (rad) - C35-37

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_35], label =channel_Spine_Ro_rad_35)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_36], label =channel_Spine_Ro_rad_36)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_37], label =channel_Spine_Ro_rad_37)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - Compare - C35-37.png')
plt.show()

#Plot Spine NA Rotation (rad) - C36-37

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_35], label =channel_Spine_Ro_rad_35)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_36], label =channel_Spine_Ro_rad_36)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_37], label =channel_Spine_Ro_rad_37)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - Compare - C36-37.png')
plt.show()

#Plot Spine NA Rotation (rad) - C35

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_35], label =channel_Spine_Ro_rad_35)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_36], label =channel_Spine_Ro_rad_36)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_37], label =channel_Spine_Ro_rad_37)

ax.plot(average_df[channelt],low[channel_Spine_Ro_rad_35], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_rad_35], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - C35.png')
plt.show()

#Plot Spine NA Rotation (rad) - C36

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_35], label =channel_Spine_Ro_rad_35)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_36], label =channel_Spine_Ro_rad_36)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_37], label =channel_Spine_Ro_rad_37)

ax.plot(average_df[channelt],low[channel_Spine_Ro_rad_36], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_rad_36], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - C36.png')
plt.show()

#Plot Spine NA Rotation (rad) - C37

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_35], label =channel_Spine_Ro_rad_35)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_36], label =channel_Spine_Ro_rad_36)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_37], label =channel_Spine_Ro_rad_37)

ax.plot(average_df[channelt],low[channel_Spine_Ro_rad_37], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_rad_37], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - C37.png')
plt.show()

##############################################################################################################

#Plot Spine NA Rotation (rad) - C79-80-81

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_79], label =channel_Spine_Ro_rad_79)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_80], label =channel_Spine_Ro_rad_80)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_81], label =channel_Spine_Ro_rad_81)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - Summary - C79-80-81.png')
plt.show()

#Plot Spine NA Rotation (rad) - C79-80

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_79], label =channel_Spine_Ro_rad_79)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_80], label =channel_Spine_Ro_rad_80)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_81], label =channel_Spine_Ro_rad_81)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - Compare - C79-80.png')
plt.show()

#Plot Spine NA Rotation (rad) - C79-81

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_79], label =channel_Spine_Ro_rad_79)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_80], label =channel_Spine_Ro_rad_80)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_81], label =channel_Spine_Ro_rad_81)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - Compare - C79-81.png')
plt.show()

#Plot Spine NA Rotation (rad) - C80-81

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_79], label =channel_Spine_Ro_rad_79)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_80], label =channel_Spine_Ro_rad_80)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_81], label =channel_Spine_Ro_rad_81)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - Compare - C80-81.png')
plt.show()

#Plot Spine NA Rotation (rad) - C79

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_79], label =channel_Spine_Ro_rad_79)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_80], label =channel_Spine_Ro_rad_80)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_81], label =channel_Spine_Ro_rad_81)

ax.plot(average_df[channelt],low[channel_Spine_Ro_rad_79], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_rad_79], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - C79.png')
plt.show()

#Plot Spine NA Rotation (rad) - C80

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_79], label =channel_Spine_Ro_rad_79)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_80], label =channel_Spine_Ro_rad_80)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_81], label =channel_Spine_Ro_rad_81)

ax.plot(average_df[channelt],low[channel_Spine_Ro_rad_80], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_rad_80], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - C80.png')
plt.show()

#Plot Spine NA Rotation (rad) - C81

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_79], label =channel_Spine_Ro_rad_79)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_80], label =channel_Spine_Ro_rad_80)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_rad_81], label =channel_Spine_Ro_rad_81)

ax.plot(average_df[channelt],low[channel_Spine_Ro_rad_81], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_rad_81], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (rad)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (rad)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation rad - C81.png')
plt.show()

##############################################################################################################