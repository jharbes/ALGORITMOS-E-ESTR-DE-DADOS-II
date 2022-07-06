def soma(n):
    resultado = 0
    if n == 1:
        return 1
    else:
        resultado = n + soma(n - 1)

    return resultado


numero = int(input("Digite o valor de N:"))
print(soma(numero))