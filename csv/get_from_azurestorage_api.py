from fastapi import FastAPI, HTTPException
from azure.storage.blob import BlobServiceClient
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Datos de conexión de Azure Storage
connection_string = ""  # Reemplaza esto con tu cadena de conexión
container_name = ""  # El nombre del contenedor en tu Azure Storage
blob_name = "uploads/Iris1.csv"  # La ruta del blob dentro del contenedor
download_file_path = "Iris1.csv"  # Ruta en tu máquina local para guardar el archivo temporalmente


@app.get("/download-csv")
async def download_csv():
    try:
        # Crear un cliente para el servicio Blob
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        # Obtener el cliente del contenedor
        container_client = blob_service_client.get_container_client(container_name)

        # Obtener el cliente del blob
        blob_client = container_client.get_blob_client(blob_name)

        # Descargar el blob y guardarlo localmente
        with open(download_file_path, "wb") as download_file:
            download_data = blob_client.download_blob()
            #print(download_data.readall())
            download_file.write(download_data.readall())

        # Devolver el archivo como respuesta para descarga
        return FileResponse(download_file_path, media_type="text/csv", filename=blob_name.split('/')[-1])

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al descargar el archivo: {str(e)}")

    finally:
        if os.path.exists(download_file_path):
            print("Cleaning up the local file", download_file_path)
        # Opcional: Eliminar el archivo local después de enviarlo si no quieres mantenerlo
        #if os.path.exists(download_file_path):
        #    os.remove(download_file_path)

