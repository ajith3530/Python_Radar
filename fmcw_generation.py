""""
FMCW Wave Generation
"""
import matplotlib.pyplot as plt
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
        self.chirp_count = 8
        self.chirp_samples = 128

    def generate_waveform(self):
        """
        Generate FMCW Waveform
        :return:
        """
        chirp_bandwidth = self.light_speed/(2*self.radar_specs["resolution"])
        chirp_time = (2*self.sweep_time_factor*self.radar_specs["range"])/(self.light_speed)
        slope = chirp_bandwidth/chirp_time
        timescale = np.arange(0 , chirp_time * self.chirp_count, (chirp_time * self.chirp_count)/(self.chirp_count * self.chirp_samples)).astype(dtype=float)
        transmitted_signal = received_signal = distance_covered = time_delay = np.zeros(len(timescale))
        for index in range(len(transmitted_signal)):
            distance_covered[index] = self.object_specs["position"] + self.object_specs["velocity"]*timescale[index]
            time_delay[index] = 2*distance_covered[index]/self.light_speed
            transmitted_signal[index] = math.cos(2*math.pi*(self.radar_specs["frequency"]*timescale[index] + slope*(math.pow(timescale[index],2)/2 )))

        plt.plot(transmitted_signal)
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

