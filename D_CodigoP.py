
class CodigoPP():
    def Codigo_CodigoP_2(self,exp):
        co = ""
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

        for i in range(len(exp)):
            co = co + exp[i]
        #cadena = "Suma=x+2*13+4+5/12*65;"
        cadena = (co + ";")
        print("operacion sin ser lista xdxdxdxdxd")
        print(cadena)
        contador_total = 0
        tam_linea = len(cadena)
        conca = ""
        cant_pos = 0
        tokens = []
        operadores = 0
        posicion = 1
        contador_chido = 0
        contador_cucho = 0
        bandera_igual = 0
        TokensFinal = []
        while cant_pos < tam_linea:
            if cadena[cant_pos] != "\n" and cadena[cant_pos] != " " and cadena[cant_pos] != "" and cadena[
                cant_pos] != ";" and cadena[cant_pos] != "," and cadena[cant_pos] != "/" and cadena[cant_pos] != "*" and \
                    cadena[cant_pos] != "-" and cadena[cant_pos] != "+" and cadena[cant_pos] != "=":
                conca = conca + cadena[cant_pos]

            if cadena[cant_pos] == "\n" or cadena[cant_pos] == " " or cadena[cant_pos] == "" or cadena[
                cant_pos] == ";" or cadena[cant_pos] == "," or cadena[cant_pos] == "/" or cadena[cant_pos] == "*" or \
                    cadena[cant_pos] == "-" or cadena[cant_pos] == "+" or cadena[cant_pos] == "=":
                if conca != "\n" and conca != " " and conca != "" and conca != ";" and conca != "," and conca != "int" and conca != "string" and conca != "float" and conca != "char" and conca != "bipo":
                    if conca[0] != '"':
                        if conca != "OKEYLETSGO" and conca != "YAESTODAWE" and conca != "mostrar" and conca != "guardar":
                            tokens.append(conca)

            if cadena[cant_pos] == "+" or cadena[cant_pos] == "-" or cadena[cant_pos] == "*" or cadena[
                cant_pos] == "/" or cadena[cant_pos] == "=":
                tokens.append(cadena[cant_pos])
                operadores = operadores + 1
                conca = ""
                if cadena[cant_pos] == "*" or cadena[cant_pos] == "/":
                    contador_chido = contador_chido + 1
                if cadena[cant_pos] == "+" or cadena[cant_pos] == "-":
                    contador_cucho = contador_cucho + 1
            cant_pos = cant_pos + 1

        while contador_chido > 0 or contador_cucho > 0:
            if (posicion) >= len(tokens):
                posicion = 1

            if tokens[posicion] == "=":
                print("lda ", tokens[posicion - 1], " ;")
                TokensFinal.append(("lda " + tokens[posicion - 1] + " ;"))
                bandera_igual = 1
                tokens[posicion] = "$"
                tokens[posicion - 1] = "$"

            if tokens[posicion] == "*" or tokens[posicion] == "/":
                contador_chido = contador_chido - 1

                if tokens[posicion - 1] != "$":
                    if tokens[posicion - 1][0] == "1" or tokens[posicion - 1][0] == "2" or tokens[posicion - 1][
                        0] == "3" or tokens[posicion - 1][0] == "4" or tokens[posicion - 1][0] == "5" or \
                            tokens[posicion - 1][0] == "6" or tokens[posicion - 1][0] == "7" or tokens[posicion - 1][
                        0] == "8" or tokens[posicion - 1][0] == "9" or tokens[posicion - 1][0] == "0":
                        print("ldc ", tokens[posicion - 1], " ;")
                        TokensFinal.append(("ldc " + tokens[posicion - 1] + " ;"))
                    else:
                        print("lod ", tokens[posicion - 1], " ;")
                        TokensFinal.append(("lod " + tokens[posicion - 1] + " ;"))

                if tokens[posicion + 1] != "$":
                    if tokens[posicion + 1][0] == "1" or tokens[posicion + 1][0] == "2" or tokens[posicion + 1][
                        0] == "3" or tokens[posicion + 1][0] == "4" or tokens[posicion + 1][0] == "5" or \
                            tokens[posicion + 1][0] == "6" or tokens[posicion + 1][0] == "7" or tokens[posicion + 1][
                        0] == "8" or tokens[posicion + 1][0] == "9" or tokens[posicion + 1][0] == "0":
                        print("ldc ", tokens[posicion + 1], " ;")
                        TokensFinal.append(("ldc " + tokens[posicion + 1] + " ;"))
                    else:
                        print("lod ", tokens[posicion + 1], " ;")
                        TokensFinal.append(("lod " + tokens[posicion + 1] + " ;"))

                if tokens[posicion] != "$":
                    if tokens[posicion] == "*":
                        print("mpi ;")
                        TokensFinal.append(("mpi ;"))
                    if tokens[posicion] == "/":
                        print("div ;")
                        TokensFinal.append(("div ;"))

                tokens[posicion] = "$"
                tokens[posicion + 1] = "$"
                tokens[posicion - 1] = "$"

                if contador_chido == 0:
                    posicion = 1

            if (tokens[posicion] == "+" or tokens[posicion] == "-") and contador_chido == 0:
                contador_cucho = contador_cucho - 1
                if tokens[posicion - 1] != "$":
                    if tokens[posicion - 1][0] == "1" or tokens[posicion - 1][0] == "2" or tokens[posicion - 1][
                        0] == "3" or tokens[posicion - 1][0] == "4" or tokens[posicion - 1][0] == "5" or \
                            tokens[posicion - 1][0] == "6" or tokens[posicion - 1][0] == "7" or tokens[posicion - 1][
                        0] == "8" or tokens[posicion - 1][0] == "9" or tokens[posicion - 1][0] == "0":
                        print("ldc ", tokens[posicion - 1], " ;")
                        TokensFinal.append(("ldc " + tokens[posicion - 1] + " ;"))
                    else:
                        print("lod ", tokens[posicion - 1], " ;")
                        TokensFinal.append(("lod " + tokens[posicion - 1] + " ;"))

                if tokens[posicion + 1] != "$":
                    if tokens[posicion + 1][0] == "1" or tokens[posicion + 1][0] == "2" or tokens[posicion + 1][
                        0] == "3" or tokens[posicion + 1][0] == "4" or tokens[posicion + 1][0] == "5" or \
                            tokens[posicion + 1][0] == "6" or tokens[posicion + 1][0] == "7" or tokens[posicion + 1][
                        0] == "8" or tokens[posicion + 1][0] == "9" or tokens[posicion + 1][0] == "0":
                        print("ldc ", tokens[posicion + 1], " ;")
                        TokensFinal.append(("ldc " + tokens[posicion + 1] + " ;"))
                    else:
                        print("lod ", tokens[posicion + 1], " ;")
                        TokensFinal.append(("lod " + tokens[posicion + 1] + " ;"))

                if tokens[posicion] != "$":
                    if tokens[posicion] == "+":
                        print("adi ;")
                        TokensFinal.append(("adi ;"))
                    if tokens[posicion] == "-":
                        print("sbi ;")
                        TokensFinal.append(("sbi ;"))

                tokens[posicion] = "$"
                tokens[posicion + 1] = "$"
                tokens[posicion - 1] = "$"

            posicion = posicion + 2
        if bandera_igual == 1:
            print("sto ;")
            TokensFinal.append(("sto ;"))
        print("LIsta de tonkens final", TokensFinal)
        return TokensFinal

    def Codigo_CodigoP_4(self, exp):
        PreLista = []
        ListaTriplos = []

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
        msj= ""
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
                        if ((self.OperadorActual == "-")):
                            print("Encontramos un (-)")
                            self.prioridadActual = 2
                            self.posicionDePrioridadActual = i
                            msj = "sbi, "

                        elif (self.OperadorActual == "+"):
                            print("Encontramos un (+)")
                            self.prioridadActual = 2
                            self.posicionDePrioridadActual = i
                            msj = "adi, "

                        elif ((self.OperadorActual == "/")):
                            print("Encontramos un (/)")
                            self.prioridadActual = 3
                            self.posicionDePrioridadActual = i
                            msj = "div, "

                        elif (self.OperadorActual == "*"):
                            print("Encontramos un (*)")
                            self.prioridadActual = 3
                            self.posicionDePrioridadActual = i
                            msj = "mpi, "

                        elif ((self.OperadorActual == "=")):
                            print("Encontramos un (=)")
                            self.prioridadActual = 1
                            self.posicionDePrioridadActual = i
                            msj = "sto, "

                if self.prioridadActual > self.prioridadGeneral:
                    print("Encontramos una prioridad mayor, guardamos la posicion y prioridad")
                    self.prioridadGeneral = self.prioridadActual
                    self.posicionDePrioridadGeneral = self.posicionDePrioridadActual
                    print(self.prioridadGeneral, self.posicionDePrioridadGeneral)

                elif self.prioridadActual == self.prioridadGeneral:
                    print("Encontramos una prioridad Igual, continuamos con el primero")

                print("\n")


        return ListaTriplos


    def Codigo_CodigoP_3(self, exp):
        Insertar_CodigoP_Interfaz = []
        BanEncontrado = False
        BanAux = False
        Insertar_CodigoP_Interfaz.append("lda, "+ str(exp[1] + ";"))
        GuardPos = 0
        GuardPosIGUAL = 0
        AUX = ""
        for ig in range(len(exp)):
            if exp[ig] == "=":

                GuardPosIGUAL = ig+1
                print("Encontramos el igual, desde aqui empezamos a contar, posicion: ", GuardPosIGUAL)
                break

        while BanAux == False:
            print("\n\n")
            for i in range(GuardPosIGUAL,(len(exp))):
                #print(exp[i])
                if exp[i] == ")":
                    BanEncontrado = True
                    GuardarPos = i
                    break
            if BanEncontrado == True:
                    print(exp, "lista antes")
                    elementos = [exp[GuardarPos - 3],exp[GuardarPos - 2],exp[GuardarPos - 1]]
                    print(elementos)

                    (exp.pop(GuardarPos))
                    (exp.pop(GuardarPos-1))
                    (exp.pop(GuardarPos - 2))
                    (exp.pop(GuardarPos - 3))
                    exp[GuardarPos - 4] = "AUXILIAR"
                    print(exp, "Lista despues")
                    msj = ""
                    for j in range(len(elementos)):
                        print("Elemento", elementos[j])
                        if (elementos[j] == "*"):
                            msj = "mpi, "
                            GuardPos = j
                        elif (elementos[j] == "/"):
                            msj = "div, "
                            GuardPos = j
                        elif (elementos[j] == "+"):
                            msj = "adi, "
                            GuardPos = j
                        elif (elementos[j] == "-"):
                            msj = "sbi, "
                            GuardPos = j
                        elif (elementos[j] == "="):
                            msj = "sto, "
                            GuardPos = j
                            BanAux = True

                        elif (elementos[j] == "AUXILIAR"):
                            msj = "AUXILIAR xd, "
                        else:
                            print(elementos[j])
                            ban = self.NumeroEntero1(elementos[j])
                            if ban == False:
                                ban2 = self.NumeroFlotante1(elementos[j])
                                if ban2 == False:
                                    msj = "lod, "
                                else:
                                    print(elementos[j],"Flotante")
                                    msj = "ldc, "
                            else:
                                print(elementos[j],"Entero")
                                msj = "ldc, "
                            print(msj, "Mensaje")
                        if msj =="AUXILIAR xd, ":
                            pass
                        else:
                            print (msj + str(elementos[j] + ";"))
                            Insertar_CodigoP_Interfaz.append(msj + str(elementos[j] + ";"))

            print(Insertar_CodigoP_Interfaz)
            if (Insertar_CodigoP_Interfaz[len(Insertar_CodigoP_Interfaz)-1] == "mpi, *;") or \
                (Insertar_CodigoP_Interfaz[len(Insertar_CodigoP_Interfaz)-1] == "div, /;") or \
                (Insertar_CodigoP_Interfaz[len(Insertar_CodigoP_Interfaz)-1]== "adi, +;") or  \
                (Insertar_CodigoP_Interfaz[len(Insertar_CodigoP_Interfaz)-1] == "sbi, -;"):

                print(Insertar_CodigoP_Interfaz)
            else:
                AUX = Insertar_CodigoP_Interfaz[(len(Insertar_CodigoP_Interfaz) - 2)]
                print("AUZ", AUX)
                print(Insertar_CodigoP_Interfaz.pop((len(Insertar_CodigoP_Interfaz) - 2)))
                Insertar_CodigoP_Interfaz.append(AUX)
                print(Insertar_CodigoP_Interfaz)

        if BanAux == True:
            (Insertar_CodigoP_Interfaz.pop(len(Insertar_CodigoP_Interfaz) - 1))
        print("Lista Final",Insertar_CodigoP_Interfaz)
        return Insertar_CodigoP_Interfaz

#=========================================
#cadena=['(', 'C', '=', '(', '(', '(', '55', '*', '7', ')', '+', '79', ')', '-', '(', '(', '9', '*', '16', ')', '/', '28', ')', ')', ')']
#H=Hola()
#H.Codigo_CodigoP_2(cadena)