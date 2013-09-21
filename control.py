import wx
import collections

class control():
    def __init__(self, klasse):

        self.gui = klasse

        self.gui.Bind(self.gui.wx.EVT_RADIOBOX, self.radioBoxSelection)
        self.gui.Bind(self.gui.wx.EVT_COMBOBOX, self.coilselectorchange)
        self.gui.Bind(self.gui.wx.EVT_BUTTON, self.onOk, okbutton)
        self.gui.Bind(self.gui.wx.EVT_BUTTON, self.onCancel, cancelbutton)


    def radioBoxSelection(self, e):
        sel = self.gui.rb.GetSelection()
        if sel == 0:
            print str(sel) + " selected"
            self.gui.coilselector.Enable(False)
            self.gui.labelAmp.Hide()
            self.gui.textAmp.Hide()
            self.gui.panel.Layout()
            self.gui.mode = "auto"
        else:
            print str(sel) + " selected"
            self.gui.coilselector.Enable(True)
            self.gui.labelAmp.Show()
            self.gui.textAmp.Show()
            self.gui.textAmp.SetValue(str(self.gui.currentincoils[self.gui.coilselector.GetValue()]))
            self.gui.panel.Layout()
            self.gui.mode = "manual"

    def coilselectorchange(self, e):
        choice = self.gui.coilselector.GetValue()
        if choice != "other":
            self.gui.textAmp.SetValue(str(self.gui.currentincoils[choice]))
        if choice == "other":
            pop = sefl.gui.wx.TextEntryDialog(None, "Enter Amplitude: ", "Amplitude", "")
            answ = self.gui.pop.ShowModal()
            if answ == self.gui.wx.ID_OK:
                nr = pop.GetValue()
            else:
                nr = "No Amplitude"
            try:
                isfloat = float(nr)
                self.gui.textAmp.SetValue(str(nr))
            except ValueError:
                self.gui.textAmp.SetValue("No Amplitude set")            
                self.gui.textAmp.SetFocus()
            pop.Destroy()

    def onCancel(self, e):
        dlg = self.gui.wx.MessageDialog(self.gui.panel, "Do you really want to quit the app?", "Confirm Exit", self.gui.wx.OK|self.gui.wx.CANCEL|self.gui.wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == self.gui.wx.ID_OK:
            self.gui.Destroy()

    def onOk(self, e):
        self.gui.dev = self.inputDev.GetValue()
        print str(self.gui.dev)
        if self.gui.mode == "manual":
            self.gui.runManual()
        elif self.gui.mode == "auto":
            self.gui.runAuto()

    def runManual(self):
        coil = self.gui.coilselector.GetValue()
        amp = self.gui.textAmp.GetValue()
        print str(coil)
        print str(amp)

    def runAuto(self):
        autocoils = {i:self.gui.currentincoils[i] for i in self.currentincoils if
                i!="other"}
        print repr(autocoils)
        keepgoing = True
        for coil in autocoils:
            count = 0
            dlg = wx.ProgressDialog("Progress", str(coil), maximum=10, parent = self.gui.panel, style = wx.PD_CAN_ABORT|wx.PD_APP_MODAL|wx.PD_ELAPSED_TIME|wx.PD_REMAINING_TIME)
            while keepgoing and count < 10:
                count += 1
                wx.MilliSleep(1000)
                (keepgoing, skip) = dlg.Update(count)
            dlg.Destroy()
