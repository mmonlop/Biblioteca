class Usuario: 
    def __init__(self,id,nombre,apellidos,email):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self):
        return f"ID: {self.id}  NOMBRE_USUARIO: {self.nombre} {self.apellidos} - EMAIL {self.email}"


    def to_dict(self):
        return{
            "id": {self.id},
            "nombre": {self.nombre},
            "apellidos": {self.apellidos},
            "email": {self.email}
        } 