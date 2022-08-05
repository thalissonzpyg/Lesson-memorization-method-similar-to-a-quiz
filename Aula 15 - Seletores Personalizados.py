print(''' 

    Seja bem-vindo a prova da Aula 15 - Seletores Personalizados do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 -  Em um mesmo documento HTML, vários elementos podem possuir o mesmo _____ para criarmos formatações em grupo com CSS, mas só podemos ter um elemento com um _____ único para criar formatações individuais.
A) id / class
B) class / id
C) style / class
D) code / id
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'B) class / id':
    print("Acertou")
    pontos1 += 1

print('''
2 - Toda configuração de folhas de estilo que fizermos para um determinado id, deve ser feita iniciando pelo símbolo _____ antes do identificador. Já as configurações para um determinado class serão feitas usando o símbolo _____ antes do nome da classe.
A) # e .
B) . e #
C) # e $
D) $ e .
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'A) # e .':
    print("Acertou")
    pontos2 += 1

print('''
3 - Como já sabemos, existem três técnicas para inserir configurações CSS a um código HTML5: inline, local e externa. Se uma página usa as três técnicas ao mesmo tempo e cria uma configuração duplicada para uma determinada propriedade, qual delas vai se sobrepor às demais?
A) CSS local
B) CSS externo
C) CSS inline
D) Não existe ordem de prioridades para casos de duplicidade
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'C) CSS inline':
    print('Acertou')
    pontos3 += 1

print('''
4 - Uma pseudo-classe CSS é uma palavra-chave adicionada às declarações de um seletor após um sinal de
A) dois pontos (:)
B) ponto-e-vírgula (;)
C) porcentagem (%)
D) arroba (@)
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'A) dois pontos (:)':
    print('Acertou')
    pontos4 += 1

print('''
5 - Qual dos itens a seguir é o único que não se refere a uma pseudo-classe CSS?
A) hover
B) before
C) checked
D) empty
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'B) before':
    print('Acertou')
    pontos5 += 1

print('''
6 - Para realizar configurações de formatação em um pedaço específico do elemento HTML referenciado (a primeira letra de um texto, por exemplo), devemos aprender a criar seletores para _____.
A) pseudo-classes
B) pseudo-textos
C) pseudo-formatos
D) pseudo-elementos
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'D) pseudo-elementos':
    print('Acertou')
    pontos6 += 1

print('''
7 - Qual dos itens a seguir é o único que não se refere a um pseudo-elemento CSS?
A) first-line
B) first-letter
C) active
D) before
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'C) active':
    print('Acertou')
    pontos7 += 1

print('''
8 - Considere que temos o seguinte link em uma mesma página: <a href=“pag002.html” class=“link”>Página 2</a>. Qual será o nome do seletor para configurarmos o que vai acontecer quando o usuário mover o cursor do mouse por cima do link?
A) a#link:hover
B) a.hover:link
C) a.hover#link
D) a.link:hover
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'D) a.link:hover':
    print('Acertou')
    pontos8 += 1

print('''
9 - Se quisermos que todos os links de uma página tenham um símbolo » depois do texto, devemos usar a formatação:
A) a::after { content: ‘»’; }
B) a { content: ‘»’; }::after
C) after::a { content: ‘»’; }
D) ::after { content: ‘»’; } a
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'A) a::after { content: '>'; }':
    print('Acertou')
    pontos9 += 1

print('''
10 - Podemos definir seletores com o símbolo de maior que (>) para indicar o que chamamos de:
A) larger tag
B) next tag
C) direct children
D) alternative element
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'C) direct children':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
