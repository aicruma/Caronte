def strings(w):
    index = 0
    c = len(w)
    while index < len(w):
        letter = w[c-1]
        print(letter)
        c = c-1
        index = index + 1

w = input("Ingrese una palabra:\n")
strings(w)
