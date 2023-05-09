class RECUPERA:

    def Guardar_en_Arhivo(self,T1):
        print ("creando un archivo")
        f = open('TokensValidos.txt', 'w')
        for i in range(len(T1)):
            if i == len(T1)-1:
                f.write(str(T1[i]))
            else:
                f.write(str(T1[i] + "\n"))
        f.close()


    def Obtener_Token_de_Archivo(self):
        f = open('TokensValidos.txt', 'r')
        Tokens = f.read()
        #print("entre a buscar tokens", Tokens)
        f.close()
        return Tokens


    def Meter_Linea(self, Lista):
        f = open('Mostrar.txt', 'a')
        f.write(str(Lista) + "\n")
        f.close()

    def Limpiar_archivo(self):
        f = open('Mostrar.txt', 'w')
        f.write("")
        f.close()

    def Sacar_Lineas(self):
        f = open('Mostrar.txt', 'r')
        Tokens = f.read()
        f.close()

        return Tokens











