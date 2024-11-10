# PRÁCTICA 7A1
import random
lista = []
num_obj = random.randint(1,10)
i = 0
for i in range(0,20):
    num_ran = random.randint(1,10)
    lista.append(num_ran)

# Ya hemos creado la lista y el número aleatorio a buscar

print("La lista es:", lista)
print("El número es", num_obj)

# Ahora, buscamos en la lista, combinaciones de pajeras juntas que nos den el número buscado

for u in range(0,len(lista)-1):
    if lista[u] + lista[u+1] == num_obj:
        print(f"{lista[u]} + {lista[u+1]}")

# PRÁCTICA 7A2
import random
lista = []
num_obj = random.randint(1,10)
i = 0
while i < 20:
    num_ran = random.randint(1,10)
    lista.append(num_ran)
    i += 1

# Repetimos el proceso

print("La lista es:", lista)
print("El número es", num_obj)

# Ahora, buscamos de cada elemento de la lista, otro elemento de la lista que sumado a él de el num_obj...
# Pero, sin que sea sumado a el mismo, y para que no se repita la combinación cuando llegue al otro número, le cambiamos el...
# Valor a -10, para que sumado a ningún número pueda volver a dar el num_obj y volver a ser combinación. 
 

for u in range(0,len(lista)):
    for m in range(0,len(lista)):
        if lista[u] + lista[m] == num_obj and u != m:
            print(f"{lista[u]} + {lista[m]}")
    lista[u] = -10

# PRÁCTICA 7B
import matplotlib.pyplot as plt

eje_x = []
f_x = []
g_x = []

for x in range(-20, 21):
    eje_x += [x * 0.25] 
    f_x += [x**2 - 3*(x * 0.25) + 5]  
    g_x += [-5 * (x * 0.25)**2 + 4*(x * 0.25) + 25]  
    
plt.ylim(-50, 50)
plt.plot(eje_x, f_x)  
plt.plot(eje_x, g_x)  
plt.show()
