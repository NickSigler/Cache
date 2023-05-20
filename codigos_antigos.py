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

#tentativa falha em reproduzir o mapeamento associativo

def mapeamento_associativo_conjunto(dic):
    hit = 0
    miss = 0
    for i in range(len(pos_memoria)):

        posicao_conjunto = pos_memoria[i] % num_blocos

        for j in range(2):
            dic2 = dic[j]

            #acessando bloco por bloco
            for chave in dic2.keys():

                dic3 = dic2[chave]
                lista = dic3[3]
                #adicionar if para  ver se tem RLU
                if dic3[1] != -1:

                    dic3.remove(dic3[0])
                    dic3.insert(0, "LRU")
                    dic2[chave] = dic3

                    #adicionando no outro bloco do conjunto
                    # virou lista dic3

                    #Erro encontrado, quando está fazendo a verificação do conjunto 2, o j está valendo 1, sendo isso, a soma aqui em baixo 2,
                    lista1 = dic2[j+1]
                    lista1.remove(lista1[3])
                    lista1.insert(3, pos_memoria[i])
                    lista1.remove(lista1[2])
                    lista1.insert(2, chave)
                    #lista1.remove(lista1[1])
                    #lista1.insert(1, chave)


                else:
                    if chave == posicao_conjunto:

                        #Erro encontrado, ta dando hit
                        if lista == pos_memoria[i]:
                            hit += 1
                        else :
                            dic2 = dic[j]
                            dic2 = dic[j]
                            # virou lista dic3
                            lista1 = dic2[j]
                            lista1.remove(lista1[3])
                            lista1.insert(3, pos_memoria[i])
                            lista1.remove(lista1[2])
                            lista1.insert(2, chave)
                            lista1.remove(lista1[1])
                            lista1.insert(1, chave)


    print(dic)



num_conjuntos = int(input("Informe o número de conjuntos da cache: "))
num_blocos = int(input("Informe o número de blocos por conjunto: "))

cache = criar_cache_conjunto_associativo(num_conjuntos, num_blocos,dic)
mapeamento_associativo_conjunto(dic)


          
                        for chave2 in filtro1.keys():

                            if (-1 in filtro1[chave2]) == True:
                                 





                                 