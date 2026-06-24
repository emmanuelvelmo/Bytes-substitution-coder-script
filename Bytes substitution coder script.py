import pathlib # Manejo moderno de rutas de archivos y directorios
import shutil # Copia de archivos y directorios
import os # Operaciones del sistema operativo para creación de directorios

# VARIABLES GLOBALES
# Lista de mapeo de bytes (índice = valor original, contenido = valor nuevo)
mapeo_bytes = [0x81, 0xB3, 0xA9, 0xB0, 0xC9, 0xC0, 0x25, 0x29, 0x72, 0xAD, 0x65, 0xAC, 0xAE, 0x0F, 0xD2, 0x39, 0x30, 0xDC, 0xA6, 0x04, 0x3A, 0x5C, 0x46, 0xB9, 0x35, 0xCC, 0x53, 0x62, 0x94, 0x6E, 0x91, 0x7B, 0x44, 0x96, 0xE2, 0xEC, 0x3F, 0x8D, 0xD9, 0x15, 0x8E, 0xE9, 0x2D, 0x12, 0x16, 0x74, 0x89, 0x61, 0x7E, 0x1C, 0xD8, 0x76, 0x52, 0x1B, 0xFD, 0x19, 0x85, 0x5A, 0x9F, 0x92, 0x9D, 0x93, 0xD6, 0x1A, 0x6C, 0x82, 0x4F, 0xF4, 0xC2, 0x69, 0x05, 0xBE, 0x95, 0xA1, 0x34, 0x03, 0x22, 0x83, 0x01, 0x68, 0x56, 0x71, 0x4E, 0x4B, 0xF7, 0x1D, 0xDE, 0x18, 0xC4, 0x3C, 0xD4, 0xCA, 0xE6, 0xE8, 0xA3, 0xA2, 0xB2, 0x31, 0x5B, 0x0E, 0xA8, 0x00, 0xB6, 0x4D, 0xBC, 0xCE, 0x50, 0x60, 0x5E, 0x77, 0xB7, 0xE3, 0x8A, 0x5F, 0xB4, 0xF2, 0x8C, 0x07, 0x8F, 0xA0, 0xE0, 0x13, 0x2F, 0xBF, 0x51, 0xF0, 0x28, 0xB1, 0xAA, 0xAF, 0x2E, 0xDD, 0x9A, 0xE7, 0xC6, 0x80, 0xFE, 0xC8, 0x37, 0x36, 0xF3, 0x3E, 0x20, 0xD3, 0x27, 0x21, 0x3B, 0xD7, 0xFF, 0x9E, 0x0C, 0xE4, 0xEF, 0xB8, 0x59, 0x7F, 0xFB, 0x02, 0x63, 0x48, 0x84, 0x58, 0xC3, 0x70, 0x33, 0xDB, 0xEB, 0x6D, 0x88, 0x24, 0x97, 0xEA, 0xAB, 0x3D, 0xF6, 0xF5, 0x11, 0xF9, 0x2A, 0x47, 0xA4, 0xCF, 0x7D, 0xA7, 0xD5, 0x90, 0xE1, 0x6B, 0xBB, 0xBD, 0xCD, 0x0D, 0x23, 0x9B, 0x08, 0x41, 0x49, 0x4A, 0x67, 0x78, 0xBA, 0xD1, 0x1E, 0xDA, 0x99, 0xDF, 0x5D, 0x45, 0xF1, 0x0A, 0x79, 0x42, 0x64, 0x6A, 0xC7, 0x2B, 0xA5, 0x75, 0xD0, 0x7C, 0xCB, 0x40, 0x8B, 0x32, 0xC1, 0x7A, 0xEE, 0xFC, 0x43, 0x10, 0x0B, 0xFA, 0x54, 0xC5, 0x57, 0x66, 0x6F, 0x55, 0x38, 0x17, 0x98, 0x9C, 0x4C, 0x06, 0xF8, 0x73, 0x2C, 0xB5, 0x09, 0x26, 0x1F, 0xED, 0x86, 0xE5, 0x14, 0x87]

# FUNCIONES
# Procesa un archivo binario aplicando mapeo de bytes (codificar)
def procesar_archivo_codificar(origen_archivo, destino_archivo, mapeo_bytes):
    # Leer todos los bytes del archivo original
    with open(origen_archivo, 'rb') as archivo_origen:
        datos_originales = archivo_origen.read()
    
    # Aplicar mapeo a cada byte
    datos_procesados = bytearray(len(datos_originales))
    
    # Recorrer cada byte del archivo
    for indice, byte_actual in enumerate(datos_originales):
        # Reemplazar byte según mapeo
        datos_procesados[indice] = mapeo_bytes[byte_actual]
    
    # Escribir archivo procesado
    with open(destino_archivo, 'wb') as archivo_destino:
        archivo_destino.write(datos_procesados)

# Procesa un archivo binario aplicando mapeo inverso (decodificar)
def procesar_archivo_decodificar(origen_archivo, destino_archivo, mapeo_bytes):
    # Crear mapeo inverso (valor mapeado -> índice original)
    mapeo_inverso = [0] * 256
    
    # Construir mapeo inverso
    for indice, valor in enumerate(mapeo_bytes):
        mapeo_inverso[valor] = indice
    
    # Leer todos los bytes del archivo original
    with open(origen_archivo, 'rb') as archivo_origen:
        datos_originales = archivo_origen.read()
    
    # Aplicar mapeo inverso a cada byte
    datos_procesados = bytearray(len(datos_originales))
    
    # Recorrer cada byte del archivo
    for indice, byte_actual in enumerate(datos_originales):
        # Reemplazar byte según mapeo inverso
        datos_procesados[indice] = mapeo_inverso[byte_actual]
    
    # Escribir archivo procesado
    with open(destino_archivo, 'wb') as archivo_destino:
        archivo_destino.write(datos_procesados)

# Crea la estructura de directorios de salida
def crear_directorio_salida(directorio_origen):
    # Obtener nombre de la carpeta origen
    nombre_carpeta = pathlib.Path(directorio_origen).name
    
    # Crear nombre para carpeta de salida
    nombre_salida = nombre_carpeta + " (output)"
    
    # Obtener directorio padre
    directorio_padre = pathlib.Path(directorio_origen).parent
    
    # Ruta completa del directorio de salida
    directorio_salida = directorio_padre / nombre_salida
    
    # Crear directorio de salida
    directorio_salida.mkdir(exist_ok = True)
    
    return directorio_salida

# Procesa recursivamente el directorio de origen y cuenta elementos
def procesar_directorio(directorio_origen, directorio_salida, mapeo_bytes, modo_operacion):
    # Convertir a objetos Path
    origen_path = pathlib.Path(directorio_origen)
    salida_path = pathlib.Path(directorio_salida)
    
    # Contadores para estadísticas
    contador_directorios = 0
    contador_archivos = 0
    
    # Recorrer recursivamente todos los archivos
    for archivo_iter in origen_path.rglob('*'):
        # Verificar que sea un archivo
        if archivo_iter.is_file():
            # Calcular ruta relativa desde el directorio origen
            ruta_relativa = archivo_iter.relative_to(origen_path)
            
            # Construir ruta de salida manteniendo estructura
            destino_archivo = salida_path / ruta_relativa
            
            # Crear directorios necesarios
            destino_archivo.parent.mkdir(parents = True, exist_ok = True)
            
            # Procesar archivo según modo de operación
            if modo_operacion == 1:
                procesar_archivo_codificar(archivo_iter, destino_archivo, mapeo_bytes)
            else:
                procesar_archivo_decodificar(archivo_iter, destino_archivo, mapeo_bytes)
            
            # Incrementar contador de archivos
            contador_archivos += 1
    
    # Contar directorios creados (excluyendo el directorio raíz de salida)
    for directorio_iter in salida_path.rglob('*'):
        if directorio_iter.is_dir():
            contador_directorios += 1
    
    return contador_directorios, contador_archivos

# PUNTO DE PARTIDA
# Bucle principal del programa
while True:
    # Solicitar directorio de entrada
    while True:
        directorio_entrada = input("Enter directory: ").strip('"\'')
        
        # Verificar que el directorio exista
        if not pathlib.Path(directorio_entrada).exists():
            print("Wrong directory\n")
        else:
            break
    
    # Solicitar modo de operación
    while True:
        modo_entrada = input("Select option (Encode: 1 , Decode: 2): ").strip()
        
        # Verificar que sea 1 o 2
        if modo_entrada == '1':
            modo_operacion = 1
            break
        elif modo_entrada == '2':
            modo_operacion = 2
            break
        else:
            print("Wrong format\n")
            continue
    
    # Crear directorio de salida
    directorio_salida = crear_directorio_salida(directorio_entrada)
    
    # Procesar todos los archivos en el directorio
    contador_directorios, contador_archivos = procesar_directorio(directorio_entrada, directorio_salida, mapeo_bytes, modo_operacion)
    
    # Mostrar estadísticas de salida
    if contador_directorios == 1:
        print(f"Output: {contador_directorios} directory, {contador_archivos} file")
    else:
        print(f"Output: {contador_directorios} directories, {contador_archivos} files")
    
    print() # Línea en blanco para separar iteraciones

# Detener el programa (no se alcanza debido al while True)
input()