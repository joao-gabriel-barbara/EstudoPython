# %%

dados_teo = [32, 1, "Casado", "dev python"]
dados_teo

# %%

dados_teo.append("3321.31")
dados_teo
# %%


tupla_teo = (31, 1, "Casado", "dev python")
print(type(tupla_teo))
print(tupla_teo)
# %%

dados = {}

while True:
    frase = input("Entre com a frase: ")
    if frase == "":
        break

    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

items = list(dados.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i, j in items:
    print(i, "->", j)
# %%
