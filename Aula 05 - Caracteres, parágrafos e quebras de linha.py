print(''' 

    Seja bem-vindo a prova da Aula 05 - Caracteres, parágrafos e quebras de linha do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Os símbolos de < e de > são usados em HTML para delimitar tags. Mas se quisermos mostrá-los no navegador, precisamos representá-los como: 
A) &lt; e &gt;
B) #lt; e #gt;
C) &menor; e &maior;
D) #<; e #>;
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'A) &lt; e &gt;':
    print("Acertou")
    pontos1 += 1

print('''
2 - Dentro de um parágrafo no código HTML, se escrevermos uma palavra em cada linha, elas serão apresentadas no navegador de que maneira? 
A) uma em cima da outra
B) uma ao lado da outra
C) exatamente da maneira que digitamos
D) nenhuma palavra será exibida
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'B) uma ao lado da outra':
    print("Acertou")
    pontos2 += 1

print('''
3 - A qualquer momento do código HTML, se quisermos criar uma quebra de linha, devemos usar qual tag?
A) <row>
B) <new>
C) <br>
D) Não precisa usar tag, é só apertar ENTER
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'C) <br>':
    print('Acertou')
    pontos3 += 1

print('''
4 - A melhor estratégia para criar um espaço relativo a dez quebras de linha em nosso site é: 
A) usar a tag de quebra por 10 vezes consecutivas
B) usar a tag de parágrafo por 5 vezes consecutivas
C) usar configurações de estilo em CSS e especificar o espaçamento todo de uma vez
D) não existe a possibilidade de criar um espaçamento desse tamanho 
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'C) usar configurações de estilo em CSS e especificar o espaçamento todo de uma vez':
    print('Acertou')
    pontos4 += 1

print('''
5 - Os códigos como &euro; para mostrar o símbolo € nas páginas são conhecidos pelo nome de: 
A) HTML entities 
B) Symbol codes
C) HTML symbols 
D) Symbol entities
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'A) HTML entities':
    print('Acertou')
    pontos5 += 1

print('''
6 - Que código utilizaremos para mostrar uma seta apontando para a direita (→) na página? 
A) &right;
B) &rarrow;
C) &arrow;
D) &rarr;
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'D) &rarr':
    print('Acertou')
    pontos6 += 1

print('''
7 - Qual site é recomendado nas aulas para buscar os códigos usados para representar os emojis?
A) WikiMoji 
B) EmojiBook 
C) Emojipedia
D) Symbolpedia 
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'C) Emojipedia':
    print('Acertou')
    pontos7 += 1

print('''
8 - Se o código de um emoji é U+1F913, como devemos representá-lo em nosso código HTML? 
A) U+1F913;
B) &#X+1F913;
C) &#xU1F913;
D) &#x1F913; 
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'D) &#x1F913':
    print('Acertou')
    pontos8 += 1

print('''
9 - A marca br significa: 
A) Que o idioma está em Português do Brasil
B) Break row, ou quebra de linha
C) Break right, ou quebra à direita
D) Broked row, ou linha quebrada 
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'B) Break row, ou quebra de linha':
    print('Acertou')
    pontos9 += 1

print('''
10 - Qual é o TLD do domínio do site que indicamos para buscar emojis? 
A) .org 
B) .gov 
C) .com 
D) .edu 
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'A) .org':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
