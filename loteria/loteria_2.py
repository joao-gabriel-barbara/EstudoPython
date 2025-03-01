# %%
numero_sorte = 7

for i in range(3):
    while True:
        try:
            numero = int(input("Entre com um número entre 1 e 15: "))
            break

        except ValueError:
            print("Mano, tu é burro? Pedi um número, um digito!")



    if numero == numero_sorte:
        print("Você acertou!")
        break

    elif numero > numero_sorte:
        print("Você errou! Tente um número menor!")
    else:
        print("Errou. Tente um número maior!")
# %%
try:
    numero = int(input("Entre com um número: "))

except ValueError as err:
    print("Mano, tu é burro? Pedi um número, um digito!")
# %%
