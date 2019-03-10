
def buscar(arreglo):
    sub = []
    for x in arreglo:
        sub = arreglo.copy()
        sub.remove(x)
        resultado = 1
        for y in sub:
            resultado = resultado*y
        sol.append(resultado)

sol = []
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
for x in sol:
    print(x)