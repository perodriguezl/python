print "Lista de Edades"
 
edad=input("Ingresa una Edad (<=0 para terminar): ")
 
lista = []
while edad > 0:
   lista.append(edad)
   edad=input("Ingresa una Edad (<=0 para terminar): ")
 
print ("Esta es la lista de Edades: " + str(lista)) #muestra el contenido de la lista

edadPromedio = sum(lista)/len(lista) #calcula el promedio

print ("Promedio de Edades: " + str(edadPromedio)) #muestra el promedio de las edades
