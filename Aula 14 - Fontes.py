print(''' 

    Seja bem-vindo a prova da Aula 14 - Fontes do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 -  A tipografia é uma arte antiga cujo nome vem da junção de duas palavras gregas. Marque a opção que descreve corretamente cada um destes termos.
A) týpos que significa impressão e graphía que significa escrita
B) tipus que significa letra e graphia que significa escrever
C) týpos que significa escrita e graphía que significa impressão
D) tipus que significa escrever e graphia que significa letra
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'A) týpos que significa impressão e graphía que significa escrita':
    print("Acertou")
    pontos1 += 1

print('''
2 - A tipografia se inicia em 1450, com o inventor alemão chamado:
A) Edmund Germer
B) Konrad Zuse
C) Johannes Gutenberg
D) Alois Senefelder
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'C) Johannes Gutenberg':
    print("Acertou")
    pontos2 += 1

print('''
3 - Para os estudos em tipografia, uma letra também pode ser chamada de:
A) epístola
B) glifo
C) família
D) cunho
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'B) glifo':
    print('Acertou')
    pontos3 += 1

print('''
4 - Qual das frases a seguir melhor define o que é uma família tipográfica?
A) é um grupo de palavras que podem ser consideradas harmonicamente organizadas em um texto
B) é um conjunto de letras que possuem variações nas suas características anatômicas
C) é o nome dado a uma fonte e que não pode ser replicado em nenhum serviço de disponibilidade de arquivos
D) é o conjunto de caracteres que possuem as mesmas características anatômicas, independente das suas variações
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'D) é o conjunto de caracteres que possuem as mesmas características anatômicas, independente das suas variações':
    print('Acertou')
    pontos4 += 1

print('''
5 - Em relação à anatomia do tipo, temos a medida da altura das letras minúsculas de uma determinada fonte, que chamamos de:
A) altura das minúsculas
B) altura-x
C) altura-y
D) altura-mini
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'B) altura-x':
    print('Acertou')
    pontos5 += 1

print('''
6 - As letras g, j e Q possuem uma pequena curva que geralmente é representada na área da descendente. Qual é o nome que se dá a essa curva nas letras indicadas?
A) cauda
B) enlace
C) esporão
D) perna
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'A) cauda':
    print('Acertou')
    pontos6 += 1

print('''
7 - As fontes _____ são aquelas com bastante efeitos visuais, enfeitadas e até mesmo curiosas. Também são chamadas de fontes comemorativas.
A) serifadas
B) monoespaçadas
C) script
D) display
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'D) display':
    print('Acertou')
    pontos7 += 1

print('''
8 - Em CSS, para definir que tipo de fonte será utilizado a um determinado elemento HTML, usamos a propriedade:
A) font-type
B) font-face
C) font-name
D) font-family
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'D) font-family':
    print('Acertou')
    pontos8 += 1

print('''
9 - Na maioria dos casos, o tamanho padrão de uma fonte é de _____px, o que equivale a _____em na medida referencial.
A) 10px / 10em
B) 30px / 2em
C) 16px / 1em
D) 12px / 10em
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'C) 16px / 1em':
    print('Acertou')
    pontos9 += 1

print('''
10 - No exemplo de uso da shorthand font: italic bold 1em Arial, Helvetica, sans-serif; quais são as propriedades que estão sendo definidas, na ordem?
A) font-style, font-weight, font-size, font-family
B) font-variant, font-weight, font-size, font-style
C) font-style, font-variant, font-style, font-family
D) font-family, font-variant, font-size, font-style
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'A) font-style, font-weight, font-size, font-family':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
