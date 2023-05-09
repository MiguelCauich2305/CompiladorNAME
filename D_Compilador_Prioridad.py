from RecuperaTOKENS import RECUPERA as REC
from RecuperaOPERACIONES import OPERACIONES_REC as REC2
from RecuperaOPERACIONES_DIVI import OPERACIONES_DIV as LOL

class DividePrioridades():
    def Funcion_Separa_Parentesis(self):
        self.LISTA_GENERAL=[]
        self.Operaciones = (REC2.Obtener_Operaciones_de_Archivo(self))
        print(self.Operaciones)

        for x in range(len(self.Operaciones)):
            self.Operadores = ["+", "-", "/", "*", "="]
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

            self.x[PosUltElement] = UltElement
            ########################################################################################################

            BanderaIgual = False

            while BanderaIgual == False:
                self.Provicional = []
                self.Conca = ""
                self.ConcaCompleto = ""
                self.y = []
                self.prioridadGeneral = 0
                self.prioridadActual = 0
                self.posicionDePrioridadGeneral = 0
                self.posicionDePrioridadActual = 0
                for i in range (len(self.x)):
                    self.ElementoActual = self.x[i]

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
                        #print("Encontramos una prioridad mayor, guardamos la posicion y prioridad")
                        self.prioridadGeneral = self.prioridadActual
                        self.posicionDePrioridadGeneral = self.posicionDePrioridadActual
                        #print (self.prioridadGeneral, self.posicionDePrioridadGeneral)

                    elif self.prioridadActual == self.prioridadGeneral:
                        pass
                        #print("Encontramos una prioridad Igual, continuamos con el primero")

                    print("\n")

                self.Conca = "(" + ","\
                             + self.x[(self.posicionDePrioridadGeneral)-1] + "," \
                             + self.x[(self.posicionDePrioridadGeneral)] + "," \
                             + self.x[(self.posicionDePrioridadGeneral)+1] + "," \
                             + ")"

                C = 0
                while C < ((len(self.x))):
                    print(C)
                    if C == ((self.posicionDePrioridadGeneral)-1):
                        self.Provicional.append(self.Conca)
                        C =(self.posicionDePrioridadGeneral)+2
                    else:
                        self.Provicional.append(self.x[C])
                        C = C + 1
                self.x = self.Provicional
                print (self.x)

                if self.prioridadActual == 1:
                    pre = self.x[0]
                    self.ConcaCompleto = pre.split(",")
                    print("\n")
                    print("Concatenacion final: ", self.ConcaCompleto)
                    #self.LISTA_GENERAL.append(self.ConcaCompleto)
                    LOL.Guardar_en_Arhivo(self, pre+"\n")
                    BanderaIgual = True