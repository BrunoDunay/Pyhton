usuario = input("Ingresa tu nombre de usuario: ").lower()
contraseña = input("Ingresa tu contraseña: ")
ip_origen = input("Ingresa tu dirección IP de origen: ")

if usuario == "superadmin":
    red_corporativa = ip_origen.startswith("192.168.")
    if contraseña == "@superadmin123" and red_corporativa:
        print("ACCESO TOTAL - superadmin: Todos los modulos habilitados.")
        print(f"Sesion iniciada desde red corporativa: {red_corporativa}")
    elif contraseña != "@superadmin123":
        print("ACCESO DENEGADO: acceso remoto no permitido para este rol. Contraseña incorrecta")
    else: 
        print("ACCESO DENEGADO: acceso remoto no permitido para este rol.")
elif usuario == "admin":
    if contraseña == "@admin123":
        print("ACCESO CONCEDIDO - admin: Modulo de gestión de usuarios habilitado.")
    else:
        print("ACCESO DENEGADO: Contraseña incorrecta para admin.")
elif usuario == "operador":
    if contraseña == "@operador123":
        print("ACCESO CONCEDIDO - operador: Acceso limitado a funciones básicas.")
    else:
        print("ACCESO DENEGADO: Contraseña incorrecta para operador.")
else: 
    print(f"ACCESO DENEGADO: Usuario '{usuario}' no reconocido.")
    print("Contacte con el administrador")