from multiprocessing.sharedctypes import Value
from optparse import Values

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
    
def mapeamento_direto(tamanho_cache, pos_memoria):
    
    #Posições atuais da memoria
    
    
           
       
       
        
        
tamanho_cache = int(input("Informe o tamanho da cache"))
inicializar_cache(tamanho_cache, dic)
imprimir_cache(dic)

