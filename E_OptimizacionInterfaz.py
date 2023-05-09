import tkinter as tk
from tkinter import *


class Optimizacion():

    def __init__(self):

        self.Ventana()


    def Ventana(self):
        self.root1 = Tk()
        self.root1.geometry('841'
                           'x700')
        self.root1.title("COMPILADOR ")
        self.root1.configure(bg="olive drab1")

        self.LEN1= tk.Label(self.root1, text="Precalcular expresiones", width=34, borderwidth=3,
                            font=("Helvatica", 15, "bold"), fg="white",
                            bg="dark green", anchor="c")
        self.LEN1.place(x=0, y=0)
        self.LEN2 = tk.Label(self.root1, text="constantes", width=34, borderwidth=3,
                             font=("Helvatica", 15, "bold"), fg="white",
                             bg="dark green", anchor="c")
        self.LEN2.place(x=0, y=25)

        self.frame = Frame(self.root1)
        self.frame.place(x=5, y=55)
        self.frame.config(bg="lightblue")

        self.frame.config(width=405, height=294)
        self.Pantalla = Text(self.frame, height=18, width=50)
        self.Pantalla.tag_bind('bite',
                               '<1>',
                               lambda e, t=self.Pantalla: t.insert(END, "Text"))
        self.Pantalla.place(x=0, y=0)

        f = open("E_FilePreCalc.txt", "r")
        self.Pantalla.delete("1.0", tk.END)
        for x in f:
            self.Pantalla.insert(END, x)
            print(x)
        f.close()

        #==============================================================NULOS=============================
        self.LEN3 = tk.Label(self.root1, text="Eliminación de", width=36, borderwidth=3,
                             font=("Helvatica", 15, "bold"), fg="white",
                             bg="dark green", anchor="c")
        self.LEN3.place(x=416, y=0)
        self.LEN4 = tk.Label(self.root1, text="secuencias nulas", width=36, borderwidth=3,
                             font=("Helvatica", 15, "bold"), fg="white",
                             bg="dark green", anchor="c")
        self.LEN4.place(x=416, y=25)

        self.frame1 = Frame(self.root1)
        self.frame1.place(x=425, y=55)
        self.frame1.config(bg="lightblue")

        self.frame1.config(width=405, height=294)

        self.Pantalla1 = Text(self.frame1, height=18, width=50)
        self.Pantalla1.tag_bind('bite',
                                '<1>',
                                lambda e, t=self.Pantalla1: t.insert(END, "Text"))
        self.Pantalla1.place(x=0, y=0)

        f = open("E_FileNulos.txt", "r")
        self.Pantalla1.delete("1.0", tk.END)
        for x in f:
            self.Pantalla1.insert(END, x)
            print(x)
        f.close()
        #===========================================================================================

        #=======================POTENCIAS==========================================================

        self.LEN5 = tk.Label(self.root1, text="Reducción de potencias", width=34, borderwidth=8,
                             font=("Helvatica", 15, "bold"), fg="white",
                             bg="dark green", anchor="c")
        self.LEN5.place(x=0, y=358)

        self.frame2 = Frame(self.root1)
        self.frame2.place(x=5, y=400)
        self.frame2.config(bg="lightblue")

        self.frame2.config(width=405, height=294)
        # lsta donde se muestra la eliminacion de secuencias nulas

        self.Pantalla2 = Text(self.frame2, height=18, width=50)
        self.Pantalla2.tag_bind('bite',
                                '<1>',
                                lambda e, t=self.Pantalla2: t.insert(END, "Text"))
        self.Pantalla2.place(x=0, y=0)

        f = open("E_FileReduPot.txt", "r")
        self.Pantalla2.delete("1.0", tk.END)
        for x in f:
            self.Pantalla2.insert(END, x)
            print(x)
        f.close()


        #====================================================================================


        self.LEN6 = tk.Label(self.root1, text="Propagación de copias", width=34, borderwidth=8,
                             font=("Helvatica", 15, "bold"), fg="white",
                             bg="dark green", anchor="c")
        self.LEN6.place(x=416, y=358)

        self.frame3 = Frame(self.root1)
        self.frame3.place(x=425, y=400)
        self.frame3.config(bg="lightblue")

        self.frame3.config(width=405, height=294)
        self.Pantalla3 = Text(self.frame3, height=18, width=50)
        self.Pantalla3.tag_bind('bite',
                                '<1>',
                                lambda e, t=self.Pantalla3: t.insert(END, "Text"))
        self.Pantalla3.place(x=0, y=0)

        f = open("E_FilePropCopy.txt", "r")
        self.Pantalla3.delete("1.0", tk.END)
        for x in f:
            self.Pantalla3.insert(END, x)
            print(x)
        f.close()


        self.root1.mainloop()

