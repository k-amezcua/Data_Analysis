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
# print(stdev_df)

low = average_df-stdev_df
# print(low)
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

figure, ax = plt.subplots(4, 2)

ax[0, 0].plot(average_df[channelt],average_df[channel_Head_Dx_mm_1], label =channel_Head_Dx_mm_1)
ax[0, 0].plot(average_df[channelt],average_df[channel_Head_Dx_mm_2], label =channel_Head_Dx_mm_2)
ax[0, 0].plot(average_df[channelt],average_df[channel_Head_Dx_mm_60], label =channel_Head_Dx_mm_60)
ax[0, 0].set_title('Head X Displacement (mm)')

ax[0, 1].plot(average_df[channelt],average_df[channel_Head_Dz_mm_5], label =channel_Head_Dz_mm_5)
ax[0, 1].plot(average_df[channelt],average_df[channel_Head_Dz_mm_6], label =channel_Head_Dz_mm_6)
ax[0, 1].plot(average_df[channelt],average_df[channel_Head_Dz_mm_62], label =channel_Head_Dz_mm_62)
ax[0, 1].set_title('Head Z Displacement (mm)')

ax[1, 0].plot(average_df[channelt],average_df[channel_Head_Ro_rad_7], label =channel_Head_Ro_rad_7)
ax[1, 0].plot(average_df[channelt],average_df[channel_Head_Ro_rad_8], label =channel_Head_Ro_rad_8)
ax[1, 0].plot(average_df[channelt],average_df[channel_Head_Ro_rad_9], label =channel_Head_Ro_rad_9)
ax[1, 0].set_title('Head NA Rotation (rad)')

ax[1, 1].plot(average_df[channelt],average_df[channel_Head_Ro_rad_63], label =channel_Head_Ro_rad_63)
ax[1, 1].plot(average_df[channelt],average_df[channel_Head_Ro_rad_64], label =channel_Head_Ro_rad_64)
ax[1, 1].plot(average_df[channelt],average_df[channel_Head_Ro_rad_65], label =channel_Head_Ro_rad_65)
ax[1, 1].set_title('Head NA Rotation (rad)')

ax[2, 0].plot(average_df[channelt],average_df[channel_Spine_Dx_mm_29], label =channel_Spine_Dx_mm_29)
ax[2, 0].plot(average_df[channelt],average_df[channel_Spine_Dx_mm_30], label =channel_Spine_Dx_mm_30)
ax[2, 0].plot(average_df[channelt],average_df[channel_Spine_Dx_mm_76], label =channel_Spine_Dx_mm_76)
ax[2, 0].set_title('Spine X Displacement (mm)')

ax[2, 1].plot(average_df[channelt],average_df[channel_Spine_Dz_mm_33], label =channel_Spine_Dz_mm_33)
ax[2, 1].plot(average_df[channelt],average_df[channel_Spine_Dz_mm_34], label =channel_Spine_Dz_mm_34)
ax[2, 1].plot(average_df[channelt],average_df[channel_Spine_Dz_mm_78], label =channel_Spine_Dz_mm_78)
ax[2, 1].set_title('Spine Z Displacement (mm)')

ax[3, 0].plot(average_df[channelt],average_df[channel_Spine_Ro_rad_35], label =channel_Spine_Ro_rad_35)
ax[3, 0].plot(average_df[channelt],average_df[channel_Spine_Ro_rad_36], label =channel_Spine_Ro_rad_36)
ax[3, 0].plot(average_df[channelt],average_df[channel_Spine_Ro_rad_37], label =channel_Spine_Ro_rad_37)
ax[3, 0].set_title('Spine NA Rotation (rad)')

ax[3, 1].plot(average_df[channelt],average_df[channel_Spine_Ro_rad_79], label =channel_Spine_Ro_rad_79)
ax[3, 1].plot(average_df[channelt],average_df[channel_Spine_Ro_rad_80], label =channel_Spine_Ro_rad_80)
ax[3, 1].plot(average_df[channelt],average_df[channel_Spine_Ro_rad_81], label =channel_Spine_Ro_rad_81)
ax[3, 1].set_title('Spine NA Rotation (rad)')

plt.tight_layout()
plt.savefig('Head and Spine Displacement Kinematics Summary.png')
plt.show()

# fig = plt.figure(figsize=(6,4))
