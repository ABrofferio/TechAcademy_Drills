from tkinter import *
from tkinter import ttk
import webbrowser, WebPageGenImport
import DbImport


class frame:
    def __init__(self, master):
        frame = ttk.Frame(master)
        frame.pack()

        title_label = ttk.Label(frame, text = "Create a promotional webpage for us!")
        title_label.pack()
        tag_label = ttk.Label(frame, text = "Select from the three themes below")
        tag_label.pack()

        self.tree = ttk.Treeview(frame, columns = ('name', 'title', 'message', 'background_color', 'font_style', 'font_size'),height = 3)
        self.tree.pack()
        self.tree['show'] = 'headings'
        name_h = self.tree.heading('0', text = "name")
        title_h = self.tree.heading('1', text = "title")
        message_h = self.tree.heading('2', text = "message")
        background_h = self.tree.heading('3', text = "background_color")
        font_h = self.tree.heading('4', text = "font_style")
        size_h = self.tree.heading('5', text = "font_size")
        name_c = self.tree.column('0', width = 60)
        title_c = self.tree.column('1', width = 100)
        message_c = self.tree.column('2', width = 400)
        background_c = self.tree.column('3', width = 70)
        font_c = self.tree.column('4', width = 55)
        size_c = self.tree.column('5', width = 50)
        sale = self.tree.insert('', 'end', '', text = '1', values = \
                         ('Sale', 'Sa!e Sa!e Sa!e', 'Come join us this weekend for a blowout sale!', 'red', 'normal', '12'))
        charity = self.tree.insert('', 'end', '', text = '2', values = \
                         ('Charity', 'Help us help others!', 'Come visit us this weekend when 20% of proceeds go to local charity!', 'yellow', 'italic', '14'))
        free = self.tree.insert('', 'end', '', text = '3', values = \
                         ('Free', 'Free coffee!', 'Stop by this weekend for free coffee while you shop!', 'lightblue', 'normal', '16'))
        
        self.listbox = Listbox(frame, height = 3)
        self.listbox.pack()
        self.listbox.insert(0, "Sale")
        self.listbox.insert(1, "Charity")
        self.listbox.insert(END, "Free")
        choose_label = ttk.Label(frame, text = "If you are happy with the theme you have selected click the 'submit theme'")
        choose_label.pack()
        button = ttk.Button(frame, text="submit theme", command = self.theme)
        button.pack()
        
        label = ttk.Label(frame, text = "Personalize our webpage with a short message.")
        label.pack()
        self.userText = ttk.Entry(frame, width = 75)
        self.userText.pack()
        label_1 = ttk.Label(frame, text = "If you're happy with your message, click 'submit'.")
        label_1.pack()
        button_1 = ttk.Button(frame, text="submit", command = self.webPage)
        button_1.pack()
        label_2 = ttk.Label(frame, text = "To see our webpage personalized with your message, click 'view'")
        label_2.pack()
        button_2 = ttk.Button(frame, text="view", command = self.runPage)
        button_2.pack()

    def theme(self):
        theme_selection = self.listbox.get(self.listbox.curselection())
        #print(theme_selection)
        jerry = DbImport.pull_theme(theme_selection)
        print(jerry)
        for item in jerry:
            self.background = item[4]
            self.font = item[5]
            self.size = item[6]
            self.name = item[1]
            self.title = item[2]
            self.message = item[3]

    def webPage(self):
        userInput = self.userText.get()
        WebPageGenImport.open_page(self.name, self.background, self.font, self.size, self.title, self.message, userInput)
    def runPage(self):
        WebPageGenImport.run_webpage()

def main():
    root = Tk()
    app = frame(root)
    root.mainloop
if __name__ == "__main__" : main()
