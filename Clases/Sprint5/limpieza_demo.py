nombre_sucio = "     ana    torres     "
email_sucio = "     ANA.Torres@inadaptados.MX"
area_sucia = "finanzas"
habilidades_raw = "Python, sql , Excel , power bi"

print(f"nombre original: [({nombre_sucio})]")
nombre = nombre_sucio.strip()
print(f"paso 1 strip: [({nombre})]")
demo=nombre.replace("    ", " ")
print(f"paso 2 replace: [({demo})]")

email = email_sucio.strip().lower()
print(f"email: [({email})]")

partes = habilidades_raw.split(",")
limpias = []
for h in partes:
    limpias.append(h.strip().lower())
    print(limpias)

habilidades = ",".join(limpias)
print(f"habilidades: [({habilidades})]")

print(habilidades)
