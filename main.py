class Persona():
    def __init__(self, nombre, rut, sexo, fnacimiento, peso, fechapesaje, altura, aon):
        self.nom=nombre
        self.rut=rut
        self.sex=sexo
        self.fecha=fnacimiento
        self.aon=aon #esto determina si es atleta o persona normal
        self.peso=peso
        self.fechapesaje=fechapesaje
        self.altura=altura
        self.desc_imc=''
    def obtenerIMC(self, peso, altura):
        self.imc=peso/altura**2
        if(self.sex=='m' or self.sex=='M'):
            if(self.imc<20):
                self.desc_imc='BAJO PESO'
            elif(self.imc>=20 and self.imc<24.9):
                self.desc_imc='NORMAL'
            