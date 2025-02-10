from datetime import datetime

def verificarVazio(nomeVar):
    varValor = input(f"\n{nomeVar}:")
    while varValor == "":
        if varValor == "":
            print(f'{nomeVar} Não pode estar vazio.')
            varValor = input('Tente novamente: ')
        else:
            return varValor

def adicionar(varNome, varEspecie, varData, varTutor):
    cadastro = (varNome, varEspecie, varData, varTutor)
    return cadastroAnimais.append(cadastro)

def remover(varPosição):
    return cadastroAnimais.pop(varPosição)
    
cadastroAnimais = []
print("- Seja bem vindo(a), o que deseja fazer?")

while True:
    print("\n1 - Cadastrar animal\n2 - Remover animal\n3 - Exibir cadastros")
    Menu = (int(input('Escolha uma das opções: ')))
    
    match Menu:
        case 1:
            print('Você escolheu cadastrar.')
            Nome = verificarVazio('Nome')
            Especie = input('\nEspécie: ')
            dataNascS = input('\nData de Nascimento: ')
            dataNasc = datetime.strptime(dataNascS, "%d/%m/%Y")
            Tutor = input('\nTutor: ')
            
            adicionar(Nome, Especie, dataNasc.strftime('%d/%m/%Y'), Tutor)
            print(cadastroAnimais)
            
        case 2:
            print('Você escolheu remover.')
            remover(int(input('Escolha o cadastro que deseja remover: ')))
            print(cadastroAnimais)
            
        case 3:
            print('Você escolheu exibir a lista.')
            print(cadastroAnimais)
            
        case _:
            print('Número inválido, tente novamente.')