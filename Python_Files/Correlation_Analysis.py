import pandas as pd

file_name = r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\Analysis\Parametric Study Summary.csv"
df = pd.read_csv(file_name)

df.dropna(inplace=True)

print(df)

# Calculate correlation coefficients
correlation_matrix = df.corr()

# Display correlation matrix
print(correlation_matrix)

import seaborn as sns
import matplotlib.pyplot as plt

# Plot heatmap of correlation matrix
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Adjust layout to prevent cutoff of x-axis labels
plt.tight_layout()

# Show plot
plt.show()
plt.title('Correlation Heatmap')
plt.show()
