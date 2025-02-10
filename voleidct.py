#cadastro vôlei

from datetime import datetime

jogadores = []

def ler_valor_nao_vazio(nome_variavel):
    valor_lido = input(f'Dê algum valor para {nome_variavel}: ')
    while valor_lido == '':
        print(f'Invalido! o valor para {nome_variavel} não pode ser vazio.')
        valor_lido = input(f'Dê algum valor para {nome_variavel}: ')
    return valor_lido

def ler_altura(valor_altura):
    valor_lido = float(input(f'Defina o {valor_altura} em metros.:')).strip().lower()
    if valor_lido < 0.83 or valor_lido > 2.51:
        print(f'invalido! o valor para {valor_altura} não pode ser este.')
        valor_lido = input(f'defina o {valor_altura} em metros.:').strip().lower()
    return valor_lido

def ler_sexo(valor_sexo):
    valor_lido = input(f'Defina o {valor_sexo} como masculino ou feminino:').strip().lower()
    while valor_lido not in ['masculino', 'feminino']:
        print(f'invalido! o valor para {valor_sexo} não pode ser este.')
        valor_lido = input(f'defina o {valor_sexo} como masculino ou feminino:').strip().lower()
    return valor_lido
        
def ler_posição(valor_posição):
    opcoes = ['libero', 'levantador', 'ponteiro', 'central', 'oposto']
    print(f'Opções disponiveis:')
    print(opcoes)
    valor_lido = input(f'Defina sua {valor_posição}: ').strip().lower()
    while valor_lido not in opcoes: 
        print(f'invalido! o valor para {valor_posição} não pode ser este.')
        valor_lido = input(f'Defina sua {valor_posição}: ').strip().lower()
    return valor_lido
        
def ler_experiencia(valor_exp):
    opcoes = ['pouca', 'mediana', 'alta']
    print(f'Opções disponiveis:')
    print(opcoes)
    valor_lido = input(f'Defina sua {valor_exp}: ')
    while valor_lido not in opcoes:
        print(f'Invalido! o valor para {valor_exp} não pode ser este.')
        valor_lido = input(f'Defina sua {valor_exp}: ')
    return valor_lido
 


def ler_pessoa():
    print("\n--- Cadastro do Jogador ---")
    nome = ler_valor_nao_vazio('nome')
    dataNascimentoString = input('Digite sua data de nascimento(dd/mm/aaaa): ')
    
    try:
        dataNascimento = datetime.strptime(dataNascimentoString, "%d/%m/%Y")
    except ValueError:
        print('Data inválida. Use o formato dd/mm/aaaa')
        return ler_pessoa()
    altura = ler_valor_nao_vazio('altura')
    sexo = ler_sexo('sexo')
    posição = ler_posição('posição')
    experiencia = ler_experiencia('experiencia')

    jogador = {
        'nome': nome,
        'dataNascimento': dataNascimento,
        'altura': altura,
        'sexo': sexo,
        'posição': posição,
        'experiencia': experiencia,
    
    }
    return jogador

def imprimir_jogador(jogador):
    print("\n--- Dados do Jogador ---")
    print(f"Nome:\t\t{jogador['nome']}")
    print(f"Data:\t\t{jogador['dataNascimento'].strftime('%d/%m/%Y')}")
    print(f"Sexo:\t\t{jogador['sexo']}")
    print(f"Altura:\t\t{jogador['altura']}")
    print(f"Posição:\t{jogador['posição']}")
    print(f"Nivel de Exp.:\t{jogador['experiencia']}")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Incluir Jogadores")
        print("2. Exibir Jogadores")
        print("3. Editar Jogadores")
        print("4. Remover Jogadores")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            jogador = ler_pessoa()
            jogadores.append(jogador)
            print("Jogador cadastrado com sucesso.")
        elif opcao == "2":
            jogador = ler_pessoa()
            if not jogadores:
                print("Nenhum jogador cadastrado.")
            else:
                exibir_jogadores()
        elif opcao =="3":
            if not jogadores:
                print("Nenhum jogador para editar.")
            else:
                exibir_jogadores()
                indice = int(input("Informe o número do jogador a editar: ")) - 1
                if 0 <= indice < len(jogadores):
                    jogadores[indice] = ler_pessoa()
                    print("Jogador atualizado com sucesso.")
                else:
                    print("Número inválido.")
        elif opcao == "4":
            if not jogadores:
                print("Nenhum jogador para remover.")
            else:
                exibir_jogadores()
                indice = int(input("Informe o número do jogador a editar: ")) - 1
                if 0 <= indice < len(jogadores):
                    jogadores.pop(indice)
                    print("Jogador removio com sucesso.")
                else:
                    print("Número inválido.")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_jogadores():
    for i, jogador in enumerate(jogadores):
        print(f"\n Jogador {i+1}")
        imprimir_jogador(jogador)

print(f'seja bem vindo as inscrições para o time de vôlei!')
menu()


