#Leer un archivo línea por línea
"""with open('caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las líneas en una lista
"""with open('caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

#Añadir texto
"""with open('caperucita.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")"""

#Sobreescribir el texto
with open('caperucita.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")

# RETO conteo de las lineas del cuento de caperucita
with open ("clase30/caperucita.txt", "r") as file:
    lines = file.readlines()
    print(len(lines)) # 63

with open('cuento.txt','r') as file:
    number_lines=0
    for lines in file:
        number_lines+=1
        print(f"{number_lines}.{lines.strip()}")
```with open('cuento.txt','r') as file:    number\_lines=0    for lines in file:        number\_lines+=1        print(f"{number\_lines}.{lines.strip()}")
