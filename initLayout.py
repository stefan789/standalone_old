import wx
import collections

class initLayout(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Frame')

        self.__initMenu__()

        self.panel = wx.Panel(self, wx.ID_ANY)

        topSizer = wx.BoxSizer(wx.VERTICAL)
        outerbagSizer = wx.GridBagSizer(hgap = 5, vgap = 5)
        box = wx.StaticBox(self.panel, label = 'Degaussing Parameters')
        boxSizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        bagSizer = wx.GridBagSizer(hgap = 5, vgap = 5)

        sampleList = ['Dev0', 'Dev1', 'Dev2']

        labelDev = wx.StaticText(self.panel, wx.ID_ANY,'Device')
        self.inputDev = wx.ComboBox(self.panel, wx.ID_ANY, 'Dev0/',
                wx.DefaultPosition, (200, -1), sampleList, wx.CB_DROPDOWN)
        self.dev = self.inputDev.GetValue()
        
        self.rb = wx.RadioBox(self.panel, wx.ID_ANY, 'Mode', wx.DefaultPosition,
                wx.DefaultSize, ['Auto', 'Manual'], 2, wx.RA_SPECIFY_COLS)
        self.rb.SetSelection(1)
        self.mode = "manual"

        coilList = ['A-X', 'A-Y', 'A-Z', 'I-X', 'I-Y', 'I-Z', "other"]
        self.currentincoils = collections.OrderedDict([("A-X", 4), ("A-Y", 3), ("A-Z",
            3.5), ("I-X", 9), ("I-Y", 8.7), ("I-Z", 9.1), ("other", 0)])
        
        self.coilselector = wx.ComboBox(self.panel, wx.ID_ANY, 'A-X',
                wx.DefaultPosition, (200,-1), coilList, wx.CB_READONLY)

        bagSizer.Add(labelDev, pos = (0,0), flag = wx.ALIGN_CENTER_VERTICAL, border = 5)
        bagSizer.Add(self.inputDev, pos = (0,1), flag = wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)

        bagSizer.Add(self.rb, pos = (1,0), span = (2,2), flag =
                wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND)
        bagSizer.AddGrowableCol(1,1)

        self.labelCoil = wx.StaticText(self.panel, wx.ID_ANY, 'Coil')
        self.labelAmp = wx.StaticText(self.panel, wx.ID_ANY, 'Amp')
        self.textAmp = wx.TextCtrl(self.panel)
        self.textAmp.SetValue(str(self.currentincoils[self.coilselector.GetValue()]))
        self.textAmp.Show()
        self.labelAmp.Show()

        bagSizer.Add(self.labelCoil, pos = (3,0), flag =
                wx.ALIGN_CENTER_VERTICAL, border = 5)
        bagSizer.Add(self.coilselector, pos = (3,1), span = (1,2), flag =
                wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)
        self.coilselector.Enable(True)

        bagSizer.Add(self.labelAmp, pos = (5,0), flag =
                wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)
        bagSizer.Add(self.textAmp, pos = (5,1), flag =
                wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, border = 5)

        textctrl = wx.TextCtrl(self.panel, wx.ID_ANY, '')

        boxSizer.Add(bagSizer, wx.EXPAND)
        outerbagSizer.Add((300,0), pos = (0,0), flag = wx.EXPAND)
        outerbagSizer.Add(boxSizer, pos = (1,0), span = (7,1), flag = wx.EXPAND)
        outerbagSizer.Add(textctrl, pos = (1,1), flag = wx.EXPAND)
        outerbagSizer.AddGrowableCol(1,1)

        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        okbutton = wx.Button(self.panel, label = "Ok")
        cancelbutton = wx.Button(self.panel, label = "cancel")
        buttonSizer.Add(okbutton, 0, wx.ALIGN_RIGHT, 5)
        buttonSizer.Add(cancelbutton, 0, wx.ALIGN_RIGHT, 5)
        
        topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(outerbagSizer, 0, wx.ALL|wx.EXPAND, 5)
        topSizer.Add(buttonSizer, 0, wx.EXPAND, 5)

        self.panel.SetSizer(topSizer)
        self.SetSizeHints(600, 350, 700, 500)

        self.Centre()
        self.Show()

    def __initMenu__(self):
        self.menubar = wx.MenuBar()
        filem = wx.Menu()
        editm = wx.Menu()
        helpm = wx.Menu()

        self.menubar.Append(filem, '&File')
        self.menubar.Append(editm, '&Edit')
        self.menubar.Append(helpm, '&Help')
        self.SetMenuBar(self.menubar)
            
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = initLayout()
    app.MainLoop()
