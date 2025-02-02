import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Function to calculate the frequency spectrum of the signal
def calculate_fft(signal, sampling_rate):
    n = len(signal)
    fft_values = fft(signal)
    freq = np.fft.fftfreq(n, 1/sampling_rate)
    magnitude = np.abs(fft_values)[:n//2]
    freq = freq[:n//2]
    return freq, magnitude

# Function to detect bearing faults based on frequency bands
def detect_bearing_fault(signal, sampling_rate, fault_threshold=0.1):
    # Get FFT of the signal
    freq, magnitude = calculate_fft(signal, sampling_rate)

    # Define fault frequencies (example: BPFI, BPFO, etc. - based on the bearing geometry)
    BPFI = 100  # Ball Pass Frequency Inner race (example value)
    BPFO = 50   # Ball Pass Frequency Outer race (example value)

    # Search for peaks in the frequency spectrum that match fault frequencies
    fault_frequencies = [BPFI, BPFO]
    for fault_freq in fault_frequencies:
        # Find closest frequency index
        idx = np.argmin(np.abs(freq - fault_freq))
        if magnitude[idx] > fault_threshold:
            print(f"Potential fault detected at {fault_freq} Hz.")
            return True
    print("No bearing fault detected.")
    return False

# Function to plot the frequency spectrum
def plot_frequency_spectrum(signal, sampling_rate):
    freq, magnitude = calculate_fft(signal, sampling_rate)
    plt.figure(figsize=(10, 6))
    plt.plot(freq, magnitude)
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()
