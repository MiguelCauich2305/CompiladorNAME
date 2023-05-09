import tkinter as tk
from tkinter import ttk
from tkinter import *
import A_Identificador as I
from A_PatrónPAL_RES import Clase_PALABRAS_RESERVADAS as PR
from RecuperaTOKENS import RECUPERA as REC


class LEXICO:
    def __init__(self, CODIGO, consola, Pantalla):
        self.Pantalla= Pantalla
        self.Codigo= CODIGO
        self.Tokens = []
        self.TipoToken = []
        self.Tokens_FULL = []
        self.TipoToken_FULL = []
        self.TokenDeclaracion=[]
        self.TokenRef=[]
        self.SimbolosNoReconocidos = ["|", "º", "¿", "?", "_", "@", "!", "¡", "ç", "Ç", "]", "[", "ª", "<", ">", "´",
                                      "´", "¨", "%", "$", "(", ")", "·", "^", "&", "``", "`", "{", "}"]
        self.num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z"]
        self.abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
                    "t", "u", "v", "w", "x", "y", "z"]
        self.ListaPalabras=["ENT", "DEC", "CHAR", "STR", "SHOW", "FLAG", "VALUE", "ENTER", "GO", "GON"]

        #BANDERAS LOCAS para detectar PALRES Y Variables Igualadas
        self.Ban_Found_PALRES= False
        self.BAN_LINEA_SHOW_OPEN= False
        #self.Ban_Found_Variable_Igualada= False
        self.Identificador_Found_wo_equals=False #Identifica inicio de OPERACION ARITMETICA

        self.aux_PalRes =""

        self.Consola=consola #Pantalla en blanco grande
        self.CantidadLineas = 0
        self.Recorrer_Codigo_Carac()

    def Recorrer_Codigo_Carac(self):
        self.BanderaErrores = False
        self.CAD = ""
        keepends=True
        TOTAL_CARACTERES= len(self.Codigo)
        self.Codigo_SplitLines= self.Codigo.splitlines(keepends)
        print (self.Codigo_SplitLines)
        Contador_General = 0

        for numlinea in range(0, len(self.Codigo_SplitLines)): #Para cada line en el codigo...
           self.CantidadLineas =  self.CantidadLineas + 1

           self.Ban_Found_PALRES=False #para que si hay palabras reservadas en una linea
           #que no tienen identificador en seguida no busque en ñas demas
           #automaticamente es un error


           self.Current_Line= self.Codigo_SplitLines[numlinea] #Cadena con saltos y espacios incluidos
           print("     ANALIZANDO LINEA DE CODIGO:", self.CantidadLineas)
           print ("ULTIMA POS DE LA LINEA: ", len(self.Current_Line), self.Current_Line)

            #==========================================================================================
           #VERIFICA QUE HAYYA PUNTO Y COMA AL FINAL DE UNA SENTENCIA

           #_____________________________________________________
           Parte_linea_a_analizar=""
           Linea_que_tiene_algo_Para_analizar1=True
           self.Comentario=""
           Hay_comment=False
           for i in range (0, len(self.Current_Line)):           #Verifica si la linea esta VACÍA
               if self.Current_Line[i] != "\n" and self.Current_Line[i] != " ":
                   Linea_que_tiene_algo_Para_analizar1= Linea_que_tiene_algo_Para_analizar1

               if self.Current_Line[i] == "#": #si empieza con un comentario no se toma la linea completa
                   Linea_que_tiene_algo_Para_analizar1=False
                   Hay_comment= True

                   for a in range (i+1, len(self.Current_Line)):
                       if self.Current_Line[a] != "\n" and self.Current_Line[a] != "\t":
                           self.Comentario= self.Comentario+ self.Current_Line[a]
                           #print (self.Comentario)

           if Hay_comment==True:
               print ("Comentario: ", self.Comentario)

               self.Insertar_Información_TOKENS_SINTACTICO("#", "Comentario")
               self.Insertar_Información_TOKENS_SINTACTICO(self.Comentario, "Comentario")

            # #Hola comentario
           for i in range (0, len(self.Current_Line)):
              if self.Current_Line[i]== " " or self.Current_Line[i]=="#" or self.Current_Line[i] =="\n":
                   Linea_que_tiene_algo_Para_analizar1= False
              #else: #no es vacio, ni # ni salto.... entonces hay que analizarlo.
               #    Parte_linea_a_analizar = Parte_linea_a_analizar + self.Current_Line[i]
           # _____________________________________________________

           print ("bandera coment", Linea_que_tiene_algo_Para_analizar1)
           if Linea_que_tiene_algo_Para_analizar1==True:
               Punto_Coma=False
               c=len(self.Current_Line)-1
               while Punto_Coma ==False and c >=0:
                   if self.Current_Line[c] != "\n" and self.Current_Line[c] != " ":
                       if self.Current_Line[c] == ";":
                           Punto_Coma= True
                       else:
                           Punto_Coma= Punto_Coma
                   c=c-1

               if Punto_Coma ==False:
                   self.Consola.insert(tk.END,
                                       " ERROR : Terminación de línea:" + " Línea " + str(self.CantidadLineas))
                   self.BanderaErrores = True
#==========================================================================   PUNTO Y COMA   =====================

           self.C = 0 #recorre caracter por caracter.

           while self.C < len(self.Current_Line):

                    Caract= self.Current_Line[self.C]
                    #print("\n   EVALUANDO CARACTER: ",self.Codigo[Contador_General],Contador_General)
                    print("\n   EVALUANDO CARACTER: ",self.Current_Line[self.C])


                    if (Caract == "\n" or Caract == " " or Caract == "\t" or Caract== "") and len(self.CAD)!=0:
                        #si encuentro un espacio, o vacio tambien envio a verificar lo que esta detras siempre y cuando la cadena
                        #no este vacia
                        # si HAY un ESPACIO etc y self.CAD trae algo...
                        # puede ser PAL RES, IDENTI o NÚMERO
                        print("        Mando la cadena a verificar.")
                        self.Clasifica_CADENA_CONCATENADA()
                        self.CAD=""

                    # =====================PALABRA RESERVADA QUE NO TIENE NADA EN FRENTE======================================================
                    elif (Caract == "\n" or Caract == " " or Caract == "\t" or Caract == "")  and self.C==len(self.Current_Line)-2 and self.Ban_Found_PALRES==True:
                        self.Consola.insert(tk.END,
                                            " ERROR : PALABRA RESERVADAa :"+ str(self.aux_PalRes) +" Línea " + str(
                                                self.CantidadLineas))
                        self.BanderaErrores = True
                    #=======================================================================================================================

                    else:

                        BanOPERA = self.OPERADORES_SENCILLO(Caract) #Es operador?...
                        if BanOPERA == False: #si no es Operador....
                                BanCARACT = self.CARACTERES_SENCILLO(Caract) # Es caracter?....
                                if BanCARACT == False: #si no es caracter...
                                        BanSimNorec = self.Verifica_sies_SimboloNoReconocido(Caract)
                                        if BanSimNorec== False:
                                            #no fue simbolo, ni caracter, ni operador, entonces se concatena porque...
                                            #puede ser PAL RES, IDENTI o NUMERO
                                            if Caract != "\n" and Caract!= " " and Caract != "\t":
                                                self.CAD = self.CAD + str(Caract)
                                                print ("         Se concatenó: ", self.CAD)

                                        else: #si fue un Simbolo No reconocido...
                                            self.BanderaErrores=True
                                else:

                                    #========================================================================
                                    if Caract == "#": #si enocntramos un #.... ignoramos y sumamos a C
                                        self.C= len(self.Current_Line)

                                    #=========================================================================


                                    #checamos si PalRes esta abierta para mandar un error...........
                                    #if self.Ban_Found_PALRES == True:
                                     #   if self.BanderaErrores== False:
                                      #      self.Consola.insert(tk.END,
                                       #                         " ERROR : IDENTIFICADOR : Línea " + str(
                                        #                            self.CantidadLineas))
                                         #   self.BanderaErrores = True

                                    else:

                                        #si el caracter es CARACTER
                                        # puede ser PAL RES, IDENTI o NUMERO
                                        print("Se retorno BanCARACT=True")
                                        self.Clasifica_CADENA_CONCATENADA()
                                        Repetidos = self.Verifica_Token_Repetidos(Caract)
                                        if Repetidos == False:
                                            self.Insertar_Información_TOKENS_NUEVOS(Caract, "Caracter")
                                        self.Insertar_Información_TOKENS_SINTACTICO(Caract, "Caracter")


                        else: #si el Caracter fue un OPERADOR...
                              # puede ser PAL RES, IDENTI o NUMERO
                              if self.Ban_Found_PALRES == True:

                                  if self.BanderaErrores == False:
                                      self.Consola.insert(tk.END,
                                                          " ERROR : IDENTIFICADOR : Línea " + str(self.CantidadLineas))
                                      self.BanderaErrores = True

                              else:

                                  self.Clasifica_CADENA_CONCATENADA()
                                  Repetidos = self.Verifica_Token_Repetidos(Caract)
                                  if Repetidos == False:
                                      self.Insertar_Información_TOKENS_NUEVOS(Caract, "Operador")
                                  self.Insertar_Información_TOKENS_SINTACTICO(Caract, "Operador")

                                  if BanOPERA == True and Caract == "=" and self.Identificador_Found_wo_equals == True:
                                        # self.Ban_Found_Variable_Igualada=True
                                        self.Identificador_Found_wo_equals = False  # FOUND:  " IDENTI = "
                                        print("++++ Identificador CON igual. ")
                                        # Mandamos llamar a patron de operadores para ver si es correcta la operación
                                        self.PATRON_OPERACIONES_ARITMETICAS(self.Current_Line)

                                        #Aumantamos en el caracter para que no analice de nuevo
                                        self.C= len(self.Current_Line)


                    self.C = self.C + 1


        print ("\nTokens Obtenidos:")
        for i in range(len(self.Tokens)):
            print(self.Tokens[i], self.TipoToken[i])

        print ("TOKENS COMPLETOS")
        for i in range(len(self.Tokens_FULL)):
            print(self.Tokens_FULL[i], self.TipoToken_FULL[i])

        REC.Guardar_en_Arhivo(self,self.Tokens_FULL)
        self.TABLA()



    def Clasifica_CADENA_CONCATENADA(self): #Identifica si la self.CAD es Palabra, Identificador o Numero.

        if len(self.CAD)!=0:
            # SI ENCONTRO palres ENVIAMOS a IDENTI
            #======================================================================
            if self.Ban_Found_PALRES == True: #Bandera de palres ABIERTA...
                BanIdenti = I.IDENTIFICADOR_SENCILLO(self.CAD)
                if BanIdenti==True:
                    Repetidos = self.Verifica_Token_Repetidos(self.CAD)
                    if Repetidos == False:
                        self.Insertar_Información_TOKENS_NUEVOS(self.CAD, "Identificador")
                    self.Insertar_Información_TOKENS_SINTACTICO(self.CAD, "Identificador")

                    self.CAD="" #se encontro un IDENTI, limpiamos la variable

                else:
                    if self.BanderaErrores==False:
                        self.Consola.insert(tk.END," ERROR : IDENTIFICADORR : "+ self.CAD+ "Línea: "+ str(self.CantidadLineas))
                        self.BanderaErrores=True

                self.Ban_Found_PALRES= False #Ya no busco IDENTI para palabra reservada.
            #========================================================================

            else:#RECORRIDO DEL CODIGO DE MANERA NORMAL
                Flag_Palabra= PR.PAL_RESERVADAS(self, self.CAD) #1ro PALABRA RESERVADA
                if Flag_Palabra==False:
                        Flag_Identificador= I.IDENTIFICADOR_SENCILLO(self.CAD)#2do IDENTIFICADOR
                        if Flag_Identificador==False:
                                Flag_Numero= self.NUMEROS_SENCILLO(self.CAD) #3ro NÚMEROS
                                if Flag_Numero== False:
                                    # Si no hay ningun  numero en la cadena podemos mandar un
                                    #error de Identificador no valido...
                                                BANDERA = 0
                                                for i in range(0, len(self.CAD)):
                                                        Ban = I.Verifica_sies_numero(self.CAD[i])
                                                        if Ban == True:
                                                            BANDERA = 1
                                                if BANDERA == 0:
                                                    if self.BanderaErrores==False:
                                                        self.Consola.insert(tk.END, " ERROR : IDENTIFICADOR :"+ self.CAD+ " Línea: "  + str(
                                                                                self.CantidadLineas))
                                                        self.BanderaErrores=True
                                                else:
                                                    #si dentro de la cadena hay numeros, y no fue PalRes,
                                                    #tampoco fue identi, nu numero valido.
                                                    #mandamos error de numero por default.
                                                    self.Consola.insert(tk.END,
                                                                            " ERROR : NÚMERO :" + self.CAD + " Línea "+ str(
                                                                                self.CantidadLineas))
                                                    self.BanderaErrores=True


                                else: #Si si se encontro un numero...
                                    Repetidos = self.Verifica_Token_Repetidos(self.CAD)
                                    if Repetidos == False:
                                        self.Insertar_Información_TOKENS_NUEVOS(self.CAD, "Número")
                                    self.Insertar_Información_TOKENS_SINTACTICO(self.CAD, "Número")

                                    self.CAD = ""




                        else:#Se encontró identificador, se limpia self.CAD.

                            Repetidos = self.Verifica_Token_Repetidos(self.CAD)
                            if Repetidos == False:
                                self.Insertar_Información_TOKENS_NUEVOS(self.CAD, "Identificador")
                            self.Insertar_Información_TOKENS_SINTACTICO(self.CAD, "Identificador")

                            self.CAD = ""
                            self.Identificador_Found_wo_equals = True
                            print("    ++++ Se encontro un IDENTI sinn igual, ", self.Identificador_Found_wo_equals)


                else: #Se encontro palabra reservada, entonces se limpia la self.CAD
                    self.aux_PalRes= self.CAD
                    self.CAD = ""



#============================================================================================0======================

    def PATRON_OPERACIONES_ARITMETICAS(self, Current_Line):

        print("\n\n\n                ENTRAMOS A PATRON OPERACIONES", Current_Line, self.CantidadLineas)
        BANDERA_PATRON = True  # Por default esta aceptado el patron

        Codigo_concatenado = ""

        # CREACION DE LA CADENA QUE SE ANALIZARA SI CUMPLE CON EL PATRÓN DE OPERACIÓN O NO
        # ================================================================================
        # ciclo para concatenar a partir del igual en adelante
        for i in range(0, len(Current_Line)):
            if Current_Line[i] == "=":
                aux = i

        for a in range(aux + 1, len(Current_Line)):
                Codigo_concatenado = Codigo_concatenado + Current_Line[a]

        print("           Patrón Opera: Código a analizar: ", Codigo_concatenado)
        # =================================================================================

        self.Encontrando_Identi_o_Num= True
        self.Encontrando_Opera= False

        self.cad2 = ""
        C2= 0
        while C2  < len(Codigo_concatenado):
            Caract = Codigo_concatenado[C2]

            print("\n   EVALUANDO CARACTER2: ", Caract)

            if C2 == len(Codigo_concatenado)-1 and self.Encontrando_Identi_o_Num == True:
                self.Consola.insert(tk.END,
                                    " ERROR : OPERANDO  " + Caract + " : Línea " + str(
                                        (self.CantidadLineas)))
                self.BanderaErrores = True


            if (Caract == "\n" or Caract == " " or Caract == "\t" or Caract == "") and len(self.cad2) != 0:
                # si encuentro un espacio, o vacio tambien envio a verificar lo que esta detras siempre y cuando la cadena
                # no este vacia
                # si HAY un ESPACIO etc y self.self.cad2 trae algo...
                # puede ser PAL RES, IDENTI o NUMERO
                print("        Mando la cadena a verificar.")
                self.Clasifica_CADENA_CONCATENADA2()
                self.cad2 = ""

            else:

                BanOPERA = self.OPERADORES_SENCILLO(Caract)  # Es operador?...
                if BanOPERA == False:  # si no es Operador....
                    BanCARACT = self.CARACTERES_SENCILLO(Caract)  # Es caracter?....
                    if BanCARACT == False:  # si no es caracter...
                        BanSimNorec = self.Verifica_sies_SimboloNoReconocido(Caract)
                        if BanSimNorec == False:
                            # no fue simbolo, ni caracter, ni operador, entonces se concatena porque...
                            # puede ser PAL RES, IDENTI o NUMERO

                            if Caract != "\n" and Caract != " " and Caract != "\t":
                                self.cad2 = self.cad2 + str(Caract)
                                print("         Se concatenó: ", self.cad2)

                        else:  # si fue un Simbolo No reconocido...
                            self.BanderaErrores = True
                    else:

                        if Caract == "#":  # si enocntramos un #.... ignoramos y sumamos a C

                            C2 = len(Current_Line)

                        # si el caracter es CARACTER
                        # puede ser PAL RES, IDENTI o NUMERO
                        Repetidos = self.Verifica_Token_Repetidos(Caract)
                        if Repetidos == False:
                            self.Insertar_Información_TOKENS_NUEVOS(Caract, "Caracter")
                        self.Insertar_Información_TOKENS_SINTACTICO(Caract, "Caracter")


                        print ("ERROR DE OPERACION ARITMETICA")

                else:  # si el Caracter fue un OPERADOR...
                    # puede ser PAL RES, IDENTI o NUMERO

                        self.Clasifica_CADENA_CONCATENADA2()
                        Repetidos = self.Verifica_Token_Repetidos(Caract)
                        if Repetidos == False:
                            self.Insertar_Información_TOKENS_NUEVOS(Caract, "Operador")
                        self.Insertar_Información_TOKENS_SINTACTICO(Caract, "Operador")

                        print ("bandera del operador", self.Encontrando_Opera)

                        if self.Encontrando_Opera == False:
                            self.Consola.insert(tk.END,
                                                " ERROR : OPERADOR  " + Caract + " : Línea " + str(
                                                    (self.CantidadLineas)))
                            self.BanderaErrores = True


                        self.Encontrando_Identi_o_Num = True  # cambiamos lo que buscamos en seguida...
                        self.Encontrando_Opera = False

                        print("bandera del operador", self.Encontrando_Opera)

            C2=C2+1


    def Clasifica_CADENA_CONCATENADA2(self): #para el patron de operaciones aritmeticas
        print ("ENTRAMOS A Clasifica_CADENA_CONCATENADA2")

        if len(self.cad2)==0:
            pass
        else:
            if self.Encontrando_Identi_o_Num == True: #si estamos buscando numero o IDENTI
                #llamamos a verificar identi o numero
                Ban1_identi= I.IDENTIFICADOR_SENCILLO(self.cad2)
                Ban2_numero= self.NUMEROS_SENCILLO(self.cad2)

                if Ban1_identi == True or Ban2_numero==True: #si cumplió con alguna de estas dos...


                    #=============================================================================
                        #Para que meta los nuemros o identi VALIDOS A LA TABLA
                    if Ban1_identi== True:
                        Repetidos = self.Verifica_Token_Repetidos(self.cad2)
                        if Repetidos == False:
                            self.Insertar_Información_TOKENS_NUEVOS(self.cad2, "Identificador")
                        self.Insertar_Información_TOKENS_SINTACTICO(self.cad2, "Identificador")

                    elif Ban2_numero ==True:
                        Repetidos = self.Verifica_Token_Repetidos(self.cad2)
                        if Repetidos == False:
                            self.Insertar_Información_TOKENS_NUEVOS(self.cad2, "Numero")
                        self.Insertar_Información_TOKENS_SINTACTICO(self.cad2, "Numero")

                    #============================================================================
                    self.cad2=""
                else:
                    self.Consola.insert(tk.END,
                                        " ERROR : OPERANDO:  " + self.cad2 + " : Línea " + str(
                                            (self.CantidadLineas)))
                    self.BanderaErrores=True
                    self.cad2=""

                #No importa si no concordo con Identi o Numero, ahora buscamos Opera
                self.Encontrando_Identi_o_Num = False  # cambiamos lo que buscamos en seguida...
                self.Encontrando_Opera = True

            elif self.Encontrando_Opera== True:

                Ban3_Opera= self.OPERADORES_SENCILLO(self.cad2)
                if Ban3_Opera== True:
                    self.Encontrando_Identi_o_Num = True  # cambiamos lo que buscamos en seguida...
                    self.Encontrando_Opera = False
                else:
                    self.Consola.insert(tk.END,
                                        " ERROR : OPERANDO:  " + self.cad2 + " : Línea " + str(
                                            (self.CantidadLineas)))
                    self.BanderaErrores=True

#============================================================================================================================0



    def Verifica_sies_SimboloNoReconocido(self, Car):
        print ("      Entra a simbolos especiales")
        Ban = False

        for i in range (0, len(self.SimbolosNoReconocidos)):

            if Car== self.SimbolosNoReconocidos[i]:
                Ban=True
                aux=Car
        if Ban== True:
            self.Consola.insert(tk.END, " ERROR : SÍMBOLO NO RECONOCIDO : " + aux + " : Línea " + str(self.CantidadLineas))
            self.BanderaErrores=True
        return Ban

    def CARACTERES_SENCILLO(self, Tok):
        BAN = False
        print("      Entra a verificar Caracteres")
        ListaCaracteres = [";", ",", "'","#"]

        for i in range(len(ListaCaracteres)):
            if Tok == ListaCaracteres[i]:
                BAN = True
                print("    Se encontró el caracter: ", ListaCaracteres[i])
                break
        return BAN

    def OPERADORES_SENCILLO(self, Tok):
        BAN = False
        print("      Entra a verificar Operadores sencillo")
        ListaOperadores = ["+", "-", "/", "*", "=", ]
        for i in range(0, len(ListaOperadores)):
            if Tok == ListaOperadores[i]:
                BAN = True
                print("            Se encontró el Caracter: ", ListaOperadores[i])
                break

        return BAN

    def NUMEROS_SENCILLO(self, Tok):

        BanNONumero = False
        Ban = True
        print("        Entra a Verifica Numeros", Tok)
        NumeroslistaSTR = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

        for i in range(len(Tok)):
            BanNONumero = False

            for j in range(len(NumeroslistaSTR)):
                if Tok[i] == NumeroslistaSTR[j]:
                    BanNONumero = True
                    # print(BanNONumero)
            if BanNONumero == False:
                Ban = False


        if Ban== False:
            print ("             No es Numero ",Tok)
        else:
            print ("             Si es Numero", Tok)

        return Ban

    def Verifica_siHAY_numero(self, Tok):
        Ban7= False
        for i in range (0, len(Tok)):
            for a in range (0, len(self.num)):
                if Tok[i]== self.num[a]:
                    Ban7=True
        return Ban7

    def Verifica_sies_MAYUS(self, Car):
        Ban2= False
        for a in range(0, len(self.ABC)):
            if Car == self.abc[a]:
                Ban2= True
            else:
                Ban2=Ban2
        return Ban2

    def Verifica_Token_Repetidos(self, Tok):
        print ("Entra a verificar tokens repetidos")
        Ban3=False
        for i in range(0, len(self.Tokens)):
            if str(self.Tokens[i]) == str(Tok):

                if Tok== "GO":
                    self.BanderaErrores=True
                    self.Consola.insert(tk.END,
                                        " ERROR : PALABRA RESERVADA DE INICIO REPETIDA:  " + Tok + " : Línea " + str((self.CantidadLineas)))

                if Tok == "GON":
                    self.BanderaErrores=True
                    self.Consola.insert(tk.END,
                                        " ERROR : PALABRA RESERVADA DE FIN REPETIDA:  " + Tok + " : Línea " + str(
                                            (self.CantidadLineas)))

                Ban3=True
                print("Dentro de Verificar Tokens Rep: ", self.Tokens[i], Tok)

                Ban= self.Descartar_Linea_enReferencia(i, self.CantidadLineas)
                if Ban== False:

                        self.TokenRef[i].append(self.CantidadLineas)
        return Ban3

    def Descartar_Linea_enReferencia(self,Tok,  Linea ):

        Ban2= False  # #verifica que dentro de las referencias no se repitan
        Res=True

        for j in range(0, len(self.TokenRef[Tok])):
            if Linea == self.TokenRef[Tok][j]:
                Ban2 = True

        if  Ban2==False:
            Res= False


        return Res

    def Insertar_Información_TOKENS_NUEVOS(self, Tok, Tipo):

        print ("\nLista de Tokens: ")
        self.Tokens.append(Tok)  # Agrega el token NUEVO
        self.TipoToken.append(Tipo)  # Agrega el tipo de token
        self.TokenRef.append([self.CantidadLineas])  # Agrega su lista de Referencias NUEVA
        self.TokenDeclaracion.append(self.CantidadLineas)  # Agrega su primera declaracion en codigo

        print("    ", self.Tokens, self.TipoToken, self.TokenDeclaracion,self.TokenRef)

    def Insertar_Información_TOKENS_SINTACTICO(self, Tok, Tipo):

        print ("\nLista de Tokens: ")
        self.Tokens_FULL.append(Tok)  # Agrega el token NUEVO
        self.TipoToken_FULL.append(Tipo)  # Agrega el tipo de token

        print("    ", self.Tokens_FULL, self.TipoToken_FULL)



    def Insertar_Tokens(self):
        if len(self.Tokens) != 0:
            for i in range(0,len(self.Tokens)):
                self.tabla.insert('','end', values=[self.Tokens[i], self.TipoToken[i],
                                                    self.TokenDeclaracion[i], self.TokenRef[i]])

    def TABLA(self):


        if self.BanderaErrores == False:
            self.root2 = Tk()
            self.root2.geometry('730'
                               'x500')
            self.root2.title("COMPILADOR ")
            self.root2.configure(bg="olive drab1")

            self.LEN = tk.Label(self.root2, text="ANÁLISIS LÉXICO", width=52, borderwidth=3,
                                font=("Helvatica", 17, "bold"), fg="white",
                                bg="dark green", anchor="c")
            self.LEN.place(x=0, y=0)

            self.labelframe2 = tk.LabelFrame(self.root2, font=("Arial", 18), bg="cornflower blue")
            self.labelframe2.place(x=10, y=50)

            self.tabla = ttk.Treeview(self.labelframe2, columns=("0", "1", "2", "3"), height="20")
            self.tabla.column("#0", width=0, )
            self.tabla.column("1", width=140, )
            self.tabla.column("2", width=145, )
            self.tabla.column("3", width=145, )
            self.tabla.heading("0", text="TOKEN", anchor='center')
            self.tabla.heading("1", text="TIPO", anchor='center')
            self.tabla.heading("2", text="DECLARACIÓN", anchor='center')
            self.tabla.heading("3", text="REFERENCIA", anchor='center')


            self.tabla.grid(column=0, row=0)
            self.Insertar_Tokens()
            self.root2.mainloop()
        else:
            pass