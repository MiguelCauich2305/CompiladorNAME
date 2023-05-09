from RecuperaOPERACIONES import OPERACIONES_REC as REC2
from E_Opti_RecuperaVARIABLES import RECUPERA as REC3

class DameOperaciones():
    def Funcion_Separa_Parentesis(self):
        self.LISTA_GENERAL=[]
        self.Operaciones = (REC2.Obtener_Operaciones_de_Archivo(self))
        print(self.Operaciones)
        for x in range(len(self.Operaciones)):
            self.Operadores = ["+", "-", "/", "*",]
            #self.x = ["Suma1","=","1","+","3","-","Var1","/","8","*","16","-","90","/","Var2"]

            self.x = (self.Operaciones[x]).split(",")
            ############################################ quitamos el \n ############################################
            UltElement = ""
            PosUltElement = (len(self.x))-1
            #print(PosUltElement)
            #print(self.x[PosUltElement])
            #print(len(self.x[PosUltElement]))
            TamUltimoElem = (len(self.x[PosUltElement]))
            for salto in range(TamUltimoElem-1):
                    UltElement =UltElement + self.x[PosUltElement][salto]
                    print(UltElement, "Correccion")
            self.x[PosUltElement] = UltElement
            self.Operaciones[x] = self.x
            ########################################################################################################
        print("self.Operaciones PARAMETRO de OPTIMIZACION ", self.Operaciones)
        DameOperaciones.Precalcular_Expresiones_Constantes(self,self.Operaciones)

        #self.Propagacion_De_Copias(self.Operaciones)

    def Precalcular_Expresiones_Constantes(self,Operaciones):
        print("Iniciamos con precalcular expresiones constantes")
        for i in range(len(Operaciones)):
            BanIgual = False
            BanVariable = False
            OperacionActual = Operaciones[i]
            SumaGeneral = 0
            GuardarPosicionIgual = 0
            OperadorActual = ""
            print ("Esta es la operacion actual", OperacionActual)
            for j in range(len(OperacionActual)):
                BanOperador = False

                if OperacionActual[j] == "=":
                    BanIgual = True
                    GuardarPosicionIgual = j
                    print ("======================= ENCONTRAMOS UN IGUAL =======================")
                else:
                    if BanIgual == True:
                        ElementoActual = OperacionActual[j]
                        for k in range(len(self.Operadores)):
                            if ElementoActual == self.Operadores[k]:
                                BanOperador = True
                                OperadorActual = ElementoActual
                                print("Operador Guardado")

                        if BanOperador == True:
                            print("encontramos un operador, lo omitimos y contunuamos")
                            print("Operador Actual: ", OperadorActual)

                        else:
                            BanNumero = False
                            TypeNumero = ""
                            print("No es un operador, buscaremos que sea un numero")
                            BanEntero = DameOperaciones.NumeroEntero(self,ElementoActual)
                            if BanEntero == False:
                                print("No es un Entero, Buscaremos flotante")
                                BanFloat = DameOperaciones.NumeroFlotante(self,ElementoActual)
                                if BanFloat == False:
                                    print("No es Flotante, es variable, SALIMOS DEL CICLO")
                                    BanVariable = True
                                    break
                                else:
                                    print("Si es flotante, ES NUMERO")
                                    BanNumero = True
                                    TypeNumero = "Float"
                                    #SumaGeneral = SumaGeneral + float(ElementoActual)
                            else:
                                print("Si es entero, ES NUMERO")
                                BanNumero = True
                                TypeNumero = "Int"
                                #SumaGeneral = SumaGeneral + float(ElementoActual)
                            if (BanNumero == True) and(BanVariable == False):
                                if (OperadorActual == "") or (OperadorActual == " "):
                                    if (TypeNumero == "Int"):
                                        SumaGeneral = int(ElementoActual)
                                    elif(TypeNumero == "Float"):
                                        SumaGeneral = float(ElementoActual)
                                    print("Operacion hasta el momento", SumaGeneral)

                                else:
                                    if (OperadorActual == "*"):
                                        if (TypeNumero == "Int"):
                                            SumaGeneral = SumaGeneral * int(ElementoActual)
                                        elif (TypeNumero == "Float"):
                                            SumaGeneral = SumaGeneral * float(ElementoActual)
                                        print("Operacion hasta el momento (Multi)", SumaGeneral)

                                    elif (OperadorActual == "+"):
                                        if (TypeNumero == "Int"):
                                            SumaGeneral = SumaGeneral + int(ElementoActual)
                                        elif (TypeNumero == "Float"):
                                            SumaGeneral = SumaGeneral + float(ElementoActual)
                                        print("Operacion hasta el momento (Suma)", SumaGeneral)

                                    elif (OperadorActual == "-"):
                                        if (TypeNumero == "Int"):
                                            SumaGeneral = SumaGeneral - int(ElementoActual)
                                        elif (TypeNumero == "Float"):
                                            SumaGeneral = SumaGeneral - float(ElementoActual)
                                        print("Operacion hasta el momento (Resta)", SumaGeneral)

                                    elif (OperadorActual == "/"):
                                        if (TypeNumero == "Int"):
                                            SumaGeneral = SumaGeneral / int(ElementoActual)
                                        elif (TypeNumero == "Float"):
                                            SumaGeneral = SumaGeneral / float(ElementoActual)
                                        print("Operacion hasta el momento (Divi)", SumaGeneral)
                    else:
                        print("Aun no encontramos un igual")


            if BanVariable == True:
                print("Encontramos una variable, contiunuamos con la siguiente operacion")

            elif BanVariable == False:
                print("Si es una operacion de puras constantes")
                print("Esta es la Operacion original", OperacionActual)
                for operacion in range(GuardarPosicionIgual+1, len(OperacionActual)):
                    OperacionActual.pop()
                OperacionActual.append(SumaGeneral)
                print("Esta es la Operacion Optimizada",OperacionActual)
                Operaciones[i] = OperacionActual
                print("AL FINAL DE PRECALCULAR EXPRESIONES CONSTANTES....", Operaciones)

            print("\n")


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

    def Propagacion_De_Copias(self,Operaciones):
        print("Iniciamos con propagacion de Copias")
        for i in range(len(Operaciones)):
            BanIgual = False
            BanVariable = False
            OperacionActual = Operaciones[i]
            GuardarPosicionIgual = 0
            print("Esta es la operacion actual", OperacionActual)
            for j in range(len(OperacionActual)):

                if OperacionActual[j] == "=":
                    BanIgual = True
                    GuardarPosicionIgual = j
                    print("======================= ENCONTRAMOS UN IGUAL =======================")

                else:
                    if BanIgual == True:
                        SiguienteElemento = ((len(OperacionActual))- 1)
                        if (GuardarPosicionIgual + 1) == (SiguienteElemento):
                            print("======================== ES UNA IGUALACION =========================")
                            print("Intentaremos convertir el siguiente elemento despues del igual a numero")

                            ElementoSiguiente = OperacionActual[(GuardarPosicionIgual + 1)]
                            BanEntero = DameOperaciones.NumeroEntero(self,ElementoSiguiente)
                            if BanEntero == False:
                                print("No es un Entero, Buscaremos flotante")
                                BanFloat = DameOperaciones.NumeroFlotante(self, ElementoSiguiente)
                                if BanFloat == False:
                                    print("No es Flotante, es variable, SI APLICA!!!")
                                    BanVariable = True
                                else:
                                    print("Si es flotante, ES NUMERO")
                                    print("Salimos, no aplica")
                                    break
                            else:
                                print("Si es entero, ES NUMERO")
                                print("Salimos, no aplica")
                                break

                            if BanVariable == True:
                                print("AQUI EMPEZA EL ANALISIS DE LAS VARIABLES")
                                VARIABLES = (REC3.Obtener_Token_de_Archivo(self)).split("\n")
                                print("Variable Validas por analizar")
                                print(VARIABLES)
                                for k in range(len(VARIABLES)):
                                    print("Varible: ",k,VARIABLES[k])
                            else:
                                print("Salimos, no aplica")
                                break
                        else:
                            print("***************** No es una igualacion, es operacion! *****************")
                            break
                    else:
                        print("***************** Aun no encontramos un igual *****************")
                print("\n")

