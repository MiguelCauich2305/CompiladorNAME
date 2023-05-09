
import graphviz
from RecuperaOPERACIONES import OPERACIONES_REC as REC_OPERA


class Arbol1():
    def __init__(self):

        #REC_OPERA.Guardar_en_Arhivo(self) #creamos el archivo mientras
        self.Lineas_operaciones= REC_OPERA.Obtener_Operaciones_de_Archivo(self)
        self.Archivo_Clasificacion= REC_OPERA.Obtener_Clasificacion_de_Archivo(self)


        self.Default()

    def Default(self):


        for i in range (len(self.Lineas_operaciones)): #Verificamos linea por linea, es decir, operacion por operacion
            self.operacion = self.Lineas_operaciones[i] #guardamos la operacion de cada linea
            self.Clasi= self.Archivo_Clasificacion[i]#guardamos la clasificacion de cada linea


            print ("Operacion: ", self.operacion, i)

            # aqui dividimos de cada linea por comas, de la operacion y de clasificacion
            self.operacion_divididos = self.operacion.split(",")
            self.Clasi_divididos = self.Clasi.split(",")

            nombre = ""  # este nombre será la operacion completa sin comas de cada linea del archivo

            for j in range(0, len(self.operacion_divididos)):
                if self.operacion_divididos[j] != ",":
                    nombre = nombre + self.operacion_divididos[j]

            var= 'Operacion'+str(i)+'.gv'
            g = graphviz.Digraph('G', filename=var)
            g.edge('Sent', 'GO')
            g.edge('Sent', ';')
            g.edge('Sent', 'Sentencias'+ ' Operaciones'+nombre)
            g.edge('Sent', 'GON')
            g.edge('Sent', '; ')


            g.edge('Sentencias'+ ' Operaciones'+nombre, 'Operaciones  '+nombre)#ponemos la operacion en la parte de arriba del arbol


            for a in range(0, len(self.operacion_divididos)):#recorremos la cantidad comppleta de tokens que hay en una opera

                print (self.operacion_divididos[a])
                Elemento= self.operacion_divididos[a]
                Tipo_elem= self.Clasi_divididos[a]
                print("por que no entra", Elemento, Tipo_elem)


                if Tipo_elem=="caracter":
                    print ("caracter")
                    g.edge('Operaciones  '+nombre, "=")

                elif Tipo_elem== "Operador":
                    print ("operad")

                    g.edge('Operaciones  '+nombre,"Operador"+Elemento+str((" " * a)) )
                    g.edge('Operador'+Elemento+str((" " * a)),Elemento+str((" " * a)))

                elif Tipo_elem== "Identificador" and a == 0: #ARMA LA PRIMERA RAMA DEL ARBOL, PARA VARIABLE ANTES DE =
                    print ("1er identi")

                    g.edge('Operaciones  '+nombre,"nombrevar "+Elemento)
                    g.edge("nombrevar "+Elemento, "LMayus, LMinus|Numero "+Elemento)
                    g.edge("LMayus, LMinus|Numero "+Elemento, Elemento)


                elif Tipo_elem== "Identificador\n" and a != 0 or (Tipo_elem== "Identificador" and a != 0):
                    print("mas identi")

                    g.edge('Operaciones  '+nombre, "nombrevar|numero "+ Elemento)
                    g.edge("nombrevar|numero "+Elemento, 'nombrevar  '+Elemento)
                    g.edge("nombrevar  "+Elemento, Elemento)


                elif (Tipo_elem== "ENT") or (Tipo_elem =="DEC") or \
                        (Tipo_elem== "ENT\n") or (Tipo_elem == "DEC\n") or \
                        (Tipo_elem== "STR") or (Tipo_elem =="CHAR") or\
                        (Tipo_elem== "STR\n") or (Tipo_elem == "CHAR\n"):
                    print ("num")

                    g.edge('Operaciones  '+nombre," nombrevar|numero "+Elemento+str((" " * a)) )
                    g.edge(" nombrevar|numero "+Elemento+str((" " * a)) , "numero "+Elemento+str((" " * a)))
                    g.edge("numero "+Elemento+str((" " * a)), Elemento+str((" " * a)))

            print ("Ya se acabo el analisisd de la operaxcion a hacer el arbol")
            g.view()


