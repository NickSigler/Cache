def mapeamento_associativo_conjunto(tamanho_conjunto, pos_memoria, dic):
    miss = 0
    hit = 0
    inicializar_conjunto(tamanho_conjunto, dic)

    for i in range(len(pos_memoria)):
   
        posicao_cache = pos_memoria[i] % tamanho_conjunto

        for chave in dic.keys():

            if chave == posicao_cache:
                lista2 = dic[chave]
                comparar = lista2[2]
                if comparar == pos_memoria[i]:
                    hit += 1
                else:
                    lista = dic[chave]
                    lista.remove(lista[2])
                    lista.insert(2, pos_memoria[i])
                    lista.remove(lista[1])
                    lista.insert(1, chave)
                    lista.remove(lista[0])
                    lista.insert(0, chave)
                    dic[chave] = lista
                    miss += 1
    i += 1