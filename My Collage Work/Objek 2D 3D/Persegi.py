 
class persegi(object):

    def __init__(self, sisi=int(input("sisi = "))):
        self.sisi = sisi

    def keliling(self):
        return(self.sisi*4)

    def luas(self):
        return(self.sisi**2)
