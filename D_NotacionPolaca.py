

class Polaca():

    def Concatenar(self, parametro, expresion):

        if parametro=="(" or parametro==")":
            pass
        else:
            expresion= expresion+str(parametro)
        return expresion

    def Pol(self,Cadena):
        print ("Cadena: ", Cadena)
        expresion=""


        pos=0
        operando_variables = []
        operador = []
        Lista_de_Variables = []
        lista_parcial = []
        lista_operadores = []
        Exprecion_por_partes = []
        cont=0

        BAN=0


        while len(Cadena)>0:

            elem= Cadena[pos]

            if elem == "(" or elem == ")" or elem == "=" or elem == "/" or elem == "*" or elem == "+" or elem == "-":
                operador.append(elem)
                print ("\n METIENDO A LA PILA....")
                print ("Operadores +-*: ", operador)
            else:
                print ("\n METIENDO A LA PILA....")
                operando_variables.append(elem)
                print("Variables: ", operando_variables)
                print ("\n")

            if elem== ")":
                # ==========================================Modifico la cadena original
                print("     Parentesis CIERRA: ")

                for i in range(0, len(operando_variables)):
                    lista_parcial.append(operando_variables[i])
                Lista_de_Variables.append(lista_parcial)
                lista_parcial = []
                print("         LISTAS DE VARIABLES MOS", Lista_de_Variables)

                for i in range(0, len(operador)):
                    lista_parcial.append(operador[i])
                lista_operadores.append(lista_parcial)
                lista_parcial = []

                print("         LISTAS DE OPERADORES MOS", lista_operadores)

                # ===================================================================
                print("          Parentesis en pos: ", pos, "Contador: ", cont)
                print (Cadena)

                if cont==0:
                    print ("       SACA DOS VARIABLES AL INICIO.")

                    #NECESITO SACAR SI ES LA PRIMERA VEZ LAS DOS VARIABLES Y EL OPERADOR DE ARRIBA
                    d = operando_variables.pop()  #saco variable
                    expresion= Polaca.Concatenar(self, d, expresion)
                    e = operando_variables.pop() #saco variable 2
                    expresion= Polaca.Concatenar( self, e, expresion)  #saco parentesis y operador de la pila
                    a = operador.pop()
                    expresion= Polaca.Concatenar(self,  a, expresion)
                    b = operador.pop()
                    expresion=Polaca.Concatenar(self, b, expresion)
                    c = operador.pop()
                    expresion=Polaca.Concatenar(self, c, expresion)
                    cont=cont+1
                    print("Operadores +-*: ", operador)
                    print("Variables: ", operando_variables)


                else:
                    if ( Cadena[pos-1] =="AUXILIAR" or Cadena[pos-1] == ")" or Cadena[pos-3] =="AUXILIAR" or Cadena[pos-3] == ")"):


                        if Cadena[pos - 2] == "=":
                            print ("Legamos al final")

                            print("Operadores +-*: ", operador)
                            print("Variables: ", operando_variables)

                            expresion=""
                            x = operando_variables.pop()  # saco variable
                            expresion= Polaca.Concatenar(self, x, expresion)
                            # sacamos lo de la pila de operadores

                            print ("despues de sacar s1", expresion)

                            a = operador.pop()
                            print("pare", expresion)
                            expresion=Polaca.Concatenar(self, a, expresion)

                            b = operador.pop()
                            print("opera", expresion)
                            expresion=Polaca.Concatenar(self, b, expresion)

                            c = operador.pop()
                            expresion=Polaca.Concatenar(self, c, expresion)
                            print("1pare", expresion)
                            BAN=1


                            print("Operadores +-*: ", operador)
                            print("Variables: ", operando_variables)
                            print ("exprssion", expresion)

                        elif len(operando_variables)==1 and len(operador) >3:
                            print ("solo queda una varoiable, no la sacamos por que hay mas operadores")
                            #no sacamos la varoable
                            a = operador.pop()
                            expresion = Polaca.Concatenar(self, a, expresion)
                            b = operador.pop()
                            expresion = Polaca.Concatenar(self, b, expresion)
                            c = operador.pop()
                            expresion = Polaca.Concatenar(self, c, expresion)
                            #solo sacamos el operador CASO: AUXILIAR-AUXILIAR


                            print("Operadores +-*: ", operador)
                            print("Variables: ", operando_variables)

                        else:
                            print("SOLO SACO UNA VARIABLE")

                            # NECESITO SACAR SI ES LA PRIMERA VEZ LAS DOS VARIABLES Y EL OPERADOR DE ARRIBA
                            d = operando_variables.pop()  # saco variable
                            expresion=Polaca.Concatenar(self, d, expresion)
                            a = operador.pop()
                            expresion=Polaca.Concatenar(self, a, expresion)
                            b = operador.pop()
                            expresion=Polaca.Concatenar(self, b, expresion)
                            c = operador.pop()
                            expresion=Polaca.Concatenar(self, c, expresion)
                            cont = cont + 1
                            print("Operadores +-*: ", operador)
                            print("Variables: ", operando_variables)

                    else:
                            print ("SACA DOS VARIABLES")
                            # NECESITO SACAR SI ES LA PRIMERA VEZ LAS DOS VARIABLES Y EL OPERADOR DE ARRIBA
                            d = operando_variables.pop()  # saco variable
                            expresion=Polaca.Concatenar(self, d, expresion)
                            e = operando_variables.pop()  # saco variable 2
                            expresion=Polaca.Concatenar(self, e, expresion)  # saco parentesis y operador de la pila
                            a = operador.pop()
                            expresion=Polaca.Concatenar(self, a, expresion)
                            b = operador.pop()
                            expresion=Polaca.Concatenar(self, b, expresion)
                            c = operador.pop()
                            expresion=Polaca.Concatenar(self, c, expresion)
                            cont = cont + 1
                            print("Operadores +-*: ", operador)
                            print("Variables: ", operando_variables)

                if BAN==1:
                    Cadena=[]

                else:
                    print("  \n  MODIFICANDO PILAS : ")
                    print (Cadena, "Pos: ", pos)
                    Cadena.pop(pos)
                    Cadena.pop(pos - 1)
                    Cadena.pop(pos - 2)
                    Cadena.pop(pos - 3)
                    Cadena.pop(pos - 4)
                    Cadena.insert(pos - 4, "AUXILIAR")
                    pos= pos-4

                print("Sacamos: ", expresion)
                Exprecion_por_partes.append(expresion)
                expresion = ""
                print (Cadena, "Continuamos en: ", pos)


            pos=pos+1


        return Lista_de_Variables, lista_operadores, Exprecion_por_partes


