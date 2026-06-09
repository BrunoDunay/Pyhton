# EL DETECTOR VIP

# TODO 1: Crea una variable 'nombre' (tipo str) con el nombre de tu invitado.
nombre = "Carlos"

# TODO 2: Crea una variable 'edad' (tipo int) que sea mayor a 18.
edad = 25

# TODO 3: Crea una variable 'dinero' (tipo float) que tenga decimales, ej. 500.50.
dinero = 500.50

# TODO 4: Crea una variable 'en_lista' (tipo bool) y asígnale True.
en_lista = True

# TODO 5: Crea una variable llamada 'puede_entrar'.
# Asígnale una evaluación lógica que verifique si la edad es mayor o igual a 18
# AND (y) si el dinero es mayor a 100 AND (y) si está en_lista.
puede_entrar = edad >= 18 and dinero > 100 and en_lista

# TODO 6: Usa print() con una f-string para anunciar el resultado:
# "El acceso de [nombre] es: [puede_entrar]"
print(f"El acceso de {nombre} es: {puede_entrar}")