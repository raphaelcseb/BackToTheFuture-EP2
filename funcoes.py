def rolar_dados (n):

    import random

    dados = []

    for i in range(0,n):

        dado = random.randint(1,6)

        dados.append(dado)

    return dados


def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
   
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
   
    del(dados_rolados[dado_para_guardar])
    
    return [dados_rolados,dados_no_estoque]


def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):

    dados_rolados.append(dados_no_estoque[dado_para_remover])
   
    del(dados_no_estoque[dado_para_remover])
    
    return [dados_rolados,dados_no_estoque]


def calcula_pontos_regra_simples (lista):
   
    dic = {1:0,2:0,3:0,4:0,5:0,6:0}
   
    for dado in lista:
       
        dic[dado] += dado
   
    return dic

def calcula_pontos_soma (dados):

    soma = 0

    for dado in dados:

        soma += dado

    return soma

def crescente(dados,tamanho_da_sequencia):
    
    crescente = []

    while len(crescente) < tamanho_da_sequencia:

        menor = 7

        for dado in dados:
            if dado < menor:
                menor = dado
            
        crescente.append(menor)

        dados_novo = []

        for dado in dados:
            if dado != menor:
                dados_novo.append(dado)
        
        dados = dados_novo
    
    return crescente

def calcula_pontos_sequencia_baixa (dados):

    if crescente(dados,4) == [1,2,3,4] or crescente(dados,4) == [2,3,4,5] or crescente(dados,4) == [3,4,5,6]:

        return 15
    
    else:

        return 0

def calcula_pontos_sequencia_alta (dados):

    if crescente(dados,5) == [1,2,3,4,5] or crescente(dados,5) == [2,3,4,5,6]:
        
        return 30
    
    else:

        return 0

