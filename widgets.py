import tkinter as tk
import tkinter as ttk
import ttkbootstrap as ttk
from random import choice
from tkinter import scrolledtext

def main():
    win=ttk.Window(themename = 'darkly') 
    #Cyborg Darkly Solar Superhero Vapor (dark theme)
    #cerculean simplex morph yeti united sandstone pulse minty lumen litera journal flatly cosmo

    #call class
    App(win)

    #run
    win.mainloop()

class App:
    def __init__(self, win):
        self.win=win
        self.win.title('Widgets')
        self.win.geometry('650x1450')

        self.title_label=ttk.Label(master=self.win, text='Miles to Kilometers', font='Calibri 20 bold')
        self.title_label.pack(pady=20)

        def convert():
            output_string.set(entry_int.get()*1.61)
            self.title_label.config(text='Your Value')
            #self.title_label['text']='Your Value'
            self.entry['state']='disabled'
            #create another function and give the command to a button to 'enabled' it

        # Input field
        self.input_frame=ttk.Frame(master=self.win)
        entry_int=tk.IntVar()
        self.entry=ttk.Entry(master=self.input_frame, textvariable=entry_int) # it has the Get method only
        self.button=ttk.Button(master=self.input_frame,text='Convert', command=convert)
        self.entry.pack(side='left',padx=10)
        self.button.pack()
        self.input_frame.pack(pady=6)

        # Output
        output_string=tk.StringVar(value='Output')
        self.output_label=ttk.Label(master=self.win,text='Output', font='Calibri 18', textvariable=output_string)
        self.output_label.pack(pady=8)

        #text
        self.text=ttk.Text(master=self.win, width=30, height=2).pack()

        def window():
            self.newWindow=ttk.Toplevel(self.win)
            self.app=Window2(self.newWindow)

        #buttons
        self.buttoning=ttk.Button(self.win, text='Button', command=window).pack()

        #check button
        check_var=tk.IntVar()
        self.checking1=ttk.Checkbutton(master=self.win, text='Check Box 1', command=lambda: print(check_var.get()), variable=check_var,onvalue=5,offvalue=10,padding=15).pack()
        self.checking2=ttk.Checkbutton(master=self.win, text='Check Box 2', command=lambda: print(check_var.get()), padding=10).pack()
        #radio button
        rad_var=tk.StringVar()
        self.radding1=ttk.Radiobutton(master=self.win, text='Rad Button 1', command=lambda: print(rad_var.get()), variable=rad_var,value=1,padding=10).pack()
        self.radding2=ttk.Radiobutton(master=self.win, text='Rad Button 2', command=lambda: print(rad_var.get()), variable=rad_var,value=2,padding=10).pack()

        #Events
        #https://www.pythontutorial.net/tkinter/tkinter-event-binding/   (Events binder notes)
        def get_pos(event):
            print(f'x: {event.x} y: {event.y}')

        # self.win.bind('<KeyPress>', lambda event: print('a button was pressed'))
        # self.win.bind('<Motion>', get_pos)
        # self.entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
        # self.text.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))

        #Combobox
        self.items=('ice cream', 'Pizza', 'Broccoli')
        self.food=tk.StringVar(value=self.items[0])
        combo=ttk.Combobox(self.win, textvariable=self.food)
        combo['value']=self.items
        combo.pack()
        combo.bind('<<ComboboxSelected>>', lambda event: self.combo_label.config(text=f'Selected: {self.food.get()}'))
        self.combo_label=ttk.Label(self.win, text='A Label')
        self.combo_label.pack()

        #Spinbox
        self.spin=ttk.Spinbox(self.win, from_=3, to=20,increment=3, command= lambda: print('Arrow was pressed'))
        self.spin.bind('<<Increment>>', lambda event: print('up'))
        self.spin.bind('<<Decrement>>', lambda event: print('down'))
        self.spin.pack()

        #TreeView
        first_names=['Tahmeed', 'Sadnan', 'Tasfia', "sid", 'Bushra', 'Orchi', 'Parisa', 'Ifaz']
        last_names=['Ferdous', 'sanim', 'kazi','nasim', 'dhor', 'akhter','akbar', 'maggi']

        self.table=ttk.Treeview(self.win, columns=('first','Last','Email'), show='headings')
        self.table.heading('first', text='First Name')
        self.table.heading('Last', text='Surname')
        self.table.heading('Email', text='Email')
        self.table.pack()

        for i in range(100):
            first=choice(first_names)
            last=choice(last_names)
            email=f'{first[0]}{last}@gmail.com'
            data=(first, last, email)
            self.table.insert(parent='',index=0,values=data)
        self.table.insert(parent='',index=tk.END,values=('john','Doe','JohnDoe@gmail.com'))
        def item_select(_):
            print(self.table.selection())
            for i in self.table.selection():
                print(self.table.item(i)['values'])
        def delete_items(_):
            print('delete')
            for i in self.table.selection():
                self.table.delete(i)

        self.table.bind('<<TreeviewSelect>>', item_select)
        self.table.bind('<Delete>', delete_items)


        #Canvas
        def draw(event):
            x=event.x
            y=event.y
            self.canvas.create_oval((x-self.brush_size/2-10,y-self.brush_size/2-10,x+self.brush_size/2-10,y+self.brush_size/2-10), fill='white')
        def brush_size(event):
            global brush_size
            if event.delta>0:
                brush_size+=4
            else:
                brush_size-=4
            brush_size=max(0,min(brush_size, 50))

        self.canvas=ttk.Canvas(self.win, bg='white', height=2000, width=300)
        self.canvas.pack()
        self.canvas.create_rectangle((150,20,600,300), fill='black', width=1, dash=(1,1,1,1),outline='gray')
        self.canvas.create_oval((250,20,400,100), fill='white')
        self.canvas.create_arc((250,20,400,100), fill='gray',start=45,extent=140,style=tk.CHORD,outline='black',width=1)
        self.canvas.create_line((250,20,400,100), fill='white')
        self.canvas.create_polygon((50,50, 150,50, 150,100),fill='gray')
        self.brush_size=2
        self.canvas.bind('<Motion>', draw)
        self.canvas.bind('<MouseWheel>', brush_size)

        # Scrollbar
        self.scrollbar=ttk.Scrollbar(self.win, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=1,rely=0,relheight=1, anchor='ne')
        self.canvas.bind('<MouseWheel>', lambda event: self.canvas.yview_scroll(int(event.delta/60),'units'))

        # slider
        self.scale_float=tk.DoubleVar(value=10)
        self.scale=ttk.Scale(self.win,command=lambda value: self.scale_float.get(),from_=0,to=25,length=300,orient='horizontal',variable=self.scale_float).pack()

        # progress bar
        self.progress=ttk.Progressbar(self.win,variable=self.scale_float,maximum=25,orient='horizontal',mode='determinate',length=400).pack()

        #scrolled text
        self.scrolled=scrolledtext.ScrolledText(self.win, width=100, height=5).pack()

class Window2:
    def __init__(self, win):
        self.win=win
        self.win.geometry('1350x950+0+0')
        self.win.title('Restaurant Management System')
        self.win.configure(bg='#FFFBEB')



if __name__=='__main__':
    main()
