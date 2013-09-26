import wx
import collections

class control():
    def __init__(self, klasse):

        self.gui = klasse

        self.gui.Bind(wx.EVT_BUTTON, self.onStart, self.gui.startbtn)
        self.gui.Bind(wx.EVT_BUTTON, self.onAbort, self.gui.abortbtn)

        self.overallbar = self.gui.overallbar
        self.overalltimer = wx.Timer(self.gui, 999)
        self.currentbar = self.gui.currentbar
        self.currenttimer = wx.Timer(self.gui, 1000)


    def on_overalltimer(self, e):
        self.overallcount += self.duration/0.1
        self.overallbar.SetValue(self.overallcount)
        if self.overallcount >= 100:
            self.overallcount = 0
            self.overalltimer.Stop()
            self.overallbar.SetValue(100)
            dia = wx.MessageDialog(self.gui.panel, "Done", "Info", wx.OK)
            dia.ShowModal()

    def on_currenttimer(self, e):
        self.count += self.coilduration/0.1
        self.currentbar.SetValue(self.count)
        if self.count >= 100:
            self.currenttimer.Stop()
            self.currentbar.SetValue(0)
            self.count = 0


    def onAbort(self, e):
        dlg = wx.MessageDialog(self.gui.panel, "Do you really want to quit the app?", "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.gui.Destroy()

    def onStart(self, e):
        # dauer hier berechnet, nachher aus parametern von dodegauss
        self.nrCoils = 3
        self.coilduration = 3
        self.duration = self.nrCoils * self.coilduration
        self.count = 0
        self.overallcount = 0
        self.gui.Bind(wx.EVT_TIMER, self.on_overalltimer, self.overalltimer,
                999)
        self.gui.Bind(wx.EVT_TIMER, self.on_currenttimer, self.currenttimer,
                1000)
        self.currenttimer.Start(100)
        self.overalltimer.Start(100)

