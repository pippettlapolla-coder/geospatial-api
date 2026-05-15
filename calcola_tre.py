class Libro:
    def __init__(self,titolo,autore):
        self.titolo=titolo
        self.autore=autore
        self.disponibile=True
    def __str__(self):
        return f'{self.titolo} di : {self.autore}- Disponibile: {self.disponibile}'
class Utente:
    def __init__(self,nome):
        self.nome=nome
        self.libri_presi=[]
    def prendere_libro(self,libro):
        if libro.disponibile:
            self.libri_presi.append(libro)
            libro.disponiible=False
    def restituire_libro(self,libro):
        if libro in self.libri_presi:
            self.libri_presi.remove(libro)
            libro.disponibile=True
class Biblioteca:
    def __init__(self):
        pass