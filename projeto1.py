print('=> restaurante aberto')
comando = ''
areas = {}
cardapio = {}
estoque = {}
pedidos = {}
pedidos_geral = []
while comando != '+ fechar restaurante':

    comando = input()

    if comando == '+ fechar restaurante':
        if pedidos_geral == []:
            print('- historico vazio')
        else:
            n = 1
            for i in pedidos_geral:
                print(f'{n}. {i}')
                n += 1

    elif comando == '+ atualizar mesas':
        arquivo = input()
        with open(arquivo) as f:
            sel = str(f.read())
            sel = sel.split('\n')
            for i in sel:
                i = i.split(', ')
                for u in areas:
                    if int(i[0]) in areas[u]:
                        del areas[u][int(i[0])]
                if i[1] in areas:
                    areas[i[1]][int(i[0])] = i[2]
                else:
                    areas[i[1]] = {int(i[0]) : i[2]}
    
    elif comando == '+ atualizar cardapio':
        arquivo = input()
        with open(arquivo) as f:
            card = str(f.read()).split('\n')
            #card.pop(0)
            for i in card:
                i = i.split(', ')
                comida = i[0]
                cardapio[comida] = {}
                i.pop(0)
                for u in i:
                    if u in cardapio[comida]:
                        cardapio[comida][u] += 1
                    else:
                        cardapio[comida][u] = 1
        try:
            del cardapio['']
        except:
            pass
    
    elif comando == '+ atualizar estoque':
        arquivo = input()
        with open(arquivo) as f:
            estq = str(f.read())
            estq = estq.split('\n')
            for i in estq:
                i = i.split(', ')
                if i[0] in estoque:
                    estoque[i[0]] += int(i[1])
                else:
                    estoque[i[0]] = int(i[1])

    elif comando == '+ relatorio mesas':
        cond = True
        for i in areas:
            if areas[i] == {}:
                continue
            else:
                cond = False

        if not cond:
            areas = dict(sorted(areas.items(), key=lambda item: item[0]))
            for i in areas:
                print(f'area: {i}')
                if areas[i] == {}:
                    print('- area sem mesas')
                else:
                    areas[i] = dict(sorted(areas[i].items(), key=lambda i : i[0]))
                    for u in areas[i]:
                        print(f'- mesa: {u}, status: {areas[i][u]}')
        else:
            print('- restaurante sem mesas')
    
    elif comando == '+ relatorio cardapio':
        #cardapio = {comida : {ingredientes : qtd}}
        if cardapio == {}:
            print('- cardapio vazio')
        else:
            cardapio = dict(sorted(cardapio.items(), key=lambda i : i[0]))
            for i in cardapio:
                print(f'item: {i}')
                cardapio[i] = dict(sorted(cardapio[i].items(), key=lambda i : i[0]))
                for u in cardapio[i]:
                    print(f'- {u}: {cardapio[i][u]}')
    
    elif comando == '+ relatorio estoque':
        if estoque == {}:
            print('- estoque vazio')
        else:
            estoque = dict(sorted(estoque.items(), key=lambda i : i[0]))
            for i in estoque:
                print(f'{i}: {estoque[i]}')

    elif comando == '+ fazer pedido':
        mesa, comida = map(str, input().split(', '))
        mesa = int(mesa)
        cond = True
        erros = []
        for i in areas:
            if mesa in areas[i]:
                cond = False
                x = i
                break
        cond2 = False        
        if cond:
            cond2 = True
            print(f'erro >> mesa {mesa} inexistente')
        elif areas[x][mesa] == 'livre':
            cond2 = True
            print(f'erro >> mesa {mesa} desocupada')
        elif comida not in cardapio:
            cond2 = True
            print(f'erro >> item {comida} nao existe no cardapio')
        elif comida in cardapio:
            ingredientes = cardapio[comida]
            araara = []
            dale = []
            for i in ingredientes:
                try:
                    if estoque[i] < ingredientes[i]:
                        cond2 = True
                        araara = []
                        print(f'erro >> ingredientes insuficientes para produzir o item {comida}')
                        break
                    elif estoque[i] == ingredientes[i]:
                        dale.append(estoque[i])
                    else:
                        #estoque[i] -= ingredientes[i]
                        araara.append((i, cardapio[comida][i]))
                except:
                    cond2 = True
                    print(f'erro >> ingredientes insuficientes para produzir o item {comida}')
                    break
        if not cond2:
            for i in araara:
                estoque[i[0]] -= i[1]
            for i in dale:
                del estoque[i]
            pedidos_geral.append(f'mesa {mesa} pediu {comida}')
            print(f'sucesso >> pedido realizado: item {comida} para mesa {mesa}')
            if mesa in pedidos:
                pedidos[mesa].append(comida)
            else:
                pedidos[mesa] = [comida]

    elif comando == '+ relatorio pedidos':
        if pedidos == {}:
            print('- nenhum pedido foi realizado')
        else:
            pedidos = dict(sorted(pedidos.items(), key=lambda item: item[0]))
            for mesa in pedidos:
                print(f'mesa: {mesa}')
                sort_pedidos = sorted(pedidos[mesa])
                for p in sort_pedidos:
                    print(f'- {p}')

    else:
        print('erro >> comando inexistente')

print('=> restaurante fechado')
        

# estoque = {ingrediente : qtd}
#cardapio = {comida : {ingredientes : qtd}}
#areas = {area : {mesa: ocupação}}