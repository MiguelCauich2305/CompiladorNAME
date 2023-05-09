
class OPERACIONES_DIV:

    def Obtener_Operaciones_de_Archivo(self): #para leer los tokens de la operacion
        f = open('OperacionesDivididas.txt', 'r')
        Tokens = f.readlines()
        f.close()
        return Tokens


    def Guardar_en_Arhivo(self,Operacion):
        print ("creando un archivo_")
        f = open('OperacionesDivididas.txt', 'a')
        f.write(Operacion)
        f.close()

    def Limpiar_archivo(self):
        f = open('OperacionesDivididas.txt', 'w')
        f.write("")
        f.close()

