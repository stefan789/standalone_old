import wx
import collections

class control():
    def __init__(self, klasse):

        self.gui = klasse

        self.gui.Bind(wx.EVT_BUTTON, self.onStart, self.gui.startbtn)
        self.gui.Bind(wx.EVT_BUTTON, self.onAbort, self.gui.abortbtn)

        self.overallbar = self.gui.overallbar
        self.overalltimer = wx.Timer(self.gui)
        self.currentbar = self.gui.currentbar
        self.currenttimer = wx.Timer(self.gui)


    def on_overalltimer(self, e):
        pass

    def on_currenttimer(self, e):
        self.count += 10
        self.currentbar.SetValue(self.count)
        if self.count == 100:
            self.currenttimer.Stop()
            self.currentbar.SetValue(0)


    def onAbort(self, e):
        dlg = wx.MessageDialog(self.gui.panel, "Do you really want to quit the app?", "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.gui.Destroy()

    def onStart(self, e):
        self.count = 0
        self.gui.Bind(wx.EVT_TIMER, self.on_overalltimer, self.overalltimer)
        self.gui.Bind(wx.EVT_TIMER, self.on_currenttimer, self.currenttimer)
        self.currenttimer.Start(1000)

