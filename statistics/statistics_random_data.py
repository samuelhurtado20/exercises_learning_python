import statistics
import random

# Generar datos de ejemplo
data = [random.randint(1, 20) for _ in range(20)]  # 20 números aleatorios entre 1 y 20

# Medidas de tendencia central
media = statistics.mean(data)
mediana = statistics.median(data)
moda = statistics.mode(data)

# Medidas de dispersión
varianza = statistics.variance(data)
desviacion_estandar = statistics.stdev(data)

# Correlación (generar otro conjunto de datos relacionado)
data2 = [x + random.randint(-3, 3) for x in data]  # Datos relacionados con un poco de ruido
correlacion = statistics.correlation(data, data2)

# Imprimir resultados
print("Datos:", data)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Varianza:", varianza)
print("Desviación Estándar:", desviacion_estandar)
print("Correlación entre data y data2:", correlacion)
print("Dato maximo", max(data))
print("Dato minimo", min(data))
```Hice este un poco mas sencillo para entender mejor (:
