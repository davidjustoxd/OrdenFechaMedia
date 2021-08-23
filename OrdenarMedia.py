#Programa para organizar media (fotos y vídeos) por año y mes en carpetas automáticamente.
#FUNCION RECURSIVA. PARA CADA TIPO DE ARCHIVO VER SI ES ARCHIVO O CARPETA. SI SE TRATA DE UNA CARPETA, LLAMAR DE NUEVO A LA FUNCIÓN QUE LOS ORDENA.
import os
import shutil
import sys

#Función diccionario que devuelve en qué carpeta se debe encontrar el fichero en base a ser imagen o vídeo



    
extensiones = {
    "jpg" : "Fotos",
    "jpeg" : "Fotos",
    "png" : "Fotos",
    "raw" : "Fotos",
    "mp4" : "Videos",
    "mkv" : "Videos",
    "avi" : "Videos"
}

#Función recursiva que 
def MoveFile (path, dstImg, dstVideo, dstOthers):
    #Si no existe el directorio donde buscar, devolver mensaje de error
    if not os.path.exists(path):
        print(f"ERROR; path {path} not found")
        return
    #Si las carpetas dstImg o dstVideo no existen, las creamos
    if not os.path.exists(dstImg):
        os.mkdir(dstImg);
    if not os.path.exists(dstVideo):
        os.mkdir(dstVideo);
    if not os.path.exists(dstOthers):
        os.mkdir(dstOthers);


    #Para cada elemento en la carpeta, comprobar si es carpeta o archivo.
    for filename in os.scandir(path):
        #Si es una carpeta, llamada recursiva para volver a hacer la búsqueda
        if filename.is_dir:
            return MoveFile(filename, dstImg, dstVideo)
            #Sino, comprobar si se trata de una imagen o un vídeo
        else:
            ext = os.path.splitext(filename)[1]
            #Primero quitamos los archivos con extension no contemplada en diccionario.
            if ext not in extensiones.keys:
                shutil.move(os.path.join("C:", os.sep, path,filename), os.path.join("C:", os.sep, dstOthers,filename)) 

            

    




"""def organize (path: str):
        if not os.path.exists(path):
            print (f"ERROR. Ruta {path} no encontrada: no hay permisos o la ruta no existe.")
            return
        files = os.listdir(path)
        extensions = [os.path.splitext(file)[1].strip(".") for file in files]

    for ext in extensions: 
        dir = directory (ext) or ""
    #ESTA ES LA LINEA QUE HAY QUE CAMBIAR PARA ELEGIR EL DIRECTORIO DE DESTINO
        new_directory = os.path.join(path,dir)
        if dir and not os.path.exists(new_directory):
            os.makedirs(new_directory)

    for file in files:
        ext = os.path.splitext(file)[1].strip(".")
        _dir = directory (ext)
        if not _dir:
            continue

        source_filepath = os.path.join(path, file)
        destination_filepath = os.path.join(path, _dir, file)

        if not os.path.exists(destination_filepath):
            shutil.move(source_filepath, destination_filepath)
            printf(f"Was moved {file} into {_dir} directory. \n")
    printf(f"All the files was organized succdesfully in {path}")"""