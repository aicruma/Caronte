def comparar(x, y):
    n = 0
    if x > y:
        n = 1
    if x == y:
        n = 0
    if x < y:
        n = -1
    print(n)
    return n

x = input("Ingrese un valor para x:\n")
y = input("Ingrese un valor para y:\n")

print("El resultado es:")
comparar(x, y)
print("se supone que sale n")
