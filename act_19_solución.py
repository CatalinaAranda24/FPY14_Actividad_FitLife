import os
import msvcrt
import csv

#Función para crear titulos
def titulo(texto : str):
    print(f"\033[033m>>{texto.upper()}<<\033[0m")
def error(texto : str):
    print(f"\033[031m❌ {texto.upper()} ❌\033[0m")
def exito(texto : str):
    print(f"\033[032m  ✅ {texto.upper()} ✅\033[0m")

#tuplas - clases
clases=[
("Pesas","LUN-MIE 8:30-10:00 a.m",10),
("Zumba","MAR-JUE 3:30-5:40 p.m",20),
("Nutrición","VIE 6:00-7:30 a.m",2),
("Crossfit","SAB 11:30-12:55 p.m",10)
]
#Diccionario - Usuarios
usuarios={}
#Listas - Reservas
reservas=[]
#contador de id
numero_usuario=100
#Comenzamos sistema
while True:
    print(">>Press any key<<")
    msvcrt.getch()
    os.system("cls")

    print("""
Sistema de gestión FitLife
═══════════════════════════
1) Registrar usuario
2) Reservar clase
3) Consultar clases disponibles
4) Consultar clases de usuario
5) Consultar usuarios
0) Salir
═══════════════════════════""")
    opcion=input("Seleccione: ")
    if opcion=="0":
        titulo("Adios")
        break
    elif opcion=="1":
        titulo("Registrar usuario")
        nombre=input("Ingrese nombre de usuario: ").title()
        #Validar que el nombre de usuario no se repita
        if nombre not in usuarios.values():
            usuarios[numero_usuario]=nombre
            exito(f"Usuario {numero_usuario}  registrado")
            numero_usuario+=100
        else:
            error("❌ Usuario ya registrado ❌")
    elif opcion=="2":
        titulo("Reservar clase")
        codigo=int(input("Ingrese su código de usuario: "))
        if codigo in usuarios:
            curso=input("Ingrese curso a inscribir: ").capitalize()
            centinelaCurso=False
            centinelaCupo=False
            for c in clases:
                if c[0].capitalize()==curso:
                    centinelaCurso=True
                    if c[2]>0: #Verificamos si hay cupos
                        centinelaCupo=True
                        #Realizar reserva
                        reservas.append([codigo,usuarios[codigo],c[0],c[1]])
                        exito("Reserva realizada")
                        #descontar cupo
                        actualizacionCupo=(c[0],c[1],c[2]-1)
                        clases.remove(c)
                        clases.append(actualizacionCupo)
                        #Registrar reservas en csv
                        with open('Junio\siete\porte_reservas.csv','w',newline='',encoding='utf-8') as a:
                            escribir=csv.writer(a, delimiter=',')
                            escribir.writerows(reservas)
                        break
                    elif centinelaCupo==False:
                        error("Sin cupos disponibles")
            if centinelaCurso==False:
                error("Clase inexistente")        
        else:
            error("Codigo no registrado")
    elif opcion=="3":
        titulo("Consutar clases disponibles")
        for c in clases:
            print(f"{c[0]} Horario: {c[1]} Cupos: {c[2]}")
    elif opcion=="4":
        titulo("Consultar reservas de usuario")
        if len(reservas)>0:
            codigo=int(input("Ingrese código de usuario: "))
            centinela=False
            for r in reservas:
                if r[0]==codigo:
                    print(f"{r[0]} {r[1]} Curso: {r[2]} Horario: {r[3]}")
                    centinela=True
            if centinela==False:
                error("No tiene ninguna reserva")
    elif opcion=="5":
        titulo("Consultar usuario")
        if len(usuarios)>0:
            for u in usuarios:
                print(f"{u} : {usuarios[u]}")
        else:
            error("Sin usuarios registrados")
    else:
        error("Opción no válida")