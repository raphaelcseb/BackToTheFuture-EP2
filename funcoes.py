def rolar_dados (n):
    import random
    dados = []
    for i in range(0,n):
        dado = random.randint(1,6)
        dados.append(dado)
    return dados

