class Fila:
    # método constrututor __init__
    # self paramentro de conversão, ou seja a instancia do metodo
    def __init__(self): # letra (A)
        self.fila=[]
    def primeiroElemento(self): # letra (B)
        if len(self.fila)!=0:
            print("PRIMEIRO ELEMENTO = ",self.fila[0])
        else:
            print("FILA VAZIA")
    def inserir(self,n): # letra (D)
        self.fila.append(n)
        print("ELEMENTO INSERIDO = ",n)
    def tamanho(self):
        print("TAMANHO DA FILA = ",len(self.fila))
    def vazia(self): # letra (C)
        if len(self.fila)!=0:
            print("FILA NAO VAZIA")
        else:
            print("FILA VAZIA")
    def excluir(self): # letra (E)
        if len(self.fila)!=0:
            del self.fila[0]
        else:
            print("FILA VAZIA")
    def imprimir(self):
        print("FILA = ", end=" ")
        for i in range(len(self.fila)):
            y=self.fila[i]
            print(y,end=" ")
        print("")
    def destruir(self):
        self.fila=[]

fila=Fila()
fila.inserir(1)
fila.inserir(2)
fila.inserir(3)
fila.inserir(4)
fila.destruir()
fila.vazia()
fila.primeiroElemento()
fila.imprimir()
fila.tamanho()
fila.excluir()
fila.tamanho()
fila.imprimir()