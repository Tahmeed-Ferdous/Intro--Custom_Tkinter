
import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import Image, ImageTk
    
window=ttk.Window(themename='darkly')
window.geometry('600x400')
window.title('Images')

image=Image.open('images/raccoon.jpg').resize((100,100))
imagetk=ImageTk.PhotoImage(image)

imagectk=ctk.CTkImage(
    light_image=Image.open('images/raccoon.jpg').resize((100,100)),
    dark_image=Image.open('images/raccoon.jpg').resize((100,100))
)

label=ttk.Label(window, text='raccoon', image=imagetk)
label.pack()

button=ttk.Button(window, text='A button', image=imagetk,compound='left')
button.pack()

buttonctk=ctk.CTkButton(window, text='A button', image=imagectk,compound='left')
buttonctk.pack()

window.mainloop()