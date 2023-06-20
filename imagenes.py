from tkinter import *
import random
from PIL import ImageTk,Image
pg = Tk()
pg.geometry("500x500")
pg.title("Imagen")

lb = Label(pg,text="Imagen" )
lb.place(relx=0.5, rely=0.05, anchor=CENTER,)

img = Label(pg,text="Imagen" )
img.place(relx=0.5, rely=0.5, anchor=CENTER,)

var = ImageTk.PhotoImage(Image.open ("imagen.jpg"))
img["image"] = var
var2 = ImageTk.PhotoImage(Image.open ("imagen2.jpg"))

def fn1():
    img["image"] = var2


bt1 = Button(pg, text="Ejecutar", bg="#e76f51", fg="white", command=fn1)
bt1.place(relx=0.5, rely=0.95, anchor=CENTER,)

pg.mainloop()