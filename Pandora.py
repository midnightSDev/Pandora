
from os import system, name 

def main():
    #Limpiamos la pantalla al inicio de la aplicación
    clear()

    print("Bienvenido a PANDORA by MidnightSDev")
    print()
    print("OPCIONES DISPONIBLES")
    print()
    menu = construyeMenu()    
    for m in menu:
        print(m)

    print()
    accion = int(input("Introduce la opción deseada: "))
    controllerPandora(accion)

def controllerPandora(accion):
    clear()

    menu = construyeMenu()
    accionSelecionada = ""

    #Selecciona opción para la gestión de passwords
    if accion == 1:
        accionSelecionada = menu[0]
        submenu = construyeSubMenuContrasenia()
        
        print("OPCIONES DISPONIBLES")
        print()

        for s in submenu:
            print(s)
        
        print()
        accion=int(input("Introduce la opción seleccionada: "))
        print("La acción seleccionada ha sido {}".format({accion}))

    #Selecciona opción para la gestión de notas seguras
    elif accion == 2:
        accionSelecionada = menu[1]

    #Si la opción seleccionada no es válida se da la posibildiad de volver a intentarlo
    else: 
        clear()
        accionSelecionada = "Acción seleccionada no correcta"
        menu = construyeMenu()    
        for m in menu:
            print(m)
        
        print()
        accion=int(input("Introduce la opción correcta: "))

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def construyeMenu():
    menuOpciones = ["1.Contraseñas", "2.Notas Seguras"]
    return menuOpciones

def construyeSubMenuContrasenia():
    menuContrasenia = ["1.Ver Contraseñas", "2.Crear Contraseña", "3.Buscar Contraseña", "4.Modificar Contraseña", "5.Borrar Contraseña"]
    return menuContrasenia

if __name__ == "__main__":main()