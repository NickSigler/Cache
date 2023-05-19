pos_memoria= [33,3,11,5,33]
dic = {}
def criar_cache_conjunto_associativo(num_conjuntos, num_blocos,dic):

    for i in range(num_conjuntos):
        conjunto = {}
        for j in range(num_blocos):
            nome_bloco = j
            conjunto[nome_bloco] = [-1, 1, -1, 2]
        nome_conjunto = i
        dic[nome_conjunto] = conjunto
    print(dic)


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