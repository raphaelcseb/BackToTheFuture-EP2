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
