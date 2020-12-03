class lingkaran(object):

    def __init__(self, phi=3.14):
        self.phi = phi

    def luas_lingkaran(self, input_diameter):
        rumus = self.phi*(0.5*input_diameter)*(0.5*input_diameter)
        return(rumus)

    def keliling_lingkaran(self, input_diameter):
        rumus = self.phi*(0.5*input_diameter)*2
        return(rumus)
