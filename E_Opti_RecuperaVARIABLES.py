class RECUPERA:

    def Guardar_en_Arhivo(self,T1):
        print ("creando un archivo")
        f = open('VariablesValidas.txt', 'w')
        for i in range(len(T1)):
            if i == len(T1)-1:
                f.write(str(T1[i]))
            else:
                f.write(str(T1[i] + "\n"))
        f.close()


    def Obtener_Token_de_Archivo(self):
        f = open('VariablesValidas.txt', 'r')
        Tokens = f.read()
        #print("entre a buscar tokens", Tokens)
        f.close()
        return Tokens
