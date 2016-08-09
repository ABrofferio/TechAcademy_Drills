#!/usr/bin/env python
from Tkinter import *
import ttk
import datetime
from datetime import datetime
import time
import pytz
from pytz import timezone
from dateutil.tz import tzutc, tzlocal

class Zones:
    def __init__(self, master):
        frame1 = Frame(master, height = 300, width = 100)
        frame1.pack()
        main_label = Label(frame1, text = "Office Time Manager")
        main_label.grid(row = 0, column = 1)


        frame2 = Frame(master, height = 300, width = 100)
        frame2.pack()
        curr_butt = Button(frame2, text = "Current Time", command = self.ct_butt)
        curr_butt.grid(row = 0, column = 1)
        port_label = Label(frame2, text = "Portland")
        port_label.grid(row = 1, column = 0)
        self.port_entry = Entry(frame2, width = 30)
        self.port_entry.grid(row = 2, column = 0)
        nyc_label = Label(frame2, text = "New York City")
        nyc_label.grid(row = 1, column = 1)
        self.nyc_entry = Entry(frame2, width = 30)
        self.nyc_entry.grid(row = 2, column = 1)
        lon_label = Label(frame2, text = "London")
        lon_label.grid(row = 1, column = 2)
        self.lon_entry = Entry(frame2, width = 30)
        self.lon_entry.grid(row = 2, column = 2)
        
    def ct_butt(self):
        utc = datetime.now(tzutc())
        port = utc.astimezone(tzlocal())
        portie = port.strftime("%a | %d %b %Y | %H : %M")
        red_portie = port.strftime("%H")
        self.port_entry.insert(0, portie)
        lon = utc.astimezone(pytz.timezone('Europe/London'))
        londie = lon.strftime("%a | %d %b %Y | %H : %M")
        red_londie = lon.strftime("%H")
        self.lon_entry.insert(0, londie)
        nyc = utc.astimezone(pytz.timezone('US/Eastern'))
        newie = nyc.strftime("%a | %d %b %Y | %H : %M")
        red_newie= nyc.strftime("%H")
        self.nyc_entry.insert(0, newie)
        if 9 < int(red_portie) < 21:
            self.port_entry.config(background = "green")
        if 9 < int(red_londie) < 21:
            self.port_entry.config(background = "green")
        if 9 < int(red_newie) < 21:
            self.port_entry.config(background = "green")       

def main ():
    root = Tk()
    app = Zones(root)
    root.mainloop()
if __name__ == "__main__" : main()
    
    


