import random


def get_input():
    while True:
            try:
                numero_usuario = int(input("Entre com um número: "))

            except ValueError as err:
                print("Valor inválido")
                continue

            if 1 <= numero_usuario <= 15:
                return numero_usuario

            print("Valor inválido! O valor deve ser de 1 a 15!")

def check_numbers(numero_sorteio, numero_usuario):
    if numero_usuario == numero_sorteio:
        print("Parabéns!")
        return True

    elif numero_usuario > numero_sorteio:
        print("Número muito alto. Tente um número menor!")
        return False
    
    else:
        print("Número muito baixo. Tente um número menor!")
        return False

numero_sorteio = random.randint(1,15)

for i in range(3):

    numero_usuario = get_input()

    if check_numbers(numero_sorteio=numero_sorteio, numero_usuario=numero_usuario):
            break
    

else:
    print("Suas tentativas acabaram!")