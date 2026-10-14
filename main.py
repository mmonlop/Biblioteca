from modelos.libro import Libro
from modelos.usuario import Usuario
from modelos.prestamo import Prestamo
from servicios.biblioteca import Biblioteca


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

    while True:
        menu()
        op = int( input("Introduce una opcion: "))


        if op == 1:
            isbn = input("ISBN: ")
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            año = input("Año: ")
            genero = input("Genero: ")

            libro = Libro(isbn,titulo,autor,año,genero)

            biblioteca.registrar_libro(libro)

        elif op == 3:
            isbn = input("ISBN: ")
            biblioteca.buscar_libro(isbn)
        elif op == 4:
            biblioteca.listar_libros()

        elif op == 0:
            break 



if __name__ == "__main__":
    main()