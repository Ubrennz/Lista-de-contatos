def add_dados_arquivo(caminho: str, modo: str, dados: list):
    with open(caminho, modo, encoding="utf-8") as arquivo:
        for dado in dados:
            arquivo.write(f"{dado}\n")

def leitor_dados(caminho: str) -> list:
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return [linha.strip() for linha in arquivo.readlines()]

def atualizar_dados(caminho: str, dado_antigo: str, novo_dado: str):
    dados = leitor_dados(caminho)

    for index, valor in enumerate(dados):
        if valor.strip() == dado_antigo:
            dados[index] = novo_dado
            break

    add_dados_arquivo(caminho, "w", dados)

def apagar_dados(caminho: str, dado_para_apagar: str):
    dados = leitor_dados(caminho)
    dados.remove(dado_para_apagar)
    add_dados_arquivo(caminho, "w", dados)


caminho1 = "teste.txt"
dados1 = ["1", "2", "3", "5", "3"]
dados2 = [1, 3, 4, 5, 4]

add_dados_arquivo(caminho1, "w", dados1)

for dado in leitor_dados(caminho1):
    print(dado.strip())

atualizar_dados(caminho1, str(2), str(19))

for dado in leitor_dados(caminho1):
    print(dado.strip())

apagar_dados(caminho1, str(5))