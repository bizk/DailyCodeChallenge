def solucion(arreglo, k):
    no = []
    doble = []
    arreglo.sort()
    for x in arreglo:
        if x > k:
            no.append(x)
            continue
        doble = arreglo.copy()
        if len(no) > 0:
            doble.remove(no)
        for y in doble:
            if (y + x) == k:
                print("Solucion:",y,x)

arr = []
print("Ingrese los caracteres:")
while True:
    ln = input()
    try:
        ln = int(ln)
    except:
        break
    arr.append(ln)


print("Inserte el numero k")
m = input()
solucion(arr,int(m))

