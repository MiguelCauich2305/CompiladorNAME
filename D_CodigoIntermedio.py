
import tkinter as tk
from tkinter import ttk
from tkinter import *

from D_CodigoP import CodigoPP as CP #CODIGO P
from D_NotacionPolaca import Polaca
from D_CodigoIntermedio_Logica2 import COD_INTER2 #TRIPLOS Y CUADRUPLOS


class Interfaz_FaseD():


    def INTERFAZ (self, LISTA, LISTA_OPERA,ExpresionFraccionada, CodigoP, TRIPLOS,
                  InsertarCUA, ORIG, Lista1, Lista2, Lista3,posicion):
            self.posicion1 =posicion


            self.LISTA = LISTA
            self.LISTA_OPERA = LISTA_OPERA
            self.Expresion = ExpresionFraccionada
            self.Codigop = CodigoP
            self.Triplos = TRIPLOS
            self.InsertarCUA = InsertarCUA
            self.Original = ORIG

            print ("ENTRO A LA PRIMERA INTERFAZ", ORIG)

            cade=""
            for i in range(0,len(self.Original[self.posicion1])):
                cade=cade+self.Original[self.posicion1][i]

            self.posicion1 = self.posicion1 + 1
            self.root4= Toplevel()
            self.root4.geometry('1150'
                               'x700')
            self.root4.title("Codigo Intermedio")
            self.root4.configure(bg="olive drab1")

            self.BOT = tk.Button(self.root4, text="NEXT", width=15, height=2, borderwidth=3,
                                    font=("Arial", 10), activebackground="azure2", bg="pink",
                                    relief="ridge", command=lambda: [Interfaz_FaseD.Recorrer_LISTAS(self,Lista1, Lista2, Lista3, self.posicion1, ORIG)])
            self.BOT.place(x=950, y=50)



            self.Pol = tk.Label(self.root4, text="EXPRESIÓN: "+ cade, width=89, borderwidth=3,
                                font=("Helvatica", 10, "bold"), fg="black",
                                bg="olive drab1", anchor="c")
            self.Pol.place(x=0, y=40)

            self.Pol = tk.Label(self.root4, text="NOTACIÓN POLACA", width=89, borderwidth=3,
                                font=("Helvatica", 17, "bold"), fg="white",
                                bg="dark green", anchor="c")
            self.Pol.place(x=0, y=0)

            # =================================================PILA DE VARIABLES============================
            for i in range(0, len(self.LISTA)):

                if i == 0:
                    self.Pila0 = tk.Listbox(self.root4)
                    self.Pila0.configure(width=7, height=15)
                    self.Pila0.place(x=5, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila0.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila0.insert("0", " ")

                elif i == 1:
                    self.Pila1 = tk.Listbox(self.root4)
                    self.Pila1.configure(width=7, height=15)
                    self.Pila1.place(x=125, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila1.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila1.insert("0", " ")

                elif i == 2:
                    self.Pila2 = tk.Listbox(self.root4)
                    self.Pila2.configure(width=7, height=15)
                    self.Pila2.place(x=245, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila2.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila2.insert("0", " ")

                elif i == 3:
                    self.Pila3 = tk.Listbox(self.root4)
                    self.Pila3.configure(width=7, height=15)
                    self.Pila3.place(x=365, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila3.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila3.insert("0", " ")

                elif i == 4:
                    self.Pila4 = tk.Listbox(self.root4)
                    self.Pila4.configure(width=7, height=15)
                    self.Pila4.place(x=485, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila4.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila4.insert("0", " ")

                elif i == 5:
                    self.Pila5 = tk.Listbox(self.root4)
                    self.Pila5.configure(width=7, height=15)
                    self.Pila5.place(x=605, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila5.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila5.insert("0", " ")

                elif i == 6:

                    self.Pila6 = tk.Listbox(self.root4)
                    self.Pila6.configure(width=7, height=15)
                    self.Pila6.place(x=725, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila6.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila6.insert("0", " ")

                elif i == 7:

                    self.Pila7 = tk.Listbox(self.root4)
                    self.Pila7.configure(width=7, height=15)
                    self.Pila7.place(x=845, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila7.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila7.insert("0", " ")

                elif i == 8:
                    self.Pila8 = tk.Listbox(self.root4)
                    self.Pila8.configure(width=7, height=15)
                    self.Pila8.place(x=965, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila8.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila8.insert("0", " ")

                elif i == 9:
                    self.Pila9 = tk.Listbox(self.root4)
                    self.Pila9.configure(width=7, height=15)
                    self.Pila9.place(x=1205, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila9.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila9.insert("0", " ")


                elif i == 10:
                    self.Pila10 = tk.Listbox(self.root4)
                    self.Pila10.configure(width=7, height=15)
                    self.Pila10.place(x=1325, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila10.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila10.insert("0", " ")

                elif i == 11:
                    self.Pila11 = tk.Listbox(self.root4)
                    self.Pila11.configure(width=7, height=15)
                    self.Pila11.place(x=1445, y=80)
                    for a in range(0, len(self.LISTA[i])):
                        self.Pila11.insert("0", self.LISTA[i][a])
                    if len(self.LISTA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA[i])):
                            self.Pila11.insert("0", " ")

            # =================================================OPERADORES Y PARENTESIS============================
            for i in range(0, len(self.LISTA_OPERA)):

                if i == 0:
                    self.Pila01 = tk.Listbox(self.root4)
                    self.Pila01.configure(width=7, height=15)
                    self.Pila01.place(x=55, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila01.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila01.insert("0", " ")

                elif i == 1:
                    self.Pila11 = tk.Listbox(self.root4)
                    self.Pila11.configure(width=7, height=15)
                    self.Pila11.place(x=175, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila11.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila11.insert("0", " ")

                elif i == 2:
                    self.Pila21 = tk.Listbox(self.root4)
                    self.Pila21.configure(width=7, height=15)
                    self.Pila21.place(x=295, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila21.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila21.insert("0", " ")

                elif i == 3:
                    self.Pila31 = tk.Listbox(self.root4)
                    self.Pila31.configure(width=7, height=15)
                    self.Pila31.place(x=415, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila31.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila31.insert("0", " ")

                elif i == 4:
                    self.Pila41 = tk.Listbox(self.root4)
                    self.Pila41.configure(width=7, height=15)
                    self.Pila41.place(x=535, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila41.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila41.insert("0", " ")

                elif i == 5:
                    self.Pila51 = tk.Listbox(self.root4)
                    self.Pila51.configure(width=7, height=15)
                    self.Pila51.place(x=655, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila51.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila51.insert("0", " ")

                elif i == 6:

                    self.Pila61 = tk.Listbox(self.root4)
                    self.Pila61.configure(width=7, height=15)
                    self.Pila61.place(x=775, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila61.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila61.insert("0", " ")

                elif i == 7:

                    self.Pila71 = tk.Listbox(self.root4)
                    self.Pila71.configure(width=7, height=15)
                    self.Pila71.place(x=895, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila71.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila71.insert("0", " ")

                elif i == 8:
                    self.Pila81 = tk.Listbox(self.root4)
                    self.Pila81.configure(width=7, height=15)
                    self.Pila81.place(x=1015, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila81.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila81.insert("0", " ")

                elif i == 9:
                    self.Pila91 = tk.Listbox(self.root4)
                    self.Pila91.configure(width=7, height=15)
                    self.Pila91.place(x=1135, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila91.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila91.insert("0", " ")

                elif i == 10:
                    self.Pila101 = tk.Listbox(self.root4)
                    self.Pila101.configure(width=7, height=15)
                    self.Pila101.place(x=1015, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila101.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila101.insert("0", " ")

                elif i == 11:
                    self.Pila111 = tk.Listbox(self.root4)
                    self.Pila111.configure(width=7, height=15)
                    self.Pila111.place(x=1135, y=80)
                    for a in range(0, len(self.LISTA_OPERA[i])):
                        self.Pila111.insert("0", self.LISTA_OPERA[i][a])

                    if len(self.LISTA_OPERA[i]) < 15:
                        for i in range(0, 15 - len(self.LISTA_OPERA[i])):
                            self.Pila111.insert("0", " ")

            # ============================ETIQUETAS PARA MOSTRAR LO QUE SALE DE LA PILA===========================
            for i in range(0, len(self.Expresion)):
                if i == 0:
                    self.a00 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                        font=("Helvatica", 10, "bold"), fg="white",
                                        bg="dark green", anchor="c")
                    self.a00.place(x=5, y=330)

                elif i == 1:

                    self.a01 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                        font=("Helvatica", 10, "bold"), fg="white",
                                        bg="dark green", anchor="c")
                    self.a01.place(x=125, y=330)
                elif i == 2:

                    self.a02 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                        font=("Helvatica", 10, "bold"), fg="white",
                                        bg="dark green", anchor="c")
                    self.a02.place(x=245, y=330)
                elif i == 3:

                    self.a03 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                        font=("Helvatica", 10, "bold"), fg="white",
                                        bg="dark green", anchor="c")
                    self.a03.place(x=365, y=330)
                elif i == 4:
                    self.a04 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                        font=("Helvatica", 10, "bold"), fg="white",
                                        bg="dark green", anchor="c")
                    self.a04.place(x=485, y=330)
                elif i == 5:

                    self.a05 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                        font=("Helvatica", 10, "bold"), fg="white",
                                        bg="dark green", anchor="c")
                    self.a05.place(x=605, y=330)
                elif i == 6:

                    self.a06 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                        font=("Helvatica", 10, "bold"), fg="white",
                                        bg="dark green", anchor="c")
                    self.a06.place(x=725, y=330)
                elif i == 7:
                    self.a07 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                        font=("Helvatica", 10, "bold"), fg="white",
                                        bg="dark green", anchor="c")
                    self.a07.place(x=845, y=330)
                elif i == 8:
                    self.a08 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                        font=("Helvatica", 10, "bold"), fg="white",
                                        bg="dark green", anchor="c")
                    self.a08.place(x=965, y=330)

                elif i == 9:
                    self.a09 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                        font=("Helvatica", 10, "bold"), fg="white",
                                        bg="dark green", anchor="c")
                    self.a09.place(x=1085, y=330)
                elif i == 10:
                    self.a010 = tk.Label(self.root4, text=self.Expresion[i], width=11, borderwidth=1,
                                         font=("Helvatica", 10, "bold"), fg="white",
                                         bg="dark green", anchor="c")
                    self.a010.place(x=1205, y=330)



            self.P1 = tk.Label(self.root4, text="CÓDIGO P", width=23, borderwidth=3,
                              font=("Helvatica", 17, "bold"), fg="white",
                              bg="dark green", anchor="c")
            self.P1.place(x=0, y=369)

            self.P = tk.Listbox(self.root4)
            self.P.configure(width=55, height=17)
            self.P.place(x=5, y=410)

            for a in range(0, len(self.Codigop)):
                self.P.insert(END, self.Codigop[a])

            print("\n\n\n\n TROPLOS", self.Triplos)

            self.P = tk.Label(self.root4, text=" TRIPLOS", width=30, borderwidth=3,
                              font=("Helvatica", 17, "bold"), fg="white",
                              bg="dark green", anchor="c")
            self.P.place(x=320, y=369)

            self.labelframe2 = tk.LabelFrame(self.root4, font=("Arial", 18), bg="cornflower blue")
            self.labelframe2.place(x=360, y=410)

            self.tabla = ttk.Treeview(self.labelframe2, columns=("1", "11", "111", "1111"), height="12")
            self.tabla.column("#0", width=0)
            self.tabla.column("1", width=88)
            self.tabla.column("11", width=88)
            self.tabla.column("111", width=89)
            self.tabla.column("1111", width=90)

            self.tabla.heading('1', text='Dirección')
            self.tabla.heading('11', text='Operador')
            self.tabla.heading('111', text='Operando 1')
            self.tabla.heading('1111', text='Operando 2')

            for i in range(0, len(self.Triplos)):
                self.tabla.insert('', 'end', values=[self.Triplos[i][0],
                                                     self.Triplos[i][1],
                                                     self.Triplos[i][2],
                                                     self.Triplos[i][3]])

            self.tabla.grid(column=0, row=0)

            self.PM = tk.Label(self.root4, text=" CUÁDRUPLOS", width=30, borderwidth=3,
                               font=("Helvatica", 17, "bold"), fg="white",
                               bg="dark green", anchor="c")
            self.PM.place(x=748, y=369)

            self.labelframe3 = tk.LabelFrame(self.root4, font=("Arial", 18), bg="cornflower blue")
            self.labelframe3.place(x=750, y=410)

            self.tabla1 = ttk.Treeview(self.labelframe3, columns=("1", "11", "111", "1111"), height="12")
            self.tabla1.column("#0", width=0)
            self.tabla1.column("1", width=88)
            self.tabla1.column("11", width=88)
            self.tabla1.column("111", width=89)
            self.tabla1.column("1111", width=90)

            self.tabla1.heading('1', text='Operador')
            self.tabla1.heading('11', text='Operando 1')
            self.tabla1.heading('111', text='Operando 2')
            self.tabla1.heading('1111', text='Auxiliar')

            self.tabla1.grid(column=0, row=0)
            for i in range(0, len(self.Triplos)):
                self.tabla1.insert('', 'end', values=[self.InsertarCUA[i][0],
                                                      self.InsertarCUA[i][1],
                                                      self.InsertarCUA[i][2],
                                                      self.InsertarCUA[i][3]])




            self.root4.mainloop()


    def Recorrer_LISTAS(self, Lista1, Lista2, Lista3, posicion, ORIG):

        print ("Entramos a Recorrer_LISTAS para mostrar CODIGO OBJETO", posicion)


        if posicion < len(Lista1):
            print("entramos al IF")
            print (posicion, Lista1)

            if len(Lista1[posicion]) > 5:
                # LLAMAR A NOTACION POLACA
                Lista_de_Variables, lista_operadores, Exprecion_por_partes = Polaca.Pol(self, Lista1[posicion])
                print("SE RETORNO EN POLACA:", Lista_de_Variables, lista_operadores, Exprecion_por_partes)

                # LLAMAR CODIGO P
                InsertarP = CP.Codigo_CodigoP_2(self, Lista2[posicion])
                print("SE RETORNO CODIGO P:", InsertarP)

                # Lista_TRIPLOS=[]
                Lista_TRIPLOS = COD_INTER2.Triplos(self, Lista3[posicion])

                InsertarCUA = COD_INTER2.Cuadruplos(self, Lista_TRIPLOS)
                # InsertarCUA = []
                Interfaz_FaseD.INTERFAZ(self, Lista_de_Variables, lista_operadores, Exprecion_por_partes, InsertarP,
                                    Lista_TRIPLOS, InsertarCUA, ORIG, Lista1, Lista2, Lista3, posicion)
        else:
            pass









