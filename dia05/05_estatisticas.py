
def soma(a:float,b:float, *args)->float:
    valores = [a, b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args)+ 2)

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))

print("Média: ", media(a,b))  