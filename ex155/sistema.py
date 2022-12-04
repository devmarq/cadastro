from ex115.lib.interface import *
from tudo import cores
from time import sleep
from tudo import matematica
from ex115.lib.arquivo import *

arq= 'cursoemvideo.txt'
#str(input('Qual o nome do arquivo? '))+'.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        #o.l.c.a.
        lerArquivo(arq)

    elif resposta == 2:
        # o.c.n.p.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('\033[36mNome:\033[m '))
        idade = leiaInt('\033[35mIdade:\033[m')
        cadastrar(arq, nome,idade)
    elif resposta==3:
        # o.s.s.
        cabeçalho('Saindo da sistema... Até logo')
        break
    else:
        # D.o.e.m.
        print(cores.vermelho('ERRO! Digite uma opção válida!'))
    sleep(2)
