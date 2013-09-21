import wx
import collections

class initLayout(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Frame')

#        self.__initMenu__()

        self.panel = wx.Panel(self, wx.ID_ANY)

        topSizer = wx.BoxSizer(wx.VERTICAL)
        # outerbag sizer for 2 columns 'Control' and 'Progress'
        outerbagSizer = wx.GridBagSizer(hgap = 5, vgap = 5)
        controlbbox = wx.StaticBox(self.panel, label = 'Control')
        controlbox = wx.StaticBoxSizer(controlbbox, wx.VERTICAL)
        progressbbox = wx.StaticBox(self.panel, label = 'Progress')
        progressbox = wx.StaticBoxSizer(progressbbox, wx.VERTICAL)

        # two GridBagSizers for control and progess with two spacers in (0,0)
        controlbag = wx.GridBagSizer(hgap = 5, vgap = 5)
        progressbag = wx.GridBagSizer(hgap = 5, vgap = 5)
        controlbag.Add((380,100), pos = (0,0), flag = wx.EXPAND)
        progressbag.Add((380,165), pos = (0,0), flag = wx.EXPAND)

        # create start button and add them to controlbag
        startbuttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.startbtn = wx.Button(self.panel, label = 'Start', size = (200,123))
        startbuttonSizer.Add((-1,-1), wx.ALIGN_LEFT|wx.EXPAND)
        startbuttonSizer.Add(self.startbtn)
        startbuttonSizer.Add((-1,-1), wx.ALIGN_RIGHT|wx.EXPAND)
        controlbag.Add(startbuttonSizer, pos = (1,0), flag = wx.EXPAND)
        controlbag.AddGrowableRow(1,0)

        controlbag.Add((-1,40), pos = (2,0), flag = wx.EXPAND)

        # create abort button and add them to controlbag
        abortbuttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.abortbtn = wx.Button(self.panel, label = 'Abort', size = (200,123))
        abortbuttonSizer.Add((-1,-1), wx.ALIGN_LEFT|wx.EXPAND)
        abortbuttonSizer.Add(self.abortbtn,flag = wx.EXPAND)
        abortbuttonSizer.Add((-1,-1), wx.ALIGN_RIGHT|wx.EXPAND)
        controlbag.Add(abortbuttonSizer, pos = (3,0), flag = wx.EXPAND)
        controlbag.AddGrowableRow(3)

        
        # create overall progress bar and add to progressbag
        self.overalllabel = wx.StaticText(self.panel, wx.ID_ANY, "Overall progress", size=(-1,-1), style=wx.ALIGN_BOTTOM)
        progressbag.Add(self.overalllabel, pos = (1,0), flag = wx.ALIGN_LEFT|wx.EXPAND)
        progressbag.AddGrowableRow(1)
        self.overallbar = wx.Gauge(self.panel, range = 100, size = (-1,-1))
        self.overallbar.SetValue(20)
        progressbag.Add(self.overallbar, pos = (2,0), flag = wx.EXPAND)

        # spacer in between progress bars
        progressbag.Add((-1,40), pos = (3,0), flag = wx.EXPAND)
        # create overall progress bar and add to progressbag
        self.currentlabel = wx.StaticText(self.panel, wx.ID_ANY, "Current progress")
        progressbag.Add(self.currentlabel, pos = (4,0), flag = wx.ALIGN_LEFT)
        progressbag.AddGrowableRow(4)
        self.currentbar = wx.Gauge(self.panel, range = 100, size = (-1,-1))
        self.currentbar.SetValue(70)
        progressbag.Add(self.currentbar, pos = (5,0), flag = wx.EXPAND)
        progressbag.Add((-1,-1), pos = (6,0))


        # add them to their boxes
        controlbox.Add(controlbag, wx.EXPAND)
        progressbox.Add(progressbag, wx.EXPAND)
        
        # add boxes to outerbag
        outerbagSizer.Add(controlbox, pos = (0,0), flag=wx.ALIGN_TOP, border = 5)
        outerbagSizer.Add(progressbox, pos = (0,1), flag=wx.ALIGN_TOP, border = 5)

        # add outerbag to top
        topSizer.Add(outerbagSizer, wx.EXPAND)
        self.panel.SetSizer(topSizer)
        self.SetSizeHints(800, 600, 800, 600)

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
