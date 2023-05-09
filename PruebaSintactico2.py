from RecuperaTOKENS import RECUPERA as REC
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import  filedialog

class Sintactico():
    def __init__(self, Con_sentencias, Con_decvar, Con_MOstrarD, Con_TDato, Con_Operaci, Con_NombreVar, Con_PedDato, Con_sent):
        REC.Limpiar_archivo(self)
        self.NT = ["sent","sentencias","declaravar","asignavar", "pedirdatos", "mostrardatos",
                   "tipodatoDec","tipodatoPide" , "nombrevar","operaciones","numero","operador","caracter",
                   "mensaje","comentar",  "LMayus", "LMinus | Numero","(sentencias)*", "(,nombrevar)+",
                   "LMayus, LMinus | Numero",  "(nombrevar | numero)",
                   "(operador (nombrevar)  |  (numero))*",
                   "(operador (nombrevar)  |  (numero))"
                   , "(,nombrevar | 'mensaje')*", "(nombrevar | 'mensaje')", "textomsj"]

        self.Sent = [["GO",";","sentencias","GON",";"]]

        self.Sentencias = [["operaciones", "(sentencias)*"], ["declaravar", "(sentencias)*"],
                           ["asignavar", "(sentencias)*"], ["pedirdatos", "(sentencias)*"],
                           ["mostrardatos", "(sentencias)*"], ["comentar", "(sentencias)*"]]

        self.DeclararVar = [[ "tipodatoDec", "nombrevar", "(,nombrevar)+",";"]]
        self.AsignaVar = [["nombrevar" , "=", "(nombrevar | numero)", ";"]]
        self.PedirDatos = [["tipodatoPide", "nombrevar", ";" ]]
        self.Mensaje = [["'","textomsj", "'"]]
        self.MostrarDatos = [["SHOW", "mensaje", "(,nombrevar | 'mensaje')*",";"]]

        self.TipoDatoDeclara = ["ENT", "DEC", "CHAR", "STR", "FLAG"]
        self.TipoDatoPide = ["VALUE", "ENTER"]

        self.Operaciones = [["nombrevar" , "=", "(nombrevar | numero)" ,"operador","(nombrevar | numero)", "(operador (nombrevar)  |  (numero))*", ";"]]
        self.Operador = ["+","-", "/", "*"]
        self.Comentar = [["#","textomsj"]]
        self.NombreVariable=[["LMayus, LMinus | Numero"]]
        self.LMinus=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]
        self.LMayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R",
                       "S", "T", "U", "V", "W", "X", "Y", "Z"]

        self.PilaAnalisisReverse = ["$", self.NT[0]]
        self.PilaAnalizados = ["&"]
        self.Regla = ""
        self.Letra="n" #iniciamos con la n

        #Variables para analizar los NOMBRES DE VARIABLES
        self.pos = 0
        self.car =0
        self.Palabra=""

        #variables Contadores para recorrer NT´S
        self.Conta=None

        self.BAN_Operaciones = False

        obtenertokens = (REC.Obtener_Token_de_Archivo(self))
        self.Tokens = obtenertokens.split("\n")

        self.LineaDeAnalisis = [self.Letra,1, self.PilaAnalizados, self.PilaAnalisisReverse[1], self.PilaAnalisisReverse[0]]

        BanCierre = False
        while BanCierre == False:
            #input()
            BanCierre =self.Logico()
        self.TABLAResultados()
        REC.Limpiar_archivo(self)

    def Logico(self):
        Termino = False
        Ban = False
        self.CicloRight() #mostramos la primera liena

        if self.LineaDeAnalisis[0] == "n":
            UltimoElemento = (len(self.PilaAnalisisReverse))-1
            #=========================Determina cual es el elemento sin contador a analizar
            ElementoAnalisis = self.PilaAnalisisReverse[UltimoElemento]
            print (ElementoAnalisis, "= Elemento Analisis en N")

            if ElementoAnalisis== "$":
                self.Regla_3(ElementoAnalisis)
            else:
                Es_NT = False
                for i in range(len(self.NT)):
                    E = self.NT[i]
                    if ElementoAnalisis == E:
                        Es_NT = True

                if Es_NT == True: #NO TERMINAL
                    self.Conta=None
                    self.Regla = "Regla 1: Expansion del árbol"
                    print ("\n" ,self.Regla)
                    self.Regla_1(ElementoAnalisis)

                elif Es_NT == False: #TERMINAL
                    Concordancia = self.Concordancia(ElementoAnalisis)
                    if Concordancia == True: #Tiene concordancia con la posision
                        self.Regla = "Regla 2: Concordancia de un símbolo"
                        print ("\n" ,self.Regla)
                        self.Regla_2(ElementoAnalisis)

                    elif Concordancia == False: #No tiene concordancia con la posicion
                        self.Regla = "Regla 4: No Concordancia de un símbolo"
                        print ("\n" ,self.Regla)
                        self.Regla_4()
            #self.Logico()
        elif self.LineaDeAnalisis[0] == "r":

            LastPos= len(self.PilaAnalizados)-1
            ElementoAnalisis = self.PilaAnalizados[LastPos]

            #para no tomar el elemento con su numero de opcion
            ElementoAnalisis= self.Elemento_Original(ElementoAnalisis)

            print(ElementoAnalisis, "= Elemento Analisis r")

            #saber si tiene más opciones o nel
            Bandera_alternativas= self.Regla_6a(ElementoAnalisis) # Tener otra alternativa
            print ("viendo opciones para", ElementoAnalisis, Bandera_alternativas)

            if Bandera_alternativas==True:
                self.Regla= "Regla 6a: Hay otra alternativa para NT"
                self.Letra="n"
                print ("\n" ,self.Regla)
                self.MeterProduccionPila(ElementoAnalisis)
            else:
                print ("ver si es terminal o no terminal")
                Es_NT = False
                for i in range(len(self.NT)):
                    E = self.NT[i]
                    if ElementoAnalisis == E:
                        Es_NT = True #
                        print ("es No terminal")

                if Es_NT == False: #cuando es un terminal
                    self.Regla = "Regla 5: Retroceso a la entrada"
                    print ("es un terminal")
                    print(self.Regla)
                    self.Regla_5()

                else:
                    print ("Es un NO terminal")
                    if ElementoAnalisis == "sent":
                        self.Regla= "Regla 6b: Siguiente Alternativa: ERROR"
                        print ("\n ", self.Regla)
                        self.Regla_6b()

                    else:
                        print("entra a 6c", "alternativas disponibles: ", Bandera_alternativas)
                        self.Regla = "Regla 6c: Siguiente Alternativa: Retroceso a la entrada"
                        self.Regla_6c()

        elif (self.LineaDeAnalisis[0] == "t" or self.LineaDeAnalisis[0] == "e"):
            Termino = True
        return Termino
        #self.Logico()

#=========================================================================================================================
#=========================================================================================================================
    def Elemento_Original(self, ElementoAnalisis):
        ToConvert = ElementoAnalisis[(len(ElementoAnalisis)) - 1]
        print ("Estamos en Elemento Original")
        print (ElementoAnalisis, ToConvert)
        BanNumero = False
        BanTerminal = False
        ElementWONum = ""

        for i in range(0, 9):
            if (ToConvert) == str(i):
                BanNumero = True

        if BanNumero == True:
            for i in range((len(ElementoAnalisis)) - 1):
                ElementWONum = ElementWONum + ElementoAnalisis[i]


            for j in range(0, (len(self.NT)) ):
                if self.NT[j] == ElementWONum:  # si es a huevo un no terminal
                    BanTerminal == True
                    ElementoAnalisis = self.NT[j]

        return ElementoAnalisis

    def CicloRight(self):
        LDA= self.LineaDeAnalisis
        self.PilaAnalisis_Mostrar = []
        C = ((len(self.PilaAnalisisReverse)) - 1)
        while C >= 0:
            self.PilaAnalisis_Mostrar.append(self.PilaAnalisisReverse[C])
            C = C - 1
        self.LineaDeAnalisis=[self.Letra, LDA[1], LDA[2], self.PilaAnalisis_Mostrar]
        print ("\n Nueva Linea de Analisis")
        print(self.LineaDeAnalisis)
        REC.Meter_Linea(self, self.LineaDeAnalisis)

    def MeterProduccionPila(self,ElementoNoTerminal):
        #Vemos que NT es el que se analizo para buscar su produccion y meterla a la lista por analisar

        #YA ESTA
        if ElementoNoTerminal == "sent":
            if self.Conta == None:
                print("Primera vez en sent")
                # meter el elemento con su primer numero de indice en cero ya que
                # cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)

                Produccion = self.Sent[0]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

        # AL PARECER YA ESTA
        elif ElementoNoTerminal == "sentencias": #Tenemos varias opciones en sentencias

            if self.Conta==None:
                print ("Primera vez en sentencias")
                #meter el elemento con su primer numero de indice en cero ya que
                #cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)

                Produccion = self.Sentencias[0]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

            elif self.Conta >6:
                self.Conta=None
            else:
                #sacamos la produccion de sentencias anterior

                for i in range(0, 2):
                    self.SacarElementoPila(self.PilaAnalisisReverse)

                # Sacamos y metemos para cambio de NUMERO
                self.SacarElementoPila(self.PilaAnalizados)
                self.Conta = self.Conta + 1
                self.PilaAnalizados.append(ElementoNoTerminal + str(self.Conta))

                Produccion= self.Sentencias[self.Conta-1]
                #Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

        # AL PARECER YA ESTA
        elif ElementoNoTerminal == "declaravar":
            if self.Conta == None:
                print("Primera vez en declaravar")
                # meter el elemento con su primer numero de indice en cero ya que
                # cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)

                Produccion = self.DeclararVar[0]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

        #AL PARECER YA ESTA
        elif ElementoNoTerminal == "asignavar":
            if self.Conta == None:
                print("Primera vez en asignavar")
                # meter el elemento con su primer numero de indice en cero ya que
                # cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)

                Produccion = self.AsignaVar[0]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

        #AL PARECER YA ESTA
        elif ElementoNoTerminal == "pedirdatos":
            if self.Conta == None:
                print("Primera vez en pedirdatos")
                # meter el elemento con su primer numero de indice en cero ya que
                # cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)

                Produccion = self.PedirDatos[0]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

            elif self.Conta > 2:
                self.Conta = None
            else:
                # sacamos la produccion de sentencias anterior

                for i in range(0, 3):
                    self.SacarElementoPila(self.PilaAnalisisReverse)

                # Sacamos y metemos para cambio de NUMERO
                self.SacarElementoPila(self.PilaAnalizados)
                self.Conta = self.Conta + 1
                self.PilaAnalizados.append(ElementoNoTerminal + str(self.Conta))

                Produccion = self.PedirDatos[self.Conta - 1]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

        #YA ESTA
        elif ElementoNoTerminal == "mostrardatos":
            if self.Conta == None:
                print("Primera vez en mostrardatos")
                # meter el elemento con su primer numero de indice en cero ya que
                # cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)

                Produccion = self.MostrarDatos[0]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

        #YA ESTA
        elif ElementoNoTerminal == "mensaje":
            if self.Conta == None:
                print("Primera vez en mensaje")
                # meter el elemento con su primer numero de indice en cero ya que
                # cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)

                Produccion = self.Mensaje[0]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

        # AL PARECER YA ESTA
        elif ElementoNoTerminal == "tipodatoDec":
            print ("valor se selc.Conta;", self.Conta)

            if self.Conta==None:
                print ("Primera vez en tipode dato")
                #meter el elemento con su primer numero de indice en cero ya que
                #cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append(self.TipoDatoDeclara[0])

            elif self.Conta >7:
                self.Conta=None
            else:

                self.SacarElementoPila(self.PilaAnalizados)
                self.Conta=self.Conta+1
                self.PilaAnalizados.append(ElementoNoTerminal + str(self.Conta) )
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append(self.TipoDatoDeclara[self.Conta-1])

        # AL PARECER YA ESTA
        elif ElementoNoTerminal == "tipodatoPide":
            print ("valor se selc.Conta;", self.Conta)
            self.BAN_DeclaraVar = False
            self.BAN_nombrevar = False
            self.BAN_PedirDato = False
            self.BAN_MostrarDatos = False
            self.BAN_Operaciones = False

            if self.Conta==None:
                print ("Primera vez en tipode dato")
                #meter el elemento con su primer numero de indice en cero ya que
                #cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append(self.TipoDatoPide[0])

            elif self.Conta >7:
                self.Conta=None
            else:

                self.SacarElementoPila(self.PilaAnalizados)
                self.Conta=self.Conta+1
                self.PilaAnalizados.append(ElementoNoTerminal + str(self.Conta) )
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append(self.TipoDatoPide[self.Conta-1])

        #YA ESTA
        elif ElementoNoTerminal == "nombrevar":
            if self.Conta == None:
                print("Primera vez en nombrevar")
                # meter el elemento con su primer numero de indice en cero ya que
                # cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)

                Produccion = self.NombreVariable[0]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

        #ya estaaa
        elif ElementoNoTerminal== "LMayus, LMinus | Numero":

            Posicion = (self.LineaDeAnalisis[1]) - 1
            self.Tokens[Posicion]

            self.SacarElementoPila(self.PilaAnalisisReverse)
            self.PilaAnalizados.append("LMayus, LMinus | Numero")

            #print ("ANlizando NOmbre de variable", self.Tokens)
            Bandera= self.IDENTIFICADOR_SENCILLO(self.Tokens[Posicion])
            if Bandera==True:
                print ("si es un identificador")
                self.PilaAnalisisReverse.append(self.Tokens[Posicion])
            else:
                print ("no es un identi")
                self.PilaAnalisisReverse.append(" x ")

        #PARECE QUE YA ESTA
        elif ElementoNoTerminal == "operaciones":
            if self.Conta == None:
                print("Primera vez en operaciones")
                # meter el elemento con su primer numero de indice en cero ya que
                # cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)

                Produccion = self.Operaciones[0]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

        elif ElementoNoTerminal == "operador":

            banOperador = False
            Posicion = (self.LineaDeAnalisis[1]) - 1
            Token = self.Tokens[Posicion]

            for i in range((len(self.Operador))):
                operador = self.Operador[i]
                if operador == Token:
                    banOperador = True
                    Val = i

            if banOperador == True:
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalizados.append(ElementoNoTerminal+ str(Val))
                self.PilaAnalisisReverse.append(self.Operador[Val])
                self.Con_NomVar_Num = 0

            else:
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalizados.append(ElementoNoTerminal)
                self.PilaAnalisisReverse.append(" x ")

        #YA ESTA
        elif ElementoNoTerminal == "comentar":
            if self.Conta == None:
                print("Primera vez en mensaje")
                # meter el elemento con su primer numero de indice en cero ya que
                # cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)

                Produccion = self.Comentar[0]
                # Metemos la produccion del elementoAnalisis a REVERSE
                TamañoProd = len(Produccion) - 1
                while TamañoProd >= 0:
                    self.PilaAnalisisReverse.append(Produccion[TamañoProd])
                    TamañoProd -= 1

        #PARECE QUE YA ESTA
        elif ElementoNoTerminal== "numero":
            Numero=True
            Token=self.Tokens[int(self.LineaDeAnalisis[1])-1]
            for i in range (0, len(Token)):
                Ban = self.Verifica_sies_numero(Token[i])
                if Ban== False:
                    Numero=False
            if Numero==False:

                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append(" x .")
            else:
                self.PilaAnalizados.append(ElementoNoTerminal)
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append(Token)

        #YA ESTA
        elif ElementoNoTerminal== "(sentencias)*":
            #Primero verificamos si lo necesitamos o  no....
            print ("Posicion TOKEN *:", self.LineaDeAnalisis[1] - 1, self.Tokens[self.LineaDeAnalisis[1] - 1])

            if (self.Tokens[self.LineaDeAnalisis[1] - 1]) == "GON":
                self.SacarElementoPila(self.PilaAnalisisReverse)

            elif (self.Tokens[self.LineaDeAnalisis[1] - 1]) != "GON":
                self.SacarElementoPila(self.PilaAnalisisReverse)
                print ("Hay más elementos enfrente.")
                self.PilaAnalisisReverse.append("sentencias")

        #YA ESTA
        elif ElementoNoTerminal == "(,nombrevar)+":
            if self.Tokens[self.LineaDeAnalisis[1] - 1] == ";":
                print("Condicional PARA QUE PARE DE BUSCAR MÁS NOMBRES DE VARIABLES: ",
                self.Tokens[self.LineaDeAnalisis[1] - 1])
                self.SacarElementoPila(self.PilaAnalisisReverse)
                print("salio ;")
            else:
                print("Primera vez en (,nombrevar)+")
                # meter el elemento con su primer numero de indice en cero ya que
                # cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato

                #la produccion de ,nombrevar+ es de dos la coma y nombrevar
                self.PilaAnalisisReverse.append("nombrevar")
                self.PilaAnalisisReverse.append(",")

        #YA ESTA
        elif ElementoNoTerminal== "(nombrevar | numero)":

            if self.Conta==None:
                print ("Primera vez en nombrevar | numero")
                #meter el elemento con su primer numero de indice en cero ya que
                #cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append("nombrevar")

            elif self.Conta >2:
                self.Conta=None
            else:

                # Sacamos y metemos para cambio de NUMERO
                self.SacarElementoPila(self.PilaAnalizados)
                self.Conta = self.Conta + 1
                self.PilaAnalizados.append(ElementoNoTerminal + str(self.Conta))
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append("numero")

        elif ElementoNoTerminal == "(operador (nombrevar)  |  (numero))*":

            if self.Tokens[self.LineaDeAnalisis[1] - 1] == ";":
                print("Condicional PARA QUE PARE DE BUSCAR MÁS operadores y nombres de variables o numeros: ",
                      self.Tokens[self.LineaDeAnalisis[1] - 1])
                self.SacarElementoPila(self.PilaAnalisisReverse)

            else:
                self.PilaAnalizados.append(ElementoNoTerminal + "1")

                self.PilaAnalisisReverse.append("(operador (nombrevar)  |  (numero))")
                #self.PilaAnalisisReverse.append("(nombrevar | numero)")
                #self.PilaAnalisisReverse.append("operador")

        #YA ESTA
        elif ElementoNoTerminal == "(operador (nombrevar)  |  (numero))":

            if self.Tokens[self.LineaDeAnalisis[1] - 1] == ";":
                print("Condicional PARA QUE PARE DE BUSCAR MÁS operadores y nombres de variables o numeros: ",
                      self.Tokens[self.LineaDeAnalisis[1] - 1])
                self.SacarElementoPila(self.PilaAnalisisReverse)


            else:
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append("(nombrevar | numero)")
                self.PilaAnalisisReverse.append("operador")

        elif ElementoNoTerminal == "(,nombrevar | 'mensaje')*":

            print("Print el token en el que vamos ",
                  self.Tokens[self.LineaDeAnalisis[1] - 1])

            if self.Tokens[self.LineaDeAnalisis[1] - 1] == ";":
                print("Condicional PARA QUE PARE DE BUSCAR MÁS : ",
                      self.Tokens[self.LineaDeAnalisis[1] - 1])
                self.SacarElementoPila(self.PilaAnalisisReverse)
                print("salio ;")

            else:
                self.PilaAnalisisReverse.append("(nombrevar | 'mensaje')")
                self.PilaAnalisisReverse.append(",")

        #YA ESTA
        elif ElementoNoTerminal == "(nombrevar | 'mensaje')":


            if self.Conta==None:
                print ("Primera vez en nombrevar | mensaje")
                #meter el elemento con su primer numero de indice en cero ya que
                #cself.Conta no tiene ningun valor ya que se metio directo a regla1
                self.PilaAnalizados.append(ElementoNoTerminal + "1")
                # meter la produccion de la lista de tipo de dato
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append("nombrevar")

            elif self.Conta >2:
                self.Conta=None
            else:

                # Sacamos y metemos para cambio de NUMERO
                self.SacarElementoPila(self.PilaAnalizados)
                self.Conta = self.Conta + 1
                self.PilaAnalizados.append(ElementoNoTerminal + str(self.Conta))
                self.SacarElementoPila(self.PilaAnalisisReverse)
                self.PilaAnalisisReverse.append("mensaje")

        #YA ESTA
        elif ElementoNoTerminal == "textomsj":
            self.SacarElementoPila(self.PilaAnalisisReverse)
            self.PilaAnalizados.append(ElementoNoTerminal)
            self.PilaAnalisisReverse.append(self.Tokens[self.LineaDeAnalisis[1]-1])

    def Concordancia(self,ElementoAnalisis):
        print ("Posicion:", self.LineaDeAnalisis[1],
               "\nElemento de análisis:",ElementoAnalisis,
               "\nElemento del código:", self.Tokens[self.LineaDeAnalisis[1] - 1])
        BanConcordancia = False

        Posicion = (self.LineaDeAnalisis[1]) - 1 # sacamos la posicion del elemento  que debemos analizar
        Token = self.Tokens[Posicion] #este es el token completo ejemplo ("Var1", "STR", "123", etc...)

        if Token == ElementoAnalisis:
            BanConcordancia = True
        else:
            BanConcordancia = False

        return BanConcordancia

    def SacarElementoPila(self,Pila):
        Pila.pop()

    def Regla_1(self, ElementoAnalisis): #Expansion del árbol
        print ("REGLA 1 ELEMENTO", ElementoAnalisis)
        self.MeterProduccionPila(ElementoAnalisis)

    def Regla_2(self, ElementoAnalisis): #concordancia de un simbolo AQUI SUMAMOS PARA AVANZAR EN LOS TOKENS DEL CODIGO

        #Agregamos elemento que estamos analizando a la pila de analizados y lo sacamos de la pila
        #de analisis y aumentamos la posision de la cadena.
        self.PilaAnalizados.append(ElementoAnalisis)

        self.LineaDeAnalisis[1] = self.LineaDeAnalisis[1] + 1 #POSICION ++
        self.SacarElementoPila(self.PilaAnalisisReverse)
        #==========================================================================================

    def Regla_3(self,ElementoAnalisis):
        if (self.LineaDeAnalisis[1])-1 == len(self.Tokens):
            print("LA CADENA SE ACEPTA :D")
            self.Regla = "Regla 3: Terminación con ÉXITO."
            print("\n", self.Regla)
            self.Letra = "t"
            self.SacarElementoPila(self.PilaAnalisisReverse)
            self.PilaAnalisisReverse.append("&")
            self.CicloRight()
        else:
            print("EXISTEN MAS TOKENS DESPUES DEL GON ; ")
            print(self.Tokens)
            self.Regla_6b()

    def Regla_4(self): #NO CONCORDANCIA DE UN SIMBOLO ALV
        #La n pasa a ser "r"
        self.Letra= "r"

    def Regla_5(self):
        ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados) - 1]
        Elemento_SIN_numero = self.Elemento_Original(ElementoAnalisis_con_numero)
        print (Elemento_SIN_numero, "Elemento sin numero en regla 5")
        print("Elementos necesarios para la condicional: ")
        print(self.LineaDeAnalisis[0], Elemento_SIN_numero, self.PilaAnalisisReverse[(len(self.PilaAnalisisReverse))-1], self.PilaAnalizados[(len(self.PilaAnalizados))-2])
        if (self.LineaDeAnalisis[0] == "r") \
                and (Elemento_SIN_numero == ";") \
                and (self.PilaAnalisisReverse[(len(self.PilaAnalisisReverse))-1] == "sentencias" or
                     self.PilaAnalisisReverse[(len(self.PilaAnalisisReverse))-1] == "(sentencias)*") \
                and (self.PilaAnalisisReverse[(len(self.PilaAnalisisReverse)) - 2] == "sentencias" or
                     self.PilaAnalisisReverse[(len(self.PilaAnalisisReverse)) - 2] == "(sentencias)*"):
            print("ENCONTRAMOS UN SENTENCIAS REPETIDO QUE SE REPETIRA")
            self.SacarElementoPila(self.PilaAnalisisReverse)
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            self.SacarElementoPila(self.PilaAnalizados)
            self.LineaDeAnalisis[1] = self.LineaDeAnalisis[1] - 1  # POSICION --

        elif (self.LineaDeAnalisis[0] == "r") \
                and (Elemento_SIN_numero == ";") \
                and (self.PilaAnalisisReverse[(len(self.PilaAnalisisReverse))-1] == "sentencias" or
                     self.PilaAnalisisReverse[(len(self.PilaAnalisisReverse))-1] == "(sentencias)*")\
                and (self.PilaAnalisisReverse[(len(self.PilaAnalisisReverse)) - 2] != "sentencias" or
                     self.PilaAnalisisReverse[(len(self.PilaAnalisisReverse)) - 2] != "(sentencias)*"):
            print("ESTE SENTENCIAS ES EL ORIGINAL")
            #self.SacarElementoPila(self.PilaAnalisisReverse)
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            self.SacarElementoPila(self.PilaAnalizados)
            self.LineaDeAnalisis[1] = self.LineaDeAnalisis[1] - 1  # POSICION --
        else:
            print("NO ENCONTRAMOS UN SENTENCIAS")
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            self.SacarElementoPila(self.PilaAnalizados)
            self.LineaDeAnalisis[1] = self.LineaDeAnalisis[1] - 1  # POSICION --

    def Regla_6c(self): #Retroceso a la entrada
        #buscamos la produccion del elemento analizadp
        ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados)-1]
        Elemento_SIN_numero= self.Elemento_Original(ElementoAnalisis_con_numero)
        if Elemento_SIN_numero == "tipodatoDec":
            #como tipo dato solo tiene una produccion la sacamos con pop
            self.SacarElementoPila(self.PilaAnalisisReverse)
            #volvemos a meter el elemento analizado a la Pila reverse
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            #sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        elif Elemento_SIN_numero == "tipodatoPide":
            #como tipo dato solo tiene una produccion la sacamos con pop
            self.SacarElementoPila(self.PilaAnalisisReverse)
            #volvemos a meter el elemento analizado a la Pila reverse
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            #sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        #YA ESTA
        elif Elemento_SIN_numero == "declaravar": #sip
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = self.DeclararVar[0]
            #TamañoProdAnterior = len(ProdAnterior) #menos uno por que ya saque el extra
            postemp = (len(self.PilaAnalisisReverse)) - len(ProdAnterior)
            print("Posiciones n lista reverse y en produccion de Declaravar")
            print(self.PilaAnalisisReverse[postemp], self.DeclararVar[0][len(ProdAnterior) - 1])
            # if self.Operaciones[0][ProdAnterior - 1] == self.PilaAnalisisReverse[postemp]
            if self.PilaAnalisisReverse[postemp] == self.DeclararVar[0][len(ProdAnterior) - 1]:
                TamañoProdAnterior = len(ProdAnterior)
            else:
                TamañoProdAnterior = len(ProdAnterior) - 1

            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        #YA ESTA
        elif Elemento_SIN_numero == "asignavar":
            #tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior= self.AsignaVar[0]
            TamañoProdAnterior = len(ProdAnterior)
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            #==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        elif Elemento_SIN_numero == "operador":
            #tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior= 1
            TamañoProdAnterior = (ProdAnterior)
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            #==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        #YA ESTA
        elif Elemento_SIN_numero == "mensaje":
            #tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior= 3
            for i in range(ProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            #==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        elif Elemento_SIN_numero == "numero":
            #tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior= 1
            TamañoProdAnterior = (ProdAnterior)
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            #==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        #YA ESTA
        elif Elemento_SIN_numero == "pedirdatos":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = self.PedirDatos[0]
            TamañoProdAnterior = len(ProdAnterior)
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        #YA ESTA
        elif Elemento_SIN_numero == "comentar":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = 2
            for i in range(ProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        #YA ESTA
        elif Elemento_SIN_numero == "mostrardatos":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = self.MostrarDatos[0]
            #TamañoProdAnterior = len(ProdAnterior)
            postemp = (len(self.PilaAnalisisReverse)) - len(ProdAnterior)
            print("Posiciones n lista reverse y en produccion de Mostrardatos")
            print(self.PilaAnalisisReverse[postemp], self.MostrarDatos[0][len(ProdAnterior) - 1])
            # if self.Operaciones[0][ProdAnterior - 1] == self.PilaAnalisisReverse[postemp]
            if self.PilaAnalisisReverse[postemp] == self.MostrarDatos[0][len(ProdAnterior) - 1]:
                TamañoProdAnterior = len(ProdAnterior)
            else:
                ban = False
                for i in range(len(self.MostrarDatos[0])):
                    if (self.PilaAnalisisReverse[postemp] == self.MostrarDatos[0][i]) or (self.PilaAnalisisReverse[postemp] == ",") or (self.PilaAnalisisReverse[postemp] == "(nombrevar | 'mensaje')") or (self.PilaAnalisisReverse[postemp] == "(,nombrevar | 'mensaje')*"):
                        ban = True
                if ban == True:
                    TamañoProdAnterior = len(ProdAnterior) + 2
                else:
                    TamañoProdAnterior = len(ProdAnterior) - 1
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        elif Elemento_SIN_numero=="nombrevar":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            TamañoProdAnterior = 1
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        #YA ESTA
        elif Elemento_SIN_numero== "sentencias":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = self.Sentencias[0]
            TamañoProdAnterior = len(ProdAnterior)
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        #YA ESTA
        elif Elemento_SIN_numero== "operaciones":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = len(self.Operaciones[0]) # Nombrevar, =  , Nomvre|Num , Opera , Nombre|Num
            postemp = (len(self.PilaAnalisisReverse)) - ProdAnterior
            print("Posiciones n lista reverse y en produccion de operaciones")
            print(self.PilaAnalisisReverse[postemp],self.Operaciones[0][ProdAnterior - 1])
            #if self.Operaciones[0][ProdAnterior - 1] == self.PilaAnalisisReverse[postemp]
            if self.PilaAnalisisReverse[postemp] == self.Operaciones[0][ProdAnterior - 1]:
                TamañoProdAnterior = (ProdAnterior)
            else:
                TamañoProdAnterior = (ProdAnterior) -1
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        elif ElementoAnalisis_con_numero== "LMayus, LMinus | Numero":
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)
            self.SacarElementoPila(self.PilaAnalisisReverse)
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)

        elif Elemento_SIN_numero == "(nombrevar | numero)":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = 1
            print("\n PRODUCCION ANTERIOR DE (nombrevar | numero):", ProdAnterior)
            TamañoProdAnterior = (ProdAnterior)
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================

            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        #YA ESTA
        elif Elemento_SIN_numero == "(nombrevar | 'mensaje')":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = 1
            print("\n PRODUCCION ANTERIOR DE (nombrevar | numero):", ProdAnterior)
            TamañoProdAnterior = (ProdAnterior)
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================

            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

        #YA ESTA sacamos extra
        elif Elemento_SIN_numero == "(,nombrevar)+":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = 2  #TIENE coma y nombrevar
            print("\n PRODUCCION ANTERIOR DE (nombrevar | numero):", ProdAnterior)
            TamañoProdAnterior = (ProdAnterior)
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================

            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)
            self.SacarElementoPila(self.PilaAnalisisReverse)

        #YA ESTA
        elif Elemento_SIN_numero == "(operador (nombrevar)  |  (numero))*":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = 2  # TIENE coma y nombrevar
            print("\n PRODUCCION ANTERIOR DE (nombrevar | numero):", ProdAnterior)
            TamañoProdAnterior = (ProdAnterior)
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================

            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)
            self.SacarElementoPila(self.PilaAnalisisReverse) #sacamos uno extra XD

        #YA ESTA
        elif Elemento_SIN_numero == "textomsj":
            # tenemos que sacar la produccion de la ultima opcion de declaravar
            ProdAnterior = 1
            TamañoProdAnterior = (ProdAnterior)
            for i in range(TamañoProdAnterior):
                self.SacarElementoPila(self.PilaAnalisisReverse)
            # ==================================================================
            self.PilaAnalisisReverse.append(Elemento_SIN_numero)
            # sacamos el elemento de analizados
            self.SacarElementoPila(self.PilaAnalizados)

    def Regla_6a(self, ElemAnal): #ver si tiene más caminos u opciones
        print("Entramos a 6a")
        print(ElemAnal)

        Ban=False
        if ElemAnal=="sentencias": #Sip
            ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados) - 1]
            numero = ElementoAnalisis_con_numero[len(ElementoAnalisis_con_numero) - 1]
            self.Conta = int(numero)
            Opciones= len(self.Sentencias)
            if self.Conta < Opciones:
                Ban=True

        elif ElemAnal=="declaravar":
            ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados) - 1]
            numero = ElementoAnalisis_con_numero[len(ElementoAnalisis_con_numero) - 1]
            self.Conta = int(numero)

            Opciones = len(self.DeclararVar) - 1
            if self.Conta < Opciones:
                Ban = True

        elif ElemAnal == "tipodatoDec": #Sip
            ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados) - 1]
            numero = ElementoAnalisis_con_numero[len(ElementoAnalisis_con_numero) - 1]
            self.Conta = int(numero)
            Opciones= len(self.TipoDatoDeclara)

            if self.Conta < Opciones:
                Ban = True

        elif ElemAnal == "tipodatoPide": #Sip
            ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados) - 1]
            numero = ElementoAnalisis_con_numero[len(ElementoAnalisis_con_numero) - 1]
            self.Conta = int(numero)
            Opciones= len(self.TipoDatoPide)

            if self.Conta < Opciones:
                Ban = True

        elif ElemAnal== "pedirdatos":
            ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados) - 1]
            numero = ElementoAnalisis_con_numero[len(ElementoAnalisis_con_numero) - 1]
            self.Conta = int(numero)

            Opciones=len(self.PedirDatos)
            if self.Conta < Opciones:
                Ban=True

        elif ElemAnal == "mostrardatos":
            ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados) - 1]
            numero = ElementoAnalisis_con_numero[len(ElementoAnalisis_con_numero) - 1]
            self.Conta = int(numero)
            Opciones = len(self.MostrarDatos)

            if self.Conta < Opciones:
                Ban = True

        elif ElemAnal == "operaciones":
            ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados) - 1]
            numero = ElementoAnalisis_con_numero[len(ElementoAnalisis_con_numero) - 1]
            self.Conta = int(numero)
            Opciones = len(self.Operaciones)

            if self.Conta < Opciones:
                Ban = True

        elif ElemAnal== "(nombrevar | numero)":
            ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados) - 1]
            Elemento_numero = ElementoAnalisis_con_numero[len(ElementoAnalisis_con_numero) - 1]
            self.Conta = int(Elemento_numero)

            Opciones = 2
            if self.Conta < Opciones:
                Ban = True

        elif ElemAnal == "(nombrevar | 'mensaje')":
            ElementoAnalisis_con_numero = self.PilaAnalizados[len(self.PilaAnalizados) - 1]
            Elemento_numero = ElementoAnalisis_con_numero[len(ElementoAnalisis_con_numero) - 1]
            self.Conta = int(Elemento_numero)
            print ("VIENDO MÁS OPCIONES PARA NOMBREVAR Y MENSAE", self.Conta)

            Opciones = 2
            if self.Conta < Opciones:
                Ban = True

        return Ban

    def Regla_6b(self):
        self.Letra="e"
        self.CicloRight()
        print ("LA CADENA NO SE ACEPTA")

    def Verifica_sies_numero(self,Car):
        num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","."]
        Ban1 = False
        BanPunt = False
        for i in range(0, len(num)):
            if Car == num[i]:
                Ban1 = True
        print(Ban1)
        return Ban1, BanPunt

    def Verifica_sies_minuscula(self,Car):
        abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
               "t", "u", "v", "w", "x", "y", "z"]
        Ban2 = False
        for a in range(0, len(abc)):
            if Car == abc[a]:
                Ban2 = True
            else:
                Ban2 = Ban2
        return Ban2

    def IDENTIFICADOR_SENCILLO(self,Tok):
        ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
               "T", "U", "V", "W", "X", "Y", "Z"]
        ListaPalabras = ["ENT", "DEC", "CHAR", "STR", "SHOW", "FLAG", "VALUE", "ENTER", "GO", "GON"]

        print("        Entra a Verifica Identificadores", Tok)
        BAN_I = False  # quiere decir que no se ha aceptado que es IDENTI

        if BAN_I == False:  # si paso el primer filtro de arriba entonces continua ya que puede

            # Identifica que la primera posicion sea una letra Mayuscula
            if Tok != " " and Tok != "" and Tok != "\n":
                for i in range(0, len(ABC)):
                    if Tok[0] == ABC[i]:
                        BAN_I = True

                # si esto se cumplio, entonces verificamos el resto de caracteres
                if BAN_I == True:
                    for i in range(1, len(Tok)):  # para los caracteres restantes
                        BanNumero = self.Verifica_sies_numero(Tok[i], )
                        if BanNumero == False:
                            BanMinuscula = self.Verifica_sies_minuscula(Tok[i])
                            if BanMinuscula == False:
                                BAN_I = False

        if BAN_I == True:
            print("            Es un Identificador", Tok)

        else:
            print("             No es Identificador", Tok)

        return BAN_I

    def TABLAResultados(self):
        self.root3 = Tk()
        self.root3.geometry('1200'
                            'x600')
        self.root3.title("COMPILADOR ")
        self.root3.configure(bg="olive drab1")

        self.LEN1 = tk.Label(self.root3, text="ANÁLISIS SINTACTICO", width=220, borderwidth=3,
                            font=("Helvatica", 17, "bold"), fg="white",
                            bg="dark green", anchor="c")
        self.LEN1.place(x=0, y=0)

        self.labelframe2 = tk.LabelFrame(self.root3, font=("Arial", 18), bg="cornflower blue")
        self.labelframe2.place(x=10, y=50)

        self.tabla2 = ttk.Treeview(self.labelframe2, columns=("0"), height="25")
        self.tabla2.column("#0", width=0)
        self.tabla2.column("0", width=990)

        self.tabla2.heading("0", text="ANALISIS", anchor='center')
        self.tabla2.grid(column=0, row=1)
        self.Insertar()
        self.root3.mainloop()

    def Insertar(self):
        obtener = (REC.Sacar_Lineas(self))
        self.Lineas = obtener.split("\n")
        for i in range(0, len(self.Lineas)):
            self.tabla2.insert('', 'end', values=[self.Lineas[i]])

#A = Sintactico(0,0,0,0,0,0,0,0)