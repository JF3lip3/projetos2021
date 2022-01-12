class arvore_binaria:
    def __init__(self, data = '*'):
        self.data = data
        self. left = None
        self.right = None
    
    def add(self, letra, codigo):
        if len(codigo) == 0:
            self.data = letra
        elif codigo == '.':
            if self.left is None:
                    self.left = arvore_binaria()
                    self.left.add(letra, '')
            else:
                self.left.add(letra, '')
        elif codigo == '-':
            if self.right is None:
                self.right = arvore_binaria()
                self.right.add(letra, '')
            else:
                self.right.add(letra, '')
        else:
            if codigo[0] == '.':
                if self.left is None:
                    self.left = arvore_binaria()
                    self.left.add(letra, codigo[1:])
                else:
                    self.left.add(letra, codigo[1:])
            elif codigo[0] == '-':
                if self.right is None:
                    self.right = arvore_binaria()
                    self.right.add(letra, codigo[1:])
                else:
                    self.right.add(letra, codigo[1:])
    
    def print_arvore(arvore):
        fila = []
        
        fila.append(arvore)

        while len(fila) > 0:
            print(fila[0].data + ' ', end = '')
            no = fila.pop(0)
            if no.left is not None:
                fila.append(no.left)
            if no.right is not None:
                fila.append(no.right)

arvore = arvore_binaria()
n = int(input())
codigos = []
for _ in range(n):
    letra, codigo = input().split()
    arvore.add(letra, codigo)
    codigos.append(letra)
    codigos.append(codigo)

n = int(input())

if n == 0:
    frase = input().split()
    traducao = ''
    n_possivel = False
    for i in frase:
        try:
            if i[0] == '/':
                traducao += ' ' + codigos[codigos.index(i[1:]) - 1]
            else:
                traducao += codigos[codigos.index(i) - 1]
        except:
            n_possivel = True
            break
    if n_possivel:
        print('Impossível decodificar a mensagem!')
    else:
        print(traducao)
        arvore_binaria.print_arvore(arvore)

elif n == 1:
    frase = input().split()
    traducao = []
    n_possivel = False
    for i in frase:
        try:
            palavra = ''
            for u in i:
                palavra += codigos[codigos.index(u) + 1] + ' '
            traducao.append(palavra)
        except:
            n_possivel = True
            break
    if n_possivel:
        print('Impossível codificar a mensagem!')
    else:
        print(*traducao, sep = '/')
        arvore_binaria.print_arvore(arvore)

#codigos = [letra, codigo, letra, codigo]