print(''' 

    Seja bem-vindo a prova da Aula 01 - História da internet.pdf do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Em qual período Histórico da humanidade a Internet surgiu?
A) Durante a 2º Guerra Mundial
B) Durante a Guerra dos 100 anos
C) Durante a Guerra Fria
D) Durante a Guerra do Golfo
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'C) Durante a Guerra Fria':
    print("Acertou")
    pontos1 += 1

print('''
2 - A agência militar americana DARPA foi a responsável pelo início dos estudos que deram origem à Internet. Logo no início, a rede teve um nome. Você sabe qual foi?
A) DARPANET
B) ARPANET
C) MILNET
D) NSFNET
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'B) ARPANET':
    print("Acertou")
    pontos2 += 1

print('''
3 - A primeira transmissão registrada na rede foi no ano de _____. A primeira palavra enviada de um computador para outro foi _____.
A) 1949 / HELLO
B) 1955 / FIRST
C) 1962 / WORKS
D) 1969 / LOGIN
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'D) 1969 / LOGIN':
    print('Acertou')
    pontos3 += 1

print('''
4 - A primeira versão da rede que deu origem à Internet interligava quantos computadores?
A) 4 computadores
B) 40 computadores
C) 4 mil computadores
D) 400 mil computadores
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'A) 4 computadores':
    print('Acertou')
    pontos4 += 1

print('''
5 - O primeiro protocolo usado na transmissão de dados entre os controladores tinha o nome de: 
A) TCP
B) NetBEUI
C) NCP 
D) IP 
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'C) NCP':
    print('Acertou')
    pontos5 += 1

print('''
6 - No dia 1 de Janeiro do ano de _____ o TCP/IP passou a ser o único protocolo aceito pela Internet. Esse dia ficou conhecido como ______.
A) 1973 / Turn Point 
B) 1983 / Flag Day
C) 1985 / New Hope
D) 1988 / Brand Tech
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'B) 1983 / Flag Day':
    print('Acertou')
    pontos6 += 1

print('''
7 - O conjunto de protocolos TCP/IP foi criado por um funcionário da DARPA e um pesquisador da universidade de Stanford. São eles, respectivamente:
A) Vint Cerf e Robert Kahn
B) Robert Kahn e Tim Berners-Lee 
C) Tim Berners-Lee e Vint Cerf
D) Robert Kahn e Vint Cerf
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'D) Robert Kahn e Vint Cerf':
    print('Acertou')
    pontos7 += 1

print('''
8 - O cientista inglês Tim Berners-Lee foi o responsável pela criação de três coisas muito importantes para a Internet. Foram elas:
A) a linguagem HTML, o protocolo HTTP e o primeiro navegador Mosaic 
B) o TCP/IP, o primeiro navegador Mosaic e o nome WWW
C) a linguagem HTML, o protocolo HTTP e o nome WWW
D) o nome WWW, o primeiro navegador Mosaic e a linguagem HTML
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'C) a linguagem HTML, o protocolo HTTP e o nome WWW':
    print('Acertou')
    pontos8 += 1

print('''
9 - O primeiro backbone brasileiro surgiu em _____ para acesso acadêmico, mas só foi liberado para empresas em _____.
A) 1991 / 1995
B) 1990 / 1997
C) 1989 / 1991
D) 1985 / 1995
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'A) 1991 / 1995':
    print('Acertou')
    pontos9 += 1

print('''
10 - Atualmente, a Internet Brasileira atinge quantos estados?
A) 19 estados, além do Distrito Federal
B) 23 estados, além do Distrito Federal
C) 25 estados, além do Distrito Federal
D) 26 estados, além do Distrito Federal
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'D) 26 estados, além do Distrito Federal':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
