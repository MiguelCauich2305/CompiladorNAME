from RecuperaTOKENS import RECUPERA as REC
from RecuperaOPERACIONES import OPERACIONES_REC as REC2
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import  filedialog
from C_Semantico_Interfaz import Semantico as SEMTAB
from Arbol import Arbol1


class Semantico():
    def __init__(self,consola):
        self.Consola = consola
        self.OperacionGuardar = []
        self.OperacionGuardarTipo = []
        self.ListaParaComparar = ["",""]
        #Lista de las variables declaradas
        self.VariablesDeclaradas = []
        #Lista con el tipo de dato que corresponde a cada variable
        self.VariablesDeclaradasTipo = []
        #Tipos de variables usadas para declarar
        self.TipoDatoDeclara = ["ENT", "DEC", "CHAR", "STR", "FLAG"]
        self.TipoDatoPide = ["VALUE", "ENTER"]
        #Operadores
        self.Operador = ["+", "-", "/", "*", "="]

        #letras
        self.LMinus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r",
                       "s",
                       "t", "u", "v", "w", "x", "y", "z"]
        self.LMayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R",
                       "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.Logico()

    def Logico(self):
        REC2.Limpiar_archivo(self)
        # Obtenemos todos los tokens para analizarlos
        obtenertokens = (REC.Obtener_Token_de_Archivo(self))
        self.Tokens = obtenertokens.split("\n")

        self.ProcesoAsignarVariables = False
        self.ProcesoOperaciones = False
        self.BanderaEncontramosTipoDato = False
        self.BanderaVariableYaDeclarada = False
        self.BanderaDeError = False
        self.BanderaDeErrorGeneral = True
        self.VariableAlInicioEncontrada=False
        self.TipoDeDatoEncontrado = ""
        self.EncontrarVariable = False
        self.PosicionActual = 0
        self.ContadorDeVariables = 0
        self.BanderaComentario = False
        self.BanderaShow = False
        self.ContadordeComillas = 0
        self.BanderaNumero = False
        self.TipoDatoVariableInicial = ""
        self.TipoDeError = ""
        self.ContadorDeLineas = 1
        self.BanderaPideDato = False

        print("Empezamos")
        for i in range(len(self.Tokens)):
            print("\n")
            TokenActual = self.Tokens[i]
            self.PosicionActual = i
            print("Token Actual: ",TokenActual)

            if (TokenActual == ";"):
                self.ContadorDeLineas = self.ContadorDeLineas + 1
                if (self.ProcesoOperaciones == True):
                    print("antes de eliminar esta es la operacion final: ")
                    print (self.OperacionGuardar)
                    print("y sus tipos de datos: ")
                    print (self.OperacionGuardarTipo)
                    OperacionConComas = ""
                    OperacionTipoConComas = ""
                    for acomoda in range(len(self.OperacionGuardar)):
                        if acomoda == ((len(self.OperacionGuardar))- 1):
                            OperacionConComas = OperacionConComas + (str(self.OperacionGuardar[acomoda]) + "\n")
                            OperacionTipoConComas = OperacionTipoConComas + (str(self.OperacionGuardarTipo[acomoda])+ "\n")
                        else:
                            OperacionConComas = OperacionConComas +(str(self.OperacionGuardar[acomoda]) + ",")
                            OperacionTipoConComas = OperacionTipoConComas + (str(self.OperacionGuardarTipo[acomoda]) + ",")
                    REC2.Guardar_en_Arhivo(self,OperacionConComas,OperacionTipoConComas)
                    self.OperacionGuardar = []
                    self.OperacionGuardarTipo = []

                print("Salto de Linea, Reiniciando Variables")
                self.ProcesoAsignarVariables = False
                self.ProcesoOperaciones = False
                self.BanderaEncontramosTipoDato = False
                self.BanderaVariableYaDeclarada = False
                self.TipoDeDatoEncontrado = ""
                self.VariableAlInicioEncontrada = False
                self.IntentarEncontrarVariable = False
                self.ContadorDeVariables = 0
                self.BanderaComentario = False
                self.BanderaShow = False
                self.ContadordeComillas = 0
                self.BanderaNumero = False
                self.TipoDatoVariableInicial = ""
                self.BanderaPideDato = False

            elif (TokenActual == "#"):
                self.BanderaComentario = True

            elif (self.BanderaComentario == True):
                print("Los comentarios estan activos hasta nuevo aviso xd")
                print("Token Actual: ", TokenActual)
                print("lo ignoramos")
                self.BanderaComentario = False

            elif (TokenActual == "SHOW"):
                print("Encontramos un show")
                self.BanderaShow = True
                print("Vamos a Analizar hasta salto de Linea")

            elif ((TokenActual == self.TipoDatoPide[0]) or (TokenActual == self.TipoDatoPide[1])):
                if (TokenActual == self.TipoDatoPide[0]):
                    print("Encontramos una pedida de datos")
                    self.BanderaPideDato = True
                    print ("Vamos a buscar variables")
                    self.TipoDeDatoEncontrado = "VALUE"

                elif (TokenActual == self.TipoDatoPide[1]):
                    print("Encontramos una pedida de datos")
                    self.BanderaPideDato = True
                    print("Vamos a buscar variables")
                    self.TipoDeDatoEncontrado = "ENTER"

            elif (self.BanderaShow == True):
                print("Empezaremos el analisis del SHOW")
                if (TokenActual == ("'")):
                    self.ContadordeComillas = self.ContadordeComillas + 1
                    print("Contador actual: ", self.ContadordeComillas)
                    if self.ContadordeComillas == 2:
                        print("pasamos el mensaje")
                        self.ContadordeComillas = 0

                elif (TokenActual == (",")):
                    print("Encontramos una coma, continuaremos buscando variables o mensajes")

                elif (((TokenActual != (",")) and (TokenActual != ("'"))) and (self.ContadordeComillas > 0)):
                    print("Este es el mensaje, lo saltamos")

                else:
                    print("Bien ya no es mensaje, apostrofe o coma, puede ser una variable o un numero")
                    print("Vamos a analizar")
                    for k in range(len(self.VariablesDeclaradas)):
                        if TokenActual == self.VariablesDeclaradas[k]:
                            self.BanderaVariableYaDeclarada = True
                    if self.BanderaVariableYaDeclarada == True:
                        print("Todo bien por aqui, la variable si existe")
                    else:
                        print("La Variable que se quiere imprimir no exite, Toca analizar Numeros")
                        print("Tal vez es un numero, intentaremos convertirlo")
                        try:
                            if ((int(TokenActual)) and (self.BanderaNumero == False) ):
                                print("Es un numero, linea 127")
                                NumeroEncontrado = int(TokenActual)
                                print(NumeroEncontrado)
                                self.BanderaNumero = True
                                print("Antes de entrar a la funcion")
                                BanTipoDato = self.AnalizaTipoDatoNumeros("ENT")
                                if BanTipoDato == True:
                                    print("Encontramos un numero")
                                    print("Lo Guardamos")
                                    self.OperacionGuardar.append(NumeroEncontrado)

                                    if self.ContadorDeVariables == 0:
                                        self.ListaParaComparar[0] = "ENT"
                                        self.ContadorDeVariables = self.ContadorDeVariables + 1

                                    elif self.ContadorDeVariables > 0:
                                        self.ListaParaComparar[1] = "ENT"
                                        print("Tipos de Datos a comparar:")
                                        print(self.ListaParaComparar[0], self.ListaParaComparar[1])

                                        if self.ListaParaComparar[0] == self.ListaParaComparar[1]:
                                            print("Los tipos de datos son iguales")
                                            self.ListaParaComparar[0] = self.ListaParaComparar[1]
                                            self.ListaParaComparar[1] = ""
                                            self.ContadorDeVariables = self.ContadorDeVariables + 1
                        except:
                            try:
                                if ((float(TokenActual)) and (self.BanderaNumero == False)):
                                    print("Es un numero decimal")
                                    NumeroEncontrado = float(TokenActual)
                                    self.BanderaNumero = True
                                    BanTipoDato = self.AnalizaTipoDatoNumeros("DEC")
                                    if BanTipoDato == True:
                                        print("Encontramos un numero con decimal")
                                        print("Lo Guardamos")
                                        self.OperacionGuardar.append(NumeroEncontrado)

                                        if self.ContadorDeVariables == 0:
                                            self.ListaParaComparar[0] = "DEC"
                                            self.ContadorDeVariables = self.ContadorDeVariables + 1

                                        elif self.ContadorDeVariables > 0:
                                            self.ListaParaComparar[1] = "DEC"
                                            print("Tipos de Datos a comparar:")
                                            print(self.ListaParaComparar[0], self.ListaParaComparar[1])

                                            if self.ListaParaComparar[0] == self.ListaParaComparar[1]:
                                                print("Los tipos de datos son iguales")
                                                self.ListaParaComparar[0] = self.ListaParaComparar[1]
                                                self.ListaParaComparar[1] = ""
                                                self.ContadorDeVariables = self.ContadorDeVariables + 1
                            except:
                                if (self.BanderaNumero == False):
                                    print("No es Un elemento Imprimible, ERROR")
                                    self.TipoDeError = (TokenActual + " ,ERROR")
                                    self.BanderaDeError = True
                                else:
                                    print("Encontramos numero, continua")

            elif(self.BanderaPideDato == True):
                if(self.TipoDeDatoEncontrado == "VALUE"):
                    for Variable in range(len(self.VariablesDeclaradas)):
                        if (self.VariablesDeclaradas[Variable]) == TokenActual:
                            print("Si la encontramos")
                            GuardarPosicion = Variable
                            self.BanderaVariableYaDeclarada = True

                    if self.BanderaVariableYaDeclarada == False:
                            self.BanderaDeError = True
                            print("No la encontramos")
                            self.TipoDeError = "No la encontramos"

                    elif self.BanderaVariableYaDeclarada == True:
                        TipodeDatoVar = self.VariablesDeclaradasTipo[GuardarPosicion]
                        if (TipodeDatoVar == "ENT" or TipodeDatoVar == "DEC"):
                            print("Si se puede asignar el valor a esta variable")
                        else:
                            print("NO se puede asignar el valor a la variable")
                            self.BanderaDeError = True
                            self.TipoDeError = "NO se puede asignar el valor a la variable"

                elif(self.TipoDeDatoEncontrado == "ENTER"):
                    for Variable in range(len(self.VariablesDeclaradas)):
                        if (self.VariablesDeclaradas[Variable]) == TokenActual:
                            print("Si la encontramos")
                            GuardarPosicion = Variable
                            self.BanderaVariableYaDeclarada = True

                    if self.BanderaVariableYaDeclarada == False:
                        self.BanderaDeError = True
                        print("No la encontramos")
                        self.TipoDeError = "No la encontramos"

                    elif self.BanderaVariableYaDeclarada == True:
                        TipodeDatoVar = self.VariablesDeclaradasTipo[GuardarPosicion]
                        if (TipodeDatoVar == "STR" or TipodeDatoVar == "CHAR"):
                            print("Si se puede asignar el valor a esta variable")
                        else:
                            print("NO se puede asignar el valor a la variable")
                            self.BanderaDeError = True
                            self.TipoDeError = "NO se puede asignar el valor a la variable"

            elif(self.BanderaEncontramosTipoDato == False) and ((TokenActual ==  "GO") or TokenActual ==  "GON"):
                print("Simplemente continua xd")
                if (TokenActual == "GON"):
                    self.BanderaDeErrorGeneral = False

            elif (self.ProcesoAsignarVariables == False) and (self.ProcesoOperaciones == False) and (self.BanderaEncontramosTipoDato == False):
                print("Buscaremos los tipos de datos")
                self.EncontrarTipoDato(TokenActual)
                if self.IntentarEncontrarVariable == True:
                    self.BuscarVariable(TokenActual)

            elif (self.ProcesoAsignarVariables == True) and (self.ProcesoOperaciones == False) and (self.BanderaEncontramosTipoDato == True):
                print("Encontramos un tipo de dato")
                print("Toca buscar una variable enseguida")
                self.AsignarVariables(TokenActual)

            elif(self.ProcesoAsignarVariables == False) and (self.ProcesoOperaciones == True) and (self.BanderaEncontramosTipoDato == False):
                print("Esta operacion va hasta el momento")
                print(self.OperacionGuardar)
                print("Continuamos con la Operacion:")
                self.VerificarOperaciones(TokenActual)
                print("salimos de Verificar Operaciones")

            if self.BanderaDeError == True:
                print("Entramos a un error, se va el tren araña xd")
                self.TipoDeError = (TokenActual + " ,ERROR Semantico")
                self.BanderaDeErrorGeneral = True
                self.Consola.insert(tk.END, str(self.TipoDeError) + ", Línea: " + str(self.ContadorDeLineas))
                break
            print(self.VariablesDeclaradas)
            print(self.VariablesDeclaradasTipo)

        if(self.BanderaDeErrorGeneral == False):
            Arbol1()
            SEMTAB.Tabla_de_Gramatica(self)


    def EncontrarTipoDato(self,TokenActual):
        for j in range(len(self.TipoDatoDeclara)):
            if TokenActual == self.TipoDatoDeclara[j]:
                print("Encontramos un Tipo de Dato")
                self.BanderaEncontramosTipoDato = True

        if self.BanderaEncontramosTipoDato == True:
            self.ProcesoAsignarVariables = True
            self.VariablesDeclaradasTipo.append(TokenActual)
            self.TipoDeDatoEncontrado = TokenActual
        else:
            print("No encontramos un tipo de Dato, intentaremos buscar ahora en variables")
            self.IntentarEncontrarVariable = True

    def AsignarVariables(self,TokenActual):
        TamVariablesAsignadas = len(self.VariablesDeclaradas)
        TamTiposDeVariables = len(self.VariablesDeclaradasTipo)

        if TamVariablesAsignadas == 0:
            print("Aun no hay variables asignadas, veremos si puede ser una variable nueva")
            if (TamTiposDeVariables - TamVariablesAsignadas) == 1 and ((TokenActual != "," ) or (TokenActual != ";")):
                print("Tenemos mas tipos de datos que variables")
                print("es una variable nueva")
                self.VariablesDeclaradas.append(TokenActual)

        else:
            print("ya existen Variables asignadas")
            for j in range(len(self.VariablesDeclaradas)):
                if TokenActual == self.VariablesDeclaradas[j]:
                    self.BanderaVariableYaDeclarada = True
            if self.BanderaVariableYaDeclarada == False:
                print("La variable no estaba repetida, veremos si puede ser nueva")
                if (TamTiposDeVariables - TamVariablesAsignadas) == 1 and ((TokenActual != "," ) or (TokenActual != ";")):
                    print("Tenemos mas tipos de datos que variables")
                    print("es una variable nueva")
                    self.VariablesDeclaradas.append(TokenActual)

                elif((TokenActual == "," ) and self.BanderaEncontramosTipoDato == True):
                    print(" se estan declarando aun mas variables")
                    self.VariablesDeclaradasTipo.append(self.TipoDeDatoEncontrado)

            else:
                print("Variable ya declarada, ERROR")
                self.TipoDeError = (TokenActual + " ,ERROR")
                self.BanderaDeError = True

    def BuscarVariable(self,TokenActual):
        for j in range(len(self.VariablesDeclaradas)):
            if TokenActual == self.VariablesDeclaradas[j]:
                self.VariableAlInicioEncontrada = True

        if self.VariableAlInicioEncontrada == True:
            print("Es una variable al Inicio, puede ser una operacion")
            SiguientePosicion = (self.PosicionActual + 1)
            if self.Tokens[SiguientePosicion] == ("="):
                print("encontramos un igual, es una operacion")
                self.ProcesoOperaciones = True
                #####
                self.ProcesoAsignarVariables = False
                self.BanderaEncontramosTipoDato = False
                self.BanderaVariableYaDeclarada = False
                self.TipoDeDatoEncontrado = ""
                self.VariableAlInicioEncontrada = False
                self.IntentarEncontrarVariable = False
                #####
                self.OperacionGuardar.append(TokenActual)
                print("Buscaremos su tipo de dato")
                GuardarPosi = 0
                for k in range(len(self.VariablesDeclaradas)):
                    if TokenActual == self.VariablesDeclaradas[k]:
                        print("la encontramos")
                        GuardarPosi = k
                print()
                self.OperacionGuardarTipo.append(self.VariablesDeclaradasTipo[GuardarPosi])
                self.ListaParaComparar[0]=(self.VariablesDeclaradasTipo[GuardarPosi])
                self.TipoDatoVariableInicial = (self.VariablesDeclaradasTipo[GuardarPosi])

            else:
                print("no es una operacion valida, ERROR")
                self.TipoDeError = (TokenActual + " ,ERROR")
                self.BanderaDeError = True

        else:
            print("No es ni un Tipo de Dato ni una variable antes Declarada, ERROR")
            self.TipoDeError = (TokenActual + " ,ERROR")
            self.BanderaDeError = True

    def VerificarOperaciones(self,TokenActual):
        print("Entramos a verificar Operaciones")
        SiOperador = False
        for j in range(len(self.Operador)):
            print("Operador actual: ", self.Operador[j])
            if ((TokenActual == (self.Operador[j]) and TokenActual == ("="))):
                print("Es un igual, Guardemoslo")
                self.OperacionGuardar.append(TokenActual)
                print("Guardamos su tipo de dato")
                self.OperacionGuardarTipo.append("Operador")
                SiOperador = True

            elif ((TokenActual == (self.Operador[j]) and TokenActual != ("="))):
                print("Tenemos un operador: ")
                print("Token Actual: ", TokenActual)
                if ((self.ListaParaComparar[0] != "ENT") and (self.ListaParaComparar[0] != "DEC")and (self.ListaParaComparar[0] != "FLAG")) and TokenActual != "+":
                    print(self.ListaParaComparar[0], "Tipo de Dato")
                    print("No es Un elemento operable, ERROR")
                    self.TipoDeError = (TokenActual + " ,ERROR")
                    self.BanderaDeError = True
                else:
                    self.OperacionGuardar.append(TokenActual)
                    print("Guardamos su tipo de dato")
                    self.OperacionGuardarTipo.append("Operador")
                    SiOperador = True

        if SiOperador == False:
                SiVariable = False
                print("No es un Operador, Buscaremos en variables")
                for k in range(len(self.VariablesDeclaradas)):
                    if TokenActual == self.VariablesDeclaradas[k]:
                        SiVariable = True
                        GuardarPosiciondeVariable = k
                if SiVariable == True:
                    print("Si es una variable")
                    print("Analizaremos su  tipo de dato:")
                    self.AnalizaTipoDato(GuardarPosiciondeVariable,TokenActual)
                    print("Lo Guardamos")
                    self.OperacionGuardar.append(TokenActual)
                    print("Guardamos su tipo de dato")
                    self.OperacionGuardarTipo.append(self.VariablesDeclaradasTipo[GuardarPosiciondeVariable])
                else:
                    print("No es una Variable, ni un operador")
                    print("Tal vez es un numero, intentaremos convertirlo")
                    Ban = self.NumeroEntero(TokenActual)

                    if Ban == False:
                        Ban2 = self.NumeroFlotante(TokenActual)
                        if Ban2 == True:
                            BanTipoDato = self.AnalizaTipoDatoNumeros("DEC")
                            if BanTipoDato == True:
                                print("Encontramos un numero  con decimal")
                                print("Lo Guardamos")
                                self.OperacionGuardar.append(TokenActual)
                                self.OperacionGuardarTipo.append("DEC")

                                if self.ContadorDeVariables == 0:
                                    self.ListaParaComparar[0] = "DEC"
                                    self.ContadorDeVariables = self.ContadorDeVariables + 1

                                elif self.ContadorDeVariables > 0:
                                    self.ListaParaComparar[1] = "DEC"
                                    print("Tipos de Datos a comparar:")
                                    print(self.ListaParaComparar[0], self.ListaParaComparar[1])

                                    if self.ListaParaComparar[0] == self.ListaParaComparar[1]:
                                        print("Los tipos de datos son iguales")
                                        self.ListaParaComparar[0] = self.ListaParaComparar[1]
                                        self.ListaParaComparar[1] = ""
                                        self.ContadorDeVariables = self.ContadorDeVariables + 1
                        else:
                            print("No es un entero ni un flotante, ERROR")
                            self.TipoDeError = (TokenActual + " ,ERROR")
                            self.BanderaDeError = True

                    elif Ban == True:
                        print("Antes de entrar a la funcion")
                        BanTipoDato = self.AnalizaTipoDatoNumeros("ENT")
                        print("Sabe salimos de la funcion")
                        print(BanTipoDato)
                        if BanTipoDato == True:
                            print("Encontramos un numero")
                            print("Lo Guardamos")
                            self.OperacionGuardar.append(TokenActual)
                            self.OperacionGuardarTipo.append("ENT")

                            if self.ContadorDeVariables == 0:
                                self.ListaParaComparar[0] = "ENT"
                                self.ContadorDeVariables = self.ContadorDeVariables + 1

                            elif self.ContadorDeVariables > 0:
                                self.ListaParaComparar[1] = "ENT"
                                print("Tipos de Datos a comparar:")
                                print(self.ListaParaComparar[0], self.ListaParaComparar[1])

                                if self.ListaParaComparar[0] == self.ListaParaComparar[1]:
                                    print("Los tipos de datos son iguales")
                                    self.ListaParaComparar[0] = self.ListaParaComparar[1]
                                    self.ListaParaComparar[1] = ""
                                    self.ContadorDeVariables = self.ContadorDeVariables + 1

    def AnalizaTipoDato(self,Pos,TokenActual):
        print("Posicion de la variable: ", Pos)
        print ("Posicion en Lista Variables:", self.VariablesDeclaradas[Pos])
        print("Tipo de Dato de esa Variable: ",self.VariablesDeclaradasTipo[Pos])

        if self.ContadorDeVariables == 0:
            print("el contador es cero")
            if self.VariablesDeclaradas[Pos] == TokenActual:
                self.ListaParaComparar[0] = self.VariablesDeclaradasTipo[Pos]
                if self.ListaParaComparar[0] == self.OperacionGuardarTipo[0]:
                    print("Los tipos de datos de la variable asignacion y la a asignar son iguales")
                    print("Podemos contunuar")
                    self.ListaParaComparar[0] = self.VariablesDeclaradasTipo[Pos]
                    self.ContadorDeVariables = self.ContadorDeVariables + 1

                elif (self.ListaParaComparar[0] != self.OperacionGuardarTipo[0]):
                    print("Los tipos de datos no son iguales y No son ENT")
                    print("Revisaremos Compatibilidad")
                    TipoValor1 = self.OperacionGuardarTipo[0]
                    TipoValor2 =  self.ListaParaComparar[0]

                    if (TipoValor1 == ("DEC")) and ((TipoValor2 == ("ENT")) or (TipoValor2 == ("FLAG"))):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.VariablesDeclaradasTipo[Pos]
                        self.ContadorDeVariables = self.ContadorDeVariables + 1

                    elif ((TipoValor1 == ("ENT")) and (TipoValor2 == ("DEC"))) :
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

                    elif (TipoValor1 == ("STR")) and (TipoValor2 == ("CHAR")):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.VariablesDeclaradasTipo[Pos]
                        self.ContadorDeVariables = self.ContadorDeVariables + 1

                    elif (TipoValor1 == ("CHAR")) and (TipoValor2 != ("CHAR")):
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

                    elif (TipoValor1 == ("ENT")) and (TipoValor2 == ("FLAG")):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.VariablesDeclaradasTipo[Pos]
                        self.ContadorDeVariables = self.ContadorDeVariables + 1

                    elif (TipoValor1 == ("FLAG")) and (TipoValor2 == ("ENT")):
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

                    else:
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

        elif self.ContadorDeVariables > 0:
            print("el contador es mayor a cero")
            if self.VariablesDeclaradas[Pos] == TokenActual:
                self.ListaParaComparar[1] = self.VariablesDeclaradasTipo[Pos]
                print("Tipos de Datos a comparar:")
                print(self.ListaParaComparar[0],self.ListaParaComparar[1])
                print(self.TipoDatoVariableInicial)
                if (self.ListaParaComparar[0] == self.ListaParaComparar[1] ):
                    print("Los tipos de datos son iguales")
                    print("Podemos contunuar")
                    self.ListaParaComparar[0] = self.ListaParaComparar[1]
                    self.ListaParaComparar[1] = ""
                    self.ContadorDeVariables = self.ContadorDeVariables + 1

                elif (self.ListaParaComparar[0] == self.ListaParaComparar[1] ) == "ENT":
                    print("Los tipos de datos son iguales y es ENT")
                    print("Podemos contunuar")
                    self.ListaParaComparar[0] = self.ListaParaComparar[1]
                    self.ListaParaComparar[1] = ""
                    self.ContadorDeVariables = self.ContadorDeVariables + 1

                elif (self.ListaParaComparar[0] != self.ListaParaComparar[1] ) != "ENT":
                    print("Los tipos de datos no son iguales y No son ENT")
                    print("Revisaremos Compatibilidad")
                    TipoValor1 = self.ListaParaComparar[0]
                    TipoValor2 = self.ListaParaComparar[1]

                    if (TipoValor1 == ("DEC")) and ((TipoValor2 == ("ENT")) or (TipoValor2 == ("FLAG"))):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1",TipoValor1, "Tipo 2",TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.ListaParaComparar[1]
                        self.ListaParaComparar[1] = ""
                        self.ContadorDeVariables = self.ContadorDeVariables + 1

                    elif TipoValor1 == ("ENT") and TipoValor2 == ("DEC"):
                        if ((TipoValor2) != self.TipoDatoVariableInicial):
                            print("Los Tipos de Datos no son Iguales, ERROR")
                            self.TipoDeError = (TokenActual + " ,ERROR")
                            print("Entre condicional 1 no Numeros")
                            print("Tipo 1", TipoValor2, "Tipo 2", self.TipoDatoVariableInicial)
                            self.BanderaDeError = True
                        else:
                            print("Los Tipos de Datos si son compatibles")
                            print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                            print("el tipo de dato base: ", self.TipoDatoVariableInicial)
                            print("Podemos contunuar")
                            self.ListaParaComparar[0] = self.ListaParaComparar[1]
                            self.ListaParaComparar[1] = ""
                            self.ContadorDeVariables = self.ContadorDeVariables + 1
                            banderaderegreso = True

                    elif (((TipoValor1 == ("ENT")) and (TipoValor2 == ("DEC"))) or ((TipoValor2) == self.TipoDatoVariableInicial)):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("el tipo de dato base: ", self.TipoDatoVariableInicial)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.ListaParaComparar[1]
                        self.ListaParaComparar[1] = ""
                        self.ContadorDeVariables = self.ContadorDeVariables + 1
                        banderaderegreso = True


                    elif (TipoValor1 == ("STR")) and (TipoValor2 == ("CHAR")):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.ListaParaComparar[1]
                        self.ListaParaComparar[1] = ""
                        self.ContadorDeVariables = self.ContadorDeVariables + 1

                    elif (TipoValor1 == ("CHAR")) and (TipoValor2 != ("CHAR")):
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

                    elif (TipoValor1 == ("ENT")) and (TipoValor2 == ("FLAG")):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.ListaParaComparar[1]
                        self.ListaParaComparar[1] = ""
                        self.ContadorDeVariables = self.ContadorDeVariables + 1

                    elif (TipoValor1 == ("FLAG")) and (TipoValor2 == ("ENT")):
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True
                    else:
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

    def AnalizaTipoDatoNumeros(self,TipoDato):
        banderaderegreso = False
        print("Analiza Tipo Dato Numeros")
        print("Tipo de Dato de esa Variable: ",TipoDato)
        print("Tipo de Dato de la Variable anterior:", self.ListaParaComparar[0])

        if self.ContadorDeVariables == 0:
                print("el contador es cero")
                if self.ListaParaComparar[0] == TipoDato:
                    print("Los tipos de datos de la variable asignacion y la a asignar son iguales")
                    print("Podemos contunuar")
                    self.ListaParaComparar[0] = TipoDato
                    self.ContadorDeVariables = self.ContadorDeVariables + 1
                    banderaderegreso = True

                elif (self.ListaParaComparar[0] != TipoDato):
                    print("Los tipos de datos no son iguales y No son ENT")
                    print("Revisaremos Compatibilidad")
                    TipoValor1 = self.ListaParaComparar[0]
                    TipoValor2 = TipoDato


                    if (TipoValor1 == ("DEC")) and ((TipoValor2 == ("ENT")) or (TipoValor2 == ("FLAG"))):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = TipoValor1
                        self.ContadorDeVariables = self.ContadorDeVariables + 1
                        banderaderegreso = True


                    elif ((TipoValor1 == ("ENT")) and (TipoValor2 == ("DEC"))):
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

                    elif (TipoValor1 == ("STR")) and (TipoValor2 == ("CHAR")):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = TipoValor1
                        self.ContadorDeVariables = self.ContadorDeVariables + 1
                        banderaderegreso = True

                    elif (TipoValor1 == ("CHAR")) and (TipoValor2 != ("CHAR")):
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

                    elif (TipoValor1 == ("ENT")) and (TipoValor2 == ("FLAG")):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = TipoValor1
                        self.ContadorDeVariables = self.ContadorDeVariables + 1
                        banderaderegreso = True

                    elif (TipoValor1 == ("FLAG")) and (TipoValor2 == ("ENT")):
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

                    else:
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

        elif self.ContadorDeVariables > 0:
                print("el contador es mayor a cero")
                self.ListaParaComparar[1] = TipoDato
                print("Tipos de Datos a comparar:")
                print(self.ListaParaComparar[0],self.ListaParaComparar[1])
                print (self.TipoDatoVariableInicial)
                if (self.ListaParaComparar[0] == self.ListaParaComparar[1] ):
                    print("Los tipos de datos son iguales")
                    print("Podemos contunuar")
                    self.ListaParaComparar[0] = self.ListaParaComparar[1]
                    self.ListaParaComparar[1] = ""
                    self.ContadorDeVariables = self.ContadorDeVariables + 1
                    banderaderegreso = True

                elif (self.ListaParaComparar[0] == self.ListaParaComparar[1] ) == "ENT":
                    print("Los tipos de datos son iguales y es ENT")
                    print("Podemos contunuar")
                    self.ListaParaComparar[0] = self.ListaParaComparar[1]
                    self.ListaParaComparar[1] = ""
                    self.ContadorDeVariables = self.ContadorDeVariables + 1
                    banderaderegreso = True

                elif (self.ListaParaComparar[0] != self.ListaParaComparar[1] ) != "ENT":
                    print("Los tipos de datos no son iguales y No son ENT")
                    print("Revisaremos Compatibilidad")
                    TipoValor1 = self.ListaParaComparar[0]
                    TipoValor2 = self.ListaParaComparar[1]

                    if (TipoValor1 == ("DEC")) and ((TipoValor2 == ("ENT")) or (TipoValor2 == ("FLAG"))):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1",TipoValor1, "Tipo 2",TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.ListaParaComparar[1]
                        self.ListaParaComparar[1] = ""
                        self.ContadorDeVariables = self.ContadorDeVariables + 1
                        banderaderegreso = True

                    elif TipoValor1 == ("ENT") and TipoValor2 == ("DEC"):
                        if ((TipoValor2) != self.TipoDatoVariableInicial):
                            print("Los Tipos de Datos no son Iguales, ERROR")
                            self.TipoDeError = (TokenActual + " ,ERROR")
                            print("Entre condicional 1 Numeros")
                            print("Tipo 1", TipoValor2, "Tipo 2", self.TipoDatoVariableInicial)
                            self.BanderaDeError = True
                        else:
                            print("Los Tipos de Datos si son compatibles")
                            print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                            print("el tipo de dato base: ", self.TipoDatoVariableInicial)
                            print("Podemos contunuar")
                            self.ListaParaComparar[0] = self.ListaParaComparar[1]
                            self.ListaParaComparar[1] = ""
                            self.ContadorDeVariables = self.ContadorDeVariables + 1
                            banderaderegreso = True


                    elif (((TipoValor1 == ("ENT")) and (TipoValor2 == ("DEC"))) or ((TipoValor2) == self.TipoDatoVariableInicial)):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("el tipo de dato base: ", self.TipoDatoVariableInicial)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.ListaParaComparar[1]
                        self.ListaParaComparar[1] = ""
                        self.ContadorDeVariables = self.ContadorDeVariables + 1
                        banderaderegreso = True

                    elif (TipoValor1 == ("STR")) and (TipoValor2 == ("CHAR")):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.ListaParaComparar[1]
                        self.ListaParaComparar[1] = ""
                        self.ContadorDeVariables = self.ContadorDeVariables + 1
                        banderaderegreso = True

                    elif (TipoValor1 == ("CHAR")) and (TipoValor2 != ("CHAR")):
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True

                    elif (TipoValor1 == ("ENT")) and (TipoValor2 == ("FLAG")):
                        print("Los Tipos de Datos si son compatibles")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        print("Podemos contunuar")
                        self.ListaParaComparar[0] = self.ListaParaComparar[1]
                        self.ListaParaComparar[1] = ""
                        self.ContadorDeVariables = self.ContadorDeVariables + 1
                        banderaderegreso = True

                    elif (TipoValor1 == ("FLAG")) and (TipoValor2 == ("ENT")):
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True
                    else:
                        print("Los Tipos de Datos no son Iguales, ERROR")
                        self.TipoDeError = (TokenActual + " ,ERROR")
                        print("Entre condicional Final")
                        print("Tipo 1", TipoValor1, "Tipo 2", TipoValor2)
                        self.BanderaDeError = True
        return banderaderegreso
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

#S = Semantico()
#S.Logico()