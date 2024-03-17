class Contacto:
    def __init__(self) -> None:
        self.nombre = None
        self.apellido = None
        self.celular = None
        
    def __str__(self) -> str:
        return f'{self.nombre} - {self.apellido} - {self.celular}'
    