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
#p = int(input("Ingrese el valor de p: "))
#q = int(input("Ingrese el valor de q: "))
def euclides_extendido(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclides_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def resolver_diofantica(a, b):
    gcd, x, y = euclides_extendido(a, b)

    if 1 % gcd != 0:
        return "No tiene solución"

    x *= 1 // gcd
    y *= 1 // gcd

    return x, y

# Ejemplo de uso
a = 13
b = 2436

solucion = resolver_diofantica(a, b)
print(f"Solución: x = {solucion[0]}, y = {solucion[1]}")


