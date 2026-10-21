from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo
from servicios.biblioteca import Biblioteca
from servicios.ficheros import cargar



def menu():
    print("=================================")
    print("      GESTIÓN DE BIBLIOTECA      ")
    print("=================================")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Listar libros")
    print("5. Realizar préstamo")
    print("6. Registrar devolución")
    print("7. Mostrar préstamos activos")
    print("8. Mostrar préstamos de un usuario")
    print("9. Guardar datos")
    print("0. Salir")



def main():

    biblioteca = Biblioteca()
    cargar(biblioteca)

    #biblioteca.mostrarrrr()


    while True:
        menu()
        op = int( input("Introduce una opcion: "))


        if op == 1:
            isbn = int(input("ISBN: "))
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            año = input("Año: ")
            genero = input("Genero: ")

            libro = Libro(isbn,titulo,autor,año,genero)

            biblioteca.registrar_libro(libro)

        elif op == 2:
            id = input("ID: ")
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            email = input("Email: ")

            usuario = Usuario(id,nombre,apellidos,email)

            biblioteca.registrar_usuario(usuario)

        elif op == 3:
            isbn = int(input("ISBN: "))
            biblioteca.buscar_libro_isbn(isbn)

        elif op == 4:
            biblioteca.listar_libros()

        elif op == 5:

            id_usuario = input("ID de usuario: ")
            id_libro = input("ID de libro: ")
            fecha = input("Fecha: ")

            prestamo = Prestamo(id_usuario,id_libro,fecha)

            biblioteca.realizar_prestamo(prestamo)

        elif op == 6:

            libro = input("Id libro: ")
            fecha = input("Fecha devolucion: ")

            biblioteca.registrar_devolucion(libro,fecha)

        elif op == 7:
            biblioteca.mostrar_prestamos_activos()

        elif op == 8:
            biblioteca.buscar_usuario_id(1)

        elif op == 9:
            biblioteca.guardar()
            pass

        elif op == 0:
            break


if __name__ == "__main__":
    main()