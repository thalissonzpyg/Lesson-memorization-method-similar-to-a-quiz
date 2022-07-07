print(''' 

    Seja bem-vindo a prova da Aula 09 - Listas HTML do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Em HTML5, temos vários tipos de lista. Qual dos itens a seguir não é um tipo de lista suportado pela linguagem?
A) lista ordenada
B) lista não ordenada 
C) lista semi ordenada 
D) lista de definição
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'C) lista semi ordenada':
    print("Acertou")
    pontos1 += 1

print('''
2 - Na construção das listas ordenadas e nas não ordenadas, o uso de uma das tags se repete nos dois casos. Que tag é essa?
A) <ul>
B) <ol>
C) <li>
D) <dl>
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'C) <li>':
    print("Acertou")
    pontos2 += 1

print('''
3 - Para criar uma lista ordenada, devemos limitar todos os seus itens dentro de um par único de tags:
A) <ol> e </ol>
B) <ul> e </ul>
C) <dl> e </dl>
D) <dt> e </dt>
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'A) <ol> e </ol>':
    print('Acertou')
    pontos3 += 1

print('''
4 - Segundo as novas normas da W3C, qual das tags de lista a seguir é a única que possui fechamento opcional?
A) <dt>
B) <dd>
C) <ol>
D) <li>
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'D) <li>':
    print('Acertou')
    pontos4 += 1

print('''
5 - Em listas ordenadas, podemos usar o parâmetro _____ para modificar o formato da contagem e o parâmetro ____ para mudar o número inicial da contagem. 
A) type / init
B) style / start
C) type / start 
D) style / init
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'C) type / start':
    print('Acertou')
    pontos5 += 1

print('''
6 - Ao personalizar a numeração de uma lista ordenada, podemos indicar vários tipos de contagem. Qual das opções a seguir é a única que não pode ser usada para essa personalização?
A) 1
B) A
C) I 
D) X
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'D) X':
    print('Acertou')
    pontos6 += 1

print('''
7 - Podemos personalizar as listas não ordenadas, configurando o parâmetro type da tag <ul> com alguns valores especiais. Qual dos elementos a seguir é o único aceito para modificar o marcador padrão dos itens?
A) star
B) square   
C) rectangle 
D) triangle 
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'B) square':
    print('Acertou')
    pontos7 += 1

print('''
8 - Todos os elementos de uma lista de definições devem estar limitados entre o par de tags:
A) <dt> e </dt>
B) <dd> e </dd>
C) <dl> e </dl>
D) <dc> e </dc>
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'C) <dl> e </dl>':
    print('Acertou')
    pontos8 += 1

print('''
9 - A tag <dt> em uma lista de definição tem o significado de:
A) definition term
B) description text
C) definition text 
D) description term 
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'A) definition term':
    print('Acertou')
    pontos9 += 1

print('''
10 - A tag <dd> em uma lista de definição tem o significado de:
A) description definition
B) definition description 
C) definition detail 
D) detail definition
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'B) definition description':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
