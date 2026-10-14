class Biblioteca:

    def __init__(self):
        self.libros = []
        self.usuarios = []
        prestamos = []

    ##### LIBROS ####
    def registrar_libro(self,libro):
        #buscar si hay otro libro con ese isbn
        if self.buscar_libro(libro):
            print("El libro ya existe")
            return 

        self.libros.append(libro)

    def buscar_libro(self,libro_nuevo):
        for libro in self.libros:
            if libro.isbn == libro_nuevo.isbn:
                return libro
        return None

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def buscar_libro(self,isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                print(libro)
            else:
                print("El libro no existe")
    