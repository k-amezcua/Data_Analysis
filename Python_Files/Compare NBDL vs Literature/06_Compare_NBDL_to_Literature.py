# Import Modules
import os, glob
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

filename= 'C4-C5-CT'

main_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\Original Units\\Compiled Test Data\\"
plot_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Average Plots\\Original Units\\Relative Data Plots\\"
digitized_path = "C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\NBDL Data\\Digitized Literature Data\\"
# Changing the current working directory
os.chdir(main_path)

path = main_path + "Average - Integrated.csv"
average_df_int = pd.read_csv(path, sep=',', engine = 'python', index_col=False)

path = main_path + "Standard Deviation - Integrated.csv"
stdev_df_int = pd.read_csv(path, sep=',', engine = 'python', index_col=False)

low_int = average_df_int-stdev_df_int
high_int = average_df_int+stdev_df_int

path = main_path + "Average - Integrated Rotation.csv"
average_df_int_rot = pd.read_csv(path, sep=',', engine = 'python', index_col=False)

path = main_path + "Standard Deviation - Integrated Rotation.csv"
stdev_df_int_rot = pd.read_csv(path, sep=',', engine = 'python', index_col=False)

low_int_rot = average_df_int_rot-stdev_df_int_rot
high_int_rot = average_df_int_rot+stdev_df_int_rot

#########################################################################################################
#Read Digitized Literature Curves

path = digitized_path + "Correia 2020 - Rel. Head X Displacement.csv"
rel_Head_Dx_Correia = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
path = digitized_path + "Correia 2020 - Rel. Head Y Rotation.csv"
rel_Head_Ry_Correia = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
rel_Head_Dx_Correia['Time_ms'] = rel_Head_Dx_Correia['Time_ms']/1000
rel_Head_Ry_Correia['Time_ms'] = rel_Head_Ry_Correia['Time_ms']/1000
rel_Head_Dx_Correia.rename(columns = {'Time_ms':'Time_s'}, inplace = True)
rel_Head_Ry_Correia.rename(columns = {'Time_ms':'Time_s'}, inplace = True)

path = digitized_path + "Panzer 2006 - T1 Acceleration.csv"
Spine_Ax_Panzer = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
path = digitized_path + "T1 Rotation - Panzer 2006.csv"
Spine_Ry_Panzer = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
Spine_Ry_Panzer['Time_ms'] = Spine_Ry_Panzer['Time_ms']/1000
Spine_Ry_Panzer.rename(columns = {'Time_ms':'Time_s'}, inplace = True)

path = digitized_path + "Panzer 2006 - Head Trajectory.csv"
Head_Trajectory_Panzer = pd.read_csv(path, sep=',', engine = 'python', index_col=False)

path = digitized_path + "T1 Rotation - Thunnissen 1995 - Update.csv"
Spine_Ry_Thunnissen = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
Spine_Ry_Thunnissen['Time_ms'] = Spine_Ry_Thunnissen['Time_ms']/1000
Spine_Ry_Thunnissen.rename(columns = {'Time_ms':'Time_s'}, inplace = True)

path = digitized_path + "Brolin 2005 - Rel Head X Displacement.csv"
rel_Head_Dx_Brolin = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
path = digitized_path + "Brolin 2005 - Rel Head Z Displacement.csv"
rel_Head_Dz_Brolin = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
path = digitized_path + "Brolin 2005 - Rel Head Rotation.csv"
rel_Head_Ry_Brolin = pd.read_csv(path, sep=',', engine = 'python', index_col=False)
rel_Head_Dx_Brolin['Time_ms'] = rel_Head_Dx_Brolin['Time_ms']/1000
rel_Head_Dz_Brolin['Time_ms'] = rel_Head_Dz_Brolin['Time_ms']/1000
rel_Head_Ry_Brolin['Time_ms'] = rel_Head_Ry_Brolin['Time_ms']/1000
rel_Head_Ry_Brolin['Ry-1SD'] = rel_Head_Ry_Brolin['Ry-1SD']*-1
rel_Head_Ry_Brolin['Ry+1SD'] = rel_Head_Ry_Brolin['Ry+1SD']*-1
# Spine_Ry_Thunnissen['Ry_Average'] = (Spine_Ry_Thunnissen['Ry-1SD']+Spine_Ry_Thunnissen['Ry+1SD'])/2
Spine_Ry_Thunnissen.to_excel(main_path+"T1 Rotation - Thunnissen 1995 - Average Ry.xlsx")

rel_Head_Dx_Brolin.rename(columns = {'Time_ms':'Time_s'}, inplace = True)
rel_Head_Dz_Brolin.rename(columns = {'Time_ms':'Time_s'}, inplace = True)
rel_Head_Ry_Brolin.rename(columns = {'Time_ms':'Time_s'}, inplace = True)

channelt = 'Time_s'
Head_Dx_mm_int_19 = 'Head_Dx_mm_int_19'
Sled_Dx_mm_int_57 = 'Sled_Dx_mm_int_57'
Spine_Dx_mm_int_47 = 'Spine_Dx_mm_int_47'
Head_Dz_mm_int_21 = 'Head_Dz_mm_int_21'
Spine_Dz_mm_int_49 = 'Spine_Dz_mm_int_49'
Head_ao_deg_int_22 = 'Head_ao_deg_22'
Head_ao_deg_int_23 = 'Head_ao_deg_23'
Head_ao_deg_int_24 = 'Head_ao_deg_24'
Spine_ao_deg_int_50 = 'Spine_ao_deg_50'
Spine_ao_deg_int_51 = 'Spine_ao_deg_51'
Spine_ao_deg_int_52 = 'Spine_ao_deg_52'

Rel_Head_Dx_mm = 'Rel_Head_Dx_mm'
Rel_Head_Dz_mm = 'Rel_Head_Dz_mm'
Rel_Head_to_Sled_Dx_mm = 'Rel_Head_to_Sled_Dx_mm'
Rel_Spine_to_Sled_Dx_mm = 'Rel_Spine_to_Sled_Dx_mm'

os.chdir(plot_path)


import matplotlib.pyplot as plt

##############################################################################################################
#Plot Head X Displacement (mm) - C19-I

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int[channelt],average_df_int[Head_Dx_mm_int_19], label =Head_Dx_mm_int_19)

ax.plot(average_df_int[channelt],low_int[Head_Dx_mm_int_19],color = "lightpink")
ax.plot(average_df_int[channelt],high_int[Head_Dx_mm_int_19],color = "lightpink")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head X Displacement mm - C19-I.png')
plt.show()

##############################################################################################################
#Plot Spine X Displacement (mm) - C47-I

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int[channelt],average_df_int[Spine_Dx_mm_int_47], label =Spine_Dx_mm_int_47)

ax.plot(average_df_int[channelt],low_int[Spine_Dx_mm_int_47],color = "lightpink")
ax.plot(average_df_int[channelt],high_int[Spine_Dx_mm_int_47],color = "lightpink")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine X Displacement mm - C47-I.png')
plt.show()

##############################################################################################################
#Plot Head Z Displacement (mm) - C21-I

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int[channelt],average_df_int[Head_Dz_mm_int_21], label =Head_Dz_mm_int_21)

ax.plot(average_df_int[channelt],low_int[Head_Dz_mm_int_21],color = "lightpink")
ax.plot(average_df_int[channelt],high_int[Head_Dz_mm_int_21],color = "lightpink")

ax.plot(rel_Head_Dz_Brolin[channelt],rel_Head_Dz_Brolin['Dz-1SD'], label ='rel_Head_Dz_Brolin', color = "green")
ax.plot(rel_Head_Dz_Brolin[channelt],rel_Head_Dz_Brolin['Dz+1SD'], label ='rel_Head_Dz_Brolin', color = "green")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Z Displacement mm - C21-I.png')
plt.show()

##############################################################################################################
#Plot Spine Z Displacement (mm) - C49-I

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int[channelt],average_df_int[Spine_Dz_mm_int_49], label =Spine_Dz_mm_int_49)

ax.plot(average_df_int[channelt],low_int[Spine_Dz_mm_int_49],color = "lightpink")
ax.plot(average_df_int[channelt],high_int[Spine_Dz_mm_int_49],color = "lightpink")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Z Displacement mm - C49-I.png')
plt.show()


##############################################################################################################
#Plot Rel. Head X Displacement (mm) - C19-C47-I
#
# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int[channelt],average_df_int[Rel_Head_Dx_mm], label =Rel_Head_Dx_mm)

ax.plot(average_df_int[channelt],low_int[Rel_Head_Dx_mm],color = "lightpink")
ax.plot(average_df_int[channelt],high_int[Rel_Head_Dx_mm],color = "lightpink")

ax.plot(rel_Head_Dx_Correia[channelt],rel_Head_Dx_Correia['Dx'], label ='rel_Head_Dx_Correia')
ax.plot(rel_Head_Dx_Brolin[channelt],rel_Head_Dx_Brolin['Dx-1SD'], label ='rel_Head_Dx_Brolin', color = "green")
ax.plot(rel_Head_Dx_Brolin[channelt],rel_Head_Dx_Brolin['Dx+1SD'], label ='rel_Head_Dx_Brolin', color = "green")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Rel. Head X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Rel. Head X Displacement mm - C19-C47-I.png')
plt.show()

##############################################################################################################
#Plot Rel. Head Z Displacement (mm) - C21-C49-I

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int[channelt],average_df_int[Rel_Head_Dz_mm], label =Rel_Head_Dz_mm)

ax.plot(average_df_int[channelt],low_int[Rel_Head_Dz_mm],color = "lightpink")
ax.plot(average_df_int[channelt],high_int[Rel_Head_Dz_mm],color = "lightpink")

ax.plot(rel_Head_Dz_Brolin[channelt],rel_Head_Dz_Brolin['Dz-1SD'], label ='rel_Head_Dz_Brolin', color = "green")
ax.plot(rel_Head_Dz_Brolin[channelt],rel_Head_Dz_Brolin['Dz+1SD'], label ='rel_Head_Dz_Brolin', color = "green")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Rel. Head Z Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Rel. Head Z Displacement mm - C21-C49-I.png')
plt.show()

# ##############################################################################################################
# #Plot Rel. Head X vs. Z Displacement (mm)
#
# # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
# fig,ax = plt.subplots()
# ax.plot(average_df_int[Rel_Head_Dx_mm],average_df_int[Rel_Head_Dz_mm], label ='Head Trajectory X-Z')
#
# # ax.plot(low_int[Rel_Head_Dx_mm],low_int[Rel_Head_Dz_mm],color = "lightpink")
# # ax.plot(high_int[Rel_Head_Dx_mm],high_int[Rel_Head_Dz_mm],color = "lightpink")
#
# # ax.set_xlim(0, 0.25)
# ax.set_xlabel('Rel. Dx (mm)')
# ax.set_ylabel('Rel. Dz (mm)')
# ax.grid(True)
# ax.legend()
# ax.set_title('Head Trajectory X-Z')
# plt.subplots_adjust(left = 0.17, bottom = 0.13)
# plt.savefig('Head Trajectory X-Z.png')
# plt.show()

##############################################################################################################
#Plot Rel. Head X vs. Z Displacement (mm)

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int[Rel_Head_Dx_mm],average_df_int[Head_Dz_mm_int_21], label ='Head Trajectory X-Z')
print(average_df_int[Head_Dz_mm_int_21])
print(average_df_int[Rel_Head_Dx_mm])
# ax.plot(low_int[Rel_Head_Dx_mm],low_int[Rel_Head_Dz_mm],color = "lightpink")
# ax.plot(high_int[Rel_Head_Dx_mm],high_int[Rel_Head_Dz_mm],color = "lightpink")

ax.plot(Head_Trajectory_Panzer['Head Dx'],Head_Trajectory_Panzer['Head Dz-1SD'], label ='Head Trajectory X-Z', color = "orange")
ax.plot(Head_Trajectory_Panzer['Head Dx'],Head_Trajectory_Panzer['Head Dz+1SD'], color = "orange")

ax.set_xlim(0, 200)
ax.set_xlabel('Rel. Dx (mm)')
ax.set_ylabel('Rel. Dz (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Head Trajectory X-Z')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Trajectory X-Z.png')
plt.show()
##############################################################################################################
#Plot Rel. Head X vs. Z Displacement (mm)

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()

ax.plot(rel_Head_Dz_Brolin[channelt],rel_Head_Dz_Brolin['Dz-1SD'], label ='Dz - Brolin', color = "pink")
ax.plot(rel_Head_Dz_Brolin[channelt],rel_Head_Dz_Brolin['Dz+1SD'], label ='Dz - Brolin', color = "pink")
ax.plot(rel_Head_Dx_Brolin[channelt],rel_Head_Dx_Brolin['Dx+1SD'], label ='Dx - Brolin', color = "red")
ax.plot(rel_Head_Dx_Brolin[channelt],rel_Head_Dx_Brolin['Dx-1SD'],label ='Dx - Brolin', color = "red")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Displacement (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Brolin Head Trajectory X-Z')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Brolin Head Trajectory X-Z.png')
plt.show()

##############################################################################################################
##############################################################################################################
##############################################################################################################
#Plot Head Y Rotation (deg) - C23-I
#Relative data matches Correia.
# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int_rot[channelt],average_df_int_rot[Head_ao_deg_int_23], label =Head_ao_deg_int_23)

ax.plot(average_df_int_rot[channelt],low_int_rot[Head_ao_deg_int_23],color = "lightpink")
ax.plot(average_df_int_rot[channelt],high_int_rot[Head_ao_deg_int_23],color = "lightpink")

ax.plot(rel_Head_Ry_Correia[channelt],rel_Head_Ry_Correia['Ry'], label ='rel_Head_Ry_Correia')

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head Y Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head Y Rotation deg - C23-I.png')
plt.show()


##############################################################################################################
#Plot Spine Y Rotation (deg) - Thunnissen 1995
# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(Spine_Ry_Thunnissen[channelt],Spine_Ry_Thunnissen['Ry_Average'], label ='Spine_Ry_Thunnissen')
#
# ax.plot(Spine_Ry_Thunnissen[channelt],Spine_Ry_Thunnissen['Ry-1SD'],color = "lightpink")
# ax.plot(Spine_Ry_Thunnissen[channelt],Spine_Ry_Thunnissen['Ry+1SD'],color = "lightpink")


ax.plot(Spine_Ry_Panzer[channelt],Spine_Ry_Panzer['Ry'], label ='Spine_Ry_Panzer')


ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Y Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Y Rotation deg - Thunnissen 1995.png')
plt.show()
# ##############################################################################################################
##############################################################################################################
#Plot Head Y Rotation (deg) - Brolin
#Relative data matches Correia.
# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(rel_Head_Ry_Brolin[channelt],rel_Head_Ry_Brolin['Ry-1SD'], label ='rel_Head_Ry_Brolin',color = "lightpink")
ax.plot(rel_Head_Ry_Brolin[channelt],rel_Head_Ry_Brolin['Ry+1SD'], label ='rel_Head_Ry_Brolin',color = "lightpink")


ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Brolin Head Y Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Brolin Head Y Rotation deg.png')
plt.show()

# ##############################################################################################################
# None of these curves match published data
#Plot Spine NA Rotation (deg) - C50-51-52-I

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int_rot[channelt],average_df_int_rot[Spine_ao_deg_int_50], label =Spine_ao_deg_int_50)
ax.plot(average_df_int_rot[channelt],average_df_int_rot[Spine_ao_deg_int_51],label =Spine_ao_deg_int_51)
ax.plot(average_df_int_rot[channelt],average_df_int_rot[Spine_ao_deg_int_52],label =Spine_ao_deg_int_52)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ry (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Spine NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine NA Rotation deg - Summary - C50-51-52-I.png')
plt.show()


#Plot Head Rotation (deg) - C22-23-24-I

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int_rot[channelt],average_df_int_rot[Head_ao_deg_int_22], label =Head_ao_deg_int_22)
ax.plot(average_df_int_rot[channelt],average_df_int_rot[Head_ao_deg_int_23],label =Head_ao_deg_int_23)
ax.plot(average_df_int_rot[channelt],average_df_int_rot[Head_ao_deg_int_24],label =Head_ao_deg_int_24)

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Ro (deg)')
ax.grid(True)
ax.legend()
ax.set_title('Head NA Rotation (deg)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Head NA Rotation deg - Summary - C22-23-24-I.png')
plt.show()

#Plot Sled X Displacement (mm) - C57-I

# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
ax.plot(average_df_int[channelt],average_df_int[Sled_Dx_mm_int_57], label =Sled_Dx_mm_int_57)

ax.plot(average_df_int[channelt],low_int[Sled_Dx_mm_int_57],color = "lightpink")
ax.plot(average_df_int[channelt],high_int[Sled_Dx_mm_int_57],color = "lightpink")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Sled X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Sled X Displacement mm - C57-I.png')
plt.show()

# #Plot Head Rel. Sled X Displacement (mm) - C19-57-I
# Does not match Correia or Panzer
# # mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
# fig,ax = plt.subplots()
# ax.plot(average_df_int[channelt],average_df_int[Rel_Head_to_Sled_Dx_mm], label =Rel_Head_to_Sled_Dx_mm)
#
# ax.plot(average_df_int[channelt],low_int[Rel_Head_to_Sled_Dx_mm],color = "lightpink")
# ax.plot(average_df_int[channelt],high_int[Rel_Head_to_Sled_Dx_mm],color = "lightpink")
#
# ax.plot(rel_Head_Dx_Correia[channelt],rel_Head_Dx_Correia['Dx'], label ='rel_Head_Dx_Correia')
# ax.plot(rel_Head_Dx_Brolin[channelt],rel_Head_Dx_Brolin['Dx-1SD'], label ='rel_Head_Dx_Brolin', color = "green")
# ax.plot(rel_Head_Dx_Brolin[channelt],rel_Head_Dx_Brolin['Dx+1SD'], label ='rel_Head_Dx_Brolin', color = "green")
#
# ax.set_xlim(0, 0.25)
# ax.set_xlabel('Time (s)')
# ax.set_ylabel('Dx (mm)')
# ax.grid(True)
# ax.legend()
# ax.set_title('Head Rel. Sled X Displacement (mm)')
# plt.subplots_adjust(left = 0.17, bottom = 0.13)
# plt.savefig('Head Rel. Sled X Displacement mm - C19-57-I.png')
# plt.show()



###############################################################################
#Plot Spine Rel. Sled X Displacement (mm) - C47-57-I
# mpl.use('TkAgg')  # or can use 'TkAgg' or Qt5Agg, whatever you have/prefer
fig,ax = plt.subplots()
# average_df_int['Rel_Spine_to_Sled_Dx_mm'] = (average_df_int[Spine_Dx_mm_int_47] - average_df_int[Sled_Dx_mm_int_57])
# Average_T1_Displacement_NBDL_C47_57 = average_df_int[['Time_s', 'Rel_Spine_to_Sled_Dx_mm']]/1000
# export_path = 'C:\\Users\\kamezcua\\Desktop\\0000 THESIS\\Model Development\\Model Inputs\\T1 BC\\'
# Average_T1_Displacement_NBDL_C47_57.to_csv(export_path+"Average_T1_Displacement_NBDL_C47_57.csv")

ax.plot(average_df_int[channelt],average_df_int[Spine_Dx_mm_int_47] - average_df_int[Sled_Dx_mm_int_57], label =Rel_Spine_to_Sled_Dx_mm)

ax.plot(average_df_int[channelt],low_int[Spine_Dx_mm_int_47] - low_int[Sled_Dx_mm_int_57],color = "lightpink")
ax.plot(average_df_int[channelt],high_int[Spine_Dx_mm_int_47] - high_int[Sled_Dx_mm_int_57],color = "lightpink")

ax.set_xlim(0, 0.25)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Dx (mm)')
ax.grid(True)
ax.legend()
ax.set_title('Spine Rel. Sled X Displacement (mm)')
plt.subplots_adjust(left = 0.17, bottom = 0.13)
plt.savefig('Spine Rel. Sled X Displacement mm - C47-57-I.png')
plt.show()
print('complete')