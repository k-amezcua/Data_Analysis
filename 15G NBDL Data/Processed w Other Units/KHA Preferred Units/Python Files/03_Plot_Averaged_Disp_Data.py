# Import Modules
import os, glob
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

main_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\KHA Preferred Units\\Compiled Test Data\\"
plot_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\KHA Preferred Units\\Displacement Data\\"
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
channel_Head_Dx_in_1 = 'Head_Dx_in_1'#km    #plotted
channel_Head_Dx_in_2 = 'Head_Dx_in_2'#km    #plotted
channel_Head_Dy_in_3 = 'Head_Dy_in_3'
channel_Head_Dy_in_4 = 'Head_Dy_in_4'
channel_Head_Dz_in_5 = 'Head_Dz_in_5' #km    #plotted
channel_Head_Dz_in_6 = 'Head_Dz_in_6' #km    #plotted
channel_Head_Ro_deg_7 = 'Head_Ro_deg_7' #km    #plotted
channel_Head_Ro_deg_8 = 'Head_Ro_deg_8' #km    #plotted
channel_Head_Ro_deg_9 = 'Head_Ro_deg_9' #km    #plotted
channel_Head_Vx_mph_10 = 'Head_Vx_mph_10'
channel_Head_Vx_mph_11 = 'Head_Vx_mph_11'
channel_Head_Vy_mph_12 = 'Head_Vy_mph_12'
channel_Head_Vy_mph_13 = 'Head_Vy_mph_13'
channel_Head_Vz_mph_14 = 'Head_Vz_mph_14'
channel_Head_Vz_mph_15 = 'Head_Vz_mph_15'
channel_Head_wx_deg_s_16 = 'Head_wx_deg/s_16'
channel_Head_wx_deg_s_17 = 'Head_wx_deg/s_17'
channel_Head_wx_deg_s_18 = 'Head_wx_deg/s_18'
channel_Head_Ax_G_19 = 'Head_Ax_G_19' #km
channel_Head_Ay_G_20 = 'Head_Ay_G_20' #km
channel_Head_Az_G_21 = 'Head_Az_G_21' #km
channel_Head_ao_deg_s_s_22 = 'Head_ao_deg/s^2_22' #km
channel_Head_ao_deg_s_s_23 = 'Head_ao_deg/s^2_23' #km
channel_Head_ao_deg_s_s_24 = 'Head_ao_deg/s^2_24' #km
channel_Head_oo_N_A_25 = 'Head_oo_N/A_25' #km
channel_Head_oo_N_A_26 = 'Head_oo_N/A_26' #km
channel_Head_oo_N_A_27 = 'Head_oo_N/A_27' #km
channel_Head_oo_N_A_28 = 'Head_oo_N/A_28' #km
channel_Spine_Dx_in_29 = 'Spine_Dx_in_29' #bc-      #plotted
channel_Spine_Dx_in_30 = 'Spine_Dx_in_30'#bc-      #plotted
channel_Spine_Dy_in_31 = 'Spine_Dy_in_31'
channel_Spine_Dy_in_32 = 'Spine_Dy_in_32'
channel_Spine_Dz_in_33 = 'Spine_Dz_in_33'#bc-      #plotted
channel_Spine_Dz_in_34 = 'Spine_Dz_in_34'#bc-      #plotted
channel_Spine_Ro_deg_35 = 'Spine_Ro_deg_35' #bc-    #plotted
channel_Spine_Ro_deg_36 = 'Spine_Ro_deg_36'#bc-    #plotted
channel_Spine_Ro_deg_37 = 'Spine_Ro_deg_37'#bc-    #plotted
channel_Spine_Vx_mph_38 = 'Spine_Vx_mph_38'
channel_Spine_Vx_mph_39 = 'Spine_Vx_mph_39'
channel_Spine_Vy_mph_40 = 'Spine_Vy_mph_40'
channel_Spine_Vy_mph_41 = 'Spine_Vy_mph_41'
channel_Spine_Vz_mph_42 = 'Spine_Vz_mph_42'
channel_Spine_Vz_mph_43 = 'Spine_Vz_mph_43'
channel_Spine_wo_deg_s_44 = 'Spine_wo_deg/s_44'
channel_Spine_wo_deg_s_45 = 'Spine_wo_deg/s_45'
channel_Spine_wo_deg_s_46 = 'Spine_wo_deg/s_46'
channel_Spine_Ax_G_47 = 'Spine_Ax_G_47' #bc-
channel_Spine_Ay_G_48 = 'Spine_Ay_G_48'
channel_Spine_Az_G_49 = 'Spine_Az_G_49' #bc-
channel_Spine_ao_deg_s_s_50 = 'Spine_ao_deg/s^2_50' #bc-
channel_Spine_ao_deg_s_s_51 = 'Spine_ao_deg/s^2_51' #bc-
channel_Spine_ao_deg_s_s_52 = 'Spine_ao_deg/s^2_52' #bc-
channel_Spine_oo_N_A_53 = 'Spine_oo_N/A_53' #bc-
channel_Spine_oo_N_A_54 = 'Spine_oo_N/A_54' #bc-
channel_Spine_oo_N_A_55 = 'Spine_oo_N/A_55' #bc-
channel_Spine_oo_N_A_56 = 'Spine_oo_N/A_56' #bc-
channel_Sled_Ax_G_57 = 'Sled_Ax_G_57' #sled
channel_Sled_Vx_mph_58 = 'Sled_Vx_mph_58' #sled
channel_Sled_Dx_in_59 = 'Sled_Dx_in_59' #sled
channel_Head_Dx_in_60 = 'Head_Dx_in_60' #km     #plotted
channel_Head_Dy_in_61 = 'Head_Dy_in_61'
channel_Head_Dz_in_62 = 'Head_Dz_in_62' #km    #plotted
channel_Head_Ro_deg_63 = 'Head_Ro_deg_63' #km    #plotted
channel_Head_Ro_deg_64 = 'Head_Ro_deg_64'#km    #plotted
channel_Head_Ro_deg_65 = 'Head_Ro_deg_65'#km    #plotted
channel_Head_Vx_mph_66 = 'Head_Vx_mph_66'
channel_Head_Vy_mph_67 = 'Head_Vy_mph_67'
channel_Head_Vz_mph_68 = 'Head_Vz_mph_68'
channel_Head_wx_deg_s_69 = 'Head_wx_deg/s_69'
channel_Head_wx_deg_s_70 = 'Head_wx_deg/s_70'
channel_Head_wx_deg_s_71 = 'Head_wx_deg/s_71'
channel_Head_oo_N_A_72 = 'Head_oo_N/A_72'
channel_Head_oo_N_A_73 = 'Head_oo_N/A_73'
channel_Head_oo_N_A_74 = 'Head_oo_N/A_74'
channel_Head_oo_N_A_75 = 'Head_oo_N/A_75'
channel_Spine_Dx_in_76 = 'Spine_Dx_in_76' #bc-      #plotted
channel_Spine_Dy_in_77 = 'Spine_Dy_in_77'
channel_Spine_Dz_in_78 = 'Spine_Dz_in_78'#bc-      #plotted
channel_Spine_Ro_deg_79 = 'Spine_Ro_deg_79'#bc-     #plotted
channel_Spine_Ro_deg_80 = 'Spine_Ro_deg_80'#bc-    #plotted
channel_Spine_Ro_deg_81 = 'Spine_Ro_deg_81'#bc-    #plotted
channel_Spine_Vx_mph_82 = 'Spine_Vx_mph_82'
channel_Spine_Vy_mph_83 = 'Spine_Vy_mph_83'
channel_Spine_Vz_mph_84 = 'Spine_Vz_mph_84'
channel_Spine_wo_deg_s_s_85 = 'Spine_wo_deg/s^2_85'
channel_Spine_wo_deg_s_s_86 = 'Spine_wo_deg/s^2_86'
channel_Spine_wo_deg_s_s_87 = 'Spine_wo_deg/s^2_87'
channel_Spine_oo_N_A_88 = 'Spine_oo_N/A_88' #bc-
channel_Spine_oo_N_A_89 = 'Spine_oo_N/A_89'#bc-
channel_Spine_oo_N_A_90 = 'Spine_oo_N/A_90'#bc-
channel_Spine_oo_N_A_91 = 'Spine_oo_N/A_91'#bc-


os.chdir(plot_path)
import matplotlib as mpl
import matplotlib.pyplot as plt

##############################################################################################################

#Plot Head X Displacement (in) - C1-2-60

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_1], label =channel_Head_Dx_in_1)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_2], label =channel_Head_Dx_in_2)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_60], label =channel_Head_Dx_in_60)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement in - Summary - C1-2-60.png')
plt.show()

#Plot Head X Displacement (in) - C1-2

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_1], label =channel_Head_Dx_in_1)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_2], label =channel_Head_Dx_in_2)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_60], label =channel_Head_Dx_in_60)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement in - Compare - C1-2.png')
plt.show()

#Plot Head X Displacement (in) - C1-60

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_1], label =channel_Head_Dx_in_1)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_2], label =channel_Head_Dx_in_2)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_60], label =channel_Head_Dx_in_60)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement in - Compare - C1-60.png')
plt.show()

#Plot Head X Displacement (in) - C2-60

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_1], label =channel_Head_Dx_in_1)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_2], label =channel_Head_Dx_in_2)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_60], label =channel_Head_Dx_in_60)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement in - Compare - C2-60.png')
plt.show()

#Plot Head X Displacement (in) - C1

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_1], label =channel_Head_Dx_in_1)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_2], label =channel_Head_Dx_in_2)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_60], label =channel_Head_Dx_in_60)

ax.plot(average_df[channelt],low[channel_Head_Dx_in_1],color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dx_in_1],color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement in - C1.png')
plt.show()

#Plot Head X Displacement (in) - C2

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_1], label =channel_Head_Dx_in_1)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_2], label =channel_Head_Dx_in_2)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_60], label =channel_Head_Dx_in_60)

ax.plot(average_df[channelt],low[channel_Head_Dx_in_2],color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dx_in_2],color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement in - C2.png')
plt.show()

#Plot Head X Displacement (in) - C60

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_1], label =channel_Head_Dx_in_1)
# ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_2], label =channel_Head_Dx_in_2)
ax.plot(average_df[channelt],average_df[channel_Head_Dx_in_60], label =channel_Head_Dx_in_60)

ax.plot(average_df[channelt],low[channel_Head_Dx_in_60], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dx_in_60], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement in - C60.png')
plt.show()

##############################################################################################################


#Plot Head Z Displacement (in) - C5-6-62

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_5], label =channel_Head_Dz_in_5)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_6], label =channel_Head_Dz_in_6)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_62], label =channel_Head_Dz_in_62)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement in - Summary - C5-6-62.png')
plt.show()

#Plot Head Z Displacement (in) - C5-6

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_5], label =channel_Head_Dz_in_5)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_6], label =channel_Head_Dz_in_6)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_62], label =channel_Head_Dz_in_62)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement in - Compare - C5-6.png')
plt.show()

#Plot Head Z Displacement (in) - C5-62

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_5], label =channel_Head_Dz_in_5)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_6], label =channel_Head_Dz_in_6)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_62], label =channel_Head_Dz_in_62)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement in - Compare - C5-62.png')
plt.show()

#Plot Head Z Displacement (in) - C6-62

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_5], label =channel_Head_Dz_in_5)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_6], label =channel_Head_Dz_in_6)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_62], label =channel_Head_Dz_in_62)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement in - Compare - C6-62.png')
plt.show()

#Plot Head Z Displacement (in) - C5

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_5], label =channel_Head_Dz_in_5)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_6], label =channel_Head_Dz_in_6)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_62], label =channel_Head_Dz_in_62)

ax.plot(average_df[channelt],low[channel_Head_Dz_in_5], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dz_in_5], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement in - C5.png')
plt.show()

#Plot Head Z Displacement (in) - C6

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_5], label =channel_Head_Dz_in_5)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_6], label =channel_Head_Dz_in_6)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_62], label =channel_Head_Dz_in_62)

ax.plot(average_df[channelt],low[channel_Head_Dz_in_6], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dz_in_6], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement in - C6.png')
plt.show()

#Plot Head Z Displacement (in) - C62

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_5], label =channel_Head_Dz_in_5)
# ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_6], label =channel_Head_Dz_in_6)
ax.plot(average_df[channelt],average_df[channel_Head_Dz_in_62], label =channel_Head_Dz_in_62)

ax.plot(average_df[channelt],low[channel_Head_Dz_in_62], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Dz_in_62], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement in - C62.png')
plt.show()

##############################################################################################################
##############################################################################################################

#Plot Spine X Displacement (in) - C29-30-76

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_29], label =channel_Spine_Dx_in_29)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_30], label =channel_Spine_Dx_in_30)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_76], label =channel_Spine_Dx_in_76)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement in - Summary - C29-30-76.png')
plt.show()

#Plot Spine X Displacement (in) - C29-30

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_29], label =channel_Spine_Dx_in_29)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_30], label =channel_Spine_Dx_in_30)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_76], label =channel_Spine_Dx_in_76)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement in - Compare - C29-30.png')
plt.show()

#Plot Spine X Displacement (in) - C29-76

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_29], label =channel_Spine_Dx_in_29)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_30], label =channel_Spine_Dx_in_30)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_76], label =channel_Spine_Dx_in_76)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement in - Compare - C29-76.png')
plt.show()

#Plot Spine X Displacement (in) - C30-76

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_29], label =channel_Spine_Dx_in_29)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_30], label =channel_Spine_Dx_in_30)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_76], label =channel_Spine_Dx_in_76)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement in - Compare - C30-76.png')
plt.show()

#Plot Spine X Displacement (in) - C29

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_29], label =channel_Spine_Dx_in_29)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_30], label =channel_Spine_Dx_in_30)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_76], label =channel_Spine_Dx_in_76)

ax.plot(average_df[channelt],low[channel_Spine_Dx_in_29], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dx_in_29], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement in - C29')
plt.show()

#Plot Spine X Displacement (in) - C30

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_29], label =channel_Spine_Dx_in_29)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_30], label =channel_Spine_Dx_in_30)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_76], label =channel_Spine_Dx_in_76)

ax.plot(average_df[channelt],low[channel_Spine_Dx_in_30], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dx_in_30], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement in - C30.png')
plt.show()

#Plot Spine X Displacement (in) - C76

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_29], label =channel_Spine_Dx_in_29)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_30], label =channel_Spine_Dx_in_30)
ax.plot(average_df[channelt],average_df[channel_Spine_Dx_in_76], label =channel_Spine_Dx_in_76)

ax.plot(average_df[channelt],low[channel_Spine_Dx_in_76], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dx_in_76], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement in - C76.png')
plt.show()

##############################################################################################################


#Plot Spine Z Displacement (in) - C33-34-78

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_33], label =channel_Spine_Dz_in_33)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_34], label =channel_Spine_Dz_in_34)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_78], label =channel_Spine_Dz_in_78)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement in - Summary - C33-34-78.png')
plt.show()

#Plot Spine Z Displacement (in) - C33-34

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_33], label =channel_Spine_Dz_in_33)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_34], label =channel_Spine_Dz_in_34)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_78], label =channel_Spine_Dz_in_78)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement in - Compare - C33-34.png')
plt.show()

#Plot Spine Z Displacement (in) - C33-78

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_33], label =channel_Spine_Dz_in_33)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_34], label =channel_Spine_Dz_in_34)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_78], label =channel_Spine_Dz_in_78)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement in - Compare - C33-78.png')
plt.show()

#Plot Spine Z Displacement (in) - C34-78

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_33], label =channel_Spine_Dz_in_33)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_34], label =channel_Spine_Dz_in_34)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_78], label =channel_Spine_Dz_in_78)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement in - Compare - C34-78.png')
plt.show()

#Plot Spine Z Displacement (in) - C33

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_33], label =channel_Spine_Dz_in_33)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_34], label =channel_Spine_Dz_in_34)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_78], label =channel_Spine_Dz_in_78)

ax.plot(average_df[channelt],low[channel_Spine_Dz_in_33], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dz_in_33], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement in - C33.png')
plt.show()

#Plot Spine Z Displacement (in) - C34

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_33], label =channel_Spine_Dz_in_33)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_34], label =channel_Spine_Dz_in_34)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_78], label =channel_Spine_Dz_in_78)

ax.plot(average_df[channelt],low[channel_Spine_Dz_in_34], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dz_in_34], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement in - C34.png')
plt.show()

#Plot Spine Z Displacement (in) - C78

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_33], label =channel_Spine_Dz_in_33)
# ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_34], label =channel_Spine_Dz_in_34)
ax.plot(average_df[channelt],average_df[channel_Spine_Dz_in_78], label =channel_Spine_Dz_in_78)

ax.plot(average_df[channelt],low[channel_Spine_Dz_in_78], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Dz_in_78], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (in)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (in)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement in - C78.png')
plt.show()

##############################################################################################################
##############################################################################################################
##############################################################################################################

#Plot Head NA Rotation (deg) - C7-8-9

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_7], label =channel_Head_Ro_deg_7)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_8], label =channel_Head_Ro_deg_8)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_9], label =channel_Head_Ro_deg_9)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - Summary - C7-8-9.png')
plt.show()

#Plot Head NA Rotation (deg) - C7-8

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_7], label =channel_Head_Ro_deg_7)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_8], label =channel_Head_Ro_deg_8)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_9], label =channel_Head_Ro_deg_9)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - Compare - C7-8.png')
plt.show()

#Plot Head NA Rotation (deg) - C7-9

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_7], label =channel_Head_Ro_deg_7)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_8], label =channel_Head_Ro_deg_8)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_9], label =channel_Head_Ro_deg_9)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - Compare - C7-9.png')
plt.show()

#Plot Head NA Rotation (deg) - C8-9

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_7], label =channel_Head_Ro_deg_7)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_8], label =channel_Head_Ro_deg_8)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_9], label =channel_Head_Ro_deg_9)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - Compare - C8-9.png')
plt.show()

#Plot Head NA Rotation (deg) - C7

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_7], label =channel_Head_Ro_deg_7)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_8], label =channel_Head_Ro_deg_8)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_9], label =channel_Head_Ro_deg_9)

ax.plot(average_df[channelt],low[channel_Head_Ro_deg_7], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_deg_7], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - C7.png')
plt.show()

#Plot Head NA Rotation (deg) - C8

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_7], label =channel_Head_Ro_deg_7)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_8], label =channel_Head_Ro_deg_8)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_9], label =channel_Head_Ro_deg_9)

ax.plot(average_df[channelt],low[channel_Head_Ro_deg_8], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_deg_8], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - C8.png')
plt.show()

#Plot Head NA Rotation (deg) - C9

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_7], label =channel_Head_Ro_deg_7)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_8], label =channel_Head_Ro_deg_8)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_9], label =channel_Head_Ro_deg_9)

ax.plot(average_df[channelt],low[channel_Head_Ro_deg_9], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_deg_9], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - C9.png')
plt.show()

##############################################################################################################

#Plot Head NA Rotation (deg) - C63-64-65

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_63], label =channel_Head_Ro_deg_63)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_64], label =channel_Head_Ro_deg_64)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_65], label =channel_Head_Ro_deg_65)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - Summary - C63-64-65.png')
plt.show()

#Plot Head NA Rotation (deg) - C63-64

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_63], label =channel_Head_Ro_deg_63)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_64], label =channel_Head_Ro_deg_64)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_65], label =channel_Head_Ro_deg_65)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - Compare - C63-64.png')
plt.show()

#Plot Head NA Rotation (deg) - C63-65

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_63], label =channel_Head_Ro_deg_63)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_64], label =channel_Head_Ro_deg_64)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_65], label =channel_Head_Ro_deg_65)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - Compare - C63-65.png')
plt.show()

#Plot Head NA Rotation (deg) - C64-65

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_63], label =channel_Head_Ro_deg_63)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_64], label =channel_Head_Ro_deg_64)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_65], label =channel_Head_Ro_deg_65)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - Compare - C64-65.png')
plt.show()

#Plot Head NA Rotation (deg) - C63

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_63], label =channel_Head_Ro_deg_63)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_64], label =channel_Head_Ro_deg_64)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_65], label =channel_Head_Ro_deg_65)

ax.plot(average_df[channelt],low[channel_Head_Ro_deg_63], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_deg_63], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - C63.png')
plt.show()

#Plot Head NA Rotation (deg) - C64

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_63], label =channel_Head_Ro_deg_63)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_64], label =channel_Head_Ro_deg_64)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_65], label =channel_Head_Ro_deg_65)

ax.plot(average_df[channelt],low[channel_Head_Ro_deg_64], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_deg_64], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - C64.png')
plt.show()

#Plot Head NA Rotation (deg) - C65

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_63], label =channel_Head_Ro_deg_63)
# ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_64], label =channel_Head_Ro_deg_64)
ax.plot(average_df[channelt],average_df[channel_Head_Ro_deg_65], label =channel_Head_Ro_deg_65)

ax.plot(average_df[channelt],low[channel_Head_Ro_deg_65], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Head_Ro_deg_65], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - C65.png')
plt.show()

##############################################################################################################
##############################################################################################################


#Plot Spine NA Rotation (deg) - C35-36-37

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_35], label =channel_Spine_Ro_deg_35)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_36], label =channel_Spine_Ro_deg_36)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_37], label =channel_Spine_Ro_deg_37)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - Summary - C35-36-37.png')
plt.show()

#Plot Spine NA Rotation (deg) - C35-36

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_35], label =channel_Spine_Ro_deg_35)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_36], label =channel_Spine_Ro_deg_36)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_37], label =channel_Spine_Ro_deg_37)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - Compare - C35-36.png')
plt.show()

#Plot Spine NA Rotation (deg) - C35-37

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_35], label =channel_Spine_Ro_deg_35)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_36], label =channel_Spine_Ro_deg_36)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_37], label =channel_Spine_Ro_deg_37)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - Compare - C35-37.png')
plt.show()

#Plot Spine NA Rotation (deg) - C36-37

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_35], label =channel_Spine_Ro_deg_35)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_36], label =channel_Spine_Ro_deg_36)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_37], label =channel_Spine_Ro_deg_37)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - Compare - C36-37.png')
plt.show()

#Plot Spine NA Rotation (deg) - C35

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_35], label =channel_Spine_Ro_deg_35)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_36], label =channel_Spine_Ro_deg_36)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_37], label =channel_Spine_Ro_deg_37)

ax.plot(average_df[channelt],low[channel_Spine_Ro_deg_35], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_deg_35], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - C35.png')
plt.show()

#Plot Spine NA Rotation (deg) - C36

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_35], label =channel_Spine_Ro_deg_35)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_36], label =channel_Spine_Ro_deg_36)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_37], label =channel_Spine_Ro_deg_37)

ax.plot(average_df[channelt],low[channel_Spine_Ro_deg_36], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_deg_36], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - C36.png')
plt.show()

#Plot Spine NA Rotation (deg) - C37

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_35], label =channel_Spine_Ro_deg_35)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_36], label =channel_Spine_Ro_deg_36)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_37], label =channel_Spine_Ro_deg_37)

ax.plot(average_df[channelt],low[channel_Spine_Ro_deg_37], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_deg_37], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - C37.png')
plt.show()

##############################################################################################################

#Plot Spine NA Rotation (deg) - C79-80-81

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_79], label =channel_Spine_Ro_deg_79)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_80], label =channel_Spine_Ro_deg_80)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_81], label =channel_Spine_Ro_deg_81)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - Summary - C79-80-81.png')
plt.show()

#Plot Spine NA Rotation (deg) - C79-80

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_79], label =channel_Spine_Ro_deg_79)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_80], label =channel_Spine_Ro_deg_80)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_81], label =channel_Spine_Ro_deg_81)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - Compare - C79-80.png')
plt.show()

#Plot Spine NA Rotation (deg) - C79-81

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_79], label =channel_Spine_Ro_deg_79)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_80], label =channel_Spine_Ro_deg_80)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_81], label =channel_Spine_Ro_deg_81)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - Compare - C79-81.png')
plt.show()

#Plot Spine NA Rotation (deg) - C80-81

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_79], label =channel_Spine_Ro_deg_79)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_80], label =channel_Spine_Ro_deg_80)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_81], label =channel_Spine_Ro_deg_81)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - Compare - C80-81.png')
plt.show()

#Plot Spine NA Rotation (deg) - C79

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_79], label =channel_Spine_Ro_deg_79)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_80], label =channel_Spine_Ro_deg_80)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_81], label =channel_Spine_Ro_deg_81)

ax.plot(average_df[channelt],low[channel_Spine_Ro_deg_79], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_deg_79], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - C79.png')
plt.show()

#Plot Spine NA Rotation (deg) - C80

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_79], label =channel_Spine_Ro_deg_79)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_80], label =channel_Spine_Ro_deg_80)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_81], label =channel_Spine_Ro_deg_81)

ax.plot(average_df[channelt],low[channel_Spine_Ro_deg_80], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_deg_80], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - C80.png')
plt.show()

#Plot Spine NA Rotation (deg) - C81

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_79], label =channel_Spine_Ro_deg_79)
# ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_80], label =channel_Spine_Ro_deg_80)
ax.plot(average_df[channelt],average_df[channel_Spine_Ro_deg_81], label =channel_Spine_Ro_deg_81)

ax.plot(average_df[channelt],low[channel_Spine_Ro_deg_81], color = "lightblue")
ax.plot(average_df[channelt],high[channel_Spine_Ro_deg_81], color = "lightblue")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - C81.png')
plt.show()

##############################################################################################################