

# Load data from CSV
path = r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors Only\Kinematics Data\head_aRy.csv"

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Load data from CSV and parse dates
data = pd.read_csv(path, parse_dates=[0], index_col=0)

# Inspect data
print(data.head())  # First few rows
print(data.describe())  # Statistical summary

# Clean data: handle erroneous data
data['head_rot_acc'] = pd.to_numeric(data['head_rot_acc'], errors='coerce')
cleaned_data = data.dropna()

# Filter out outliers using Z-score
z_scores = np.abs(stats.zscore(cleaned_data['head_rot_acc']))
filtered_data = cleaned_data[z_scores < 3]  # Z-score cutoff of 3

# Normalize data (optional)
normalized_data = (cleaned_data - cleaned_data.mean()) / cleaned_data.std()

# Visualize original and filtered data
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(data.index, data['head_rot_acc'], color='blue')
plt.title('Original Data')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.plot(filtered_data.index, filtered_data['head_rot_acc'], color='green')
plt.title('Filtered Data')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

filtered_path = r"C:\Users\kryst\Desktop\THESIS\00 Parameter Study\0pt2 max muscle force\Active\00 ms delay\Active - Flexors Only\Kinematics Data\filtered_head_aRy.csv"

# Save the filtered data
filtered_data.to_csv(filtered_path)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt
import pywt

# Load and clean your data
data = pd.read_csv(path, parse_dates=[0], index_col=0)
data['head_rot_acc'] = pd.to_numeric(data['head_rot_acc'], errors='coerce')
cleaned_data = data.dropna()

# Simple Moving Average
sma_data = cleaned_data['head_rot_acc'].rolling(window=10).mean()

# Exponential Moving Average
ema_data = cleaned_data['head_rot_acc'].ewm(span=10, adjust=False).mean()

# Butterworth Low-pass Filter
N, Wn = 2, 0.1  # Filter order and cutoff frequency
B, A = butter(N, Wn, output='ba')
butter_data = filtfilt(B, A, cleaned_data['head_rot_acc'])

# Wavelet Denoising
coeffs = pywt.wavedec(cleaned_data['head_rot_acc'], 'db1', mode='per')
threshold = 0.3 * max(coeffs[1])
coeffs[1:] = [pywt.threshold(i, value=threshold, mode='soft') for i in coeffs[1:]]
wavelet_data = pywt.waverec(coeffs, 'db1')

# Create a figure and axis objects
fig, axs = plt.subplots(4, 1, figsize=(10, 16), sharex=True)

# Original Data
axs[0].plot(cleaned_data.index, cleaned_data['head_rot_acc'], label='Original', color='blue')
axs[0].set_title('Original Data')
axs[0].legend()

# Simple Moving Average
axs[1].plot(cleaned_data.index, sma_data, label='SMA (Window 10)', color='red')
axs[1].set_title('Simple Moving Average')
axs[1].legend()

# Exponential Moving Average
axs[2].plot(cleaned_data.index, ema_data, label='EMA (Span 10)', color='green')
axs[2].set_title('Exponential Moving Average')
axs[2].legend()

# Butterworth Filter
axs[3].plot(cleaned_data.index, butter_data, label='Butterworth Low-pass', color='purple')
axs[3].set_title('Butterworth Low-pass Filter')
axs[3].legend()

# Uncomment the following lines if you wish to add Wavelet Denoising to the subplots
# axs[4].plot(cleaned_data.index, wavelet_data, label='Wavelet Denoising', color='orange')
# axs[4].set_title('Wavelet Denoising')
# axs[4].legend()

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

import pandas as pd
import numpy as np

# Load your data
# Assuming 'data.csv' has two columns: 'Time' and 'Data'
data = pd.read_csv(path)
time = data['time']
signal = data['head_rot_acc']

import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# Convert time format if necessary
# Uncomment the following line if 'Time' is a datetime string
# time = pd.to_datetime(time)  # Convert if 'Time' is in a string format
# time = (time - time.min()).dt.total_seconds()  # Normalize time to seconds since start

# Check for duplicate time entries and resolve them
if time.duplicated().any():
    print("Duplicates found in time data. Resolving by averaging data points.")
    data = data.groupby('time', as_index=False).mean()  # Average data points with the same timestamp
    time = data['time']
    signal = data['head_rot_acc']

# Calculate sampling rate
sampling_interval = np.mean(np.diff(time))
if sampling_interval <= 0:
    raise ValueError("Calculated sampling interval is non-positive, check your time data.")

sampling_rate = 1 / sampling_interval

# Define cutoff frequency using SAE 600 specs
cutoff_multiplier = 1000  # SAE 600 standard
tsf = 1  # Time scale factor, adjust this based on your time scale
cutoff_frequency = cutoff_multiplier * tsf / sampling_rate

# Normalize cutoff frequency by the Nyquist frequency
nyquist = 0.5 * sampling_rate
normalized_cutoff = cutoff_frequency / nyquist

# Ensure the normalized cutoff frequency is valid
if not 0 < normalized_cutoff < 1:
    raise ValueError(f"Normalized cutoff frequency is out of range: {normalized_cutoff}. It must be between 0 and 1.")

# Create the Butterworth filter
b, a = butter(N=2, Wn=normalized_cutoff, btype='low', analog=False)

# Apply the filter
filtered_signal = filtfilt(b, a, signal)

# # Plotting the results
# plt.figure(figsize=(10, 5))
# plt.plot(time, signal, label='Original Data', color='blue')
# plt.plot(time, filtered_signal, label='Filtered Data', color='red')
# plt.title('Comparison of Original and SAE 600 Filtered Data')
# plt.xlabel('Time (s)')
# plt.ylabel('Data')
# plt.legend()
# plt.show()
import matplotlib.pyplot as plt

# After you have your original and filtered signal data...
# Assuming 'time', 'signal', and 'filtered_signal' are defined and properly computed

# Create subplots with 1 row and 2 columns
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Plot original data on the first subplot
axs[0].plot(time, signal, label='Original Data', color='blue')
axs[0].set_title('Original Data')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Data')
axs[0].legend()

# Plot filtered data on the second subplot
axs[1].plot(time, filtered_signal, label='Filtered Data (SAE 600)', color='red')
axs[1].set_title('Filtered Data (SAE 600)')
axs[1].set_xlabel('Time (s)')
# axs[1].set_ylabel('Data')  # Optionally, you can skip this line since y-axis is shared
axs[1].legend()

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
