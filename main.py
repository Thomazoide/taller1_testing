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
            elif(self.imc>=20 and self.imc<=24.9):
                self.desc_imc='NORMAL'
            elif(self.imc>=25 and self.imc<=29.9):
                self.desc_imc='OBESIDAD LEVE'
            elif(self.imc>=30 and self.imc<=40):
                self.desc_imc='OBESIDAD SEVERA'
            elif(self.imc>40):
                self.desc_imc='OBESIDAD MUY SEVERA'
            else:
                self.desc_imc='caso particular...'
        else:
            if(self.imc<20):
                self.desc_imc='BAJO PESO'
            elif(self.imc>=20 and self.imc<=23.9):
                self.desc_imc='NORMAL'
            elif(self.imc>=24 and self.imc<=28.9):
                self.desc_imc='OBESIDAD LEVE'
            elif(self.imc>=29 and self.imc<=37):
                self.desc_imc='OBESIDAD SEVERA'
            elif(self.imc>37):
                self.desc_imc='OBESIDAD MUY SEVERA'
            else:
                self.desc_imc='caso particular...'