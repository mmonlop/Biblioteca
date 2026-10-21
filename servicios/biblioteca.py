from servicios.ficheros import cargar, guardar_datos

class Biblioteca:

    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    

    ### ficheros

    # def mostrarrrr(self):
    #     print("########USUARIOS#######")
    #     for us in self.usuarios:
    #         print(us)


    def guardar(self):
        guardar_datos(self.libros)


    ##### LIBROS ####
    def registrar_libro(self,libro):
        #buscar si hay otro libro con ese isbn
        if self.buscar_libro(libro):
            print("El libro ya existe")
            return

        self.libros.append(libro)
        print("Libro registrado")

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def buscar_libro(self,libro):
        for libr in self.libros:
            if libr.isbn == libro.isbn:
                #print(libro)
                return libr
        return None

    def buscar_libro_isbn(self,isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                print(libro)
                return

        print("El libro no existe")
        return None
    
    #### USUARIOS ####

    def registrar_usuario(self,usuario):

        if self.buscar_usuario(usuario):
            print("EL usuario ya existe")
            return

        self.usuarios.append(usuario)
        print("Usuario creado")


    def buscar_usuario(self,usuario):
        for usu in self.usuarios:
            if usu.id == usuario.id:
                return usu
        return None


    def buscar_usuario_id(self,id):
        for usuario in self.usuarios:
            if usuario.id == id:
                print(usuario)
                return 
        print("NO EXISTE")
        return None



    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)


    #### PRESTAMOS ####

    def realizar_prestamo(self,prestamo):

        for libro in self.libros:
            if libro.isbn == prestamo.libro:
                if libro.disponible:
                    self.prestamos.append(prestamo)
                    print("Prestamo realizado")
                    libro.disponible = False
                    return
                print("El libro no esta disponible")
                return None
            print("El libro no existe")
            return None

        print("El libro esta prestado")


    def registrar_devolucion(self,libro,fecha):
        for prestamo in self.prestamos:
            if prestamo.libro == libro and not prestamo.fecha_devolucion:
                prestamo.fecha_devolucion = fecha
                return

    def mostrar_prestamos_activos(self):
        activos = []
        for prestamo in self.prestamos:
            if not prestamo.fecha_devolucion:
                activos.append(prestamo)

        print(activos)


    def mostrar_prestamos(self):
        for prestamo in self.prestamos:
            print(prestamo)