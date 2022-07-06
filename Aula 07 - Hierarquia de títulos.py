print(''' 

    Seja bem-vindo a prova da Aula 07 - Hierarquia de títulos do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Normalmente nossos textos são organizados em sessões, e cada uma pode possuir um título. Em HTML5 existe alguma limitação em relação a quantidade de títulos que um documento pode ter?
A) sim. Só podemos ter no máximo seis títulos
B) não. Um texto pode ter quantos títulos e quantos níveis for necessário
C) não. Um texto pode ter vários títulos, mas apenas um máximo de seis níveis
D) sim. Podemos ter até 12 títulos, dois para cada nível
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'C) não. Um texto pode ter vários títulos, mas apenas um máximo de seis níveis':
    print("Acertou")
    pontos1 += 1

print('''
2 - Os títulos podem ser criados em seis níveis diferentes, usando as tags:
A) <head1> até <head6>
B) <header1> até <header6>
C) <title1> até <title6>
D) <h1> até <h6>
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'D) <h1> até <h6>':
    print("Acertou")
    pontos2 += 1

print('''
3 - Se estamos em um ponto do texto com título nível 3 e quer em os aprofundar esse assunto com um subtítulo, devemos usar qual nível? Lembrese de seguir a recomendação da W3C.
A) nível 4
B) nível 2
C) nível 3
D) qualquer nível, de 3 até 6
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'A) nível 4':
    print('Acertou')
    pontos3 += 1

print('''
4 - O título principal de um determinado documento ou página deverá sempre ser definido com um título de qual nível? 
A) nível 1
B) nível 2 
C) nível 3
D) tanto faz, o que importa é ser um título
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'A) nível 1':
    print('Acertou')
    pontos4 += 1

print('''
5 - Muitos dizem que um documento só deve ter um título de nível 1 (principal). Essa crença é uma…
A) verdade. Somente um título deve ser o principal e todos os demais deverão ter outros níveis.
B) lenda. A recomendação é que não exista nenhum título de nível 1.
C) verdade. Se colocarmos mais de um título nível 1, seu site não será indexado pelo Google.
D) lenda. É possível adicionar mais de um título de nível 1, só devemos nos dedicar a descrevê-lo muito bem para facilitar a indexação por mecanismos de busca.
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'D) lenda. É possível adicionar mais de um título de nível 1, só devemos nos dedicar a descrevê-lo muito bem para facilitar a indexação por mecanismos de busca.':
    print('Acertou')
    pontos5 += 1

print('''
6 - O estudo da indexação do conteúdo de um site por meio de mecanismos de busca é conhecido popularmente como:
A) SEO - Seek Energy Organization
B) SEO - Search Engine Optimization
C) SEO - Seek Engine Order 
D) SEO - Search Elements Order
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'B) SEO - Search Engine Optimization':
    print('Acertou')
    pontos6 += 1

print('''
7 - Todo documento HTML deverá ter obrigatoriamente algum título de nível 6?
A) não. Os títulos de menor nível serão usados apenas se for necessário
B) sim. Pelo menos um título de nível 6
C) não. Os títulos de nível 6 devem ser evitados para não confundir o visitante
D) sim. É necessário ter dois ou mais títulos de nível 6
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'A) não. Os títulos de menor nível serão usados apenas se for necessário':
    print('Acertou')
    pontos7 += 1

print('''
8 - Quando estamos desenvolvendo um site e o conteúdo ainda não foi definido, uma técnica bastante utilizada é usar blocos de texto genéricos com conteúdo composto por palavras em latim. Esses blocos são mais conhecidos pelo termo:
A) Lorem Ipsum
B) Ipsum Lorem
C) Carpe Diem
D) Memento Vivere
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'A) Lorem Ipsum':
    print('Acertou')
    pontos8 += 1

print('''
9 - Para criar um bloco de texto com termos genéricos em latim usando o VS Code, basta digitar a palavra ____ e depois apertar a tecla _____.
A) lorem / Esc 
B) ipsum / Enter 
C) lorem / Enter 
D) ipsum / Esc
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'C) lorem / Enter':
    print('Acertou')
    pontos9 += 1

print('''
10 - Se não configurarmos o estilo de cada título, os textos dentro da tag de nível 1 terão letras _____, enquanto aqueles dentro da tag de nível 6 terão letras _____. Qual dos itens abaixo é o único preenche corretamente as lacunas desta frase na ordem correta?
A) menor / maior
B) em negrito / em itálico
C) maior / menor
D) azuis / vermelhas
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'C) maior / menor':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
