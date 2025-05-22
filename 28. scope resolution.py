# Escopo de variável: onde uma variável é visível e acessível.
# Resolução de escopo = (LEGB) Local > Aninhado (Enclosed) -> Global -> Built-in.

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

x = 3

func1()
func2()