def mcd(a, b):
    c = a % b
    if (c != 0):
        return mcd(b, c)
    return b

def Encode(p, q, e):
    
    n = p*q
    f = (p-1)*(q-1)

    return 0

def Decode():
    return 0
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def verificar_primos(p, q):
    if es_primo(p) and es_primo(q):
        print(f"{p} y {q} son números primos.")
    else:
        print(f"{p} y {q} no son números primos.")

# Aquí puedes ingresar los valores de p y q que desees verificar
p = int(input("Ingrese el valor de p: "))
q = int(input("Ingrese el valor de q: "))


