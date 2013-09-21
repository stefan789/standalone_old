import time
import numpy
import threading
import matplotlib.pyplot as plt

class Degausser(threading.Thread):
    def __init__(self, device, chnnr):
        '''
        initialize NI DAQ Driver, create Task and Channel
        '''
        self.taskHandle = TaskHandle( 0 )
        dev = str(device) + "/" + "ao" + str(chnnr)
        self.CHK(nidaq.DAQmxCreateTask("", ctypes.byref( self.taskHandle )))
        self.CHK(nidaq.DAQmxCreateAOVoltageChan( self.taskHandle, dev, "", float64(-10.0), float64(10.0), DAQmx_Val_Volts, None))
        threading.Thread.__init__(self)


    def CHK(self, err):
        '''a simple error checking routine'''
        if err < 0:
            buf_size = 100
            buf = ctypes.create_string_buffer('\000' * buf_size)
            nidaq.DAQmxGetErrorString(err, ctypes.byref(buf), buf_size)
            raise RuntimeError('nidaq failed with error %d: %s'%(err, repr(buf.value)))
        if err > 0:
            buf_size = 100
            buf = ctypes.create_string_buffer('\000' * buf_size)
            nidaq.DAQmxGetErrorString(err, ctypes.byref(buf), buf_size)
            raise RuntimeError('nidaq generated waring %d: %s'%(err, repr(buf.value)))


    def createWaveform(self, amp, freq, offset, duration, keeptime, sampleRate):
        '''create waveform from given parameters'''
        self.sampleRate = sampleRate
        t = numpy.arange( 0, duration, 1.0/self.sampleRate )
        x = numpy.piecewise( t, [t < keeptime, t >= keeptime], [amp, (amp - (amp/(duration- keeptime))*t) ] * (-1) * numpy.sin( 2*numpy.math.pi * freq * t )) + offset
        self.periodLength = len( x )
        self.time = t

        '''create Timing and set Waveform''' 
        self.data = numpy.zeros( (self.periodLength, ), dtype = numpy.float64)
        self.data = x
        self.CHK(nidaq.DAQmxCFGSampClkTiming( self.taskHandle, "", float64(self.sampleRate), DAQmx_Val_Rising, DAQmx_Val_FiniteSamps, uInt64(self.periodLength)))
        self.CHK(nidaq.DAQmxWriteAnalogF64( self.taskHandle, int32(self.periodLength), 0, float64(-1), DAQmx_Val_GroupByChannel, self.data.ctypes.data, None, None))
        
    
    def plotWaveform(self):
        '''use matplotlib'''
        plt.plot(self.time, self.data)
        plt.show()

# run method called when Degausser.start() called
    def run(self):
        self.CHK(nidaq.DAQmxStartTask( self.taskHandle ))

    def stop(self):
        nidaq.DAQmxStopTask( self.taskHandle )

    def clear(self):
        nidaq.DAQmxClearTask( self.taskHandle )


