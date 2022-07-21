print(''' 

    Seja bem-vindo a prova da Aula 13 - Cores do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 -  Segundo levantamentos relacionados à psicologia das cores, qual é a cor com a maior taxa de aceitação e menor rejeição que existe?
A) vermelho
B) verde
C) azul
D) amarelo
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'C) azul':
    print("Acertou")
    pontos1 += 1

print('''
2 - De acordo com a tabela apresentada neste capítulo 13, qual é a cor que está associada a criatividade, poder, sabedoria e mistério?
A) preto
B) roxo
C) rosa
D) laranja
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'B) roxo':
    print("Acertou")
    pontos2 += 1

print('''
3 - Qual cor deve ser evitada em sites de alimentação ou relacionados com comida, pois pode induzir a uma redução no apetite? 
A) roxo
B) azul 
C) vermelho
D) marrom
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'B) azul':
    print('Acertou')
    pontos3 += 1

print('''
4 - Ao construir um site, devemos definir qual será _____ utilizado(a), pois isso vai criar a sensação de que tudo faz sentido visualmente e o usuário vai ter a sensação de harmonia, mesmo sem saber do que se trata.
A) o círculo cromático
B) a cor análoga
C) a cor tetrádica
D) a paleta de cores
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'D) a paleta de cores':
    print('Acertou')
    pontos4 += 1

print('''
5 - Qual das cores a seguir é a única que não está presente explicitamente no círculo cromático?
A) amarelo-alaranjado
B) vermelho-arroxeado
C) amarelo-arroxeado
D) azul-esverdeado
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'C) amarelo-arroxeado':
    print('Acertou')
    pontos5 += 1

print('''
6 - Qual dos itens a seguir é o único que não é considerado como uma cor quente?
A) roxo
B) vermelho
C) laranja
D) amarelo
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'A) roxo':
    print('Acertou')
    pontos6 += 1

print('''
7 - Enquanto as cores _____ são aquelas que estão no extremo oposto do círculo cromático e por isso possuem o maior contraste entre si, as cores _____ são aquelas que estão localizadas imediatamente aos lados da cor considerada (vizinhas).
A) análogas / complementares
B) complementares / análogas
C) análogas / intercaladas
D) complementares / intercaladas
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'B) complementares / análogas':
    print('Acertou')
    pontos7 += 1

print('''
8 - Qual dos itens abaixo é o único que não é uma função CSS para a representação de cores?
A) rgbl()
B) rgba()
C) hsl()
D) hsla()
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'A) rgbl()':
    print('Acertou')
    pontos8 += 1

print('''
9 - Considerando a representação de cor hsl(179, 100%, 34%), os três valores indicados são respectivamente quantidades para:
A) matiz, saturação e luminância
B) harmonia, saturação e luminosidade
C) hegemonia, salientação e lealdade
D) hierarquia, síntese e liberdade
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'A) matiz, saturação e luminância':
    print('Acertou')
    pontos9 += 1

print('''
10 - Para criar um efeito degradê em CSS, podemos usar as seguintes funções:
A) linear-degradee e radial-degradee
B) derradee-linear e degradee-radial
C) gradient-linear e gradient-radial
D) linear-gradient e radial-gradient
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'D) linear-gradient e radial-gradient':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
