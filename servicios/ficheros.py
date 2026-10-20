import json
from pathlib import Path

ruta_libros = Path("./datos/libros.json")
ruta_prestamos = Path("./datos/prestamos.json")
ruta_usuarios = Path("./datos/usuarios.json")

# def cargar_libros():
#     try:
#         with ruta_libros.open(encoding="utf-8") as libros:
#             return json.load(libros)
#     except FileNotFoundError: 
#         print("Fichero no existe")

def cargar(op):
    try:
        if op == "libros":
            with ruta_libros.open(encoding="utf-8") as libros:
                return json.load(libros)
        elif op == "usuarios":
            with ruta_usuarios.open(encoding="utf-8") as usuarios:
                return json.load(usuarios)
        elif op == "prestamos":
            with ruta_prestamos.open(encoding="utf-8") as prestamos:
                return json.load(prestamos)
    except FileNotFoundError:
        print("Fichero no existe")

def guardar_libro(libro):
    with ruta_libros.open("w",encoding="utf-8") as fichero:
        json.dump(libro,ruta_libros)
        