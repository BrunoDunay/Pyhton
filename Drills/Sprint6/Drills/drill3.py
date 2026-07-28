# DRILL 3: LA VALIDACIÓN DE CREDENCIALES DE REGINA

# TODO 1
def tiene_acceso_backstage(tipo_credencial):
    return tipo_credencial == "staff" or tipo_credencial == "artista"

# TODO 2
print(tiene_acceso_backstage("artista"))

# TODO 3
print(tiene_acceso_backstage("prensa"))

# TODO 4
tipo = "staff"

if tiene_acceso_backstage(tipo):
    print("Acceso permitido a backstage")
else:
    print("Acceso denegado")