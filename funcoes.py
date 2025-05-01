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

def crescente(dados,tamanho_da_sequencia):  #Transforma uma lista de dados em uma lista crescente, tirando as repetições
    
    #Função auxiliar necessária para o cálculo das sequências alta e baixa, com o tamanho sendo um argumento para que varie de acordo com cada sequência
    
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

def calcula_pontos_full_house (dados):
    
    numeros = {}

    for dado in dados:
        if dado not in numeros:
            numeros[dado] = 0
        numeros[dado] += 1
    
    #Ver se tem apenas dois números diferentes

    contador = 0
    for numero in numeros.keys():
        contador +=1

    if contador != 2:
        return 0
    
    total = 0
    for qtd in numeros.values():
        if qtd == 2 or qtd == 3:
            total +=1 
    
    soma = 0

    if total == 2:

        for dado in dados:
            soma += dado
    
    return soma

def calcula_pontos_quadra (dados):
    quadra = False

    numeros = {}

    for dado in dados:
        if dado not in numeros:
            numeros[dado] = 0
        numeros[dado] += 1
    
    for qtd in numeros.values():
        if qtd >= 4:
            quadra = True
    
    if quadra == True:
        soma = 0
        for dado in dados:
            soma += dado
        return soma
   
    else:
        return 0



    

