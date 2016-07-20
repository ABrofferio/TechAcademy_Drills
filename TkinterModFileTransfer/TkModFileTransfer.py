#!/usr/bin/env python
import wx
import shutil
import os
import datetime
from datetime import timedelta
from datetime import date
import time

class Mod_Orders(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title= "Daily File Transfer", size = (550, 400))
        self.panel =  wx.Panel(self)

        label_1 = wx.StaticText(self.panel, label = "Select source folder with the files to be checked for daily transfer.", pos = (10, 10))
        choose = wx.Button(self.panel, label = "Choose Source", pos = (10, 40))
        choose.Bind(wx.EVT_BUTTON, self.FolderA)
        self.entry_1 = wx.TextCtrl(self.panel, pos = (200, 45), size = (300, 20))
        
        label_2 = wx.StaticText(self.panel, label = "Check folder for new/recently modified client orders.", pos = (10, 100))
        check_button = wx.Button(self.panel, label = "Check", pos = (10, 130))
        check_button.Bind(wx.EVT_BUTTON, self.check)
        self.entry_2 = wx.TextCtrl(self.panel, pos = (200, 135), size = (300, 40), style = wx.TE_MULTILINE)

        label_3 = wx.StaticText(self.panel, label = "Select destination folder that will receive files in the daily transfer.", pos = (10, 190))
        folderB = wx.Button(self.panel, label = "Choose Destination", pos = (10, 220))
        folderB.Bind(wx.EVT_BUTTON, self.FolderB)
        self.entry_3 = wx.TextCtrl(self.panel, pos = (200, 225), size = (300, 20))
        
        label_4 = wx.StaticText(self.panel, label = "Transfer recently modified client orders from the source folder to the destination folder.", pos = (10, 280))
        transfer_button = wx.Button(self.panel, label = "Transfer", pos = (10, 310))
        transfer_button.Bind(wx.EVT_BUTTON, self.transfer)
        self.entry_4 = wx.TextCtrl(self.panel, pos = (200, 315), size = (300, 40), style = wx.TE_MULTILINE)

    def FolderA(self, event):
        DirA = wx.DirDialog(self.panel, defaultPath = "/Users/aja/GitHub/TechAcademy_Drills/TkinterModFileTransfer", pos = (10,30))
        DirA.ShowModal()
        self.pathCO = DirA.GetPath()
        print(self.pathCO)
        self.entry_1.SetValue(self.pathCO)
    def FolderB(self, event):
        DirB = wx.DirDialog(self.panel, defaultPath = "/Users/aja/GitHub/TechAcademy_Drills/TkinterModFileTransfer", pos = (10,370))
        DirB.ShowModal()
        self.pathNM = DirB.GetPath()
        print(self.pathNM)
        self.entry_3.SetValue(self.pathNM)
    def check(self, event):
        self.files_2b = []
        self.folderCO = os.listdir(self.pathCO)
        for files in self.folderCO:
            client_orders = (self.pathCO + "/" + files)
            epoch = os.stat(client_orders).st_mtime
            today = time.time()
            twenty4 = today - 86400
            if epoch > twenty4:
                t_files = files
                self.transfer_files = (self.pathCO + "/" + t_files)
                self.files_2b.append(self.transfer_files)
                print(self.transfer_files)
                self.entry_2.AppendText(t_files + "\n")

    def transfer(self, event):
        for row in self.files_2b:
            shutil.copy(row, self.pathNM)
            title = (row.split("/"))
            self.entry_4.AppendText(title[len(title)-1] + "\n")
        
            
app = wx.App()
frame = Mod_Orders()
frame.Show()
app.MainLoop()

