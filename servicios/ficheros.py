import json
from pathlib import Path
from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo



ruta_libros = Path("./datos/libros.json")
ruta_prestamos = Path("./datos/prestamos.json")
ruta_usuarios = Path("./datos/usuarios.json")




def cargar(biblioteca):

    with open(ruta_libros,"r",encoding="utf-8") as fichero:
        libros = json.load(fichero)
        for libro in libros:
            libro_obj = Libro(libro['isbn'],libro['titulo'],libro['autor'],libro['año'],libro['genero'],libro['disponible'])
            biblioteca.libros.append(libro_obj)


    with open(ruta_usuarios,"r",encoding="utf-8") as fichero:
        usuarios = json.load(fichero)
        for usuario in usuarios:
            usuario_obj = Usuario(usuario['id'], usuario['nombre'], usuario['apellidos'], usuario['email'])
            biblioteca.usuarios.append(usuario_obj)


    with open(ruta_prestamos,"r",encoding="utf-8") as fichero:
        prestamos = json.load(fichero)
        for prestamo in prestamos:
            usuario = biblioteca.buscar_usuario_id(prestamo['usuario'])
            libro = biblioteca.buscar_libro_isbn(prestamo['libro'])

            prestamo_obj = Prestamo(usuario,libro,prestamo['fecha_prestamo'], prestamo['fecha_devolucion'])
            biblioteca.prestamos.append(prestamo_obj)



def guardar_datos(biblioteca):
    libros = []
    for libro in biblioteca.libros:
        libros.append(libro.__dict__)

    with open(ruta_libros,"w",encoding="utf-8")as fichero:
        json.dump(libros,fichero,ensure_ascii=False)


    usuarios = []
    for usuario in biblioteca.usuarios:
        usuarios.append(usuario.__dict__)

    with open(ruta_usuarios,"w",encoding="utf-8")as fichero:
        json.dump(usuarios,fichero,ensure_ascii=False)


    prestamos = []
    for prestamo in biblioteca.prestamos:
        prestamos.append(prestamo.__dict__)

    with open(ruta_prestamos, 'w', encoding="utf-8") as fichero:
        json.dump(prestamos, fichero, ensure_ascii=False)
