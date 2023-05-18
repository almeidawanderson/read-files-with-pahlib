from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

moldens = caminho_arquivo.parent / 'moldens'
print(moldens)