""""
FMCW Wave Generation
"""
import matplotlib.pyplot as plt
from scipy.fft import rfft, irfft
import numpy as np
import math


class FMCWGeneration:
    """
    FMCW - Radar Frequency Modulated Continous Wave
    """
    def __init__(self):
        # Radar Specifications
        self.radar_specs = {
                            "frequency": 77e9,
                            "range": 200,
                            "resolution": 1,
                            "max_velocity": 100
                            }
        self.object_specs = {
                             "velocity": 40,
                             "position":100
                             }
        self.light_speed = 3e8
        self.sweep_time_factor = 5.5
        self.chirp_count = 128
        self.chirp_samples = 1024

    def generate_waveform(self):
        """
        Generate FMCW Waveform
        :return:
        """
        chirp_bandwidth = self.light_speed/(2*self.radar_specs["resolution"])
        chirp_time = (2*self.sweep_time_factor*self.radar_specs["range"])/(self.light_speed)
        slope = chirp_bandwidth/chirp_time
        timescale_step = (chirp_time * self.chirp_count)/(self.chirp_count * self.chirp_samples)
        timescale_stop = chirp_time * self.chirp_count
        timescale = np.linspace(0, (self.chirp_count*chirp_time), (self.chirp_count*self.chirp_samples))
        transmitted_signal = received_signal = mixed_signal = distance_covered = time_delay = np.zeros(len(timescale))
        for index in range(len(transmitted_signal)):
            distance_covered[index] = self.object_specs["position"] + self.object_specs["velocity"]*timescale[index]
            time_delay[index] = 2*distance_covered[index]/self.light_speed
            transmitted_signal[index] = np.cos(2*math.pi*(self.radar_specs["frequency"]*timescale[index] +
                                                          slope*(math.pow(timescale[index],2)/2)))
            time_diff = timescale[index] - time_delay[index]
            received_signal[index] = np.cos(2*math.pi*((self.radar_specs["frequency"]*time_diff) +
                                                       slope*(math.pow(time_diff, 2))/2))
            mixed_signal[index] = transmitted_signal[index]*received_signal[index]

        beat_signal = np.reshape(mixed_signal, [self.chirp_samples, self.chirp_count])
        # In python, DFT is calculated based on columns by default, that needs to be changed to row with axis = 0
        normalized_fft = np.fft.fft(beat_signal, self.chirp_samples, axis=0)
        signal_lenght = chirp_time*chirp_bandwidth
        absolute_fft = abs(normalized_fft/signal_lenght)
        one_side_fft = absolute_fft[1:int(signal_lenght/2)+1, 1]
        one_side_fft = np.reshape(one_side_fft, (1,-1))
        scale = chirp_bandwidth*np.arange(0, signal_lenght/2)/signal_lenght
        # Convert it into array shape of 1 x signal_lenght/2
        scale = np.reshape(scale, (1,-1))
        plt.plot(scale, one_side_fft)

        # plt.plot(timescale, transmitted_signal)
        # plt.plot(timescale, received_signal)
        plt.show()
        # plt.plot(normalized_fft)
        # plt.show()
    def run(self):
        """
        run all components
        :return:
        """
        self.generate_waveform()

if __name__ == "__main__":
    APPLICATION = FMCWGeneration()
    APPLICATION.run()

