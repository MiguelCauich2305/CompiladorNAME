import time
import tkinter as tk
from tkinter import ttk
from tkinter import *



class COD_INTER2():

#====================================================================================================
# ===================================================================================================
#====================================================================================
# ===================================================================================================
    def Triplos(self, exp):
        PreLista = []
        ListaTriplos=[]

        BanEXP = False
        Cont = 0
        while BanEXP == False:
            for i in range((len(exp))):
                if (exp[i] == ")") or (exp[i] == "("):
                    exp.pop(i)
                    BanEXP = False
                    break
                else:
                    BanEXP = True

        print("Operacion sin parentesis xd")
        print(exp)

        print("ahora toca el analisis")
        self.Operadores = ["+", "-", "/", "*", "="]
        BanderaIgual = False
        while BanderaIgual == False:
            PreLista = []
            self.Provicional = []
            self.Conca = ""
            self.ConcaCompleto = ""
            self.y = []
            self.prioridadGeneral = 0
            self.prioridadActual = 0
            self.posicionDePrioridadGeneral = 0
            self.posicionDePrioridadActual = 0
            for i in range(len(exp)):
                self.ElementoActual = exp[i]
                print("Elemento actual", self.ElementoActual)

                for j in range(len(self.Operadores)):
                    self.OperadorActual = self.Operadores[j]
                    print("Operador actual", self.Operadores[j])

                    if self.ElementoActual == self.OperadorActual:
                        if ((self.OperadorActual == "-") or (self.OperadorActual == "+")):
                            print("Encontramos un (-) o un (+)")
                            self.prioridadActual = 2
                            self.posicionDePrioridadActual = i

                        elif ((self.OperadorActual == "/") or (self.OperadorActual == "*")):
                            print("Encontramos un (/) o un (*)")
                            self.prioridadActual = 3
                            self.posicionDePrioridadActual = i

                        elif ((self.OperadorActual == "=")):
                            print("Encontramos un (=)")
                            self.prioridadActual = 1
                            self.posicionDePrioridadActual = i

                if self.prioridadActual > self.prioridadGeneral:
                    print("Encontramos una prioridad mayor, guardamos la posicion y prioridad")
                    self.prioridadGeneral = self.prioridadActual
                    self.posicionDePrioridadGeneral = self.posicionDePrioridadActual
                    print(self.prioridadGeneral, self.posicionDePrioridadGeneral)

                elif self.prioridadActual == self.prioridadGeneral:
                    print("Encontramos una prioridad Igual, continuamos con el primero")

                print("\n")
            if self.prioridadActual == 1:
                BanderaIgual = True
                Dir = "[" + str(Cont) + "]"
                PreLista.append(Dir)
                PreLista.append(exp[(self.posicionDePrioridadGeneral)])
                PreLista.append(exp[(self.posicionDePrioridadGeneral) - 1])
                PreLista.append(exp[(self.posicionDePrioridadGeneral) + 1])
                PreLista.append("---")
                print(self.Conca, "la concatenacion")
                ListaTriplos.append(PreLista)
                exp.pop((self.posicionDePrioridadGeneral) + 1)
                exp.pop((self.posicionDePrioridadGeneral))
                exp[(self.posicionDePrioridadGeneral) - 1] = Dir
                Cont = Cont + 1
                print(exp, "Reducida")
                print("Lista Triplos: ", ListaTriplos)
            else:
                Dir = "[" + str(Cont) + "]"
                PreLista.append(Dir)
                PreLista.append(exp[(self.posicionDePrioridadGeneral)])
                PreLista.append(exp[(self.posicionDePrioridadGeneral)-1])
                PreLista.append(exp[(self.posicionDePrioridadGeneral) + 1])
                print(self.Conca, "la concatenacion")
                ListaTriplos.append(PreLista)
                exp.pop((self.posicionDePrioridadGeneral) + 1)
                exp.pop((self.posicionDePrioridadGeneral))
                exp[(self.posicionDePrioridadGeneral) - 1] = Dir
                Cont = Cont + 1
                print(exp, "Reducida")
                print("Lista Triplos: ",ListaTriplos)

        return ListaTriplos

    def Triplos2(self, exp): ## este no jala bien, tiene un pequeño error
        # TRIPLOS==============================================================================
        print("TRIPLOSSSSS")
        Lista_Insertar_TRIPLOS = []
        Insertar_CodigoP_Interfaz = []
        BanEncontrado = False
        BanAux = False
        #Insertar_CodigoP_Interfaz.append("lda, " + str(exp[1] + ";"))
        GuardPos = 0
        GuardPosIGUAL = 0
        Cont = 0
        AUX = ""
        for ig in range(len(exp)):
            if exp[ig] == "=":
                GuardPosIGUAL = ig + 1
                print("Encontramos el igual, desde aqui empezamos a contar, posicion: ", GuardPosIGUAL)
                break

        while BanAux == False:
            GuardarPos = 0
            Insertar_CodigoP_Interfaz = []
            print("\n \n")
            for i in range(GuardPosIGUAL, (len(exp))):
                # print(exp[i])
                if exp[i] == ")":
                    BanEncontrado = True
                    GuardarPos = i
                    break
            if BanEncontrado == True:

                print(exp, "lista antes")
                elementos = [exp[GuardarPos - 3], exp[GuardarPos - 2], exp[GuardarPos - 1]]
                print(elementos)
                for j in range(len(elementos)):
                    if (elementos[j] == "="):
                        BanAux = True
                        break
                if BanAux == False:
                    (exp.pop(GuardarPos))
                    (exp.pop(GuardarPos - 1))
                    (exp.pop(GuardarPos - 2))
                    (exp.pop(GuardarPos - 3))
                    Direc = str ("[" + str(Cont) + "]")
                    exp[GuardarPos - 4] =  (Direc)
                    print(exp, "Lista despues")
                    Cont = Cont + 1

                    Insertar_CodigoP_Interfaz.append(Direc)
                    Insertar_CodigoP_Interfaz.append(elementos[1])
                    Insertar_CodigoP_Interfaz.append(elementos[0])
                    Insertar_CodigoP_Interfaz.append(elementos[2])
                    print("Codigo ordenado", Insertar_CodigoP_Interfaz)

                    Lista_Insertar_TRIPLOS.append(Insertar_CodigoP_Interfaz)

        elementos = [exp[1], exp[2], exp[3]]
        Direc = str("[" + str(Cont) + "]")
        Insertar_CodigoP_Interfaz.append(Direc)
        Insertar_CodigoP_Interfaz.append((elementos[1]))
        Insertar_CodigoP_Interfaz.append((elementos[0]))
        Insertar_CodigoP_Interfaz.append((elementos[2]))
        print("Final")
        Lista_Insertar_TRIPLOS.append(Insertar_CodigoP_Interfaz)
        print ("\nTROPLOSSS", Lista_Insertar_TRIPLOS)

        return Lista_Insertar_TRIPLOS


    def Cuadruplos(self,Lista_Triplos):
        print("Entre a Cuadruplos")
        self.Lista_Insertar_CUADRUPLOS = []

        for i in range((len(Lista_Triplos))):
            ListaCuadru = []
            Lista = Lista_Triplos[i]
            print(Lista, "Lista")
            El1 = Lista[0]
            El2 = Lista[1]
            El3 = Lista[2]
            El4 = Lista[3]
            BanderaDirecc = False
            if i == (len(Lista_Triplos)-1):
                for j in range((len(Lista))):
                    Elemento = Lista[j]
                    print(Elemento, "Elemento")
                    GuardarPosCar = 0
                    for k in range((len(Elemento))):
                        Car = Elemento[k]
                        print(Car, "Car")
                        if Car == "[":
                            BanderaDirecc = True
                            GuardarPosCar = k
                    if BanderaDirecc == True:
                        if j == 0:
                            El1 = "AUX" + str((int(Elemento[(GuardarPosCar) + 1])))
                        elif j == 1:
                            El2 = "AUX" + str((int(Elemento[(GuardarPosCar) + 1])))
                        elif j == 2:
                            El3 = "AUX" + str((int(Elemento[(GuardarPosCar) + 1])))
                        elif j == 3:
                            El4 = "AUX" + str((int(Elemento[(GuardarPosCar) + 1])))
                        BanderaDirecc = False

                ListaCuadru.append(El2)
                ListaCuadru.append(El1)
                ListaCuadru.append("---")
                ListaCuadru.append(El3)
                self.Lista_Insertar_CUADRUPLOS.append(ListaCuadru)

            else:
                for j in range((len(Lista))):
                    Elemento = Lista[j]
                    print(Elemento, "Elemento")
                    GuardarPosCar = 0
                    for k in range((len(Elemento))):
                        Car = Elemento[k]
                        print(Car, "Car")
                        if Car == "[":
                            BanderaDirecc = True
                            GuardarPosCar = k
                    if BanderaDirecc == True:
                        if j == 0:
                            El1 = "AUX" + str((int(Elemento[(GuardarPosCar)+1]))+1)
                        elif j == 1:
                            El2 = "AUX" + str((int(Elemento[(GuardarPosCar)+1]))+1)
                        elif j == 2:
                            El3 = "AUX" + str((int(Elemento[(GuardarPosCar)+1]))+1)
                        elif j == 3:
                            El4 = "AUX" + str((int(Elemento[(GuardarPosCar)+1]))+1)
                        BanderaDirecc = False

                ListaCuadru.append(El2)
                ListaCuadru.append(El3)
                ListaCuadru.append(El4)
                ListaCuadru.append(El1)
                self.Lista_Insertar_CUADRUPLOS.append(ListaCuadru)
            print("CUADRUPLOSSSS", self.Lista_Insertar_CUADRUPLOS)

        return self.Lista_Insertar_CUADRUPLOS

    def NumeroEntero(self,Var):
        try:
            int(Var)
            return True
        except ValueError:
            return False

    def NumeroFlotante(self,Var):
        try:
            float(Var)
            return True
        except ValueError:
            return False

    def Abrir_Interfaz(self, Lista_de_Variables, lista_operadores, Exprecion_por_partes):
        Interfaz_FaseD.__init__(self, Lista_de_Variables, lista_operadores, Exprecion_por_partes )


