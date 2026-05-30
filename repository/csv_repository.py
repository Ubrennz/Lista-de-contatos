import csv

def adicionar_dados(caminho: str, modo: str, dados: list):
    with open(caminho, modo, newline="",encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

def leitor_dados(caminho: str) -> list:
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return list(csv.reader(arquivo))

def atualizar_dados(caminho: str, dado_antigo: str, novo_dado: str):
    dados_arquivo = leitor_dados(caminho)

    for index1, linha in enumerate(dados_arquivo):
        for index2, dado in enumerate(linha):
            if dado.strip() == dado_antigo:
                dados_arquivo[index1][index2] = novo_dado
                break

    adicionar_dados(caminho, "w", dados_arquivo)

def apagar_dado(caminho: str, dado_para_apagar: str):
    atualizar_dados(caminho, dado_para_apagar, "")
