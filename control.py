import wx
import collections

class control():
    def __init__(self, klasse):

        self.gui = klasse
        self.main = klasse.mainwin

        # bind buttons in mainwindow
        self.main.Bind(wx.EVT_BUTTON, self.onStart, self.main.startbtn)
        self.main.Bind(wx.EVT_BUTTON, self.onAbort, self.main.abortbtn)
        self.main.Bind(wx.EVT_BUTTON, self.onAdv, self.main.advbtn)

        # create timers for progress bars
        self.overallbar = self.main.overallbar
        self.overalltimer = wx.Timer(self.main, 999)
        self.currentbar = self.main.currentbar
        self.currenttimer = wx.Timer(self.main, 1000)


    def on_overalltimer(self, e):
        self.overallcount += 100*0.5/(self.duration)
        self.overallbar.SetValue(self.overallcount)
        if self.overallcount >= 100:
            self.overallcount = 0
            self.overalltimer.Stop()
            self.overallbar.SetValue(100)
            dia = wx.MessageDialog(self.main.panel, "Done", "Info", wx.OK)
            dia.ShowModal()

    def on_currenttimer(self, e):
        self.count += (100*0.1)/self.coilduration
        self.currentbar.SetValue(self.count)
        if self.count >= 100:
            self.coilcounter += 1
            if self.coilcounter == self.nrCoils:
                self.currenttimer.Stop()
                self.currentbar.SetValue(0)
                self.count = 0
            else:
                self.currenttimer.Stop()
                self.currentbar.SetValue(0)
                self.count = 0
                self.currenttimer.Start(100)


    def onAbort(self, e):
        """
        dialog to abort degaussing
        """
        dlg = wx.MessageDialog(self.main.panel, "Do you really want to quit the app?", "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.main.Destroy()

    def onStart(self, e):
        """
        begins degaussing
        """
        # dauer hier berechnet, nachher aus parametern von dodegauss
        self.nrCoils = 3
        self.coilduration = 5
        self.duration = self.nrCoils * self.coilduration
        self.count = 0
        self.overallcount = 0
        self.coilcounter = 0

        # bind timers and start
        self.main.Bind(wx.EVT_TIMER, self.on_overalltimer, self.overalltimer,
                999)
        self.main.Bind(wx.EVT_TIMER, self.on_currenttimer, self.currenttimer,
                1000)
        self.currenttimer.Start(100)
        self.overalltimer.Start(500)

    def onAdv(self, e):
        """ 
        creates advanced settings window
        """
        self.gui.createAdvWindow()
        self.adv = self.gui.advwin
        self.main.Bind(wx.EVT_BUTTON, self.onAdvOk, self.adv.okbutton)
        self.main.Bind(wx.EVT_BUTTON, self.onAdvCancel, self.adv.cancelbutton)
        self.main.Bind(wx.EVT_COMBOBOX, self.coilselection, self.adv.degaP.coilselector)
        self.adv.Show()

    def onAdvOk(self, e):
        """
        called on click on ok button in advanced settings window
        """

        self.adv.Destroy()

    def onAdvCancel(self, e):
        """
        called on click on cancel button in advanced settings window
        """
        self.adv.Destroy()

    def coilselection(self, e):
        choice = self.adv.degaP.coilselector.GetValue()
        if choice != "All":
            self.adv.degaP.textAmp.SetValue(str(self.adv.degaP.currentincoils[choice]))
        if choice == "All":
            pop = wx.TextEntryDialog(self.adv.degaP.panel, "Enter Amplitude for ALL coils: ", "Amplitude", "")
            answ = pop.ShowModal()
            if answ == wx.ID_OK:
                nr = pop.GetValue()
            else:
                nr = "No Amplitude"
            try:
                isfloat = float(nr)
                self.adv.degaP.textAmp.SetValue(str(nr))
            except ValueError:
                self.adv.degaP.textAmp.SetValue("No Amplitude set")
                self.adv.degaP.textAmp.SetFocus()
            pop.Destroy()

