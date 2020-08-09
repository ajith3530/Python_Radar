""""
FMCW Wave Generation
"""
import matplotlib.pyplot as plt
from scipy.fft import rfft, irfft
import numpy as np
import math

# Radar parameters
radar_freq = 77e9
radar_range = 200
radar_resolution = 1
radar_velocity = 100

# Object parameters
object_velocity = 40
object_position = 70

# general parameters
light_speed = 3e8
sweep_time_factor = 5.5
chirp_count = 128
chirp_samples = 1024
Nd = 128
Nr = 1024

class FMCWGeneration:
    """
    FMCW - Radar Frequency Modulated Continous Wave
    """
    def __init__(self):
        pass


    def generate_waveform(self):
        """
        Generate FMCW Waveform
        :return:
        """
        chirp_bandwidth = light_speed / (2 * radar_resolution)
        sweep_factor = 5.5
        t_chirp = (sweep_time_factor * 2 * radar_range) / light_speed
        slope = chirp_bandwidth / t_chirp
        t = np.linspace(0, Nd * t_chirp, Nr * Nd)
        t_len = len(t)
        tx = np.zeros(t_len)
        rx = np.zeros(t_len)
        mix = np.zeros(t_len)
        tau = np.zeros(t_len)
        td = np.zeros(t_len)
        for index in range(t_len):
            tau[index] = object_position + (object_velocity * t[index])
            td[index] = 2 * tau[index] / light_speed
            tx[index] = np.cos(2 * np.pi * (radar_freq * t[index] + slope * math.pow(t[index], 2) / 2))
            dt = t[index] - td[index]
            rx[index] = np.cos(2 * np.pi * (radar_freq * dt + slope * math.pow(dt, 2) / 2))
            mix[index] = tx[index] * rx[index]
        # Calculating FFT
        mix_fft = np.fft.fft(mix)
        abs_fft = np.abs(mix_fft/t_len)
        real_fft = abs_fft[0:len(abs_fft)//2]
        freq_scale = chirp_bandwidth * np.arange(0,(t_len//2))/t_len
        range_scale = (light_speed * t_chirp*freq_scale)/(2 * chirp_bandwidth)
        # plt.plot(freq_scale, real_fft)
        # plt.show()
        plt.plot(range_scale, real_fft)
        plt.show()

    def run(self):
        """
        run all components
        :return:
        """
        self.generate_waveform()

if __name__ == "__main__":
    APPLICATION = FMCWGeneration()
    APPLICATION.run()

