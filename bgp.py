# bgp_as_checker_nombre.py

as_list = {
    "Marco": 15169,
    "Javier": 75303,
    "Jean": 32934,
    "Alejandro": 74783
}

def tipo_as(numero):
    if 64512 <= numero <= 75534:
        return "AS privado"
    elif 1 <= numero <= 4294967295:
        return "AS público"
    else:
        return "Número inválido"

while True:
    nombre = input("Ingrese el nombre (o escriba 'salir' para terminar): ").strip().capitalize()

    if nombre.lower() == "salir":
        print("Programa finalizado.")
        break

    if nombre in as_list:
        asn = as_list[nombre]
        print(f"{nombre} tiene asignado el AS número {asn}, que corresponde a un {tipo_as(asn)}.\n")
    else:
        print("Nombre no encontrado. Intente con otro.\n")
