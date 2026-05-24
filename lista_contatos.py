def add_dados_arquivo_csv(caminho: str, modo: str, dados: list):
    with open(caminho, modo) as arquivo:
        for dado in dados:
            arquivo.write(f"{dado}\n")

def leitor_dados(caminho: str):
    with open(caminho, "r") as arquivo:
        for dado in arquivo.readlines():
            print(dado.strip())

add_dados_arquivo_csv("teste.txt", "w", [1, 2, 3, 4])
leitor_dados("teste.txt")
