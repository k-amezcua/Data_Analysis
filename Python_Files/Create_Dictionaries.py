def create_dictionaries():

    disc_variables = ['Time', 's1', 's2', 's3', 'E1', 'E2', 'E3']

    disc_dict_list = [
        {'disc_name': 'C23_Anterior_Disc', 'disc_elements': 120, 'disc_region': 'anterior'},
        {'disc_name': 'C23_Posterior_Disc', 'disc_elements': 120, 'disc_region': 'posterior'},
        {'disc_name': 'C23_Middle_Disc', 'disc_elements': 240, 'disc_region': 'middle'},
        {'disc_name': 'C34_Anterior_Disc', 'disc_elements': 144, 'disc_region': 'anterior'},
        {'disc_name': 'C34_Posterior_Disc', 'disc_elements': 144, 'disc_region': 'posterior'},
        {'disc_name': 'C34_Middle_Disc', 'disc_elements': 288, 'disc_region': 'middle'},
        {'disc_name': 'C45_Anterior_Disc', 'disc_elements': 168, 'disc_region': 'anterior'},
        {'disc_name': 'C45_Posterior_Disc', 'disc_elements': 168, 'disc_region': 'posterior'},
        {'disc_name': 'C45_Middle_Disc', 'disc_elements': 336, 'disc_region': 'middle'},
        {'disc_name': 'C56_Anterior_Disc', 'disc_elements': 144, 'disc_region': 'anterior'},
        {'disc_name': 'C56_Posterior_Disc', 'disc_elements': 144, 'disc_region': 'posterior'},
        {'disc_name': 'C56_Middle_Disc', 'disc_elements': 288, 'disc_region': 'middle'},
        {'disc_name': 'C67_Anterior_Disc', 'disc_elements': 120, 'disc_region': 'anterior'},
        {'disc_name': 'C67_Posterior_Disc', 'disc_elements': 120, 'disc_region': 'posterior'},
        {'disc_name': 'C67_Middle_Disc', 'disc_elements': 240, 'disc_region': 'middle'},
        {'disc_name': 'C7T1_Anterior_Disc', 'disc_elements': 144, 'disc_region': 'anterior'},
        {'disc_name': 'C7T1_Posterior_Disc', 'disc_elements': 144, 'disc_region': 'posterior'},
        {'disc_name': 'C7T1_Middle_Disc', 'disc_elements': 288, 'disc_region': 'middle'}
    ]

    for disc_dict in disc_dict_list:
        disc_name = disc_dict['disc_name']
        disc_level = disc_name.split('_')[0]
        disc_region = disc_dict['disc_region'] # Assuming the level is the part before the first '_'
        disc_dict['disc_level'] = disc_level
        disc_dict['disc_variables'] = disc_variables
        disc_dict['disc_region'] = disc_region

    ALL_failure_force = 354.3
    PLL_failure_force = 339.2
    LF_failure_force = 246.7
    ISL_failure_force = 66.1
    JC_failure_force = 190
    AAOM_failure_force = 1024
    PAOM_failure_force = 354
    C01_JC_failure_force = 1186
    C12_JC_failure_force = 662
    Apical_failure_force = 251.5
    Alar_failure_force = 251.5
    VC_failure_force = 251.5
    TM_failure_force = 251.5
    TL_failure_force = 392
    AAAM_failure_force = 1068
    PAAM_failure_force = 97

    # Define ligament information
    ligament_dict_list = [
        {'ligament_name': 'C01_AAOM', 'ligament_elements': 4, 'failure_force': AAOM_failure_force},
        {'ligament_name': 'C01_JC', 'ligament_elements': 26, 'failure_force': C01_JC_failure_force},
        {'ligament_name': 'C01_PAOM', 'ligament_elements': 4, 'failure_force': PAOM_failure_force},
        {'ligament_name': 'C02_ALAR', 'ligament_elements': 2, 'failure_force': Alar_failure_force},
        {'ligament_name': 'C02_APICAL', 'ligament_elements': 1, 'failure_force': Apical_failure_force},
        {'ligament_name': 'C02_TM', 'ligament_elements': 1, 'failure_force': TM_failure_force},
        {'ligament_name': 'C02_TM_VC', 'ligament_elements': 4, 'failure_force': VC_failure_force},
        {'ligament_name': 'C12_AAAM', 'ligament_elements': 6, 'failure_force': AAAM_failure_force},
        {'ligament_name': 'C12_ISL', 'ligament_elements': 4, 'failure_force': ISL_failure_force},
        {'ligament_name': 'C12_JC', 'ligament_elements': 16, 'failure_force': C12_JC_failure_force},
        {'ligament_name': 'C12_PAAM', 'ligament_elements': 8, 'failure_force': PAAM_failure_force},
        {'ligament_name': 'C12_TL', 'ligament_elements': 4, 'failure_force': TL_failure_force},
        {'ligament_name': 'C23_ALL', 'ligament_elements': 4, 'failure_force': ALL_failure_force},
        {'ligament_name': 'C23_ISL', 'ligament_elements': 4, 'failure_force': ISL_failure_force},
        {'ligament_name': 'C23_JC', 'ligament_elements': 16, 'failure_force': JC_failure_force},
        {'ligament_name': 'C23_LF', 'ligament_elements': 8, 'failure_force': LF_failure_force},
        {'ligament_name': 'C23_PLL', 'ligament_elements': 4, 'failure_force': PLL_failure_force},
        {'ligament_name': 'C34_ALL', 'ligament_elements': 4, 'failure_force': ALL_failure_force},
        {'ligament_name': 'C34_ISL', 'ligament_elements': 4, 'failure_force': ISL_failure_force},
        {'ligament_name': 'C34_JC', 'ligament_elements': 16, 'failure_force': JC_failure_force},
        {'ligament_name': 'C34_LF', 'ligament_elements': 8, 'failure_force': LF_failure_force},
        {'ligament_name': 'C34_PLL', 'ligament_elements': 4, 'failure_force': PLL_failure_force},
        {'ligament_name': 'C45_ALL', 'ligament_elements': 4, 'failure_force': ALL_failure_force},
        {'ligament_name': 'C45_ISL', 'ligament_elements': 4, 'failure_force': ISL_failure_force},
        {'ligament_name': 'C45_JC', 'ligament_elements': 16, 'failure_force': JC_failure_force},
        {'ligament_name': 'C45_LF', 'ligament_elements': 8, 'failure_force': LF_failure_force},
        {'ligament_name': 'C45_PLL', 'ligament_elements': 4, 'failure_force': PLL_failure_force},
        {'ligament_name': 'C56_ALL', 'ligament_elements': 4, 'failure_force': ALL_failure_force},
        {'ligament_name': 'C56_ISL', 'ligament_elements': 4, 'failure_force': ISL_failure_force},
        {'ligament_name': 'C56_JC', 'ligament_elements': 16, 'failure_force': JC_failure_force},
        {'ligament_name': 'C56_LF', 'ligament_elements': 8, 'failure_force': LF_failure_force},
        {'ligament_name': 'C56_PLL', 'ligament_elements': 4, 'failure_force': PLL_failure_force},
        {'ligament_name': 'C67_ALL', 'ligament_elements': 4, 'failure_force': ALL_failure_force},
        {'ligament_name': 'C67_ISL', 'ligament_elements': 4, 'failure_force': ISL_failure_force},
        {'ligament_name': 'C67_JC', 'ligament_elements': 16, 'failure_force': JC_failure_force},
        {'ligament_name': 'C67_LF', 'ligament_elements': 8, 'failure_force': LF_failure_force},
        {'ligament_name': 'C67_PLL', 'ligament_elements': 4, 'failure_force': PLL_failure_force},
        {'ligament_name': 'C7T1_ALL', 'ligament_elements': 4, 'failure_force': ALL_failure_force},
        {'ligament_name': 'C7T1_ISL', 'ligament_elements': 4, 'failure_force': ISL_failure_force},
        {'ligament_name': 'C7T1_JC', 'ligament_elements': 16, 'failure_force': JC_failure_force},
        {'ligament_name': 'C7T1_LF', 'ligament_elements': 8, 'failure_force': LF_failure_force},
        {'ligament_name': 'C7T1_PLL', 'ligament_elements': 4, 'failure_force': PLL_failure_force}
        # Add more ligament information as needed
    ]

    for disc_dict in disc_dict_list:
        disc_dict['disc_variables'] = disc_variables

    # Define ligament information
    muscle_dict_list = [
        {'muscle_name': 'Anterior_Scalene', 'muscle_group': 'flexor', 'muscle_elements': 8},
        {'muscle_name': 'Iliocostalis_Cervicis', 'muscle_group': 'extensor', 'muscle_elements': 6},
        {'muscle_name': 'Levator_Scapulae', 'muscle_group': 'extensor', 'muscle_elements': 8},
        {'muscle_name': 'Longissimus_Capitis', 'muscle_group': 'extensor', 'muscle_elements': 16},
        {'muscle_name': 'Longissimus_Cervicis', 'muscle_group': 'extensor', 'muscle_elements': 18},
        {'muscle_name': 'Longus_Capitis', 'muscle_group': 'extensor', 'muscle_elements': 12},
        {'muscle_name': 'Longus_Colli_Inferior', 'muscle_group': 'flexor', 'muscle_elements': 8},
        {'muscle_name': 'Longus_Colli_Superior', 'muscle_group': 'flexor', 'muscle_elements': 8},
        {'muscle_name': 'Longus_Colli_Vertical', 'muscle_group': 'flexor', 'muscle_elements': 16},
        {'muscle_name': 'Middle_Scalene', 'muscle_group': 'flexor', 'muscle_elements': 12},
        {'muscle_name': 'Minor_Rhomboid', 'muscle_group': 'extensor', 'muscle_elements': 4},
        {'muscle_name': 'Multifidus', 'muscle_group': 'extensor', 'muscle_elements': 12},
        {'muscle_name': 'Oblique_Capitis_Inferior', 'muscle_group': 'extensor', 'muscle_elements': 2},
        {'muscle_name': 'Oblique_Capitis_Superior', 'muscle_group': 'extensor', 'muscle_elements': 2},
        {'muscle_name': 'Omohyoid', 'muscle_group': 'flexor', 'muscle_elements': 2},
        {'muscle_name': 'Posterior_Scalene', 'muscle_group': 'flexor', 'muscle_elements': 6},
        {'muscle_name': 'RCPM', 'muscle_group': 'extensor', 'muscle_elements': 2},
        {'muscle_name': 'RCPminor', 'muscle_group': 'extensor', 'muscle_elements': 2},
        {'muscle_name': 'Rectus_Capitis_Anterior', 'muscle_group': 'flexor', 'muscle_elements': 2},
        {'muscle_name': 'Rectus_Capitis_Lateralis', 'muscle_group': 'flexor', 'muscle_elements': 2},
        {'muscle_name': 'SCM', 'muscle_group': 'flexor', 'muscle_elements': 2},
        {'muscle_name': 'Semispinalis_Capitis', 'muscle_group': 'extensor', 'muscle_elements': 20},
        {'muscle_name': 'Semispinalis_Cervicis', 'muscle_group': 'extensor', 'muscle_elements': 12},
        {'muscle_name': 'Splenius_Capitis', 'muscle_group': 'extensor', 'muscle_elements': 2},
        {'muscle_name': 'Splenius_Cervicis', 'muscle_group': 'extensor', 'muscle_elements': 12},
        {'muscle_name': 'Sternohyoid', 'muscle_group': 'flexor', 'muscle_elements': 2},
        {'muscle_name': 'Trapezius', 'muscle_group': 'extensor', 'muscle_elements': 16},
    ]

    for muscle_dict in muscle_dict_list:
        muscle_dict['failure_strain'] = 0.30

    return disc_dict_list, ligament_dict_list, muscle_dict_list