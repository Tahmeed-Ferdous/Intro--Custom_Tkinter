
import ttkbootstrap as ttk
import customtkinter as ctk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Meter



def main():
    win=ttk.Window(themename='darkly')
    #Cyborg Darkly Solar Superhero Vapor (dark theme)
    #cerculean simplex morph yeti united sandstone pulse minty lumen litera journal flatly cosmo

    #call class
    App(win)

    #run
    win.mainloop()

class App:
    def __init__(self, win):
        self.win=win
        self.win.title('Layout')
        self.win.geometry('550x550')

        # print(font.families())

        #window attributes
        self.win.iconbitmap('tracking.ico')
        self.win.minsize(200,100)
        self.win.attributes('-alpha', 1)#0-1
        # self.win.attributes('-topmost', True)
        self.win.bind('<Escape>', lambda event: self.win.quit())

        # self.label=ctk.Label(self.win, text='A label\nand then type here', background='red', foreground='green', font=('Jokerman',20), justify='left').pack()
        # self.style=ttk.Style()
        # self.style.configure('new.TButton', foreground='green', font=('Jokerman', 20))
        # self.style.map('new.TButton',foreground=[('pressed', 'red'),('disabled', 'yellow')])
        # self.button=ttk.Button(self.win, text='A button', style='new.TButton').pack()

        # self.string=ctk.StringVar(value='a custom string')
        # self.label=ctk.CTkLabel(self.win, text='A ctk Label',fg_color=('#AA0','red'),text_color='white',corner_radius=10,textvariable=self.string).pack()
        # self.button=ctk.CTkButton(self.win, text='a ctk button', fg_color='#FF0', text_color='#000', hover_color='#AA0', command=lambda: ctk.set_appearance_mode('light')).pack()

        # self.frame=ctk.CTkFrame(self.win, fg_color='transparent').pack()
        # self.slider=ctk.CTkSlider(self.frame).pack(pady=2)

        self.win2=ctk.CTkScrollableFrame(self.win).pack()
        #https://customtkinter.tomschimansky.com/documentation/

        # toast
        self.toast=ToastNotification(
            title='this is a message', 
            message='actual', 
            duration=2000, 
            bootstyle='dark', 
            position=(0, 0, 'ne'))
        self.butn=ttk.Button(self.win, text='show text', command=self.toast.show_toast)
        self.butn.pack()
        #Tool Tip
        ToolTip(self.butn, text='This does something', bootstyle='light-inverse')

        #calendar
        self.calendar=DateEntry(self.win)
        self.calendar.pack(pady=10)



if __name__=='__main__':
    main()