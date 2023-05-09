

class OPTI_archivos():
    def Archivos_PrecalcularExpresiones(self, Lista_Operaciones):
        OPTI_archivos.Limpiar_archivo(self,'E_FilePreCalc.txt')

        print("creando archivo PreCalc", Lista_Operaciones)
        with open('E_FilePreCalc.txt', 'a') as file:
            # looping over the each ist element

            for renglon in Lista_Operaciones:
                con=""
                for i in range(0, len(renglon)):
                    con=con + (str(renglon[i]))
                file.write('%s\n' % con)

    def Archivos_EliminacionNulos(self, Lista_Operaciones):
        OPTI_archivos.Limpiar_archivo(self,'E_FileNulos.txt')

        print("creando archivo NULOS", Lista_Operaciones)
        with open('E_FileNulos.txt', 'a') as file:
            # looping over the each ist element

            for renglon in Lista_Operaciones:
                con=""
                for i in range(0, len(renglon)):
                    con=con+str(renglon[i])
                file.write('%s\n' % con)

    def Archivos_ReduccionPotencias(self, Lista_Operaciones):
        OPTI_archivos.Limpiar_archivo(self,'E_FileReduPot.txt')

        print("creando archivo ReduPot", Lista_Operaciones)
        with open('E_FileReduPot.txt', 'a') as file:
            # looping over the each ist element

            for renglon in Lista_Operaciones:
                con=""
                for i in range(0, len(renglon)):
                    con=con+str(renglon[i])
                file.write('%s\n' % con)

    def Archivos_PropagacionCopias(self, Lista_Operaciones):
        OPTI_archivos.Limpiar_archivo(self,'E_FilePropCopy.txt')

        print("creando archivo PropCopy", Lista_Operaciones)
        with open('E_FilePropCopy.txt', 'a') as file:
            # looping over the each ist element

            for renglon in Lista_Operaciones:
                con=""
                for i in range(0, len(renglon)):
                    con=con+str(renglon[i])
                file.write('%s\n' % con)


    def Limpiar_archivo(self, nombre):
        f = open(nombre, 'w')
        f.write("")
        f.close()


