from operator import itemgetter
mesas = {}
cardapio = {}
estoque = {}
r_pedidos = {}
pedidos_geral = []

def atualizar_mesas(arquivo, dic):
    #mesas = {area : [(mesa, ocupação)]}
    with open(arquivo) as p:
        p = str(p.read()).split('\n')
        for i in p:
            i = i.split(', ')
            if i[1] in dic:
                si = False
                for u in dic:
                    for p in dic[u]:
                        if p[0] == int(i[0]):
                            dic[u].remove((int(i[0]), p[1]))
                            dic[i[1]].append((int(i[0]), i[2]))
                            si = True
                if not si:
                    dic[i[1]].append((int(i[0]), i[2]))
            else:
                si = False
                dic[i[1]] = []
                for u in dic:
                    for p in dic[u]:
                        if p[0] == int(i[0]):
                            dic[u].remove((int(i[0]), p[1]))
                            dic[i[1]].append((int(i[0]), i[2]))
                            si = True
                if not si:
                    dic[i[1]].append((int(i[0]), i[2]))

def atualizar_cardapio(arquivo, dic):
    #cardapio = {comida : [[ingredientes, qtd]]}
    with open(arquivo) as p:
        p = str(p.read()).split('\n')
        for i in p:
            i = i.split(', ')
            if i[0] in dic:
                del dic[i[0]]
                dic[i[0]] = []
                comida = i[0]
                i.remove(comida)
                for u in i:
                    si = False
                    for n in dic[comida]:
                        if u in n:
                            n[1] += 1
                            si = True
                    if not si:
                        dic[comida].append([u, 1])
            else:
                dic[i[0]] = []
                comida = i[0]
                i.remove(comida)
                for u in i:
                    si = False
                    for n in dic[comida]:
                        if u in n:
                            n[1] += 1
                            si = True
                    if not si:
                        dic[comida].append([u, 1])
        try:
            del cardapio['']
        except:
            pass

def atualizar_estoque(arquivo, dic):
    # estoque = {ingrediente : qtd}
    with open(arquivo) as p:
        p = str(p.read()).split('\n')
        for i in p:
            i = i.split(', ')
            if i[0] in dic:
                dic[i[0]] += int(i[1])
            else:
                dic[i[0]] = int(i[1])

def relatorio_mesas(dic):
    #mesas = {area : [(mesa, ocupação)]]}
    if dic == {}:
        print('- restaurante sem mesas')
    else:
        dic = dict(sorted(dic.items(), key=lambda item: item[0]))
        for i in dic:
            print(f'area: {i}')
            if dic[i] == []:
                print('- area sem mesas')
            else:
                f = sorted(dic[i], key = lambda x:x[0])
                for u in f:
                    print(f'- mesa: {u[0]}, status: {u[1]}')

def relatorio_cardapio(dic):
    #cardapio = {comida : [[ingredientes, qtd]]}
    if dic == {}:
        print('- cardapio vazio')
    else:
        dic = dict(sorted(dic.items(), key=lambda item: item[0]))
        for i in dic:
            print(f'item: {i}')
            f = sorted(dic[i], key = itemgetter(0))
            for u in f:
                print(f'- {u[0]}: {u[1]}')

def relatorio_estoque(dic):
    #estoque = {ingrediente : qtd}
    if estoque == {}:
        print('- estoque vazio')
    else:
        dic = dict(sorted(dic.items(), key=lambda item: item[0]))
        for i in dic:
            print(f'{i}: {dic[i]}')

def fazer_pedido(mesa, pedido):
    si = False
    for i in mesas:
        si = False
        for u in mesas[i]:
            if u[0] == mesa:
                si = True
                ar = i
                break
        if si:
            break
    if not si:
        print(f'erro >> mesa {mesa} inexistente')
    else:
        si = False
        for i in mesas[ar]:
            if i[0] == mesa:
                if i[1] == 'livre':
                    si = True
                    break
        if si:
            print(f'erro >> mesa {mesa} desocupada')
        else:
            if pedido not in cardapio:
                print(f'erro >> item {pedido} nao existe no cardapio')
            else:
                subtrai = []
                deleta = []
                si = False
                #estoque = {ingrediente : qtd}
                for i in cardapio[pedido]:
                    try:
                        if int(i[1]) > int(estoque[i[0]]):
                            si = True
                            break
                        elif i[1] == estoque[i[0]]:
                            deleta.append(i[0])
                        else:
                            #cardapio = {comida : [[ingredientes, qtd]]}
                            subtrai.append((i[0], i[1]))
                    except:
                        si = True
                if si:
                    print(f'erro >> ingredientes insuficientes para produzir o item {pedido}')
                else:
                    for i in subtrai:
                        estoque[i[0]] -= i[1]
                    for i in deleta:
                        del estoque[i]
                    if mesa in r_pedidos:
                        r_pedidos[mesa].append(pedido)
                        pedidos_geral.append((mesa, pedido))
                    else:
                        r_pedidos[int(mesa)] = [pedido]
                        pedidos_geral.append((mesa, pedido))
                    print(f'sucesso >> pedido realizado: item {pedido} para mesa {mesa}')

def relatorio_pedidos(dic):
    #r_pedidos[int(mesa)] = [pedido]
    if dic == {}:
        print('- nenhum pedido foi realizado')
    else:
        dic = dict(sorted(dic.items(), key=lambda item: item[0]))
        for i in dic:
            print(f'mesa: {i}')
            f = sorted(dic[i])
            for u in f:
                print(f'- {u}')


#estoque = {ingrediente : qtd}
#cardapio = {comida : [[ingredientes, qtd]]}
#mesas = {area : [(mesa, ocupação)]



print('=> restaurante aberto')

comando = input()

while comando != '+ fechar restaurante':
    if comando == '+ atualizar mesas':
        arquivo = input()
        atualizar_mesas(arquivo, mesas)
    
    elif comando == '+ atualizar cardapio':
        arquivo = input()
        atualizar_cardapio(arquivo, cardapio)
    
    elif comando == '+ atualizar estoque':
        arquivo = input()
        atualizar_estoque(arquivo, estoque)
    
    elif comando == '+ relatorio mesas':
        relatorio_mesas(mesas)
    
    elif comando == '+ relatorio cardapio':
        relatorio_cardapio(cardapio)
    
    elif comando == '+ relatorio estoque':
        relatorio_estoque(estoque)

    elif comando == '+ fazer pedido':
        mesa, pedido = map(str, input().split(', '))
        fazer_pedido(int(mesa), pedido)
    
    elif comando == '+ relatorio pedidos':
        relatorio_pedidos(r_pedidos)
    
    else:
        print('erro >> comando inexistente')

    comando = input()

n = 1
if pedidos_geral == []:
    print('- historico vazio')
else:
    for i in pedidos_geral:
        print(f'{n}. mesa {i[0]} pediu {i[1]}')
        n += 1

print('=> restaurante fechado')

#estoque = {ingrediente : qtd}
#cardapio = {comida : [[ingredientes, qtd]]}
#mesas = {area : [(mesa, ocupação)]]}