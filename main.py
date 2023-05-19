from multiprocessing.sharedctypes import Value
from operator import mod
from optparse import Values

#Posições atuais da memoria
posicoes_memoria_acessar = [33,3,11,5]
dic = {}
dic_associativo = {}      





def inicializar_cache(tamanho_cache,dic):
    for i in range(tamanho_cache):
        dic[i] = -1
        print("{} {}".format(i,dic[i]))
        


def imprimir_cache(cache):
    
    #Informar o tamanho atual da cache
    print("O tamanho da cache é {}".format(len(cache)))
    
    #Informar tabela
    for chave in cache.keys():
        print("{} {}".format(chave,cache[chave]))
    
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
                if dic[chave] == posicao_cache:
                    hit += 1
                else:
                    miss += 1
                    
                
                dic[chave] = pos_memoria[i]
                
    print("Deram {} miss e {} hits".format(miss, hit)) 
               
    imprimir_cache(dic)
                
              
  
def inicializar_conjunto(tamanho_conjunto, dic_associativo):
    for i in range(tamanho_conjunto):
        dic_associativo[i] = [0,0,-1]
        print("{} {}".format(i,dic_associativo[i]))


def imprimir_conjunto(conjunto):
    
    #Informar o tamanho atual da cache
    print("O tamanho da cache é {}".format(len(conjunto)))
    
    #Informar tabela
    for chave in conjunto.keys():
        print("{} {}".format(chave,conjunto[chave]))


def mapeamento_associativo_conjunto(tamanho_conjunto, pos_memoria, dic_associativo):
    miss = 0
    hit = 0
    i = 0
    inicializar_conjunto(tamanho_conjunto, dic_associativo)
    
               
    imprimir_conjunto(dic_associativo)

       
       
        
tamanho_conjunto = int(input("Informe quantos blocos: "))       
#tamanho_cache = int(input("Informe o tamanho do conjunto: "))

#inicializar_cache(tamanho_cache, dic)
#imprimir_cache(dic)
mapeamento_associativo_conjunto(tamanho_conjunto, posicoes_memoria_acessar, dic_associativo)




