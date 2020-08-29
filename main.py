import datetime, os
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
        self.desc_gc=''
    @property
    def obtenerIMC(self):
        self.imc=self.peso/self.altura**2
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
    @property
    def obtenerGC(self):
        e=self.fecha.split('/')
        n=datetime.datetime.now()
        self.edad=int(n.year)-int(e[-1])
        self.gc=int
        if(self.sex=='m' or self.sex=='M'):
            self.gc=((1.2*self.imc)+(0.23*self.edad-10.8-5.4))
            if(self.edad>=19 and self.edad<=24):
                if(self.gc>=10.8 and self.gc<=14.9):
                    self.desc_gc='Optimo'
                elif(self.gc>15 and self.gc<=23.3):
                    self.desc_gc='Bueno'
                elif(self.gc>23.3):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=25 and self.edad<=29):
                if(self.gc>=12.8 and self.gc<=16.5):
                    self.desc_gc='Optimo'
                elif(self.gc>16.5 and self.gc<=24.4):
                    self.desc_gc='Bueno'
                elif(self.gc>24.4):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=30 and self.edad<=34):
                if(self.gc>=14.5 and self.gc<=18):
                    self.desc_gc='Optimo'
                elif(self.gc>18 and self.gc<=25.2):
                    self.desc_gc='Bueno'
                elif(self.gc>25.2):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=35 and self.edad<=39):
                if(self.gc>=16.1 and self.gc<=19.4):
                    self.desc_gc='Optimo'
                elif(self.gc>19.4 and self.gc<=26.1):
                    self.desc_gc='Bueno'
                elif(self.gc>26.1):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=40 and self.edad<44):
                if(self.gc>=17.5 and self.gc<=20.5):
                    self.desc_gc='Optimo'
                elif(self.gc>20.5 and self.gc<=26.9):
                    self.desc_gc='Bueno'
                elif(self.gc>26.9):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=45 and self.edad<=49):
                if(self.gc>=18.6 and self.gc<=21.5):
                    self.desc_gc='Optimo'
                elif(self.gc>21.5 and self.gc<=27.6):
                    self.desc_gc='Bueno'
                elif(self.gc>27.6):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=50 and self.edad<=54):
                if(self.gc>=19.8 and self.gc<=22.7):
                    self.desc_gc='Optimo'
                elif(self.gc>22.7 and self.gc<=28.7):
                    self.desc_gc='Bueno'
                elif(self.gc>28.7):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=55 and self.edad<=59):
                if(self.gc>=20.2 and self.gc<=23.2):
                    self.desc_gc='Optimo'
                elif(self.gc>23.2 and self.gc<=29.3):
                    self.desc_gc='Bueno'
                elif(self.gc>29.3):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=60):
                if(self.gc>=20.3 and self.gc<=23.5):
                    self.desc_gc='Optimo'
                elif(self.gc>23.5 and self.gc<=29.8):
                    self.desc_gc='Bueno'
                elif(self.gc>29.8):
                    self.desc_gc='Malo(Obesidad)'
            else:
                self.desc_gc='Caso particular...'
        else:
            self.gc=((1.2*self.imc)+0.23*self.edad-5.4)
            if(self.edad>=19 and self.edad<=24):
                if(self.gc>=18.9 and self.gc<=22.1):
                    self.desc_gc='Optimo'
                elif(self.gc>22.1 and self.gc<=29.6):
                    self.desc_gc='Bueno'
                elif(self.gc>29.6):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=25 and self.edad<=29):
                if(self.gc>=18.9 and self.gc<=22):
                    self.desc_gc='Optimo'
                elif(self.gc>22 and self.gc<=29.8):
                    self.desc_gc='Bueno'
                elif(self.gc>29.8):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=30 and self.edad<=34):
                if(self.gc>=19.7 and self.gc<=22.7):
                    self.desc_gc='Optimo'
                elif(self.gc>22.7 and self.gc<=30.5):
                    self.desc_gc='Bueno'
                elif(self.gc>30.5):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=35 and self.edad<=39):
                if(self.gc>=21 and self.gc<=24):
                    self.desc_gc='Optimo'
                elif(self.gc>24 and self.gc<=31.5):
                    self.desc_gc='Bueno'
                elif(self.gc>31.5):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=40 and self.edad<=44):
                if(self.gc>=22.6 and self.gc<=25.6):
                    self.desc_gc='Optimo'
                elif(self.gc>25.5 and self.gc<=32.8):
                    self.desc_gc='Bueno'
                elif(self.gc>32.8):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=45 and self.edad<=49):
                if(self.gc>=24.3 and self.gc<=27.3):
                    self.desc_gc='Optimo'
                elif(self.gc>27.3 and self.gc<=34.1):
                    self.desc_gc='Bueno'
                elif(self.gc>34.1):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=50 and self.edad<=54):
                if(self.gc>=26.6 and self.gc<=29.7):
                    self.desc_gc='Optimo'
                elif(self.gc>29.7 and self.gc<=36.2):
                    self.desc_gc='Bueno'
                elif(self.gc>36.2):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=55 and self.edad<=59):
                if(self.gc>=27.4 and self.gc<=30.7):
                    self.desc_gc='Optimo'
                elif(self.gc>30.7 and self.gc<=37.3):
                    self.desc_gc='Bueno'
                elif(self.gc>37.3):
                    self.desc_gc='Malo(Obesidad)'
            elif(self.edad>=60):
                if(self.gc>=27.6 and self.gc<=31):
                    self.desc_gc='Optimo'
                elif(self.gc>31 and self.gc<=38):
                    self.desc_gc='Bueno'
                elif(self.gc>38):
                    self.desc_gc='Malo(Obesidad)'
            else:
                self.desc_gc='Caso particular...'
def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
def menu():
    print('\n\tSistema IMC.\n1.-Agregar persona\n2.-Buscar persona\n3.-Mostrar gente sobre el peso normal\n4.-Mostrar gente bajo el peso normal\n5.-Mostrar gente dentro del peso normal\n6.-Mostrar todas las personas registradas\n7.-Eliminar persona\n8.-Salir')
if __name__=='__main__':
    personas=[]
    opc=int
    while(opc!=8):
        menu()
        opc=int(input('Ingrese opcion: '))
        if opc==1:
            n=input('Ingrese nombre: ')
            rut=input('Ingrese rut(sin puntos, con guion "nnnnnnnn-n"): ')
            sex=input('Ingrese sexo(m;f): ')
            fn=input('Ingrese fecha de naciemiento(dd/mm/aaaa):')
            wgt=float(input('Ingrese peso(Kg): '))
            fp=input('Ingrese fecha de pesaje(dd/mm/aaa): ')
            hgt=float(input('Ingrese altura (en metros):'))
            aon=input('Es esta persona atleta?(1=si ; 0=no): ')
            personas.append(Persona(n,rut,sex,fn,wgt,fp,hgt,aon))
            if len(personas)!=0:
                for i in personas:
                    i.obtenerIMC
                    i.obtenerGC
            print('Agregado/a correctamente...')
            input('Presione enter para continuar...')
            clear()
        elif opc==2:
            rut=input('Ingrese rut: ')
            for i in personas:
                if i.rut==rut:
                    print('Persona encontrada!\nNombre: ', i.nom,'\nRut: ',i.rut,'\nSexo: ', i.sex, '\nFecha de nacimiento: ', i.fecha,'\nIMC: ', i.imc, '\nGrasa corporal: ', i.gc,'%')
                    print('Peso: ', i.peso,'\nFecha de pesaje: ',i.fechapesaje,'\nAltura: ',i.altura,' mts.\nAtleta: ', i.aon, '\nEstado IMC: ', i.desc_imc,'\nEstado GC: ', i.desc_gc)
                else:
                    print('Persona no registrada...')
            input('Presione enter para continuar...')
            clear()
        elif opc==3:
            for j,i in enumerate(personas):
                if i.imc>20:
                    print('Persona encontrada!\nNombre: ', i.nom,'\nRut: ',i.rut,'\nSexo: ', i.sex, '\nFecha de nacimiento: ', i.fecha,'\nIMC: ', i.imc, '\nGrasa corporal: ', i.gc,'%')
                    print('Peso: ', i.peso,'\nFecha de pesaje: ',i.fechapesaje,'\nAltura: ',i.altura,' mts.\nAtleta: ', i.aon, '\nEstado IMC: ', i.desc_imc,'\nEstado GC: ', i.desc_gc)
            input('Presione enter para continuar...')
            clear()
        elif opc==4:
            for j,i in enumerate(personas):
                if i.imc<20:
                    print('Persona encontrada!\nNombre: ', i.nom,'\nRut: ',i.rut,'\nSexo: ', i.sex, '\nFecha de nacimiento: ', i.fecha,'\nIMC: ', i.imc, '\nGrasa corporal: ', i.gc,'%')
                    print('Peso: ', i.peso,'\nFecha de pesaje: ',i.fechapesaje,'\nAltura: ',i.altura,' mts.\nAtleta: ', i.aon, '\nEstado IMC: ', i.desc_imc,'\nEstado GC: ', i.desc_gc)
            input('Presione enter para continuar...')
            clear()
        elif opc==5:
            for j,i in enumerate(personas):
                if i.imc>20 and i.imc<23.9:
                    print('Persona encontrada!\nNombre: ', i.nom,'\nRut: ',i.rut,'\nSexo: ', i.sex, '\nFecha de nacimiento: ', i.fecha,'\nIMC: ', i.imc, '\nGrasa corporal: ', i.gc,'%')
                    print('Peso: ', i.peso,'\nFecha de pesaje: ',i.fechapesaje,'\nAltura: ',i.altura,' mts.\nAtleta: ', i.aon, '\nEstado IMC: ', i.desc_imc,'\nEstado GC: ', i.desc_gc)
            input('Presione enter para continuar...')
            clear()
        elif opc==6:
            for j,i in enumerate(personas):
                    print('Persona encontrada!\nNombre: ', i.nom,'\nRut: ',i.rut,'\nSexo: ', i.sex, '\nFecha de nacimiento: ', i.fecha,'\nIMC: ', i.imc, '\nGrasa corporal: ', i.gc,'%')
                    print('Peso: ', i.peso,'\nFecha de pesaje: ',i.fechapesaje,'\nAltura: ',i.altura,' mts.\nAtleta: ', i.aon, '\nEstado IMC: ', i.desc_imc,'\nEstado GC: ', i.desc_gc)
            input('Presione enter para continuar...')
            clear()
        elif opc==7:
            rut=input('Ingrese rut: ')
            for x in personas:
                if rut==x.rut:
                    personas.remove(x)
            print('Eliminado con exito.')
            input('Presione enter para continuar...')
            clear()