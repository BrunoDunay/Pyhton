# Limpiador de Datos de Usuario

print("=== SISTEMA DE LIMPIEZA DE DATOS ===\n")


# TODO 1: Crea 4 variables con datos "sucios" tal como llegarían de un
# formulario (con espacios sobrantes, mayúsculas o guiones):
#   nombre_sucio, email_sucio, telefono_sucio, mensaje_sucio.
# Imprime "--- DATOS ORIGINALES ---" y muéstralas entre comillas.

nombre_sucio = "   bruno acevedo   "
email_sucio = "   BRUNO@GMAIL.COM   "
telefono_sucio = "449-123-4567"
mensaje_sucio = "   hola, necesito información sobre el curso.   "

print("--- DATOS ORIGINALES ---")
print(f'"{nombre_sucio}"')
print(f'"{email_sucio}"')
print(f'"{telefono_sucio}"')
print(f'"{mensaje_sucio}"')


# TODO 2: Limpia cada dato y guárdalo en una variable nueva:
#   - nombre:   .strip().title()
#   - email:    .strip().lower()
#   - telefono: .replace("-", "")
#   - mensaje:  .strip().capitalize()
# Imprime "--- DATOS LIMPIOS ---" y muestra los resultados.

nombre = nombre_sucio.strip().title()
email = email_sucio.strip().lower()
telefono = telefono_sucio.replace("-", "")
mensaje = mensaje_sucio.strip().capitalize()

print("\n--- DATOS LIMPIOS ---")
print(nombre)
print(email)
print(telefono)
print(mensaje)


# TODO 3: Imprime "--- VALIDACIONES ---".
# Valida el email: comprueba que contiene "@" (con 'in') y que
# termina en ".com" (con .endswith()). Imprime ✅ o ❌.

print("\n--- VALIDACIONES ---")
if "@" in email and email.endswith(".com"):
    print("Email: ✅")
else:
    print("Email: ❌")


# TODO 4: Valida el teléfono: debe tener 10 caracteres (len()) y ser
# todo dígitos (.isdigit()). Imprime ✅ o ❌.

if len(telefono) == 10 and telefono.isdigit():
    print("Teléfono: ✅")
else:
    print("Teléfono: ❌")


# TODO 5: Divide el mensaje en palabras con .split() e imprime cuántas
# palabras tiene usando len().

palabras = mensaje.split()
print(f"El mensaje tiene {len(palabras)} palabras.")


# TODO 6: Separa el nombre completo con .split(). Si tiene 2 o más partes,
# toma la primera como primer_nombre y une el resto con " ".join() como
# apellido. Imprime ambos.

partes_nombre = nombre.split()

if len(partes_nombre) >= 2:
    primer_nombre = partes_nombre[0]
    apellido = " ".join(partes_nombre[1:])
    print(f"Primer nombre: {primer_nombre}")
    print(f"Apellido: {apellido}")


# TODO 7: Genera un username con email_limpio.split("@")[0] e imprímelo.

username = email.split("@")[0]
print(f"Username: {username}")