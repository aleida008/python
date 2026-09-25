#ordenamiento burbuja
precios = [5,2,9,1,6]

n = len(precios)

for i in range(n-1):
    for j in range(n - 1 - i):
       if precios[j] > precios[j + 1]:
           aux = precios[j]
           precios[j] = precios[j + 1]
           precios[j + 1] = aux

print(f"Lista original.: {precios}")
print(f"Lista ordenada.: {precios}")