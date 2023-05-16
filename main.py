from multiprocessing.sharedctypes import Value
from operator import mod
from optparse import Values

#Posições atuais da memoria
posicoes_memoria_acessar = [33,3,11,5]
dic = {}

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
                
        
           
       
       
        
        
tamanho_cache = int(input("Informe o tamanho da cache"))
#inicializar_cache(tamanho_cache, dic)
#imprimir_cache(dic)

mapeamento_direto(tamanho_cache,posicoes_memoria_acessar,dic)

