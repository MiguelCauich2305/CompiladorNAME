
def Verifica_sies_numero( Car):
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    Ban1= False

    for i in range (0,len(num)):
        if Car == num[i]:
            Ban1= True
    print (Ban1)
    return Ban1

def Verifica_sies_minuscula( Car):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]
    Ban2= False
    for a in range(0, len(abc)):
        if Car == abc[a]:
            Ban2= True
        else:
            Ban2=Ban2
    return Ban2


def IDENTIFICADOR_SENCILLO(Tok):
        ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S",
           "T", "U", "V", "W", "X", "Y", "Z"]
        ListaPalabras = ["ENT", "DEC", "CHAR", "STR", "SHOW", "FLAG", "VALUE", "ENTER", "GO", "END"]

        print("        Entra a Verifica Identificadores",Tok)
        BAN_I = False  # quiere decir que no se ha aceptado que es IDENTI



        if BAN_I == False:  # si paso el primer filtro de arriba entonces continua ya que puede

            # Identifica que la primera posicion sea una letra Mayuscula
            if Tok != " " and Tok != "" and Tok != "\n":
                for i in range(0, len(ABC)):
                    if Tok[0] == ABC[i]:
                        BAN_I = True

                # si esto se cumplio, entonces verificamos el resto de caracteres
                if BAN_I == True:
                    for i in range(1, len(Tok)):  # para los caracteres restantes
                        BanNumero = Verifica_sies_numero(Tok[i], )
                        if BanNumero == False:
                            BanMinuscula = Verifica_sies_minuscula(Tok[i])
                            if BanMinuscula == False:
                                BAN_I = False

        if BAN_I == True:
            print ("            Es un Identificador", Tok)

        else:
            print ("             No es Identificador", Tok)



        return BAN_I
