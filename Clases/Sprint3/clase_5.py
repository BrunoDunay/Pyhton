ultimo_folio_asignado=0
contador = 0

for folio in range(1,100):
    contador = contador + 1
    ultimo_folio_asignado = folio
    print(f"Último folio asignado: {ultimo_folio_asignado}")
print(f"Auditoría cerrada con {contador} folios procesados")

saldo_disponible = 1000
cargo_diario = 150
dias_transcurridos = 0

while saldo_disponible >= cargo_diario:
    saldo_disponible = saldo_disponible - cargo_diario
    dias_transcurridos = dias_transcurridos + 1
    print(f"Día {dias_transcurridos}: Saldo disponible: {saldo_disponible}")
print(f"Auditoría cerrada con {dias_transcurridos} días transcurridos")