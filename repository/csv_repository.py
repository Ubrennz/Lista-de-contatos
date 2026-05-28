import csv

def add_dados_arquivo(caminho: str, modo: str, dados: list):
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

    add_dados_arquivo(caminho, "w", dados_arquivo)

def apagar_dados(caminho: str, dado_para_apagar: str):
    dados_arquivo = leitor_dados(caminho)

    for index1, linha in enumerate(dados_arquivo):
        for index2 in range(0, len(linha)):
            if dados_arquivo[index1][index2] == dado_para_apagar:
                del dados_arquivo[index1][index2]
                break

    add_dados_arquivo(caminho, "w", dados_arquivo)
