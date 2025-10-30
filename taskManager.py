import json
import os
import sys
from datetime import date

desktop = os.path.normpath(os.path.expanduser("~/Desktop"))

if os.path.exists(desktop + "\Task List.json"):
    with open(desktop + "\Task List.json", "r") as f:
        taskList = json.load(f)
else:
    taskList = []

def createTask():
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        try:
            id = int(input('Ingresar ID de tarea: '))
            break
        except ValueError:
            print("¡Ingresar un valor númerico!")
    
    titulo = str(input('Ingresar título de tarea: '))

    descripcion = str(input('Ingresar una descripción para la tarea: '))

    while True:
        estado = str(input('Ingresar estado de tarea (pendiente, en proceso, completada): '))
        match estado.upper():
            case 'PENDIENTE' | 'EN PROCESO' | 'COMPLETADA':
                break
            case _:
                print('¡Ingresar un estado válido!')
    
    fecha_creacion = date.today()
    fecha_creacion_str = fecha_creacion.isoformat()

    nueva_tarea ={
        "id": id,
        "titulo": titulo,
        "descripcion": descripcion,
        "estado": estado,
        "fecha de creacion": fecha_creacion_str
    }

    taskList.append(nueva_tarea)
    with open(desktop + "\Task List.json", "w") as f:
        json.dump(taskList, f, indent=4)

    print("\nTarea creada con éxito.")
    input('Presione cualquier tecla para continuar.')

def editTask():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if os.path.exists(desktop + "\Task List.json"):
        while(True):
            try:
                id = int(input('Ingresar ID de tarea a modificar: '))
                break
            except ValueError:
                print("¡Ingresar un valor númerico!")

        with open(desktop + "\Task List.json", 'r') as f:
            data = json.load(f)
        
        tarea_encontrada = None
        for tarea in data:
            if tarea["id"] == id:
                tarea_encontrada = tarea
                break
            if not tarea_encontrada:
                print("No se encontró ninguna tarea con ese ID.")
                return

        while True:
            estado = input('Ingresar estado de tarea (pendiente, en proceso, completada): ').strip()
            if estado.upper() in ['PENDIENTE', 'EN PROCESO', 'COMPLETADA']:
                tarea_encontrada["estado"] = estado
                break
            else:
                print('¡Ingresar un estado válido!')

        with open(desktop + "\Task List.json", 'w') as f:
            json.dump(data, f, indent=4)

        print("\nEstado actualizado correctamente.")
        input('Presione cualquier tecla para continuar.')
    else:
        print("No se encuentran tareas registradas.")
        input('Presione cualquier tecla para continuar.')

def deleteTask():
    os.system('cls' if os.name == 'nt' else 'clear')

    if os.path.exists(desktop + "\Task List.json"):
        while(True):
            try:
                id = int(input('Ingresar ID de tarea a eliminar: '))
                break
            except ValueError:
                print("¡Ingresar un valor númerico!")

        with open(desktop + "\Task List.json", 'r') as f:
            data = json.load(f)
        
        tarea_encontrada = None
        for tarea in data:
            if tarea["id"] == id:
                tarea_encontrada = tarea
                taskList.remove(tarea_encontrada)
                break
            if not tarea_encontrada:
                print("No se encontró ninguna tarea con ese ID.")
                return

        with open(desktop + "\Task List.json", 'w') as f:
            json.dump(taskList, f, indent=4)

        print("\nTarea eliminada correctamente.")
        input('Presione cualquier tecla para continuar.')
    else:
        print("No se encuentran tareas registradas.")
        input('Presione cualquier tecla para continuar.')

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""" 
¡Bienvenido!
      
1) Crear una nueva tarea
2) Editar una tarea
3) Eliminar una tarea
""")

    while True:
        try:
            option = int(input('Ingresar una opción: '))
            match option:
                case 1 | 2 | 3 | 4:
                    break
                case _:
                    print("¡Ingresar una opción válida!")
        except ValueError:
            print("¡Ingresar una opción válida!")
    
    return option

# App

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    option = menu()
    match option:
        case 1:
            createTask()
        case 2:
            editTask()
        case 3:
            deleteTask()