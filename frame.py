import tkinter as tk
import tkinter as ttk
import ttkbootstrap as ttk


def main():
    win=ttk.Window(themename = 'journal') 
    #Cyborg Darkly Solar Superhero Vapor (dark theme)
    #cerculean simplex morph yeti united sandstone pulse minty lumen litera journal flatly cosmo

    #call class
    App(win)

    #run
    win.mainloop()

class App:
    def __init__(self, win):
        self.win=win
        self.win.title('Frame')
        self.win.geometry('650x650+1000+0')

        #window attributes
        self.win.iconbitmap('tracking.ico')
        self.win.minsize(200,100)
        self.win.maxsize(1000,1000)
        self.win.resizable(True, False)
        self.win.attributes('-alpha', 1)#0-1
        self.win.attributes('-topmost', True)
        self.win.bind('<Escape>', lambda event: self.win.quit())


        # Menu
        #https://www.tutorialspoint.com/python/tk_menu.htm
        self.menu=ttk.Menu(self.win)
        # Sub Menu
        self.file_menu=ttk.Menu(self.menu, tearoff=False)
        self.file_menu.add_command(label='New', command=lambda: print('New File'))
        self.file_menu.add_command(label='Open', command=lambda: print('Open File'))
        self.menu.add_cascade(label='File', menu=self.file_menu)
        # Another Sub Menu
        self.help_menu=ttk.Menu(self.menu, tearoff= False)
        self.help_menu.add_command(label='Help', command=lambda: print(self.help_menu_string.get()))
        self.help_menu_string=tk.StringVar()
        self.help_menu.add_checkbutton(label='check',onvalue='on', offvalue='off', variable=self.help_menu_string)
        self.menu.add_cascade(label='Help', menu=self.help_menu)

        self.win.configure(menu=self.menu)

        # Menu Button
        self.menu_button=ttk.Menubutton(self.win, text='Menu Button').pack()
        self.button_sub_menu=tk.Menu(self.menu_button, tearoff=False)
        
        # Frame
        self.title_label=ttk.Label(master=self.win, text='Miles to Kilometers', font='Calibri 20 bold')
        self.title_label.pack(pady=20)
        self.frame=ttk.Frame(self.win, width=150, height=100, borderwidth=10, relief=tk.GROOVE)
        self.frame.propagate(False)
        self.label=ttk.Label(self.frame, text='Label').pack()
        self.button=ttk.Button(self.frame, text='button').pack()
        self.frame.pack(side='top')

        # Notebook widget
        self.notebook=ttk.Notebook(self.win, padding=50)

        self.tab1=ttk.Frame(self.notebook)
        self.label1=ttk.Label(self.tab1,text='Text').pack()

        self.tab2=ttk.Frame(self.notebook)
        self.label2=ttk.Label(self.tab2,text='Integer').pack()

        self.notebook.add(self.tab1, text='Tab 1')
        self.notebook.add(self.tab2, text='Tab 2')
        self.notebook.pack()
         

if __name__=='__main__':
    main()