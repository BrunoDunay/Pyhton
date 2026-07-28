# DRILL 3: BUSCAR Y REEMPLAZAR — EL CAMBIO DE NOMBRE DE DANIELA

# TODO 1: Crear la variable con el comunicado
comunicado = (
    "El Escenario Secundario abre a las 18h. "
    "Los artistas del Escenario Secundario deben presentarse 30 minutos antes."
)

# TODO 2: Reemplazar "Escenario Secundario" por "Escenario Granado"
comunicado_actualizado = comunicado.replace(
    "Escenario Secundario",
    "Escenario Granado"
)

# TODO 3: Imprimir ambas versiones
print("Comunicado original:")
print(comunicado)

print("\nComunicado actualizado:")
print(comunicado_actualizado)

# TODO 4: Intentar reemplazar una palabra que no existe
resultado = comunicado.replace("Coachella", "SonidoLibre")

print("\nIntento de reemplazar una palabra que no existe:")
print(resultado)