class Usuario: 
    def __init__(self,id,nombre,apellidos,email):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self):
        return f"NOMBRE_USUARIO: {self.nombre} {self.apellidos} - EMAIL {self.email}"


