# Formulario de Registro - Sprint 5 Práctica

print("=== FORMULARIO DE REGISTRO DE RECLUTA ===\n")

datos_sucios = {
  "nombre": "  CARLOS   RUIZ  ",
  "email": "  CARLOS.RUIZ@EXAMPLE.COM  ",
  "telefono": "555-123-4567",
  "edad": "25",
  "ciudad": "madrid"
}

print("--- DATOS RECIBIDOS (SUCIOS) ---")
for campo, valor in datos_sucios.items():
  print(f"{campo}: '{valor}'")


# TODO 1: Crea un diccionario vacío 'datos_limpios' y limpia cada campo:
#   - nombre: .strip(), luego .split() y " ".join() para quitar espacios dobles,
#             luego .title()
#   - email: .strip().lower()
#   - telefono: elimina "-", "(", ")", ".", " " con .replace() (uno por uno)
#   - edad: .strip()
#   - ciudad: .strip().title()
# Imprime datos_limpios con el mismo formato de arriba.

datos_limpios = {}

nombre_limpio = datos_sucios["nombre"].strip()
nombre_limpio = " ".join(nombre_limpio.split())
nombre_limpio = nombre_limpio.title()

email_limpio = datos_sucios["email"].strip().lower()

telefono_limpio = datos_sucios["telefono"]
telefono_limpio = telefono_limpio.replace("-", "")
telefono_limpio = telefono_limpio.replace("(", "")
telefono_limpio = telefono_limpio.replace(")", "")
telefono_limpio = telefono_limpio.replace(".", "")
telefono_limpio = telefono_limpio.replace(" ", "")

edad_limpia = datos_sucios["edad"].strip()

ciudad_limpia = datos_sucios["ciudad"].strip().title()

datos_limpios["nombre"] = nombre_limpio
datos_limpios["email"] = email_limpio
datos_limpios["telefono"] = telefono_limpio
datos_limpios["edad"] = edad_limpia
datos_limpios["ciudad"] = ciudad_limpia

print("\n--- DATOS LIMPIOS ---")
for campo, valor in datos_limpios.items():
    print(f"{campo}: '{valor}'")


# TODO 2: Crea una lista vacía 'errores' y valida cada campo:
#   - nombre: len(datos_limpios["nombre"].split()) < 2 → error "Nombre debe incluir apellido"
#   - email: debe contener "@" y "." en el dominio → error si no
#   - telefono: .isdigit() y len() == 10 → error si no
#   - edad: .isdigit() → si pasa, convierte a int y verifica 18 <= edad <= 100
# Por cada campo que pase, imprime "✅ [campo] válido".
# Por cada campo que no pase, agrega el mensaje de error a 'errores'.

errores = []

if len(datos_limpios["nombre"].split()) < 2:
    errores.append("Nombre debe incluir apellido")
else:
    print("✅ nombre válido")

if "@" in datos_limpios["email"] and "." in datos_limpios["email"].split("@")[1]:
    print("✅ email válido")
else:
    errores.append("Email inválido")

if datos_limpios["telefono"].isdigit() and len(datos_limpios["telefono"]) == 10:
    print("✅ telefono válido")
else:
    errores.append("Teléfono inválido")

if datos_limpios["edad"].isdigit():
    edad = int(datos_limpios["edad"])
    if 18 <= edad <= 100:
        print("✅ edad válida")
    else:
        errores.append("Edad fuera de rango")
else:
    errores.append("Edad inválida")


# TODO 3: Si 'errores' está vacío, imprime "--- REGISTRO EXITOSO ---"
# y muestra cada campo (nombre a la izquierda en 15 chars, valor en 30 chars).
# Formatea también el teléfono como "(555) 123-4567" usando slicing.
# Si hay errores, imprime "--- REGISTRO RECHAZADO ---" y lista cada error.

if len(errores) == 0:
    print("\n--- REGISTRO EXITOSO ---")

    telefono_formateado = f"({datos_limpios['telefono'][:3]}) {datos_limpios['telefono'][3:6]}-{datos_limpios['telefono'][6:]}"

    for campo, valor in datos_limpios.items():
        if campo == "telefono":
            valor = telefono_formateado

        print(f"{campo:<15}{valor:<30}")

else:
    print("\n--- REGISTRO RECHAZADO ---")
    for error in errores:
        print(f"- {error}")