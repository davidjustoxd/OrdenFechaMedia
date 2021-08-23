#Programa para organizar media (fotos y vídeos) por año y mes en carpetas automáticamente.
import os
import shutil
import sys

#Función diccionario que devuelve en qué carpeta se debe encontrar el fichero en base a ser imagen o vídeo


def directory (file_extension: str) -> str:
    if not file_extension:
        return "Strange"

    
    folders_by_extension = {
        "jpg" : "Fotos",
        "jpeg" : "Fotos",
        "png" : "Fotos",
        "raw" : "Fotos",
        "mp4" : "Vídeos",
        "mkv" : "Vídeos",
        "avi" : "Vídeos"
    }

    return folders_by_extension.get(file_extension, "No Reconocido")
    

def organize (path: str):
        if not os.path.exists(path):
            print (f"ERROR. Ruta {path} no encontrada: no hay permisos o la ruta no existe.")
            return
        files = os.listdir(path)
        extensions = [os.path.splitext(file)[1].strip(".") for file in files]


for ext in extensions: 
    dir = directory (ext) or ""
    #ESTA ES LA LINEA QUE HAY QUE CAMBIAR PARA ELEGIR EL DIRECTORIO DE DESTINO
    new_directory = os.path.join(path,dir)