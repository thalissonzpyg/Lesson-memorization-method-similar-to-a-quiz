print(''' 

    Seja bem-vindo a prova do Vídeo 10 - Front-end, Back-end e Full stack do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Qual o objetivo do servidor de entrega para o cliente?
A) Tipos de tecnologia: JS e NodeJS
B) Tipos de tecnologia: HTML, CSS e JS
C) Tipos de tecnologia: Rubi, Java e Python
D) Tipos de tecnologia: HTML, JS e Rubi
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'B) HTML, CSS e JS':
    print("Acertou")
    pontos1 += 1

print('''
2 - O que é site estático? 
A) Sites que são entregues diferentes para o cliente
B) Sites que o cliente tem experiência única e do jeito que ele quiser
C) Sites que são entregue aos clientes de forma igualitária, experiências de clientes diferentes pois será a mesma visualmente
D) Sites que são entregue aos clientes de forma diferente, porém 2 a cada 4 pessoas conseguem ter a mesma experiencia visual
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'C) Sites que são entregue aos clientes de forma igualitária, experiências de clientes diferentes pois será a mesma visualmente':
    print("Acertou")
    pontos2 += 1

print('''
3 - Tecnologias HTML, CSS e JS são chamadas de que?
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'Client-side/front-end':
    print('Acertou')
    pontos3 += 1

print('''
4 - Qual a função do Front-end?
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'Gerar a parte visual e interativa do site':
    print('Acertou')
    pontos4 += 1

print('''
5 - Tecnologias PHP, JS, Java, Rubi, Python, CSharp são chamadas de que?
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'Server-side/back-end':
    print('Acertou')
    pontos5 += 1

print('''
6 - Qual o interesse do back-end? 
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'No código com as entranhas do servidor':
    print('Acertou')
    pontos6 += 1

print('''
7 - Como é formado o Full Stack? 
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'Pessoa que domina o front-end e o back-end':
    print('Acertou')
    pontos7 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7)
print('Se você tirou 7, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
