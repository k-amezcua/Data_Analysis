import pandas as pd

def peak_vertebra_values(simulation):
    # Assuming simulation.discs is a list of Disc objects with processed data
    peak_values = []
    for vertebra in simulation.vertebrae:
        peak_rotation_C12 = vertebra.vertebrae['C12_Ry'].max()
        peak_rotation_C23 = vertebra.vertebrae['C23_Ry'].max()
        peak_rotation_C34 = vertebra.vertebrae['C34_Ry'].max()
        peak_rotation_C45 = vertebra.vertebrae['C45_Ry'].max()
        peak_rotation_C56 = vertebra.vertebrae['C56_Ry'].max()
        peak_rotation_C67 = vertebra.vertebrae['C67_Ry'].max()
        peak_rotation_C7T1 = vertebra.vertebrae['C7T1_Ry'].max()
        peak_values.append({'Vertebra': vertebra.name, 'Peak C12 Rotation': peak_rotation_C12, 'Peak C23 Rotation': peak_rotation_C23,
                            'Peak C34 Rotation': peak_rotation_C34, 'Peak C45 Rotation': peak_rotation_C45,
                            'Peak C56 Rotation': peak_rotation_C56, 'Peak C67 Rotation': peak_rotation_C67,
                            'Peak C7T1 Rotation': peak_rotation_C7T1
                            })
    return pd.DataFrame(peak_values)
def peak_disc_values(simulation):
    # Assuming simulation.discs is a list of Disc objects with processed data
    peak_values = []
    for disc in simulation.discs:
        peak_stress = disc.data['stress'].max()
        peak_strain = disc.data['strain'].max()
        peak_values.append({'Disc': disc.name, 'Peak Stress': peak_stress, 'Peak Strain': peak_strain})
    return pd.DataFrame(peak_values)

def peak_ligament_values(simulation):
    # Similar to peak_disc_values, but for ligaments
    peak_values = []
    for ligament in simulation.ligaments:
        peak_stress = ligament.data['stress'].max()
        peak_strain = ligament.data['strain'].max()
        peak_values.append({'Ligament': ligament.name, 'Peak Stress': peak_stress, 'Peak Strain': peak_strain})
    return pd.DataFrame(peak_values)

def peak_muscle_values(simulation):
    # Similar to peak_ligament_values, but for muscles
    peak_values = []
    for muscle in simulation.muscles:
        peak_stress = muscle.data['stress'].max()
        peak_strain = muscle.data['strain'].max()
        peak_values.append({'Muscle': muscle.name, 'Peak Stress': peak_stress, 'Peak Strain': peak_strain})
    return pd.DataFrame(peak_values)

# You can add more functions if needed for other tissues
