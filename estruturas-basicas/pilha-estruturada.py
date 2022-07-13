def pilhavazia(k):
    if len(k) ==0:
        print("Pilha vazia")
    else:
        print(k)

def inseri(p):
    for i in range(10):
        a=int(input("Digite um numero "+ str(i)+"..:"))
        p.append(a) #append inseri elemento na pilha

def lista():

    for i in range(10):
        print(stack,"topo= %d" %stack[len(stack)-1])

def remover():
    x=stack.pop() # remove elemento no topo da pilha
    print("Item removido do topo da Pilha %d" % x)
    print(stack)

stack=[]
pilhavazia(stack)
inseri(stack)
lista()
remover()