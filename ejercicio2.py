# Preguntar al usuario su nombre
nombreUsuario = input("¿Cuál es tu nombre? \n")

# Saludar por su nombre
saludo = f"Hola {nombreUsuario}"
print(saludo)

# Preguntar edad
edadUsuario = input("¿Cuantos años tienes? \n")
#Convertir edad en integer (número entero)
añoNacimiento = f"Tu año de nacimiento es {2020 - int(edadUsuario)}"

# devolver año de nacimiento
print(añoNacimiento)