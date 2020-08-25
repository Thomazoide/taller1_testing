import time, os
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
            print('Agregado/a correctamente...')
            input('Presione enter para continuar...')
            clear()
        elif opc==2:
            rut=input('Ingrese rut: ')
            for i in personas:
                if i.rut==rut:
                    print('Persona encontrada!\nNombre: ', i.nom,'\nRut: ',i.rut,'\nSexo: ', i.sex, '\nFecha de nacimiento: ', i.fecha)
                    print('Peso: ', i.peso,'\nFecha de pesaje: ',i.fechapesaje,'\nAltura: ',i.altura,' mts.\nAtleta: ', i.aon, '\nEstado: ', i.desc_imc)
                else:
                    print('Persona no registrada...')
            input('Presione enter para continuar...')
            clear()
        elif opc==3:
            for j,i in enumerate(personas):
                if i.imc>20:
                    print('\t',j ,'\nNombre: ', i.nom,'\nRut: ',i.rut,'\nSexo: ', i.sex, '\nFecha de nacimiento: ', i.fecha)
                    print('Peso: ', i.peso,'\nFecha de pesaje: ',i.fechapesaje,'\nAltura: ',i.altura,' mts.\nAtleta: ', i.aon, '\nEstado: ', i.desc_imc)
            input('Presione enter para continuar...')
            clear()
        elif opc==4:
            for j,i in enumerate(personas):
                if i.imc<20:
                    print('\t',j ,'\nNombre: ', i.nom,'\nRut: ',i.rut,'\nSexo: ', i.sex, '\nFecha de nacimiento: ', i.fecha)
                    print('Peso: ', i.peso,'\nFecha de pesaje: ',i.fechapesaje,'\nAltura: ',i.altura,' mts.\nAtleta: ', i.aon, '\nEstado: ', i.desc_imc)
            input('Presione enter para continuar...')
            clear()
        elif opc==5:
            for j,i in enumerate(personas):
                if i.imc>20 and i.imc<23.9:
                    print('\t',j ,'\nNombre: ', i.nom,'\nRut: ',i.rut,'\nSexo: ', i.sex, '\nFecha de nacimiento: ', i.fecha)
                    print('Peso: ', i.peso,'\nFecha de pesaje: ',i.fechapesaje,'\nAltura: ',i.altura,' mts.\nAtleta: ', i.aon, '\nEstado: ', i.desc_imc)
            input('Presione enter para continuar...')
            clear()
        elif opc==6:
            for j,i in enumerate(personas):
                print('\t',j ,'\nNombre: ', i.nom,'\nRut: ',i.rut,'\nSexo: ', i.sex, '\nFecha de nacimiento: ', i.fecha)
                print('Peso: ', i.peso,'\nFecha de pesaje: ',i.fechapesaje,'\nAltura: ',i.altura,' mts.\nAtleta: ', i.aon, '\nEstado: ', i.desc_imc)
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