from repository.csv_repository import add_dados_arquivo, atualizar_dados, apagar_dados

caminho1 = "teste.csv"

add_dados_arquivo(caminho1, "w", [["teste", "1", "2"]])
atualizar_dados(caminho1, "teste", "novo_teste")
apagar_dados(caminho1, "novo_teste")
apagar_dados(caminho1, "2")
