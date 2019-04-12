def is_triagle(a, b, c):
    if a > b and a > c:
        if b + c < a:
            print("No, no es un triangulo")
        else:
            print("Si, es un triangulo")

    elif b > a and b > c:
        if a + c < b:
            print("No, no es un triangulo")
        else:
            print("Si, es un triangulo")

    elif c > a and c > b:
        if a + b < c:
            print("No, no es un triangulo")
        else:
            print("Si, es un triangulo")

    elif a == b and a == c:
        print("Si, es un triangulo")

print("Ingrese la longitud de cada una de las barras:\n")
a = input("Ingrese la longitud del lado a:\n")
a = int(a)
print(type(a))
b = input("Ingrese la longitud del lado b:\n")
b = int(b)
print(type(b))
c = input("Ingrese la longitud del lado c:\n")
c = int(c)
print(type(b))

is_triagle(a,b,c)
