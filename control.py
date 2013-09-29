import wx
import collections

class control():
    def __init__(self, klasse):

        self.gui = klasse
        self.main = klasse.mainwin

        self.coils = collections.OrderedDict([
            ("A-X", dict([('Amp', 4),('Freq', 10),('Dur', 110),('Keep', 19) ])), 
            ("A-Y", dict([('Amp', 3),('Freq', 11),('Dur', 100),('Keep', 18) ])), 
            ("A-Z", dict([('Amp', 3.5),('Freq', 12),('Dur', 90),('Keep', 17) ])),       
            ("I-X", dict([('Amp', 9.5),('Freq', 13),('Dur', 80),('Keep', 16) ])),
            ("I-Y", dict([('Amp', 8.7),('Freq', 14),('Dur', 70),('Keep', 15) ])), 
            ("I-Z", dict([('Amp', 9.1),('Freq', 15),('Dur', 60),('Keep', 14) ])), 
            ("All", dict([('Amp', 0),('Freq', 16),('Dur', 50),('Keep', 13) ]))])

        self.usedcoils = self.coils

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
        self.tmpcoils = self.usedcoils
        self.gui.createAdvWindow(self.tmpcoils)
        print self.tmpcoils
        self.adv = self.gui.advwin
        self.main.Bind(wx.EVT_BUTTON, self.onAdvOk, self.adv.okbutton)
        self.main.Bind(wx.EVT_BUTTON, self.onAdvCancel, self.adv.cancelbutton)
        self.main.Bind(wx.EVT_BUTTON, self.onAdvReset, self.adv.resetbutton)
        self.main.Bind(wx.EVT_COMBOBOX, self.coilselection, self.adv.degaP.coilselector)
        self.main.Bind(wx.EVT_TEXT, self.changeAmp, self.adv.degaP.textAmp)
        self.main.Bind(wx.EVT_TEXT, self.changeFreq, self.adv.degaP.textFreq)
        self.main.Bind(wx.EVT_TEXT, self.changeDur, self.adv.degaP.textDur)
        self.main.Bind(wx.EVT_TEXT, self.changeKeep, self.adv.degaP.textKeep)
        self.main.Bind(wx.EVT_TEXT, self.changeOffset, self.adv.degaP.textOffset)
        self.adv.Show()

    def onAdvReset(self, e):
        print self.coils
        print self.usedcoils
        print self.tmpcoils
        self.usedcoils = self.coils


    def onAdvOk(self, e):
        """
        called on click on ok button in advanced settings window
        """
        self.usedcoils = self.tmpcoils
        self.adv.Destroy()

    def onAdvCancel(self, e):
        """
        called on click on cancel button in advanced settings window
        """
        self.adv.Destroy()

    def changeAmp(self, e):
        choice = self.adv.degaP.coilselector.GetValue()
        self.tmpcoils[choice]['Amp'] = self.adv.degaP.textAmp.GetValue()

    def changeFreq(self, e):
        choice = self.adv.degaP.coilselector.GetValue()
        self.tmpcoils[choice]['Freq'] = self.adv.degaP.textFreq.GetValue()
        print self.tmpcoils
        print self.usedcoils

    def changeDur(self, e):
        choice = self.adv.degaP.coilselector.GetValue()
        self.tmpcoils[choice]['Dur'] = self.adv.degaP.textDur.GetValue()

    def changeKeep(self, e):
        choice = self.adv.degaP.coilselector.GetValue()
        self.tmpcoils[choice]['Keep'] = self.adv.degaP.textKeep.GetValue()

    def changeOffset(self, e):
        pass

    def coilselection(self, e):
        choice = self.adv.degaP.coilselector.GetValue()
        if choice != "All":
            self.adv.degaP.textAmp.SetValue(str(self.usedcoils[choice]['Amp']))
            self.adv.degaP.textFreq.SetValue(str(self.adv.degaP.coils[choice]['Freq']))
            self.adv.degaP.textDur.SetValue(str(self.adv.degaP.coils[choice]['Dur']))
            self.adv.degaP.textKeep.SetValue(str(self.adv.degaP.coils[choice]['Keep']))
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

