#!/usr/bin/env python
from Tkinter import *
import ttk
import shutil
import os
import datetime
from datetime import timedelta
from datetime import date
import time


class Mod_Orders:
    def __init__(self, master):
        frame = ttk.Frame(master)
        frame.pack()
        headLabel = ttk.Label(frame, text = "Modified Customer Orders")
        headLabel.pack()
        button = ttk.Button(frame, text = "Update", command = self.transfer)
        button.pack()
        
 
        self.pathCO = "/Users/aja/GitHub/TechAcademy_Drills/WXmodifiedFileTransfer/ClientOrders"
        self.pathNM = "/Users/aja/GitHub/TechAcademy_Drills/WXmodifiedFileTransfer/ModifiedOrders"
        self.folderCO = os.listdir(self.pathCO)

    def transfer(self):
        for files in self.folderCO:
            client_orders = (self.pathCO + "/" + files)
            epoch = os.stat(client_orders).st_mtime
            today = time.time()
            twenty4 = today - 86400
            if epoch > twenty4:
                t_files = files
                transfer_files = (self.pathCO + "/" + t_files)
                print(transfer_files)
                shutil.copy(transfer_files, self.pathNM)
            
def main():
    root = Tk()
    app = Mod_Orders(root)
    root.mainloop()
if __name__ == "__main__" : main()
