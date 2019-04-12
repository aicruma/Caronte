def eval_loop():
    while True:
        e = input("ingrese la expresion a evaluar:")
        if e == "done":
            print(e+"!")
            print(resul)
            break
        else:
            print(e)
            resul = eval(e)
            print(eval(e))
eval_loop()
