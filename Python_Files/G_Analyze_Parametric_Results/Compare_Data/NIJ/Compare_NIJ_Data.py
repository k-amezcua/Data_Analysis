import matplotlib.pyplot as plt


def compare_nij_data(simulations):
    # Create subplots: one for NIJ over time, one for My vs. Fz
    fig, axs = plt.subplots(1, 2, figsize=(24, 12))

    # Plot NIJ data and My vs. Fz for each simulation
    for sim in simulations:
        if hasattr(sim, 'nij') and sim.nij is not None:
            # Retrieve critical values from the simulation's nij_injury_criterion dictionary
            Fcrit_tension = sim.nij_injury_criterion['Fcrit_tension']
            Fcrit_compression = sim.nij_injury_criterion['Fcrit_compression']
            Mcrit_flexion = sim.nij_injury_criterion['Mcrit_flexion']
            Mcrit_extension = sim.nij_injury_criterion['Mcrit_extension']

            # Define the critical force and moment lines
            x = [Mcrit_extension, 0, Mcrit_flexion]
            y_upper = [0, Fcrit_tension, 0]
            y_lower = [0, Fcrit_compression, 0]

            # Plot NIJ values over time
            axs[0].plot(sim.nij['Sim_Time_s'], sim.nij['NIJ'], label=f'{sim.label} NIJ')

            # Plot My vs. Fz
            axs[1].plot(sim.nij['My'], sim.nij['Fz'], marker='o', linestyle=' ', label=f'{sim.label} My vs. Fz')

    # Add critical force and moment lines to My vs. Fz plot
    axs[1].plot(x, y_upper, marker='o', linestyle='--', color='b')
    axs[1].plot(x, y_lower, marker='o', linestyle='--', color='b')

    # Set titles, labels, legends, etc.
    axs[0].set_title('NIJ')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('NIJ')
    axs[0].legend()
    axs[0].grid(True)

    axs[1].set_title('NIJ')
    axs[1].set_xlabel('My (Nm)')
    axs[1].set_ylabel('Fz (N)')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.savefig('NIJ_Comparison.png')
    plt.close()

