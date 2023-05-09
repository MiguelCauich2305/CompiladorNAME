import A_Compilador_Lexico
import tkinter as tk
from tkinter import ttk
from tkinter import *
from A_PatronSHOW import ClasePalabraReservadaSHOW as CPR

class Clase_PALABRAS_RESERVADAS():

    def PAL_RESERVADAS(self,Tok):
        print("        Entra a Palabras reservadas", Tok)

        #Ciclo para encontrar una palabra reservada====================TAL CUAL SIN ERRORES
        BAN= False
        for i in range (len(self.ListaPalabras)):
            if Tok ==  self.ListaPalabras[i]:
                BAN = True
                print ("        Se encontró la palabra reservada: ", self.ListaPalabras[i])
                break
        #==================================================================================

        if BAN == True: #Si se encontro una PALRES...

            Repetidos = self.Verifica_Token_Repetidos(Tok)
            if Repetidos == False:
                self.Insertar_Información_TOKENS_NUEVOS(Tok, "Palabra Reservada")
            self.Insertar_Información_TOKENS_SINTACTICO(Tok, "Palabra Reservada")

            if Tok != "GO" and Tok != "END": #estas palabras no llevan nada en frente no IDENTI
                if Tok != "SHOW" :  #No es Show, GO o END.
                    self.Ban_Found_PALRES= True #se encontro entonvces lo que siguie se envia a Identi
                    print ("        ***Necesito tener un Identi despues.", self.CAD)

                else: #es un S H O W
                    #Palabra reservada SHOW, tiene que llevar comillas en frente de a fuerzas
                    print ("CURRENT LINE", self.Current_Line)

                    BanPatronShow= CPR.PAL_RES_SHOW (self, self.Current_Line, self.C)


        #1er error. Por si hay Palabras Reservadas en MINUSCULAS
        elif BAN== False: #se verifica si hay PALRES pero en minusculas para mandar error

            Ban5= self.Verifica_siHAY_numero(Tok)
            if Ban5 == False:

                Cad_en_Mayusculas= Tok.upper()

                Flag1_palres_MINUS= False
                #Checamos si convirtiendo a mayus es igual, si si sera un error de minuscula
                for i in range(0, len(self.ListaPalabras)):
                    if Cad_en_Mayusculas == self.ListaPalabras[i]:
                        Flag1_palres_MINUS = True
                        print ("YA SE CAMBIO SI HAY EN MAYUS")
                        break
                #print ("Flag", Flag1)
                if Flag1_palres_MINUS== True : #se encontro que la pal reservada estaba escrita con MINUS
                    self.BanderaErrores= True #bandera para que no se muestre la tabla
                    self.Consola.insert(tk.END,
                                        " ERROR : PALABRA RESERVADA : " + Tok + " : Línea " + str(
                                            self.CantidadLineas))

                else:
                    for i in range (0, len(self.ListaPalabras)):

                        if Cad_en_Mayusculas.find(self.ListaPalabras[i]) != -1:
                            if self.BanderaErrores==False:
                                self.Consola.insert(tk.END,
                                                    " ERROR : PALABRA RESERVADA : " + Tok + " : Línea " + str(
                                                        self.CantidadLineas))
                                self.BanderaErrores = True


        return BAN


