# -*- coding: UTF-8 -*-
import time
import numpy
import matplotlib.pyplot as plt
import waveformthread as wft

class Degausser():
    def __init__(self, device, chnnr):
        self.device = device
        self.chnnr = chnnr

    def createNpWaveform(self, amp, freq, offset, duration, keeptime, sampleRate):
        '''create waveform from given parameters'''
        self.sampleRate = sampleRate
        t = numpy.linspace(0, duration, duration*sampleRate + 1)
        x = (-1) * numpy.sin( 2*numpy.math.pi * freq * t ) * numpy.piecewise(t, [t<keeptime, t>=keeptime], [amp, lambda t: -((t-keeptime) * amp/(duration-keeptime))+amp])
        self.periodLength = len( x )
        self.time = t
        self.data = numpy.zeros( (self.periodLength, ), dtype = numpy.float64)
        self.data = x

    def plotWaveform(self):
        plt.plot(self.time, self.data)
        plt.show()
        
    def playWaveform(self):
        mythread = wft.WaveformThread(self.device, self.chnnr, self.data, self.sampleRate, self.time)
        mythread.start()
        mythread.join()
