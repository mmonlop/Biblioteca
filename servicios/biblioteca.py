class Biblioteca:

    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    ##### LIBROS ####
    def registrar_libro(self,libro):
        #buscar si hay otro libro con ese isbn
        if self.buscar_libro(libro):
            print("El libro ya existe")
            return 

        self.libros.append(libro)

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def buscar_libro(self,isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                print(libro)
                return libro
            
        print("El libro no existe")
        return None
    
    #### USUARIOS ####

    def registrar_usuario(self,usuario):

        if self.buscar_usuario(usuario):
            print("EL usuario ya existe")
            return

        self.usuarios.append(usuario)


    def buscar_usuario(self,usuario):
        for usu in self.usuarios:
            if usu.id == usuario.id:
                return usu
        return None

    #### PRESTAMOS ####

    def realizar_prestamo(self,prestamo):

        for libro in self.libros:
            if libro.isbn == prestamo.libro and libro.disponible:
                self.prestamos.append(prestamo)
                libro.disponible = False    
                return

        print("El libro esta prestado")


    def registrar_devolucion(self,libro,fecha):
        for prestamo in self.prestamos:
            if prestamo.libro == libro and not prestamo.fecha_devolucion:
                prestamo.fecha_devolucion = fecha
                return

    def mostrar_prestamos_activos(self):
        for prestamo in self.prestamos:
            if not prestamo.fecha_devolucion:
                print(prestamo)