import A_Compilador_Lexico
import tkinter as tk
from tkinter import ttk
from tkinter import *

class ClasePalabraReservadaSHOW():


    # el patron de la palres SHOW será más grande después
    def PAL_RES_SHOW(self, LineaCompleta_show, C):
        print("             Analizamos show: ", )
        contador =0
        Texto_mostrar =""
        Texto_general="" #el texto que no esta dentro de comillas, osea puede ser de variables
        Ban_Concatenando_texto_mostrar = False

        # comenzamos a analizar desde una posicion más de la ultima letra W de SHOW
        for i in range (C +1, len (LineaCompleta_show)):

                car= LineaCompleta_show[i]
                print(car,"caracter de analisis", LineaCompleta_show)



                if car == "'" and Ban_Concatenando_texto_mostrar==False:



                    print ("encontre la primer comilla, y lameto")
                    Ban_Concatenando_texto_mostrar = True  # A partir de aqui concatenamos
                    # ya que enocntramos la primera comilla abierta

                    Repetidos = self.Verifica_Token_Repetidos(car)
                    if Repetidos == False:
                        self.Insertar_Información_TOKENS_NUEVOS(car, "Caracter")
                    self.Insertar_Información_TOKENS_SINTACTICO(car, "Caracter")


                #concatenando lo que este dentro de la comilla...
                elif Ban_Concatenando_texto_mostrar==True:
                    print ("concatenando alv")

                    if car == "'":
                        print ("ENTRE A BANDERA TRUE EN COMILLA")
                        Ban_Concatenando_texto_mostrar = False  # DEJAMOS DE CONCATENAR
                        # ya que enocntramos la SEGUNDA COMILLA QUE CIERRA EL MENSAJE

                        Repetidos = self.Verifica_Token_Repetidos(car)
                        if Repetidos == False:
                            self.Insertar_Información_TOKENS_NUEVOS(car, "Caracter")

                        self.Insertar_Información_TOKENS_SINTACTICO(Texto_mostrar, "TextoMostrar")

                        #limpiamos variable de texto
                        Texto_mostrar=""

                        # EN LA LINEA ANTERIOR METO EL TEXTO AL BLOQ O ARCHIVO DE TOKENS
                        self.Insertar_Información_TOKENS_SINTACTICO(car, "Caracter")
                    else:
                        print ("no es comillaaaaa", Texto_mostrar)
                        Texto_mostrar = Texto_mostrar + car
# ________________________________________________________________________________________-
                elif Ban_Concatenando_texto_mostrar==False and car!=" " and car!="," and car!=";" and car !="'":
                    Texto_general=Texto_general+car
                    print ("TEXTOOOOO GENERAKK", Texto_general)

                elif car == ",":
                    if len(Texto_general)!=0:
                        self.Insertar_Información_TOKENS_SINTACTICO(Texto_general, "Identificador")
                        Texto_general=""


                    Repetidos = self.Verifica_Token_Repetidos(car)
                    if Repetidos == False:
                        self.Insertar_Información_TOKENS_NUEVOS(car, "Caracter")
                    self.Insertar_Información_TOKENS_SINTACTICO(car, "Caracter")


                elif car == ";":
                    if len(Texto_general)!=0:
                        self.Insertar_Información_TOKENS_SINTACTICO(Texto_general, "Identificador")
                        Texto_general=""

                    Repetidos = self.Verifica_Token_Repetidos(car)
                    if Repetidos == False:
                        self.Insertar_Información_TOKENS_NUEVOS(car, "Caracter")
                    self.Insertar_Información_TOKENS_SINTACTICO(car, "Caracter")

                #if car != "'" :
                 #   Texto_mostrar=Texto_mostrar+car
                  #  Ban=True


            # Aumantamos en el caracter para que no analice de nuevo
                self.C = i+1


        #debo de tener a fuerzas dos apostrofes enfrente de SHOW ''
        #Despues debo de tener (  ,  ) para poder tener más apostrofes
