from funcoes import *

possiveis = ['sem_combinacao','quadra','full_house','sequencia_baixa','sequencia_alta','cinco_iguais','1','2','3','4','5','6']

cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

rodada = 0

combinacoes = []

imprime_cartela(cartela)

while rodada < 12:

    dados_no_estoque = []
    
    dados = rolar_dados(5-len(dados_no_estoque))

    print('Dados rolados: {0}'.format(dados))

    print('Dados guardados: {0}'.format(dados_no_estoque))

    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    
    rerrolar = 0
    
    opcao = input('>')

    while opcao != '0':

                
        if opcao == '1':
           
            print("Digite o índice do dado a ser guardado (0 a 4):")
            
            indice = int(input('>'))
            
            res = guardar_dado(dados,dados_no_estoque,indice)
            
            dados_no_estoque = res[1]
            
            dados = res[0]

            print('Dados rolados: {0}'.format(dados))

            print('Dados guardados: {0}'.format(dados_no_estoque))

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            
        elif opcao == '2':
            
            print("Digite o índice do dado a ser removido (0 a 4):")
            
            indice = int(input('>'))

            res = remover_dado(dados,dados_no_estoque,indice)

            dados_no_estoque = res[1]
            
            dados= res[0]

            print('Dados rolados: {0}'.format(dados))

            print('Dados guardados: {0}'.format(dados_no_estoque))

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
       
        elif opcao == '3':

            if rerrolar >= 2:
                
                print("Você já usou todas as rerrolagens.")
            
            else:
                
                dados = rolar_dados(5-len(dados_no_estoque))
                
                rerrolar += 1
            
            print('Dados rolados: {0}'.format(dados))

            print('Dados guardados: {0}'.format(dados_no_estoque))

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        

        elif opcao == '4':
            imprime_cartela (cartela)

            print('Dados rolados: {0}'.format(dados))

            print('Dados guardados: {0}'.format(dados_no_estoque))

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        

        elif opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '0':
            
            print("Opção inválida. Tente novamente.")

            
        opcao = input('>')
    
    else:

        print( "Digite a combinação desejada:")
        
        combinacao = input('>')

        while combinacao in combinacoes:
            
            print("Essa combinação já foi utilizada.")
            
            combinacao = input('>')
        
        while combinacao not in possiveis:
            
            print("Combinação inválida. Tente novamente.")
            
            combinacao = input('>')
        
        for dado in dados:
            dados_no_estoque.append(dado)

        combinacoes.append(combinacao)

        cartela = faz_jogada(dados_no_estoque,combinacao,cartela)
    
    rodada += 1


soma = 0

for regras in cartela.values():
    
    for pontos in regras.values():
        
        soma += pontos

simples = cartela['regra_simples']

soma_simples = 0

for pontos in simples.values():
    
    soma_simples += pontos


if soma_simples >= 63:
    soma+= 35

imprime_cartela(cartela)

print('Pontuação total: {0}'.format(soma))
             




