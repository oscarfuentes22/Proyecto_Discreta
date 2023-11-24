alphabet_decode = {
    0: 'A',
    1: 'B', 
    2: 'C', 
    3: 'D', 
    4: 'E', 
    5: 'F', 
    6: 'G', 
    7: 'H', 
    8: 'I', 
    9: 'J', 
    10: 'K', 
    11: 'L', 
    12: 'M', 
    13: 'N', 
    14: 'O', 
    15: 'P', 
    16: 'Q', 
    17: 'R', 
    18: 'S', 
    19: 'T', 
    20: 'U', 
    21: 'V', 
    22: 'W', 
    23: 'X', 
    24: 'Y', 
    25: 'Z'
}

alphabet_encode = {
    'A': 0, 
    'B': 1, 
    'C': 2, 
    'D': 3, 
    'E': 4, 
    'F': 5, 
    'G': 6, 
    'H': 7, 
    'I': 8, 
    'J': 9, 
    'K': 10, 
    'L': 11, 
    'M': 12, 
    'N': 13, 
    'O': 14, 
    'P': 15, 
    'Q': 16, 
    'R': 17, 
    'S': 18, 
    'T': 19, 
    'U': 20, 
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}

mensaje = "STOP"

def Translate(m: int):
    Msg = str(m)
    if (len(Msg) <= 3):
        p1 = Msg[0]
        d1 = alphabet_decode.get(int(p1))
        p2 = str.join(Msg[1], Msg[2])
        d2 = alphabet_decode.get(int(p2))

    else:
        p1 = str.join(Msg[0], Msg[1])
        d1 = alphabet_decode.get(int(p1))
        p2 = str.join(Msg[2], Msg[3])
        d2 = alphabet_decode.get(int(p2))

    msg_d = str.join(d1, d2)
    print(msg_d)
def AntiTranslate(m: str):
    Msg = m
    if (len(Msg) <= 3):
        p1 = Msg[0]
        d1 = alphabet_encode.get(p1)
        p2 = str.join(Msg[1], Msg[2])
        d2 = alphabet_encode.get(p2)

    else:
        p1 = str.join(Msg[0], Msg[1])
        d1 = alphabet_encode.get(p1)
        p2 = str.join(Msg[2], Msg[3])
        d2 = alphabet_encode.get(p2)

    msg_d = str.join(d1, d2)
    print(msg_d)

def mcd(a, b):
    c = a % b
    if (c != 0):
        return mcd(b, c)
    return b

def Encode(p, q, e, mensaje):
    
    n = p*q
    f = (p-1)*(q-1)
    mcd_e_f = mcd(e, f)
    mensaje_lista = list(mensaje)
    for i in mensaje_lista:
        
        return 0

def power(b, n, m):
    if (n == 0):
        return 1
    if (n%2) == 0:
        return (power(b, n/2, m)**2) % m
    if (n%2) == 1:
        return (b*power(b, (n-1)/2, m)**2) % m

def Decode(m, e, p, q):
    n = p*q
    #print(n)
    f = (p-1)*(q-1)
    #print(f)
    d = resolver_diofantica(e, f)
    #print(d)

    #print(power(m, d, n))
    to_translate = pow(m, d, f)

    Translate(to_translate)

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

    return x

# Ejemplo de uso
a = 13
b = 2436

#solucion = resolver_diofantica(a, b)
#print(f"Solución: x = {solucion[0]}, y = {solucion[1]}")

Decode(1366, 17, 53, 37)
Decode(416, 13, 43, 59)


