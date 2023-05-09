
class P():


    def EliminacionNulos(self, Lista_Operaciones):
        for default in (Lista_Operaciones):
            print("Reduccion de potencias: ", default)
            if len(default) > 3:  # no analiza las igualciones x=3
                # default= ["x", "=", "7", "*", "1", "-", "0"]

                a = len(default)
                i = 0
                while i < a:
                    if default[i] == "/" or default[i] == "*" or default[i] == "+" or default[i] == "-":
                        print("hay")
                        if (default[i] == "/" or default[i] == "*") and default[i + 1] == "1":
                            default.pop(i)
                            print(default)
                            default.pop(i)
                            print(default)

                            i = i - 1
                            print("despues", i)

                        if (default[i] == "+" or default[i] == "-") and default[i + 1] == "0":
                            default.pop(i)
                            print(default)
                            default.pop(i)
                            i = i - 1
                        else:
                            i = i + 1


                    else:
                        i = i + 1
                    a = len(default)

        print("Al final de Eliminar NULOS: ", Lista_Operaciones)

P=P()
Lista_Operaciones= [

                        ['S1', '=', 'S2'],
                        ['S1', '=', '5', '*', '8', '-', '20', '+', '2', '-', '19', '/', 'S3'],
                        ['S2', '=', 'E1', '+', 'E2', '*', '10', '/', '7', '*', 'S2', '-', '30', '-', '15']

                           ]
P.EliminacionNulos(Lista_Operaciones)
