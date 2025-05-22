# def mi_decorador(funcion_original):
#     def funcion_envoltorio():
#         print("Me ejecuto antes de la funcion ogirinal")
#         resultado = funcion_original()
#         print("Me ejecute despues de la función original")
#     return funcion_envoltorio


# @mi_decorador
# def saludar():
#     print("Hola ¿qué tal?")

# saludar()  




person = {
        "id":2,
        "name":"Antonio Capra",
        "age": 21
    }

person.update({"email":"deimian@gmail.com"})

print(person)