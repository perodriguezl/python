import random

#Ejemplo de lanzar dado

print ("Aleatorios entre el 1 y el 6: " + str(random.randint(1, 6))) #La salida va a ser: 0, 1, 2, 3, 4 o 5

#Ejemplo de funcion eleccion aleatoria

lista = [2, 190, False, "hola", "pelota", 123]
print("Eleccion: " + str(random.choice(lista)))

#Ejemplo de Barajado

a = [1, 2, 3, 4, 5]

random.shuffle(a)

print("Nuevo Orden: "+str(a))
