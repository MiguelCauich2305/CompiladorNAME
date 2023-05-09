import time
import tkinter as tk
from tkinter import *
from tkinter import  filedialog

from A_Compilador_Lexico import LEXICO
from PruebaSintactico2 import Sintactico as SIN
from B_Compilador_Semantico2 import Semantico as SEM
from D_Compilador_Prioridad import DividePrioridades as DIV
from RecuperaOPERACIONES_DIVI import OPERACIONES_DIV as LOL
from E_Opti_CalculoExpConst import DameOperaciones as OPTIM

from E_OptimizacionLOGICA import Logica_OPTI as LOG_OPTI

import D_CodigoIntermedio as ID

class GRAFICO:
    def __init__(self):
        self.Ventana()

    def Ventana(self):
            colorbg= "lime green"
            self.root9 = Tk()
            self.root9.geometry('841'
                               'x650')
            self.root9.title("COMPILADOR ")
            self.root9.configure(bg="olive drab1")

            self.frame = Frame(self.root9)

            # Empaqueta el frame en la raíz
            self.frame.place(x=5, y=55)

            # Color de fondo, background
            self.frame.config(bg="lightblue")

            # Podemos establecer un tamaño,
            # la raíz se adapta al frame que contiene
            self.frame.config(width=680, height=400)

            self.Pantalla = Text(self.frame, height=80, width=100)
            #scroll = Scrollbar(self.frame, command=self.Pantalla.yview)

            #self.Pantalla.configure(yscrollcommand=scroll.set)

            self.Pantalla.tag_configure('bold_italics',
                               font=('Verdana', 12, 'bold', 'italic'))

            self.Pantalla.tag_configure('big',
                               font=('Verdana', 24, 'bold'))
            self.Pantalla.tag_configure('color',
                               foreground='blue',
                               font=('Tempus Sans ITC', 14))

            self.Pantalla.tag_configure('groove',
                               relief=GROOVE,
                               borderwidth=2)

            self.Pantalla.tag_bind('bite',
                          '<1>',
                          lambda e, t=self.Pantalla: t.insert(END, "Text"))

            self.Pantalla.place(x=0, y=0)
            #scroll.pack(side=RIGHT, fill=Y)

            self.listbox2 = tk.Listbox(self.root9)
            self.listbox2.configure(width=114, height=9)
            self.listbox2.place(x=5, y=490)

            self.LEN = tk.Label(self.root9, text="COMPILADOR NOMBRE", width=52, borderwidth=3,
                                font=("Helvatica", 20, "bold"),fg="white",
                                bg="dark green", anchor="c")
            self.LEN.place(x=0, y=0)

            self.LEXICO = tk.Button(self.root9, text="LÉXICO", width=15, height=2, borderwidth=3,
                                      font=("Arial", 10), activebackground="azure2",bg=colorbg,
                                      relief="ridge", command=lambda: [self.Lexico()])
            self.LEXICO.place(x=700, y=60)

            self.SINTaCTICO = tk.Button(self.root9, text="SINTÁCTICO", width=15, height=2, borderwidth=3,
                                    font=("Arial", 10), activebackground="azure2",
                                    relief="ridge", command=lambda: [self.Sintáctico()], state=DISABLED)
            self.SINTaCTICO.place(x=700, y=110)

            self.SEMaNTICO = tk.Button(self.root9, text="SEMÁNTICO", width=15, height=2, borderwidth=3,
                                    font=("Arial", 10), activebackground="azure2",
                                    relief="ridge", command=lambda: [self.Semantico()], state=DISABLED)
            self.SEMaNTICO.place(x=700, y=160)

            self.CODIGO = tk.Button(self.root9, text="INTERMEDIO", width=15, height=2, borderwidth=3,
                                       font=("Arial", 10), activebackground="azure2",
                                       relief="ridge", command=lambda: [self.Codigo_Intermedio()], state=DISABLED)
            self.CODIGO.place(x=700, y=210)

            self.OPTIMIZACION = tk.Button(self.root9, text="OPTIMIZACIÓN", width=15, height=2, borderwidth=3,
                                       font=("Arial", 10), activebackground="azure2",
                                       relief="ridge", command=lambda: [self.OPTI()], state=DISABLED)
            self.OPTIMIZACION.place(x=700, y=260)

            self.OBJETO = tk.Button(self.root9, text="OBJETO", width=15, height=2, borderwidth=3,
                                       font=("Arial", 10), activebackground="azure2",
                                       relief="ridge", command=lambda: [], state=DISABLED)
            self.OBJETO.place(x=700, y=310)

            self.SUBIR = tk.Button(self.root9, text="SUBIR ARCHIVO", width=15, height=2, borderwidth=3,
                                    font=("Arial", 10), activebackground="azure2",
                                    relief="ridge", command=lambda: [self.Subir()])
            self.SUBIR.place(x=700, y=360)

            self.CLEAN = tk.Button(self.root9, text="LIMPIAR", width=15, height=2, borderwidth=3,
                                    font=("Arial", 10), activebackground="azure2",
                                    relief="ridge", command=lambda: [self.Clean()])
            self.CLEAN.place(x=700, y=410)

            self.SAVE = tk.Button(self.root9, text="GUARDAR", width=15, height=2, borderwidth=3,
                                   font=("Arial", 10), activebackground="azure2",
                                   relief="ridge", command=lambda: [self.Guardar()])
            self.SAVE.place(x=700, y=459)

            self.root9.mainloop()

    def Clean(self):
        self.Pantalla.delete("1.0",END)
        self.Clean_consola()

    def Clean_consola(self):
        self.listbox2.delete(0, END)


    def Subir(self):
        archivo_texto = filedialog.askopenfilename()
        if archivo_texto == "":
            pass
        else:
            f = open(archivo_texto, "r")
            self.Pantalla.delete("1.0", tk.END)
            for x in f:
                self.Pantalla.insert(END, x)
                print(x)
            f.close()

    def Guardar(self):
        CODIGO_ALTO_NIVEL = self.Pantalla.get("1.0", tk.END)
        archivo_texto = filedialog.asksaveasfilename()
        if archivo_texto == "":
            pass
        else:
            with open(archivo_texto, 'w') as archivo:
                archivo.write(CODIGO_ALTO_NIVEL)

    def Lexico(self):
        self.Clean_consola()
        self.SINTaCTICO.configure(state=NORMAL)
        self.root9.update()
        CODIGO_ALTO_NIVEL = self.Pantalla.get("1.0", tk.END)
        LEXICO(CODIGO_ALTO_NIVEL, self.listbox2, self.Pantalla)

    def Sintáctico(self):
        self.Clean_consola()
        self.SEMaNTICO.configure(state=NORMAL)
        self.root9.update()
        SIN(0,0,0,0,0,0,0,0)

    def Semantico(self):
        self.Clean_consola()
        self.CODIGO.configure(state=NORMAL)
        SEM(self.listbox2)

    def Codigo_Intermedio(self):

        self.OPTIMIZACION.configure(state=NORMAL)
        print ("CODIGO INTERMEDIO")
        LOL.Limpiar_archivo(self)
        DIV.Funcion_Separa_Parentesis(self) #llamamos a separar en parentesis las operaciones

        OPERA_DIVIDIDAS=LOL.Obtener_Operaciones_de_Archivo(self)
        print(OPERA_DIVIDIDAS, "Lista de todas las Opraciones con comas")

        LISTA_CERO=[]
        LISTA_DOS=[]
        ORIG=[]
        LISTA_TRES=[]

        for line in OPERA_DIVIDIDAS:
            print(line, "LINE")
            Exp_Original = line.split(",")
            expresion = line.split(",")
            expresion2 = line.split(",")
            expresion3 = line.split(",")
            print (expresion, "antes")

            UltElement = ""
            PosUltElement = (len(expresion)) - 1
            TamUltimoElem = (len(expresion[PosUltElement]))
            for salto in range(TamUltimoElem - 1):
                UltElement = UltElement + expresion[PosUltElement][salto]
                print(str(UltElement), ("Correccion de la linea"))

            Exp_Original[PosUltElement] = UltElement
            expresion[PosUltElement] = UltElement
            expresion2[PosUltElement] = UltElement
            expresion3[PosUltElement] = UltElement

            print(expresion, "Despues de la correccion")
            if len(Exp_Original) > 5:
                ORIG.append(Exp_Original)
                LISTA_CERO.append(expresion)
                LISTA_DOS.append(expresion2)
                LISTA_TRES.append(expresion3)
            print("LISTAS QUE ESTAN GUARDANDO....", LISTA_CERO, LISTA_DOS, LISTA_TRES)
            print (ORIG)

        posicion=0
        ID.Interfaz_FaseD.Recorrer_LISTAS(self, LISTA_CERO, LISTA_DOS, LISTA_TRES, posicion, ORIG)

    def OPTI(self):
        LOG_OPTI()


    def NumeroEntero1(self,Var):
        try:
            int(Var)
            return True
        except ValueError:
            return False

    def NumeroFlotante1(self,Var):
        try:
            float(Var)
            return True
        except ValueError:
            return False
G=GRAFICO()