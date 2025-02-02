# Bearing Fault Detection

This project provides a method for detecting faults in bearings by analyzing vibration signal data. The detection is based on identifying characteristic fault frequencies in the frequency domain using the Fast Fourier Transform (FFT).

## Overview

The goal of this project is to analyze vibration data (e.g., from sensors attached to rotating machinery) to identify potential faults in the bearings. This is accomplished by:
1. Applying FFT to transform the vibration signal into the frequency domain.
2. Checking if certain fault frequencies (such as Ball Pass Frequency Outer race (BPFO), Ball Pass Frequency Inner race (BPFI), etc.) are present in the frequency spectrum.
3. If these fault frequencies are detected, it indicates a potential bearing fault.

## Files in the Repository

### 1. `bearing_fault_detection.py`

This file contains functions to process the vibration signal and detect faults.

- **`calculate_fft(signal, sampling_rate)`**: Computes the Fast Fourier Transform of the signal and returns the frequency and magnitude.
- **`detect_bearing_fault(signal, sampling_rate, fault_threshold=0.1)`**: Detects bearing faults by analyzing the frequency spectrum and checking for specific fault frequencies.
- **`plot_frequency_spectrum(signal, sampling_rate)`**: Visualizes the frequency spectrum of the vibration signal.

### 2. `main.py`

This is the main script for loading the vibration data, visualizing the frequency spectrum, and detecting bearing faults.

- It reads the vibration data from a CSV file (using `pandas`).
- It visualizes the frequency spectrum.
- It uses the `detect_bearing_fault` function from `bearing_fault_detection.py` to check for faults.

### 3. `vibration_data.csv`

A CSV file containing vibration data from a bearing sensor. The data should have a column named `vibration` with numerical vibration values.

## How to Run

1. **Install the required libraries:**
   You can install the necessary Python libraries by running:

   ```bash
   pip install numpy scipy matplotlib pandas
