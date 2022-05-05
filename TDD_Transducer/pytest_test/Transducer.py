
class TransducerTest:
    def __init__(self):
        self.volt = ''
        self.pump = ''
        self.Psi = 0
        self.VExp = 0

    def setReciever(self, volt):
        self.volt = volt
        if volt == 'DC':
            return 'DC'
        if volt == 'AC':
            return 'AC'
        else:
            return 'No Connection'

    def turnOnPump(self, pump):
        self.pump = pump

        if pump == 'on':
            return 'on'


    def incPsi(self, Psi):
        self.Psi = Psi
        while Psi <= 50:
            Psi += 0.1
            return 'pass'

    def VExpected(self, VExp, Psi):
        self.VExp = VExp
        self.Psi = Psi
        while VExp <= 5:
            VExp += Psi * 0.1
            Psi += 0.1
            return 'pass'


    def turnOffPump(self, pump):
        self.pump = pump

        if pump == 'off':
            return 'off'



