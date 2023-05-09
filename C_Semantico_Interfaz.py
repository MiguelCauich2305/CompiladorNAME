import tkinter as tk
from tkinter import ttk
from tkinter import *

class Semantico():
    def Tabla_de_Gramatica(self):
        self.root2 = Tk()
        self.root2.geometry('1300'
                            'x400')
        self.root2.title("COMPILADOR")
        self.root2.configure(bg="olive drab1")

        self.LEN = tk.Label(self.root2, text="GRAMÁTICA", width=89, borderwidth=3,
                            font=("Helvatica", 17, "bold"), fg="white",
                            bg="dark green", anchor="c")
        self.LEN.place(x=0, y=0)

        self.labelframe2 = tk.LabelFrame(self.root2, font=("Arial", 18), bg="cornflower blue")
        self.labelframe2.place(x=10, y=50)

        self.tabla = ttk.Treeview(self.labelframe2, columns=("1", "11"), height="15")
        self.tabla.column("#0", width=0)
        self.tabla.column("1", width=600)
        self.tabla.column("11", width=610)

        self.tabla.heading('1', text='Regla Gramatical')
        self.tabla.heading('11', text='Regla Semántica')

        self.tabla.insert('', 'end', values=["sent==> GO; sentencias GON ;|GO;GON; "  , "sent.valor==> GO.valor; sentencias.valor GON.valor ;|GO.valor;GON.valor; " ])
        self.tabla.insert('', 'end', values=["sentencias==>declaravar(sentencias)*|pedirdatos (Sentencias)* | mostrardatos (sentencias)* | operaciones (sentencias)* |  comentar (sentencias)*|asignadatos (sentencias)*" , "sentencias.valor==>declaravar.valor(sentencias.valor)*|pedirdatos.valor (Sentencias.valor)* | mostrardatos.valor (sentencias.valor)* | operaciones.valor (sentencias.valor)* |  comentar.valor (sentencias.valor)*|asignadatos.valor (sentencias.valor)*"])
        self.tabla.insert('', 'end', values=["declaravar==>tipodatoDec (nombrevar);|tipodatoDec (nombrevar) (,(nombrevar))+;" , "declaravar.valor==>tipodatoDec.valor (nombrevar.valor);|tipodatoDec.valor (nombrevar.valor) (,(nombrevar.valor))+;"])
        self.tabla.insert('', 'end', values=["tipodedatoDec==>ENT | DEC | CHAR | STR | FLAG" , "tipodedatoDec.valor==>ENT | DEC | CHAR | STR | FLAG"])
        self.tabla.insert('', 'end', values=["pedirdatos==> tipodatoPide  (nombrevar) ;", "pedirdatos.valor==> tipodatoPide.valor  (nombrevar.valor) ;"])
        self.tabla.insert('', 'end', values=["tipodatoPide==> VALUE  | ENTER ", "tipodatoPide.valor==> VALUE  | ENTER "])
        self.tabla.insert('', 'end', values=["mostrardatos==> SHOW mensaje (,(nombrevar)| mensaje)* (;)" , "mostrardatos.valor==> SHOW.valor mensaje.valor (,(nombrevar.valor)| mensaje.valor)* (;)"])
        self.tabla.insert('', 'end', values=["mensaje==> ‘textomsj‘" , "mensaje.valor==> ‘textomsj‘"])
        self.tabla.insert('', 'end', values=["operaciones==> (nombrevar)=((nombrevar) | (numero)) operador ((nombrevar) | (numero)) (operador ((nombrevar) |(numero))) * ;" , "operaciones.valor==> (nombrevar.valor)=((nombrevar.valor) | (numero.valor)) operador.valor ((nombrevar.valor) | (numero.valor)) (operador.valor ((nombrevar.valor) |(numero.valor))) * ;"])
        self.tabla.insert('', 'end', values=["nombrevar==> [A…Z ]{1}([0…9] |[a…z])*" , "nombrevar.valor==> [A…Z ]{1}([0…9] |[a…z])*"])
        self.tabla.insert('', 'end', values=["numero==>[ 0..9 ]+|[0..9]+\.\[0..9]+", "numero.valor==>[ 0..9 ]+|[0..9]+\.\[0..9]+"])
        self.tabla.insert('', 'end', values=["operador==> + | - | / | * ", "operador.valor==> + | - | / | * "])
        self.tabla.insert('', 'end', values=["comentar==> (#) textomsj  ", "comentar.valor==> (#) textomsj  "])
        self.tabla.insert('', 'end', values=["asignardatos==> nombrevar=(nombrevar|numero) ;", "asignardatos.valor==> nombrevar.valor=(nombrevar.valor|numero.valor) ;"])

        self.tabla.grid(column=0, row=0)
        self.root2.mainloop()


#AQUI DESPUES DE GENERAR EL PRIMER PASO QUE ES LA TABLA ANTERIOR, LLAMAMOS A EL CHECADOR DE ERRORES Y LUEGO AL ARBOL
