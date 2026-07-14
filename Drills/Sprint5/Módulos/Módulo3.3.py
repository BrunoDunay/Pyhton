# Caso 3: Limpiar Número de Teléfono

print("=== LIMPIEZA DE TELÉFONOS ===\n")

telefonos_test = [
  "555-123-4567",
  "(555) 123-4567",
  "555.123.4567",
  "5551234567",
  "+1 555 123 4567",
  "555-12-345"
]

# TODO 1: Define limpiar_telefono(telefono).
# Elimina los caracteres "-", "(", ")", ".", " ", "+" usando .replace().
# Retorna el string solo con dígitos.
def limpiar_telefono(telefono):
    telefono = telefono.replace("-", "")
    telefono = telefono.replace("(", "")
    telefono = telefono.replace(")", "")
    telefono = telefono.replace(".", "")
    telefono = telefono.replace(" ", "")
    telefono = telefono.replace("+", "")
    
    return telefono

# TODO 2: Define validar_telefono(telefono, longitud_esperada=10).
# Retorna True si el string solo tiene dígitos (.isdigit()) y su longitud
# es exactamente longitud_esperada. Retorna False en cualquier otro caso.
def validar_telefono(telefono, longitud_esperada=10):
    return telefono.isdigit() and len(telefono) == longitud_esperada

# TODO 3: Recorre telefonos_test.
# Para cada uno: limpia con limpiar_telefono(), valida con validar_telefono().
# Imprime con formato:
# "✅ VÁLIDO: '[sucio]' → '[limpio]' (N dígitos)"
# "❌ INVÁLIDO: '[sucio]' → '[limpio]' (N dígitos)"

for telefono_sucio in telefonos_test:
    telefono_limpio = limpiar_telefono(telefono_sucio)

    if validar_telefono(telefono_limpio):
        print(f"✅ VÁLIDO: '{telefono_sucio}' → '{telefono_limpio}' ({len(telefono_limpio)} dígitos)")
    else:
        print(f"❌ INVÁLIDO: '{telefono_sucio}' → '{telefono_limpio}' ({len(telefono_limpio)} dígitos)")

# TODO 4: Toma el string "5551234567" y formatealo como "(555) 123-4567"
# usando slicing y una f-string. Guarda en 'formato_bonito' e imprímelo.

telefono = "5551234567"

formato_bonito = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"

print(formato_bonito)