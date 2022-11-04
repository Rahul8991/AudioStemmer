import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.io import wavfile
import os

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)

BASE_DIR = r"C:/Users/Rahul/Desktop/NLP/stemming/"
car_file = "car.wav"

audio_file = os.path.join(BASE_DIR, car_file)
sampFreq, sound = wavfile.read(audio_file)

plt.figure()
plt.plot(sound)
plt.xlabel("Sample Index #")
plt.ylabel("Amplitude")
plt.title("Waveform of Test Audio")


car_ft = np.fft.fft(sound)


def plot_magnitude_spectrum(signal, title, sr, f_ratio=1):  # sr-->sampling_rate
    ft = np.fft.fft(signal)
    magnitude_spectrum = np.abs(ft)

    plt.figure(figsize=(10, 5))

    frequency = np.linspace(0, sr, len(magnitude_spectrum))
    num_frequency_bins = int(len(frequency)*f_ratio)

    plt.plot(frequency[:num_frequency_bins],
             magnitude_spectrum[:num_frequency_bins])
    plt.xlabel("Frequency (Hz)")
    plt.title(title)

    plt.show()


plot_magnitude_spectrum(sound, "Car", sampFreq, 0.1)
