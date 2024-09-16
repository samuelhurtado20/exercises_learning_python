# Este programa toma un archivo csv y crea un nuevo archivo json modificado
# luego a portir del joson modificado se crea un nuevo archivo csv

import csv, json

old_csv_file = 'products_updated.csv'
new_json_fle = 'newproducts_json.json'
new_csv_file = 'newproducts_csv.csv'

new_product = {
        "name": "Bluetooth Speaker",
        "price": "120",
        "quantity": "40",
        "brand": "SoundVibes",
        "category": "Audio",
        "entry_date": "2024-07-20",
        "total_value": "4800.0"
    }

# 1. pasar del archivo csv a un nuevo archivo json ---------------------------------

# abrir archivo csv
with open(old_csv_file, mode='r') as csvFile:
    csv_reader = csv.DictReader(csvFile)

    # convertir las filas a una lista de diccionarios
    filas = list(csv_reader)

# Guardar en un archivo JSON 
with open(new_json_fle, mode='w') as newJsonFile:
    json.dump(filas, newJsonFile, indent=4)
    pass

# 2. modificar el nuevo archivo json -------------------------------------------------

with open(new_json_fle, mode='r') as newJsonFile:
    products = json.load(newJsonFile)

# añadimos el nuevo producto la lista de productos
products.append(new_product)

# esribimos las modificaciones en el archivo json
with open(new_json_fle, mode='w') as newJsonFile:
    json.dump(products, newJsonFile, indent=4)
    pass

# 3. pasar el archivo json a un nuevo archivo csv --------------------------------------

with open(new_json_fle, mode='r') as jsonFile:
    products = json.load(jsonFile)

with open(new_csv_file, mode='w', newline='') as csvFile:
    csv_writer = csv.DictWriter(csvFile, fieldnames=products[0].keys())

    csv_writer.writeheader()

    csv_writer.writerows(products)

    pass
