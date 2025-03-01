# %%
for i in "Gabriel":
    print(i)

print(i)
# %%

for i in "Gabriel Bom":
    
    if i == "G":
        continue

    elif i == " ":
        continue

    print(i)
# %%

range(10) # começa do 0 e vai até o 9
seq = range(0, 10) #(start, stop); qtde = stop - start 

for i in seq:
    print(i)
# %%

qtde = int(input("Quantos 'Bom dia' você quer?"))

for i in range(qtde):
    print("Bom dia")
# %%

for i in range(1, 16, 2):
    if i % 2 == 0:
        print(i)
# %%
