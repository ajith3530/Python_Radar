""""
FMCW Wave Generation
"""

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
        self.light_speed = 3e8
        self.object_specs = {
                             "intial_velocity": 40,
                             "initial_position":100
                             }

    def generate_waveform(self):
        """
        Generate FMCW Waveform
        :return:
        """
        pass

    def run(self):
        """
        run all components
        :return:
        """
        pass

if __name__ == "__main__":
    APPLICATION = FMCWGeneration()
    APPLICATION.run()

