import pandas as pd

def peak_vertebra(sim):
    peak_values = {}
    for column in sim.vertebrae.columns:
        max_value = sim.vertebrae[column].max()
        time_at_max = sim.vertebrae[sim.vertebrae[column] == max_value].index[0]
        peak_values[column + " (degrees)"] = [round(max_value), round(time_at_max)]
    return peak_values

def compare_peak_vertebra(simulations):
    comparison = {}
    for sim in simulations:
        peak_values = peak_vertebra(sim)
        comparison[sim.label] = peak_values
    # Convert the dictionary to a DataFrame for easier manipulation and plotting
    comparison_df = pd.DataFrame.from_dict(comparison, orient='index')
    return comparison_df