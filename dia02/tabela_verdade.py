#Booleanos
True
False

# %%
idade = int(input("Entre com a sua idade: "))
cnh = input("Você tem CNH? ")

if idade > 18 and cnh == 'sim':
    print("Siga em frente!")

else:
    print("Preso em nome da lei!") 

condicao = idade >=18 and cnh == "sim"
print(condicao)
# %%

print(True * 100) #True = 1
print(False * 10) #False = 0

print()
# %%
