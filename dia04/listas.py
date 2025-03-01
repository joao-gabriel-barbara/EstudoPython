# %%
minha_lista = []
print(minha_lista)
# %%

minha_lista = ['joao', 'gabriel', 20, 1.70]
print(minha_lista)
# %%
notas = []

nota = 7.75

notas.append(nota)
print(notas)

notas.append(10)
print(notas)

notas.extend([5.75, 6.24])
print(notas)

notas = notas + [10, 9.25]
print(notas)
# %%

nomes = ['teo', 'joao', 'gabriel']
for i in nomes:
    print( i.title() )

# %%

dados = ['Teo', 'Calvo', 31, ['Nah', "Josefina", 'Elaina'], ["Maria"]]

dados[3][-1]

dados[-1][0][0]
 
# %%
