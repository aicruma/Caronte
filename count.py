def count(w,l):
    word = w
    count = 0
    for letter in word:
        if letter == l:
            count = count + 1
    print("se econtraron "+str(count)+" "+l)

w = input("Ingrese una palabra\n")
l = input("Ingrese la letra a contar\n")
count(w,l)
