def create_dictionaries():

    disc_variables = ['Time', 's1', 's2', 's3', 'E1', 'E2', 'E3']

    disc_dict_list = [
        {'disc_name': 'C23_Anterior_Disc', 'disc_elements': 120},
        {'disc_name': 'C23_Posterior_Disc', 'disc_elements': 120},
        {'disc_name': 'C23_Middle_Disc', 'disc_elements': 240},
        {'disc_name': 'C34_Anterior_Disc', 'disc_elements': 144},
        {'disc_name': 'C34_Posterior_Disc', 'disc_elements': 144},
        {'disc_name': 'C34_Middle_Disc', 'disc_elements': 288},
        {'disc_name': 'C45_Anterior_Disc', 'disc_elements': 168},
        {'disc_name': 'C45_Posterior_Disc', 'disc_elements': 168},
        {'disc_name': 'C45_Middle_Disc', 'disc_elements': 336},
        {'disc_name': 'C56_Anterior_Disc', 'disc_elements': 144},
        {'disc_name': 'C56_Posterior_Disc', 'disc_elements': 144},
        {'disc_name': 'C56_Middle_Disc', 'disc_elements': 288},
        {'disc_name': 'C67_Anterior_Disc', 'disc_elements': 120},
        {'disc_name': 'C67_Posterior_Disc', 'disc_elements': 120},
        {'disc_name': 'C67_Middle_Disc', 'disc_elements': 240},
        {'disc_name': 'C7T1_Anterior_Disc', 'disc_elements': 144},
        {'disc_name': 'C7T1_Posterior_Disc', 'disc_elements': 144},
        {'disc_name': 'C7T1_Middle_Disc', 'disc_elements': 288}
    ]

    for disc_dict in disc_dict_list:
        disc_name = disc_dict['disc_name']
        disc_level = disc_name.split('_')[0]  # Assuming the level is the part before the first '_'
        disc_dict['disc_level'] = disc_level
        disc_dict['disc_variables'] = disc_variables

    # Define ligament information
    ligament_dict_list = [
        {'ligament_name': 'C01_AAOM', 'ligament_elements': 4},
        {'ligament_name': 'C01_JC', 'ligament_elements': 26},
        {'ligament_name': 'C01_PAOM', 'ligament_elements': 4},
        {'ligament_name': 'C02_ALAR', 'ligament_elements': 2},
        {'ligament_name': 'C02_APICAL', 'ligament_elements': 1},
        {'ligament_name': 'C02_TM', 'ligament_elements': 1},
        {'ligament_name': 'C02_TM_VC', 'ligament_elements': 4},
        {'ligament_name': 'C12_AAAM', 'ligament_elements': 6},
        {'ligament_name': 'C12_ISL', 'ligament_elements': 4},
        {'ligament_name': 'C12_JC', 'ligament_elements': 16},
        {'ligament_name': 'C12_PAAM', 'ligament_elements': 8},
        {'ligament_name': 'C12_TL', 'ligament_elements': 4},
        {'ligament_name': 'C23_ALL', 'ligament_elements': 4},
        {'ligament_name': 'C23_ISL', 'ligament_elements': 4},
        {'ligament_name': 'C23_JC', 'ligament_elements': 16},
        {'ligament_name': 'C23_LF', 'ligament_elements': 8},
        {'ligament_name': 'C23_PLL', 'ligament_elements': 4},
        {'ligament_name': 'C34_ALL', 'ligament_elements': 4},
        {'ligament_name': 'C34_ISL', 'ligament_elements': 4},
        {'ligament_name': 'C34_JC', 'ligament_elements': 16},
        {'ligament_name': 'C34_LF', 'ligament_elements': 8},
        {'ligament_name': 'C34_PLL', 'ligament_elements': 4},
        {'ligament_name': 'C45_ALL', 'ligament_elements': 4},
        {'ligament_name': 'C45_ISL', 'ligament_elements': 4},
        {'ligament_name': 'C45_JC', 'ligament_elements': 16},
        {'ligament_name': 'C45_LF', 'ligament_elements': 8},
        {'ligament_name': 'C45_PLL', 'ligament_elements': 4},
        {'ligament_name': 'C56_ALL', 'ligament_elements': 4},
        {'ligament_name': 'C56_ISL', 'ligament_elements': 4},
        {'ligament_name': 'C56_JC', 'ligament_elements': 16},
        {'ligament_name': 'C56_LF', 'ligament_elements': 8},
        {'ligament_name': 'C56_PLL', 'ligament_elements': 4},
        {'ligament_name': 'C67_ALL', 'ligament_elements': 4},
        {'ligament_name': 'C67_ISL', 'ligament_elements': 4},
        {'ligament_name': 'C67_JC', 'ligament_elements': 16},
        {'ligament_name': 'C67_LF', 'ligament_elements': 8},
        {'ligament_name': 'C67_PLL', 'ligament_elements': 4},
        {'ligament_name': 'C7T1_ALL', 'ligament_elements': 4},
        {'ligament_name': 'C7T1_ISL', 'ligament_elements': 4},
        {'ligament_name': 'C7T1_JC', 'ligament_elements': 16},
        {'ligament_name': 'C7T1_LF', 'ligament_elements': 8},
        {'ligament_name': 'C7T1_PLL', 'ligament_elements': 4}
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

    return disc_dict_list, ligament_dict_list, muscle_dict_list