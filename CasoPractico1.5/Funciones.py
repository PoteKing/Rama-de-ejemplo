'''
Created on 15 jul. 2018

@author: Eneko
'''
import csv

def AcumularColumnaPorIndice(columna,ficheroEntrada,ficheroSalida):
    
    error = False
    list = {}
    
    try:
        pitchingFile = open(ficheroEntrada)
        exitFile = open(ficheroSalida, "w")
    
    except IOError:
                error = True

                print ("Error al intentar abrir el archivo \"PitchingPost.csv\".")
    
    if (error == False):               
        pitchingReader = csv.reader(pitchingFile)
        pitchingWriter = csv.writer(exitFile)
        
        for row in pitchingReader:
            if (row[columna] == 'yearID'):
                value = "Anyo"
                list[value] = "Frecuencia"
            elif (row[columna] == 'playerID'):
                value = "Jugador"
                list[value] = "Frecuencia"
            else:
                value = str(row[columna])
                
                if value in list:
                    list[value] = list[value] + 1
                else:
                    list[value] = 1
                
        pitchingFile.close()
        
        for value in list:
            row = [value, list.get(value)]
            pitchingWriter.writerow(row)
            
        print ("Archivo " + ficheroSalida + " generado con exito.")

def OrdenarPorNombreJugador(ficheroEntrada,ficheroSalida):
    
    error = False
    list = []
    
    try:
        pitchingFile = open(ficheroEntrada)
        exitFile = open(ficheroSalida, "w")
    
    except IOError:
                error = True

                print ("Error al intentar abrir el archivo \"PitchingPost.csv\".")
                
    if (error == False):               
        pitchingReader = csv.reader(pitchingFile)
        pitchingWriter = csv.writer(exitFile)
        
        for row in pitchingReader:
            list.append(row)
        
        pitchingFile.close()
        list = sorted(list, key=lambda row: row[0])
        
        for row in list:
            pitchingWriter.writerow(row)
            
        print ("Archivo " + ficheroSalida + " generado con exito.")
    
AcumularColumnaPorIndice(1,"PitchingPost.csv","AcumAnnos.csv")
AcumularColumnaPorIndice(0,"PitchingPost.csv","AcumJugadores.csv")
OrdenarPorNombreJugador("PitchingPost.csv", "Ordenado.csv")


