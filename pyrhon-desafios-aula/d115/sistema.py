from time import sleep

from d115.lib.archive import *
from d115.lib.interface import *

arq = "curseemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(
        ["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"]
    )

    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
        sleep(2)
