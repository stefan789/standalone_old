import dodegauss as deg
import digiport as digiport
import collections
import copy
import time
'''
for i in anzahldurchgange:
    for coil in self.coils:
        dega.createNpWaveform(paramsfromself.coils)
        changeVoltageDivider
        activatecoil
        readcoilswitch
        if switch:
            dega.playWaveform
'''
class controldega():
    def __init__(self, coils):
        self.coils = coils
        dev = self.coils['Device']
        self.dega = deg.Degausser(str(dev),0)
        self.p0 = digiport.DigiPort("Dev1", 0)
        self.p0.off()

    def changeVoltageDivider(self, nrOn):
        pass

    def activateCoil(self, coilname):
        pass

    def readcoilswitch(self, coilname):
        pass

    def degauss(self):
        print "degauss"
        degcoils = copy.deepcopy(self.coils)
        offset = degcoils['Offset']
        degcoils.pop("Offset", None)
        degcoils.pop("Device")
        degcoils.pop("All")
        for coil in degcoils:
            amp = degcoils[coil]['Amp']
            freq = degcoils[coil]['Freq']
            dur = degcoils[coil]['Dur']
            keep = degcoils[coil]['Keep']

            self.dega.createNpWaveform(amp, freq, offset, dur, keep, 20000)
            self.dega.playWaveform()
            self.p0.on()
            time.sleep(0.2)
            self.p0.off()

