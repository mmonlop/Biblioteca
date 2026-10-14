class Libro:
    def __init__(self,isbn,titulo,autor,año,genero,disponible=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.genero = genero
        self.disponible = disponible

    def __str__(self):
        self.disponible = "Disponible" if not self.disponible else "Prestado"
        return f"ISBN: {self.isbn} - TITULO: {self.titulo} - AUTOR: {self.autor} - AÑO: {self.año} - GENERO: {self.genero} - DISPONIBLE: {self.disponible}"

    def __eq__(self, value:object):
        return self.isbn == value.isbn 