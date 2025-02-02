import numpy as np
import pandas as pd
from bearing_fault_detection import detect_bearing_fault, plot_frequency_spectrum

# Example: Simulated vibration data (this should be replaced with real data)
def load_vibration_data(file_path):
    data = pd.read_csv(file_path)
    # Assuming the vibration data is in the 'vibration' column
    signal = data['vibration'].values
    sampling_rate = 1000  # Example: 1000 samples per second
    return signal, sampling_rate

def main():
    # Load the vibration data
    signal, sampling_rate = load_vibration_data("vibration_data.csv")

    # Plot frequency spectrum
    plot_frequency_spectrum(signal, sampling_rate)

    # Perform bearing fault detection
    fault_detected = detect_bearing_fault(signal, sampling_rate)
    if fault_detected:
        print("Bearing fault detected!")
    else:
        print("No bearing fault detected.")

if __name__ == "__main__":
    main()
