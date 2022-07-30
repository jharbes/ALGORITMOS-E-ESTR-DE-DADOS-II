class Arvore:
    def __init__(self, data):
        self.data = data
        self.childs = []
    
    def add_childs(self, nos):
        for x in nos:
            self.childs.append(x)
    
    def __repr__(self) -> str:
        return str(self.data)

    def busca_largura(self):
        visitado, fila = [], []
        fila.append(self)
        visitado.append(self)
        
        while fila:
            aux = fila.pop(0)
            print(aux)
            for c in aux.childs:
                if c not in visitado:
                    fila.append(c)

class ArvoreBinaria:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, n): 
        if self.left == None:
            self.left = ArvoreBinaria(n)
        elif self.right == None:
            self.right = ArvoreBinaria(n)
        else:
            print('Nivel cheio')

    def busca_largura_binaria(self):
        visitado, fila = [], []
        fila.append(self)
        visitado.append(self)
        
        while fila:
            aux = fila.pop(0)
            print(aux)
            if aux.left and aux.left not in visitado:
                fila.append(aux.left)
            if aux.right and aux.right not in visitado:
                fila.append(aux.right)

    def __repr__(self) -> str:
        return str(self.data)

class NoRedBlack:
    def __init__(self, d) -> None:
        self.data = d
        self.right = None
        self.left = None
        self.pai = None
        self.cor = 'r'

class ArvoreRubroNegra:

    def __init__(self) -> None:
        self.vazio = NoRedBlack(0)
        self.vazio.color = 'b'
        self.vazio.left = None
        self.vazio.right = None

        self.root = self.vazio
    
    def __roda_direita(self, t):
        y = t.left
        t.left = y.right

        if y.right != self.vazio:
            y.right.pai = t

        y.pai = t.pai

        if t.pai == None:
            self.root = y
        elif t == t.pai.right:
            t.pai.right = y
        else:
            t.pai.left = y
        
        y.right = t
        t.pai = y
    
    def __roda_esquerda(self, t):
        y = t.right
        t.right = y.left

        if y.left != self.vazio:
            y.left.pai = t
        
        y.pai = t.pai

        if t.pai == None:
            self.root = y
        elif t == t.pai.left:
            t.pai.left = y
        else:
            t.pai.right = y
        
        y.left = t
        t.pai = y


    def __arruma_insercao(self, t):
        
        while t.pai.cor == 'r':
            if t.pai == t.pai.pai.right:
                u = t.pai.pai.left
                if u.cor == 'r':
                    u.cor = 'b'
                    t.pai.cor = 'b'
                    t.pai.pai.cor = 'r'
                    t = t.pai.pai
                else:
                    if t == t.pai.left:
                        t = t.pai
                        self.__roda_direita(t)
                    t.pai.cor = 'b'
                    t.pai.pai.cor = 'r'
                    self.__roda_esquerda(t.pai.pai)
            else:
                u = t.pai.pai.right
                if u.cor == 'r':
                    u.cor = 'b'
                    t.pai.cor = 'b'
                    t.pai.pai.cor = 'r'
                    t = t.pai.pai
                else:
                    if t == t.pai.right:
                        t = t.pai
                        self.__roda_esquerda(t)
                    t.pai.cor = 0
                    t.pai.pai.cor = 'r'
                    self.__roda_direita(t.pai.pai)

            if t == self.root:
                break
        self.root.cor = 'b'

    def insere(self, dado):
        no = NoRedBlack(dado)

        if self.root == None:
            self.root = no
            return
        
        prev = None
        aux = self.root

        while aux != self.vazio:
            if aux.data > dado:
                prev = aux
                aux = aux.left
            elif aux.data < dado:
                prev = aux
                aux = aux.right

        no.pai = prev

        if prev.data > dado:
            prev.left = no
        else:
            prev.right = no
        
        if no.pai == None:
            no.cor = 'b'
            return
        
        if no.pai.pai == None:
            return

        self.__arruma_insercao(no)

def _arvore_cheia(no : ArvoreBinaria):
    if no.right is None and no.left is None: # condicao de parada / caso a arvore tenha somente um no
        return True
    
    if no.right is not None and no.left is not None: # avanca ate que a arvore nao seja completa ou vazia
        return _arvore_cheia(no.right) and _arvore_cheia(no.left)
    
    return False

def verifica_arvore_cheia(no : ArvoreBinaria):
    if not _arvore_cheia(no):
        print('A arvore dada não é cheia')
        return
    print("A arvore dada é cheia")

def espelha_arvore(no : ArvoreBinaria):
    if no == None:
        return
    else:
        aux = no
        espelha_arvore(no.left)
        espelha_arvore(no.right)
        aux = no.left
        no.left = no.right
        no.right = aux

    return
