from E_Opti_ARCHIVOS import OPTI_archivos
from RecuperaOPERACIONES import OPERACIONES_REC as REC2
from RecuperaVARIABLES import RECUPERA as REC3
from E_OptimizacionInterfaz import Optimizacion
from E_Opti_ARCHIVOS import OPTI_archivos

class Logica_OPTI:

    def __init__(self):
        print("\n \n \n \n")
        print("================== OPTIMIZACION ==================")
        self.Calculo=[]
        self.Copias=[]

        self.Nulos=[]
        self.Potencias=[]

        self.Operaciones123 = self.Funcion_Separa_Parentesis()

        #1 CALCULAR EXPRESIONES CONSTANTES ==================================================
        CONSTANTES = Logica_OPTI.Precalcular_Expresiones_Constantes(self,self.Operaciones123)
        #2 ELIMINACION DE EXP NULAS =========================================================
        NULOSS= Logica_OPTI.EliminacionNulos(self,CONSTANTES)
        #3 REDUCCION DE POTENCIAS ===========================================================
        POTENCIAS= Logica_OPTI.Reduccion_Potencias(self, NULOSS)
        #4 PROPAGACION DE COPIAS ============================================================
        COPIAS = Logica_OPTI.Propagacion_De_Copias(self,POTENCIAS)
        Optimizacion()

    def Funcion_Separa_Parentesis(self):
        self.LISTA_GENERAL = []
        self.Operaciones = (REC2.Obtener_Operaciones_de_Archivo(self))
        print(self.Operaciones)
        for x in range(len(self.Operaciones)):
            self.Operadores = ["+", "-", "/", "*", ]
            # self.x = ["Suma1","=","1","+","3","-","Var1","/","8","*","16","-","90","/","Var2"]

            self.x = (self.Operaciones[x]).split(",")
            ############################################ quitamos el \n ############################################
            UltElement = ""
            PosUltElement = (len(self.x)) - 1
            # print(PosUltElement)
            # print(self.x[PosUltElement])
            # print(len(self.x[PosUltElement]))
            TamUltimoElem = (len(self.x[PosUltElement]))
            for salto in range(TamUltimoElem - 1):
                UltElement = UltElement + self.x[PosUltElement][salto]
                print(UltElement, "Correccion")
            self.x[PosUltElement] = UltElement
            self.Operaciones[x] = self.x
            ########################################################################################################
        print("self.Operaciones PARAMETRO de OPTIMIZACION ", self.Operaciones)
        return self.Operaciones

    def Precalcular_Expresiones_Constantes(self,Operaciones):
        print("Iniciamos con precalcular expresiones constantes")
        for i in range(len(Operaciones)):
            BanIgual = False
            BanVariable = False
            OperacionActual = Operaciones[i]
            SumaGeneral = 0
            GuardarPosicionIgual = 0
            OperadorActual = ""
            OperacionActualizada = []
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
                            BanEntero = self.NumeroEntero(ElementoActual)
                            if BanEntero == False:
                                print("No es un Entero, Buscaremos flotante")
                                BanFloat = self.NumeroFlotante(ElementoActual)
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
                                        OperacionActualizada.append(int(ElementoActual))
                                    elif(TypeNumero == "Float"):
                                        SumaGeneral = float(ElementoActual)
                                        OperacionActualizada.append(float(ElementoActual))
                                    print("Operacion hasta el momento", SumaGeneral)

                                else:
                                    if (OperadorActual == "*"):
                                        OperacionActualizada.append("*")
                                        if (TypeNumero == "Int"):
                                            SumaGeneral = SumaGeneral * int(ElementoActual)
                                            OperacionActualizada.append(int(ElementoActual))
                                        elif (TypeNumero == "Float"):
                                            SumaGeneral = SumaGeneral * float(ElementoActual)
                                            OperacionActualizada.append(float(ElementoActual))
                                        print("Operacion hasta el momento (Multi)", SumaGeneral)

                                    elif (OperadorActual == "+"):
                                        OperacionActualizada.append("+")
                                        if (TypeNumero == "Int"):
                                            SumaGeneral = SumaGeneral + int(ElementoActual)
                                            OperacionActualizada.append(int(ElementoActual))
                                        elif (TypeNumero == "Float"):
                                            SumaGeneral = SumaGeneral + float(ElementoActual)
                                            OperacionActualizada.append(float(ElementoActual))
                                        print("Operacion hasta el momento (Suma)", SumaGeneral)

                                    elif (OperadorActual == "-"):
                                        OperacionActualizada.append("-")
                                        if (TypeNumero == "Int"):
                                            SumaGeneral = SumaGeneral - int(ElementoActual)
                                            OperacionActualizada.append(int(ElementoActual))
                                        elif (TypeNumero == "Float"):
                                            SumaGeneral = SumaGeneral - float(ElementoActual)
                                            OperacionActualizada.append(float(ElementoActual))
                                        print("Operacion hasta el momento (Resta)", SumaGeneral)

                                    elif (OperadorActual == "/"):
                                        OperacionActualizada.append("/")
                                        if (TypeNumero == "Int"):
                                            SumaGeneral = SumaGeneral / int(ElementoActual)
                                            OperacionActualizada.append(int(ElementoActual))
                                        elif (TypeNumero == "Float"):
                                            SumaGeneral = SumaGeneral / float(ElementoActual)
                                            OperacionActualizada.append(float(ElementoActual))
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
                OperaResultante = self.CalcularPorPrioridad(OperacionActualizada)
                OperacionActual.append(OperaResultante)
                print("Esta es la Operacion Optimizada",OperacionActual)
                Operaciones[i] = OperacionActual
                print("Todas las operaciones",(Operaciones))
            print("\n")
        print("===============================================")
        print("Se ha acabado el proceso")
        print("===============================================")
        OPTI_archivos.Archivos_PrecalcularExpresiones(self, Operaciones)
        return Operaciones


    def EliminacionNulos(self, Lista_Operaciones):
        for default in (Lista_Operaciones):
            if len(default) > 3:  # no analiza las igualciones x=3
                # default= ["x", "=", "7", "*", "1", "-", "0"]
                a = len(default)
                i = 0
                while i < a:
                    print(i)
                    if default[i] == "/" or default[i] == "*" or default[i] == "+" or default[i] == "-":

                        if (default[i] == "/" or default[i] == "*") and default[i + 1] == "1":
                            default.pop(i)
                            print(default)
                            default.pop(i)
                            print(default)
                            i = i - 1
                        if (default[i] == "+" or default[i] == "-") and default[i + 1] == "0":
                            default.pop(i)
                            default.pop(i)
                            i = i - 1
                        else:
                            i = i + 1
                    else:
                        i = i + 1
                    a = len(default)

        OPTI_archivos.Archivos_EliminacionNulos(self, Lista_Operaciones)
        return Lista_Operaciones

    def Reduccion_Potencias(self, Lista_Operaciones):
        for default in (Lista_Operaciones):
            if len(default) > 3:
                if default[3] == "*":

                    derecha = default[4]
                    izqu = default[2]
                    # banderas para saber si son decimales, enteros o variables.
                    IZ_Ent, IZ_Dec = self.NumeroEntero(izqu), self.NumeroFlotante(izqu)
                    DER_Ent, DER_Dec = self.NumeroEntero(derecha), self.NumeroFlotante(derecha)

                    # si a la izquierda hay una variable y a la derecha hay un entero======================
                    if (IZ_Ent == False and IZ_Dec == False) and DER_Ent == True:
                        default.pop(2)
                        default.pop(2)
                        default.pop(2)

                        print("Sin a*3", default)
                        for a in range(0, int(derecha)):  # a * 3
                            default.insert(2, izqu)  # insertar el numero
                            if a != int(derecha) - 1:
                                default.insert(2, "+")

                    # Si a la izquierda hay un numero y a la derecha hay una variable======================
                    elif (IZ_Ent == True) and (DER_Ent == False and DER_Dec == False):
                        default.pop(2)
                        default.pop(2)
                        default.pop(2)

                        print("Sin 3*a", default)
                        for a in range(0, int(izqu)):  # a * 3
                            default.insert(2, derecha)  # insertar el numero
                            if a != int(izqu) - 1:
                                default.insert(2, "+")

                    # Si hay numeros enteros a los dos lados
                    elif (IZ_Ent == True) and DER_Ent == True:
                        default.pop(2)
                        default.pop(2)
                        default.pop(2)

                        print("Sin 3*3", default)
                        for a in range(0, int(izqu)):  # a * 3
                            default.insert(2, derecha)  # insertar el numero
                            if a != int(izqu) - 1:
                                default.insert(2, "+")


                    elif IZ_Ent == True and DER_Dec == True:
                        default.pop(2)
                        default.pop(2)
                        default.pop(2)

                        print("Sin 3 * 3.5 ", default)
                        for a in range(0, int(izqu)):  # a * 3
                            default.insert(2, derecha)  # insertar el numero
                            if a != int(izqu) - 1:
                                default.insert(2, "+")


                    elif IZ_Dec == True and DER_Ent == True:
                        default.pop(2)
                        default.pop(2)
                        default.pop(2)

                        print("Sin 3 * 3.5 ", default)
                        for a in range(0, int(derecha)):  # a * 3
                            default.insert(2, izqu)  # insertar el numero
                            if a != int(derecha) - 1:
                                default.insert(2, "+")

        OPTI_archivos.Archivos_ReduccionPotencias(self, Lista_Operaciones)
        return Lista_Operaciones

    def Propagacion_De_Copias(self,Operaciones):
        print("Iniciamos con propagacion de Copias")
        EspaciosEliminar = []
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
                            BanEntero = self.NumeroEntero(ElementoSiguiente)
                            if BanEntero == False:
                                print("No es un Entero, Buscaremos flotante")
                                BanFloat = self.NumeroFlotante(ElementoSiguiente)
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
                                BanElimine = False
                                print("AQUI EMPEZA EL ANALISIS DE LAS VARIABLES")
                                ElementDespuesIgual = OperacionActual[GuardarPosicionIgual + 1]
                                ElementAntesIgual = OperacionActual[GuardarPosicionIgual - 1]

                                print("Elemento antes igual: ", ElementAntesIgual)
                                print("Elemento Despues Igual: ", ElementDespuesIgual)

                                for k in range(i+1, len(Operaciones)):
                                    SigOp = Operaciones[k]
                                    print("Operacion a evaluar:")
                                    print(SigOp)
                                    for l in range(len(SigOp)):
                                        print("elemento: ", SigOp[l])
                                        if (SigOp[l] == ElementAntesIgual) and (SigOp[l+1] != "="):
                                            BanElimine = True
                                            print("Encontramos una repeticion", SigOp[l], i)
                                            SigOp[l] = ElementDespuesIgual
                                    Operaciones[k] = SigOp
                                    print("\n")
                                if BanElimine == True:
                                    EspaciosEliminar.append(i)
                                print("Operacion actualActual",i,"Eliminiare: ",EspaciosEliminar)
                                #Operaciones.pop(i)
                                break

                            else:
                                print("Salimos, no aplica")
                                break
                        else:
                            print("***************** No es una igualacion, es operacion! *****************")
                            break
                    else:
                        print("***************** Aun no encontramos un igual *****************")
                print("\n")
        print("Antes de Eliminar: ", Operaciones)
        m = (len(EspaciosEliminar))-1
        while m >= 0:
        #for m in range(len(EspaciosEliminar)):
            print("Estoy eliminando: ", Operaciones[EspaciosEliminar[m]])
            Operaciones.pop(int(EspaciosEliminar[m]))
            m = m - 1
        print("===============================================")
        print("Se ha acabado el proceso")
        print("===============================================")
        print("Operaciones Finales Propagacion: ", Operaciones)
        OPTI_archivos.Archivos_PropagacionCopias(self, Operaciones)
        return Operaciones

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

    def CalcularPorPrioridad(self, OperaPara):
        BanderaIgual = False
        self.Operadores = ["+", "-", "/", "*", "="]
        while BanderaIgual == False:
            self.Provicional = []
            self.Conca = ""
            self.ConcaCompleto = ""
            self.y = []
            self.prioridadGeneral = 0
            self.prioridadActual = 0
            self.posicionDePrioridadGeneral = 0
            self.posicionDePrioridadActual = 0
            if (len(OperaPara) > 1):
                for i in range(len(OperaPara)):

                    self.ElementoActual = OperaPara[i]
                    print("self.ElementoActual: ",self.ElementoActual)

                    for j in range(len(self.Operadores)):
                        self.OperadorActual = self.Operadores[j]

                        if self.ElementoActual == self.OperadorActual:
                            if ((self.OperadorActual == "-") or (self.OperadorActual == "+")):

                                self.prioridadActual = 2
                                self.posicionDePrioridadActual = i

                            elif ((self.OperadorActual == "/") or (self.OperadorActual == "*")):

                                self.prioridadActual = 3
                                self.posicionDePrioridadActual = i

                            elif ((self.OperadorActual == "=")):
                                self.prioridadActual = 1
                                self.posicionDePrioridadActual = i

                    if self.prioridadActual > self.prioridadGeneral:
                        # print("Encontramos una prioridad mayor, guardamos la posicion y prioridad")
                        self.prioridadGeneral = self.prioridadActual
                        self.posicionDePrioridadGeneral = self.posicionDePrioridadActual
                        # print (self.prioridadGeneral, self.posicionDePrioridadGeneral)

                    elif self.prioridadActual == self.prioridadGeneral:
                        pass
                        # print("Encontramos una prioridad Igual, continuamos con el primero")

                    print("\n")
            else:
                self.prioridadActual = 1

            Operacion = 0
            if (OperaPara[(self.posicionDePrioridadGeneral)] == "="):
                self.prioridadActual = 1

            elif (OperaPara[(self.posicionDePrioridadGeneral)] == "*"):
                Operacion = (OperaPara[(self.posicionDePrioridadGeneral) - 1]) * (OperaPara[(self.posicionDePrioridadGeneral) + 1])
                print("Operacion hasta el momento (Multi)", Operacion)

            elif (OperaPara[(self.posicionDePrioridadGeneral)] == "+"):
                Operacion = (OperaPara[(self.posicionDePrioridadGeneral) - 1]) + (OperaPara[(self.posicionDePrioridadGeneral) + 1])
                print("Operacion hasta el momento (Suma)", Operacion)

            elif (OperaPara[(self.posicionDePrioridadGeneral)] == "-"):
                Operacion = OperaPara[(self.posicionDePrioridadGeneral) - 1] - (OperaPara[(self.posicionDePrioridadGeneral) + 1])
                print("Operacion hasta el momento (Resta)", Operacion)

            elif (OperaPara[(self.posicionDePrioridadGeneral)] == "/"):
                Operacion = (OperaPara[(self.posicionDePrioridadGeneral) - 1]) / (OperaPara[(self.posicionDePrioridadGeneral) + 1])
                print("Operacion hasta el momento (Divi)", Operacion)

            C = 0
            while C < ((len(OperaPara))):
                print(C)
                if C == ((self.posicionDePrioridadGeneral) - 1):
                    self.Provicional.append(Operacion)
                    C = (self.posicionDePrioridadGeneral) + 2
                else:
                    self.Provicional.append(OperaPara[C])
                    C = C + 1
            OperaPara = self.Provicional
            print(OperaPara)

            if self.prioridadActual == 1:
                self.pre = OperaPara[0]
                print("\n")
                print("Final: ", self.pre)
                # self.LISTA_GENERAL.append(self.ConcaCompleto)
                #LOL.Guardar_en_Arhivo(self, pre + "\n")
                BanderaIgual = True
        return self.pre


