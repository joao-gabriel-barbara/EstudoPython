# %%
nome_arquivo = "historia.txt"

open_file = open(nome_arquivo)

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

# Abre arquivo em formato de leitura
#conteudo = open_file.read()

# Lê os dados do arquivo
#print(conteudo)

# Fecha o arquivo
#open_file.close()
# %%
