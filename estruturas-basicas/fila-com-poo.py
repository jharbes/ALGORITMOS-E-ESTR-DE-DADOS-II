class Fila:
    # método constrututor __init__
    # self paramentro de conversão, ou seja a instancia do metodo
    def __init__(self):
        self.fila=[]
    def inserir(self,n):
        self.fila.append(n)
    def tamanho(self):
        return len(self.fila)
    def vazia(self):
        return self.tamanho()==0
    def excluir(self):
        if not self.vazia():
            del self.fila[0]
        #del self.fila[0]
    def imprimi(self):
        for i in range(len(self.fila)):

            y=self.fila[i]
            print(y)


fila=Fila()
fila.inserir(1)
fila.inserir(2)
fila.inserir(3)
fila.inserir(4)
print(fila.tamanho())
fila.excluir()
print(fila.tamanho())
fila.imprimi()