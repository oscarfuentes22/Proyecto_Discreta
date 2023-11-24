#Universidad del Valle de Guatemala
#Nelson Escalante - 22046
#Oscar Fuentes - 22763

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
    'A': "0", 
    'B': "01", 
    'C': "02", 
    'D': "03", 
    'E': "04", 
    'F': "05", 
    'G': "06", 
    'H': "07", 
    'I': "08", 
    'J': "09", 
    'K': "10", 
    'L': "11", 
    'M': "12", 
    'N': "13", 
    'O': "14", 
    'P': "15", 
    'Q': "16", 
    'R': "17", 
    'S': "18", 
    'T': "19", 
    'U': "20", 
    'V': "21",
    'W': "22",
    'X': "23",
    'Y': "24",
    'Z': "25"
}

mensaje = "STOP"

def Translate(m: int):
    Msg = str(m)
    if (len(Msg) <= 2):
        d1 = 'A'
        d2 = alphabet_decode.get(m % 25)
    elif (len(Msg) == 3):
        p1 = Msg[0]
        d1 = alphabet_decode.get(int(p1) % 25)
        p2 = Msg[1] + Msg[2]
        d2 = alphabet_decode.get(int(p2) % 25)
    else:
        p1 = Msg[0] + Msg[1]
        d1 = alphabet_decode.get(int(p1) % 25)
        p2 = Msg[2] + Msg[3]
        d2 = alphabet_decode.get(int(p2) % 25)

    msg_d = str(d1) + str(d2)

    return msg_d

def AntiTranslate(m: str):
    c1 = m[0]
    c2 = m[1]

    d1 = alphabet_encode.get(c1)
    d2 = alphabet_encode.get(c2)

    msg_d = int(d1 + d2)

    return msg_d

def Encode(m, e, n):
    num = AntiTranslate(m)
    print("Letras a numeros: " + str(num))

    enc = pow(num, e, n)
    return enc

def Decode(m, p, q, e):
    n = p*q
    phi = (p-1) * (q-1)
    d = resolver_diofantica(e, phi)

    num_dec = pow(m, d, n)
    print("Numero descifrado: " + str(num_dec))

    dec = Translate(num_dec)
    return dec

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

#Primer inciso
print("Numero cifrado: " + str(Encode("ST", 13, 2537)))
print("Numero cifrado: " + str(Encode("OP", 13, 2537)))
print("============")
#Segundo inciso
print("Traduccion: " + Decode(981, 43, 59, 13))
print("Traduccion: " + Decode(461, 43, 59, 13))