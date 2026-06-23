tickets = ["TKT-001: red caída en el piso 3",
           "TKT-002: impresora sin toner",
           "TKT-003: usuario sin acceso al CRM",
           "TKT-004: solicitud de licencia"]


print("======================== IMPRIMIR CADA TICKET ====================")
for ticket in tickets:
  print(ticket)

tickets.append("TKT-005: VPN Intermitente")

resultado = tickets.append("TKT-006: backup falló")

print("======================== IMPRIMIR ÚLTIMO TICKET INSERTADO ====================")
print(tickets[-1])
print(f"Índice máximo válido: {len(tickets)}")

tickets.insert(0,"TKT-URGENT: caída del ERP")

print("======================== IMPRIMIR ARRAY DE TICKETS ====================")
print(tickets)

print("======================== IMPRIMIR METODO POP DEFAULT ====================")
ultimo_cerrado = tickets.pop()
print("Lista actualizada: ",ultimo_cerrado)
print(f"Lista actualizada: {ultimo_cerrado}")

print("======================== IMPRIMIR METODO POP CON INDEX ====================")
cerrado_especifico = tickets.pop(0)
print("Ticket cerrado en posición 0: ", cerrado_especifico)

if "TKT-003: usuario sin acceso al CRM" in tickets:
  print("Encontrado, se elimina el ticket.")
  tickets.remove("TKT-003: usuario sin acceso al CRM")
else:
  print("El ticket no existe")

print("======================== IMPRIMIR ARRAY FINAL ====================")
print("Lista Actualizada: ", tickets)

# print(tickets[0:3]) # Inicio = a la posición 2
# print(tickets[1:3]) # Posición 1 = Posición 2
# print(tickets[2:]) # Sin fin = hasta el final
# print(tickets[:2]) # Sin inicio = desde el inicio
# print(tickets[-2:]) # Los últimos dos

