import wx

class advWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, "Advanced Settings")
        panel = wx.Panel(self, wx.ID_ANY)

        topSizer = wx.BoxSizer(wx.VERTICAL)
        self.okbutton = wx.Button(panel, label = "Ok", size = (100,30))
        topSizer.Add(self.okbutton, wx.ALIGN_LEFT)

        panel.SetSizer(topSizer)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = advWindow(None)
    frame.Show()
    app.MainLoop()

