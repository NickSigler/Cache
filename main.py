from multiprocessing.sharedctypes import Value
from operator import mod
from optparse import Values

#Posições atuais da memoria
posicoes_memoria_acessar = [66,69,20,12,10,4]
dic = {}
dic_associativo = {}      





def inicializar_cache(tamanho_cache,dic):
    print ("---Cache no estado inicial---\n"
           "Pos. da cache|Posi. Memória")
    
    #Informar o tamanho atual da cache
    print("Tamanho da Cache: {}".format(tamanho_cache))
    for i in range(tamanho_cache):
        dic[i] = -1
        print("         \033[7;37;40m| {} | {} |\033[m\n".format(i,dic[i]))
        


def imprimir_cache(cache):


    #Informar tabela
    for chave in cache.keys():
        print("         \033[7;37;40m| {} | {} |\033[m\n".format(chave,cache[chave]))
     
    

def mapeamento_direto(tamanho_cache, pos_memoria, dic):
    miss = 0
    hit = 0
    inicializar_cache(tamanho_cache, dic)
    
    #Acessando cada elemento da lista e usando-o na conta
    for i in range(len(pos_memoria)):
        posicao_cache = pos_memoria[i] % tamanho_cache
        #Acessando cada chave do dicionario e comparando se ele já existe,
        #caso exista, ele vai mudar a posição do valor dessa chave para o
        #da lista
        for chave in dic.keys():
            if chave == posicao_cache:
                status = 0
                if dic[chave] == posicao_cache:
                    hit += 1
                    status = "hit"
                else:
                    miss += 1
                    status = "miss"
                    
                
                dic[chave] = pos_memoria[i]
                print("=========================")
                print("Linha: {} | Posição da memória: {}\n"
                      "Status: {}".format(i,pos_memoria[i],status))
                imprimir_cache(dic)
                
     
    print("---Cache no estado final---\n"
          "Pos. da cache|Posi. Memória")     
    imprimir_cache(dic)
    print("Memórias acessadas: {}".format(len(posicoes_memoria_acessar)))
    print("Quantidade de Miss: {}\nQuantidade de Hits: {}".format(miss, hit))
    print("Taxa de acertos: {}%".format((hit/(miss+hit))*100))         
              
  
def inicializar_conjunto(num_conjuntos, num_blocos, dic_associativo):
    dic_associativo = {}
    for i in range(num_conjuntos):
        conjunto = {}
        for j in range(num_blocos):
            nome_bloco = j
            conjunto[nome_bloco] = [0, 0, 0, 0]
        nome_conjunto = i
        dic_associativo[nome_conjunto] = conjunto
        print(dic_associativo)


def imprimir_conjunto(conjunto):
    
    #Informar o tamanho atual da cache
    print("Tamanho da Cache: {}".format(len(conjunto)))
    
    #Informar tabela
    for chave in conjunto.keys():
        print("|{} | {}|".format(chave,conjunto[chave]))


def criar_cache_conjunto_associativo(num_conjuntos, num_blocos):
    inicializar_cache(num_conjuntos,num_blocos)


    imprimir_conjunto(cache)




#num_conjuntos = int(input("Informe o número de conjuntos da cache: "))
#num_blocos = int(input("Informe o número de blocos por conjunto: "))

#inicializar_conjunto(num_conjuntos, num_blocos, dic_associativo)

       
        
#tamanho_conjunto = int(input("Informe quantos blocos: "))       
tamanho_cache = int(input("Informe o tamanho da cache: "))

#inicializar_cache(tamanho_cache, dic)
#imprimir_cache(dic)


mapeamento_direto(tamanho_cache, posicoes_memoria_acessar, dic)

