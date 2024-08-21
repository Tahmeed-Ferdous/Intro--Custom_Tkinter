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
        self.win.title('Layout  ')
        self.win.geometry('650x650+1000+0')

        #window attributes
        self.win.iconbitmap('tracking.ico')
        self.win.minsize(200,100)
        self.win.attributes('-alpha', 1)#0-1
        self.win.attributes('-topmost', True)
        self.win.bind('<Escape>', lambda event: self.win.quit())

        # layout\pack
        # self.label=ttk.Label(text='Label',background='red')
        # self.label.pack(side='left', expand=True, fill='y', padx=50, pady=100)

        # layout\grid
        self.label1=ttk.Label(text='Label',background='blue')
        self.label2=ttk.Label(text='Label',background='green')

        # self.win.columnconfigure(0, weight=1, uniform='a') #uniform proportionates everything
        # self.win.columnconfigure(1, weight=1, uniform='a')
        # self.win.rowconfigure(0, weight=1, uniform='a')
        # self.label1.grid(row=0, column=0, sticky='ne', columnspan=3) # compass nsew
        # self.label2.grid(row=0, column=1, sticky='e', rowspan=2, padx=20, ipady=20) #rowspan takes the label to all the rows

        #layout\place
        self.label=ttk.Label(text='Label',background='red')
        self.label.place(relx=0.1, rely=0.5, relwidth=0.4, relheight=0.5)
        self.label.place(x=100,y=100,width=100, height=100, anchor='center')
        self.label.lift()
        self.label.lower() # front and back of frames
        self.label.tkraise() # raising the frame on top

        #toggle widget
        def toggle_label():
            if self.label_visible:
                self.label.place_forget()
                self.label_visible=False
            else:
                self.label_visible=True
        self.label_visible=True
        self.button=ttk.Button(self.win, text='toggle', command=toggle_label)
        self.button.place(x=10, y=10)

        #layout\responsive layout
        self.win.bind('<Configure>', lambda event: print(event))

        #text scroll
        self.text=ttk.Text(self.win)
        for i in range(1, 200):
            self.text.insert(f'{i}.0', f'text:{i}\n')
        self.text.pack(expand=True, fill='both')

        self.scroll_text=ttk.Scrollbar(self.win, orient='vertical', command=self.text.yview)
        self.text.configure(yscrollcommand=self.scroll_text.set)
        self.scroll_text.place(relx=1, rely=0,relheight=1,anchor='ne')



if __name__=='__main__':
    main()