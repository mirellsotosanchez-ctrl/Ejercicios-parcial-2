 name = []
age = []
birthday = []
email = []
password = []
confirmPass = []
opcion = 0

while True:
    print("Bienvenido al sistema de registro de usuarios")
    print("---------MENÚ PRINCIPAL---------")
    print("1. Registrar usuario")
    print("2. Ver información del usuario")
    print("3. Borrar información del usuario")
    print ("4. Modificar información del usuario")
    print("5. Salir")
    print("---------------------------------")
    opcion = int(input("Selecciona una opción: "))

    match opcion:#aqui inicia la validcación del codigo
        case 1:
                name.append (input("Ingresa tu nombre: "))
                lastName.append (input("Ingresa tu apellido: ")
                age = int(input("Ingresa tu edad: "))
                birthday = input("Ingresa tu fecha de nacimiento: ")
                email = input("Ingresa tu correo electrónico: ")
                password = input("Ingresa tu contraseña: ")
                confirmPass = input("Confirma tu contraseña: ")

        case 2:
            print("Lista de usuarios registrados:")
            for i in range(len(name)):
               print("Id:-", i, " Con el nombre: ", name[i], " con el apellido: ", lastName[i], "Con la 
                     #i += 1
         case 3: 
            name = ""
            lastName = ""
            age= 0
            birthday = ""
            email = ""
            password = ""
        case 4: 
            name = input("ingresa tu nombre: ")
            lastName = input("ingresa tu apellido: ")
            age = int(input("ingresa tu edad: "))
            birthday = input("ingresa tu fecha de nacimiento")
            email = input("ingresa tu correo electronico: ")
        case 5: 
            print("Hasta luego!")
            break
        case _:
            print("opcion no valida")
