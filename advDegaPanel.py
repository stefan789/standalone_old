import wx
import collections

class advDegaPanel(wx.Panel):
    def __init__(self, parent):
        self.panel = wx.Panel(parent)

        # topsizer contains bagSizer, bagsizer the other widgets
        topSizer = wx.BoxSizer(wx.VERTICAL)
        bagSizer = wx.GridBagSizer(hgap = 5, vgap = 5)

        # device section 
        labelDev = wx.StaticText(self.panel, -1, "Device")
        deviceList = ["Dev0", "Dev1", "Dev2"]
        self.inputDev = wx.ComboBox(self.panel, -1, "Dev0", wx.DefaultPosition, (200,-1), deviceList, wx.CB_DROPDOWN)
        bagSizer.Add((-1,10), pos = (0,0))
        bagSizer.Add(labelDev, pos = (1,0), flag = wx.ALIGN_CENTER_VERTICAL, border = 5)
        bagSizer.Add(self.inputDev, pos = (1,1), flag = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)

        # offset section
        labelOffset = wx.StaticText(self.panel, -1, "Offset")
        self.textOffset = wx.TextCtrl(self.panel)
        self.textOffset.SetValue(str(0))

        bagSizer.Add(labelOffset, pos = (2,0), flag = wx.ALIGN_CENTER_VERTICAL, border = 5)
        bagSizer.Add(self.textOffset, pos = (2,1), flag = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)
        
        # frequency
        labelFreq = wx.StaticText(self.panel, -1, "Frequency")
        self.textFreq = wx.TextCtrl(self.panel)
        self.textFreq.SetValue(str(10))

        bagSizer.Add(labelFreq, pos = (3,0), flag = wx.ALIGN_CENTER_VERTICAL, border = 5)
        bagSizer.Add(self.textFreq, pos = (3,1), flag = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)

        bagSizer.Add(wx.StaticLine(self.panel, -1, (25,-1), (-1,-1)), pos = (4,0), span=(1,2), flag = wx.EXPAND|wx.ALL, border = 10)


        # Coil selector
        coilList = ["A-X", "A-Y", "A-Z", "All"]
        self.currentincoils = collections.OrderedDict([("A-X", 4), ("A-Y", 3), ("A-Z",
                        3.5), ("I-X", 9), ("I-Y", 8.7), ("I-Z", 9.1), ("All", 0)])

        labelCoil = wx.StaticText(self.panel, -1, "Coil")
        self.coilselector = wx.ComboBox(self.panel, -1, "A-X", wx.DefaultPosition, (200,-1), coilList, wx.CB_READONLY)

        bagSizer.Add(labelCoil, pos = (5,0), flag = wx.ALIGN_CENTER_VERTICAL, border = 5)
        bagSizer.Add(self.coilselector, pos = (5,1), flag = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)

        # amplitude
        labelAmp = wx.StaticText(self.panel, -1, "Amplitude")
        self.textAmp = wx.TextCtrl(self.panel)
        self.textAmp.SetValue(str(self.currentincoils["A-X"]))

        bagSizer.Add(labelAmp, pos = (6,0), flag = wx.ALIGN_CENTER_VERTICAL, border = 5)
        bagSizer.Add(self.textAmp, pos = (6,1), flag = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)
        
        # duration
        labelDur = wx.StaticText(self.panel, -1, "Duration")
        self.textDur = wx.TextCtrl(self.panel)
        self.textDur.SetValue(str(110))

        bagSizer.Add(labelDur, pos = (7,0), flag = wx.ALIGN_CENTER_VERTICAL, border = 5)
        bagSizer.Add(self.textDur, pos = (7,1), flag = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)

        # keeptime
        labelkeep = wx.StaticText(self.panel, -1, "Duration")
        self.textkeep = wx.TextCtrl(self.panel)
        self.textkeep.SetValue(str(10))

        bagSizer.Add(labelkeep, pos = (8,0), flag = wx.ALIGN_CENTER_VERTICAL, border = 5)
        bagSizer.Add(self.textkeep, pos = (8,1), flag = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)

        #add everything to topsizer and set it as panel sizer
        topSizer.Add(bagSizer, flag = wx.EXPAND|wx.ALL, border = 5)
        self.panel.SetSizer(topSizer)


