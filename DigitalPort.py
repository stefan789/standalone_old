# import system libraries
import ctypes
    #"""module, that enables Python to read C++_Code. Is needed to communicate with the NI-device."""
import numpy
    #"""adds support for large multidim. arrays and matricesand contains an library of high-level mathematical funktions"""
import threading
    #"""Module that provids primitives for working with multible threads/tasks(tasks run simultaneously with the main programm)"""
# import matplotlib.pyplot as plt

# load any DLLs
nidaq = ctypes.windll.nicaiu
    # load the DLL (Dynamic Link Library) (is used to identify the NI code)

##############################
# Setup some typedefs and constants
# to correspond with values in
# C:\Program Files\National Instruments\NI-DAQ\DAQmx ANSI C Dev\include\NIDAQmx.h
# the typedefs
int32 = ctypes.c_long #"""Represents the C signed long datatype(long signed integer type. At least 32 bits in size.)The constructor accepts an optional integer initializer;no overflow checking is done."""
uInt32 = ctypes.c_ulong #"""Represents the C unsigned long datatype.(unsigned integer type. At least 32 bits in size.)The constructor accepts an optional integer initializer;no overflow checking is done."""
uInt64 = ctypes.c_ulonglong #"""Represents the C unsigned long long datatype.unsigned integer type. At least 64 bits in size)The constructor accepts an optional integer initializer;no overflow checking is done. """
float64 = ctypes.c_double #""" Represents the C double datatype.(double precision floating-point type. Actual properties unspecified)The constructor accepts an optional float initializer."""
TaskHandle = uInt32 #""" Represents the C 64-bit signed int datatype.(basic signed integer type. At least 16 bits in size.)Usually an alias for c_longlong."""
# the constants
DAQmx_Val_Cfg_Default = int32(-1)
DAQmx_Val_Volts = 10348
DAQmx_Val_Rising = 10280
DAQmx_Val_FiniteSamps = 10178
DAQmx_Val_ContSamps = 10123
DAQmx_Val_GroupByChannel = 0
DAQmx_Val_ChanForAllLines = 1
DAQmx_Val_ChanPerLine = 0
##############################

class DigitalPort( threading.Thread ):
    """
    This class performs the necessary initialization of the DAQ hardware and
    is used to change the relays. 
    It takes as input arguments
    -- the port number
    -- and the Status of the Digital port (on or off).
    These relays are used to swith the inductors of the protective barrier.
    """
    
    def __init__(self, deviceame, portnr): #initialisation of the NI-device used to switch the relays
        self.running = True
        self.output = 1
        self.port = 0
        
        self.taskHandle = TaskHandle( 0 )
        self.data = numpy.array([1])

        channel = str(devicename) + "/port" + str(portnr) + "/line0" #defines the device, channel and line used to change the relay.

        
        # setup the DAQ hardware
        self.CHK(nidaq.DAQmxCreateTask("",
                          ctypes.byref( self.taskHandle )))
        self.CHK(nidaq.DAQmxCreateDOChan( self.taskHandle,
                                   channel,
                                   "",
                                   DAQmx_Val_ChanPerLine))
        self.CHK(nidaq.DAQmxWriteDigitalU32( self.taskHandle,
                              1,
                              1,
                              float64(10.0),
                              DAQmx_Val_GroupByChannel,
                              self.data.ctypes.data,
                              None,
                              None))
        threading.Thread.__init__( self )


    def CHK( self, err ):
        """a simple error checking routine"""

        if err < 0:
            buf_size = 100
            buf = ctypes.create_string_buffer('\000' * buf_size)
            nidaq.DAQmxGetErrorString(err,ctypes.byref(buf),buf_size)
            raise RuntimeError('nidaq call failed with error %d: %s'%(err,repr(buf.value)))

        if err > 0:
            buf_size = 100
            buf = ctypes.create_string_buffer('\000' * buf_size)
            nidaq.DAQmxGetErrorString(err,ctypes.byref(buf),buf_size)
            raise RuntimeError('nidaq generated warning %d: %s'%(err,repr(buf.value)))


    def setState(self, state): #simple funktion to swith the relays on or off

        if state == PowerOn:
            self.data = numpy.array(0)

        elif state == PowerOff:
            self.data = numpy.array(1)

        self.CHK(nidaq.DAQmxWriteDigitalU32( self.taskHandle,
                              1,
                              1,
                              float64(10.0),
                              DAQmx_Val_GroupByChannel,
                              self.data.ctypes.data,
                              None,
                              None))

            

if __name__ == "__main__":
    output = 1
    
    PowerOn = 0
    PowerOff = 1

    #Devicenumber = 2
    
    #inductor_1 = SwitchRelay( Devicenumber, 0 )
    #inductor_2 = SwitchRelay( Devicenumber, 1 )
    #inductor_3 = SwitchRelay( Devicenumber, 2 )
    #inductor_4 = SwitchRelay( Devicenumber, 3 )
    #inductor_5 = SwitchRelay( Devicenumber, 4 )
    #inductor_6 = SwitchRelay( Devicenumber, 5 )
    #inductor_7 = SwitchRelay( Devicenumber, 6 )
    #inductor_8 = SwitchRelay( Devicenumber, 7 )
    #inductor_9 = SwitchRelay( Devicenumber, 8 )
    #inductor_10 = SwitchRelay( Devicenumber, 9 )
    #inductor_11 = SwitchRelay( Devicenumber, 10 )
    #inductor_12 = SwitchRelay( Devicenumber, 11 )
    #inductor_13 = SwitchRelay( Devicenumber, 12 )
    #inductor_14 = SwitchRelay( Devicenumber, 13 )
    #inductor_15 = SwitchRelay( Devicenumber, 14 )
    #inductor_16 = SwitchRelay( Devicenumber, 15 )
    #inductor_17 = SwitchRelay( Devicenumber, 16 )
    #inductor_18 = SwitchRelay( Devicenumber, 17 )
    #inductor_19 = SwitchRelay( Devicenumber, 18 )
    #inductor_20 = SwitchRelay( Devicenumber, 19 )

  
