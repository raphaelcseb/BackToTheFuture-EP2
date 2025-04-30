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





