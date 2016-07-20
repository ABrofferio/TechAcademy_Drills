#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
import pickle

class Window:
    def __init__(self, master):
        master.title("Phone List")
        master.resizable(False, False)

        
        frame1 = ttk.Frame(master)
        frame1.pack()
        label = ttk.Label(frame1, text = "Contact List")
        label.grid(row = 0, column = 0, columnspan = 3)

        label_name = ttk.Label(frame1, text = "Name")
        label_name.grid(row = 1, column = 0)
        self.entry_name = ttk.Entry(frame1, width = 30)
        self.entry_name.insert(0,"Last, First")
        self.entry_name.grid(row = 1, column = 1, columnspan = 2, padx = 10)
        label_phone = ttk.Label(frame1, text = "Phone")
        label_phone.grid(row = 2, column = 0)
        self.entry_phone = ttk.Entry(frame1, width = 30)
        self.entry_phone.insert(0,"###-###-####")
        self.entry_phone.grid(row = 2, column = 1, columnspan = 2, padx = 10)
        
        button1 = ttk.Button(frame1, text = "Add", command = self.add_but)
        button1.grid(row = 3, column = 0)
        button2 = ttk.Button(frame1, text = "Update", command = self.update_but)
        button2.grid(row = 3, column = 1)
        button3 = ttk.Button(frame1, text = "Delete", command = self.delete_but)
        button3.grid(row = 3, column = 2)
        button4 = ttk.Button(frame1, text = "Save", command = self.save_but)
        button4.grid(row = 3, column = 3)
 

        frame2 = ttk.Frame(master)
        frame2.pack()
        self.lb = Listbox(frame2, height = 3, width = 23)
        self.lb.grid(row = 0, column = 0, columnspan = 3)

        pickle_in = open("PhoneList_Drill.pickle", "rb")
        self.phone_dictionary = pickle.load(pickle_in)
        for contact in self.phone_dictionary:
            self.lb.insert(END, contact)
        scrollbar = ttk.Scrollbar(frame2, orient = VERTICAL, command = self.lb.yview)
        scrollbar.grid(row = 0, column = 3, sticky = NS)
        self.lb.configure(yscrollcommand = scrollbar.set)
        self.lb.bind('<<ListboxSelect>>', self.edit_but)

        #self.phone_dictionary = {"Adams, Johnny" : "123-123-1234", "Bills, Tina" : "321-321-4321", "Bolin, Tad" : "123-321-4123", "Dennis, Abe" : "111-223-1224", "Garret, Bob" : "333-311-4211", "Harris, Claire" : "113-322-4443"}
        

    def add_but(self):
        self.lb.insert(END,"{}".format(self.entry_name.get()))
        self.phone_dictionary.update({self.entry_name.get() : self.entry_phone.get()})
        print(self.phone_dictionary)

    def clear_entry(self):
        self.entry_name.delete(0, END)
        self.entry_phone.delete(0, END)
        
    def edit_but(self, event):
        self.clear_entry()
        self.mystring = self.lb.get(self.lb.curselection())
        self.entry_name.insert(0,"{}".format(self.mystring))
        self.entry_phone.insert(0,"{}".format(self.phone_dictionary[self.mystring]))

    def update_but(self):
        del self.phone_dictionary[self.mystring]
        self.lb.config(selectmode = SINGLE)
        self.lb.delete(ANCHOR)
        self.add_but()
        self.clear_entry()
 
    def delete_but(self):
        self.lb.config(selectmode = SINGLE)
        self.lb.delete(ANCHOR)
        delName = self.entry_name.get()
        del self.phone_dictionary[delName]
        self.clear_entry()

    def save_but(self):
        pickle_save = open("PhoneList_Drill.pickle", "wb")
        pickle.dump(self.phone_dictionary, pickle_save)
        pickle_save.close()
        print(self.phone_dictionary)
        


def main():
    root = Tk()
    app = Window(root)
    root.mainloop
if __name__ == "__main__" : main()
    
