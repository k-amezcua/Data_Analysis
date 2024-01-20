###############################################################################
#
#   CORAplus 4.0.5
#   Head Acceleration Analysis
###############################################################################

BEGIN GLOBAL_PARAMETERS
   DES_MOD             CORA Analysis
   DES_GLO             Head Acceleration X
   A_THRES             0.030
   B_THRES             0.075
   A_EVAL              0.010
   B_DELTA_END         0.200
   T_MIN/T_MAX         automatic      automatic
   K                   2
   G_1                 0.50
   a_0/b_0             0.05      0.5
   a_sigma/b_sigma     0      0
   D_MIN               0.01
   D_MAX               0.12
   INT_MIN             0.80
   K_V                 10
   K_G                 1
   K_P                 1
   G_V                 0.50
   G_G                 0.25
   G_P                 0.25
   G_2                 0.50
   WF_NORM             YES
   ISONAME_1-2/11-12   NO NO
   MIN_NORM            0.00
   Y_NORM              extremum
   OUTPUT_FORMAT       LS-PrePost
   FONT_SMALL          12
   FONT_LARGE          14
   PreT_LC/PostT_LC    0.1  0.1
END GLOBAL_PARAMETERS

BEGIN LOADCASE
  NAM_LC              Head X Acceleration Analysis
  DES_LC              Simulation 1 Evaluation
  WF_LC               1
  METHOD              ISO9790

  BEGIN DATAFILES
# Experimental Data
#   C:\Users\kryst\Desktop\THESIS\Data_Analysis\Python_Files\H_CORA_Analysis\Simulation_1\data\cae_droptest_01.dat  0.0  m-kg-s  YES
  C:\Users\kryst\Desktop\THESIS\Data_Analysis\Python_Files\H_CORA_Analysis\Simulation_1\data\exp_head_x_accel.dat  0.0  m-kg-s YES 
  C:\Users\kryst\Desktop\THESIS\Data_Analysis\Python_Files\H_CORA_Analysis\Simulation_1\data\exp_head_x_accel.dat  0.0  m-kg-s YES 
  C:\Users\kryst\Desktop\THESIS\Data_Analysis\Python_Files\H_CORA_Analysis\Simulation_1\data\exp_head_x_accel.dat  0.0  m-kg-s YES
# Simulation Data
  C:\Users\kryst\Desktop\THESIS\Data_Analysis\Python_Files\H_CORA_Analysis\Simulation_1\data\sim_head_x_accel.dat  0.0  m-kg-s  YES
  END DATAFILES

# Signal Parameters
  BEGIN SIGNALS
# Parameters format:
# 1 (Name), 2 (WF), 3 (Y_norm), 4 (t_min), 5 (t_max), 6 (g_V), 7 (g_G), 8 (g_P), 9 (g_1), 10 (g_2)
# 11 (a_0), 12 (b_0), 13 (a_t), 14 (a_s), 15 (b_s), 16 (D_min), 17 (D_max), 18 (Filter)
#   1                 2    3         4           5          6     7    8     9    10   11   12   13    14   15   16    17    18
    head_x_accel  1.0  extremum  0   0.05  0.25  0.5  0.25  0.25  0.5  0.05    0.5  C:\Users\kryst\Desktop\THESIS\Data_Analysis\Python_Files\H_CORA_Analysis\Simulation_1\data\exp_stdev_head_x_accel.at   0    0    0.01  0.12    
  END SIGNALS
END LOADCASE

