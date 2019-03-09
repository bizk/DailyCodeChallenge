def buscar(arreglo):
    ch = []
    arreglo.sort()
    for x in arreglo:
        if x > 0:
            ch.append(x)
    ch = list(set(ch))
    lench = len(ch)
    minimo = 0
    if lench > 1:
        for i in range(1, lench):
            ex = ch[i - 1] + 1
            if ex != ch[i]:
                if minimo != 0:
                    minimo = min(minimo, ex)
                else:
                    minimo = ch[i-1]+1

    print("Este es el numero que falta: ", minimo)

arr = []
print("Ingrese la cadena de caracteres: \n")
while True:
    ln = input()
    try:
        ln = int(ln)
    except:
        break
    arr.append(ln)

print("SALIO")
buscar(arr)
