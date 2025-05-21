# nested loop: Um laço (loop) dentro de outro laço (externo, interno)
#
# laço externo: Este laço controla as iterações principais. Para cada "volta" do laço externo, o laço interno será executado completamente.
# laço interno: Este laço é executado por completo para cada iteração do laço externo. Assim que ele termina, o controle retorna ao laço externo, que então avança para sua próxima iteração.

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of colum: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows): 
    for x in range(columns):
        print(symbol, end=" ")
    print()