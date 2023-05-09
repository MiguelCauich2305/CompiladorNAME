
class OPERACIONES_REC:
    def Obtener_Operaciones_de_Archivo(self): #para leer los tokens de la operacion
        f = open('OperacionesValidas.txt', 'r')
        Tokens = f.readlines()
        f.close()
        return Tokens

    def Obtener_Clasificacion_de_Archivo(self): #para leer la clasificacion de los tokens de las operaciones
        f = open('OperacionesClasi.txt', 'r')
        Tokens = f.readlines()
        f.close()
        return Tokens


    def Guardar_en_Arhivo(self,Operacion,Tipo):
        print ("creando un archivo")
        f = open('OperacionesValidas.txt', 'a')
        #f.write("Suma,=,1,+,Hola,-,Variable1")
        f.write(Operacion)
        f = open('OperacionesClasi.txt', 'a')
        #f.write("Identificador,caracter,numero,operador,Identificador,operador,Identificador")
        f.write(Tipo)
        f.close()

    def Limpiar_archivo(self):
        f = open('OperacionesValidas.txt', 'w')
        f.write("")
        f.close()
        f = open('OperacionesClasi.txt', 'w')
        f.write("")
        f.close()

