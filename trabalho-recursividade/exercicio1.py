def inverter(lista):
    if not lista:
        return lista
    return lista[-1:] + inverter(lista[:-1])

lista = inverter([1, 2, 3, 4, 5])
print(lista)