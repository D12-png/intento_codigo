import numpy as np
import json 
import os

def cargar_datos():
    try:
        with open('historial_pacientes.json', 'r') as file:
            data = json.load(file)
            pacientes =np.array(data)
    except FileNotFoundError:
        pacientes = np.empty((0,7), dtype=object)
    return pacientes
  #guardar datos en archivos json  
def guardar_datos(pacientes):
    with open('historial_pacientes.json', 'w') as file:
        json.dump(pacientes.tolist(), file)

def ingresar_ficha():
    nombre = input ("nombre del paciente:")
    rut = input ("rut del paciente:")
    edad = input ("edad del paciente:")
    sexo = input("sexo del paciente:")
    telefono = input("telefono del paciente:")
    diagnostico = input ("diagnostico del paciente:")
    medicamentos = input("medicamentos del paciente:")
    ficha = np.array([[nombre, rut, edad, sexo, telefono, diagnostico, medicamentos]])
    return ficha

def eliminar_ficha(rut,paciente):
    lista_actualizada_pacientes=[paciente for paciente in paciente[1]!=rut]
    return np.array(lista_actualizada_pacientes)

def buscar_ficha_por_rut (pacientes,rut):
    ficha_paciente = None
    for paciente in pacientes:
        if paciente[1]==rut:
            ficha_paciente = paciente
            break
    return ficha_paciente

def buscar_medicamentos_por_rut(pacientes, rut):
    medicamentos_preescritos = False
    for paciente in pacientes:
        if paciente[1]==rut: 
            print("El diagnostico de la consulta:{paciente[5]}")
            print("los medicamentos preescritos para el paciente son:{paciente[6]}")
            medicamentos_preescritos = True
    if not medicamentos_preescritos:
                print("El paciente no tiene medicamentos preescritos")

def listar_pacientes(pacientes):
     for i, paciente in enumerate(pacientes, start= 1):
          print("----------------------------------------------------")
          print(f"paciente{i}:")
          print(f"nombre:{paciente[0]}")
          print(f"rut:{paciente[1]}")
          print(f"edad:{paciente[2]}")
          print(f"sexo:{paciente[3]}")
          print(f"telefono:{paciente[4]}")
          print(f"diagnostico:{paciente[5]}")
          print(f"medicamentos:{paciente[6]}")
          print("----------------------------------------------------")

mi_array=np.array(listar_pacientes)

                
