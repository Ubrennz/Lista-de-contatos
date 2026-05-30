from repository.csv_repository import adicionar_dados, leitor_dados, atualizar_dados, apagar_dado
from time import sleep

def criar_contato():
    nome_contato = input("Digite o nome do contato: ")
    numero_contato = input("Digite o número do contato: ")
    adicionar_dados(caminho, "a", [[nome_contato, numero_contato]])

def mostrar_contatos():
    for linha in leitor_dados(caminho):
        print(f"{linha[0]} - {linha[1]}")

def atualizar_contato():
    dado_antigo = input("Digite um valor que você deseja atualizar: ")
    dado_novo = input("Digite o novo valor: ")
    atualizar_dados(caminho, dado_antigo, dado_novo)

def apagar_contato():
    dado_para_apagar = input("Digite o valor que você deseja apagar: ")
    apagar_dado(caminho, dado_para_apagar)

def interacao_saindo():
    print("Saindo", end="")

    for c in range(0, 3):
        sleep(0.3)
        print(".", end="")
    print()

caminho = "arquivo.csv"

opcoes = {
        "1": "Criar registro",
        "2": "Listar todos",
        "3": "Atualizar registro",
        "4": "Deletar registro",
        "0": "Sair",
    }

try:
    while True:
        for v, k in opcoes.items():
            print(f"[{v}] {k}")
        opcao = int(input("Digite a opcao: "))

        if opcao == 1:
            criar_contato()
        elif opcao == 2:
            mostrar_contatos()
        elif opcao == 3:
            atualizar_contato()
        elif opcao == 4:
            apagar_contato()
        elif opcao == 0:
            interacao_saindo()
            break
        else:
            print("Número inválido, digite outro número")
except ValueError:
    print("Digite apenas números")
except FileNotFoundError:
    print("O não foi encontrado")
except Exception as error:
    print(f"Erro inesperado: {error.__class__}")
