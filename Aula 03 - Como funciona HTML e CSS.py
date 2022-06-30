print(''' 

    Seja bem-vindo a prova da Aula 03 - Como funciona HTML e CSS do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Qual das frases a seguir é a única tecnicamente CORRETA de se falar?
A) “Eu programo em linguagem HTML”
B) “Eu programo em linguagem CSS”
C) “Eu programo em linguagem JavaScript”
D) “Eu programo em linguagem VSCode”
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'C) Eu programo em linguagem JavaScript':
    print("Acertou")
    pontos1 += 1

print('''
2 - A sigla HTML significa:
A) Host Text Makeup Language
B) HyperText Markup Language
C) Hyper Tree Makeup Language
D) Host Tree Markup Language
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'B) HyperText Markup Lenguage':
    print("Acertou")
    pontos2 += 1

print('''
3 - A sigla CSS significa:
A) Cascading Style Sheets
B) Cell Safety Science
C) Characteristic Score Style
D) Chief Scale Sheets
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'A) Cascading Style Sheets':
    print('Acertou')
    pontos3 += 1

print('''
4 - Correlacione a coluna da esquerda com a da direita, de acordo com o foco de cada uma das tecnologias:

( 1 ) HTML ( ) interatividade
( 2 ) CSS  ( ) conteúdo
( 3 ) JS   ( ) estilo

A) 1 - 2 - 3
B) 3 - 2 - 1
C) 1 - 3 - 2
D) 3 - 1 - 2
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'D) 3 - 1 - 2':
    print('Acertou')
    pontos4 += 1

print('''
5 - Qual tag abaixo não tem fechamento? 
A) <title>
B) <meta>
C) <strong>
D) <head>
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'B) <meta>':
    print('Acertou')
    pontos5 += 1

print('''
6 - Na tag <a>, o href é um(a):
A) conteúdo 
B) parâmetro 
C) característica
D) valor 
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'B) parâmetro':
    print('Acertou')
    pontos6 += 1

print('''
7 - Todas as configurações visuais dos elementos HTML são realizadas pela linguagem CSS. Agrupamos todas as declarações CSS de um mesmo elemento dentro de um(a): 
A) seletor
B) parâmetro
C) valor 
D) selecionador
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'A) seletor':
    print('Acertou')
    pontos7 += 1

print('''
8 - Para mudar a cor de um texto em
CSS, configuramos qual propriedade?
A) text 
B) text-color
C) color 
D) font-color 
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'C) color':
    print('Acertou')
    pontos8 += 1

print('''
9 - Para indicar que um determinado documento HTML está escrito na versão mais recente da linguagem, devemos adicionar a seguinte instrução: 
A) <html lang=“version5”>
B) <title>HTML5</title>
C) <meta name=“lang” type=“html5”>
D) <!DOCTYPE html>
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'D) <!DOCTYPE html>':
    print('Acertou')
    pontos9 += 1

print('''
10 - Qual é a tag de um documento HTML adicionada pra manter a compatibilidade com os caracteres acentuados, muito comuns na língua Portuguesa?
A) <html lang=“pt-br”>
B) <meta charset=“UTF-8”>
C) <body lang=“br”>
D) <head charset=“UTF-8”>
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'B) <meta charset="UTF-8">':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
