print(''' 

    Seja bem-vindo a prova da Aula 10 - Ligações em toda parte do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Toda vez que estamos em um site e clicamos em uma área sensível que nos leva a outro ponto ou a outro documento, estamos interagindo com um:
A) hyperlink
B) metadado
C) ancoramento
D) subdomínio
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'A) hyperlink':
    print("Acertou")
    pontos1 += 1

print('''
2 - Para criarmos links em nosso site, utilizaremos a tag:
A) <link>
B) <l>
C) <lnk>
D) <a>
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'D) <a>':
    print("Acertou")
    pontos2 += 1

print('''
3 - Dentro da tag de âncora, o parâmetro _____ serve para indicar a URL completa para onde o fluxo será desviado.
A) destiny
B) ref
C) href
D) link
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'C) href':
    print('Acertou')
    pontos3 += 1

print('''
4 - Também é possível indicar o idioma principal de um documento configurado em uma âncora usando o parâmetro:
A) lang
B) reflang
C) rellang
D) hreflang
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'D) hreflang':
    print('Acertou')
    pontos4 += 1

print('''
5 - A tag de âncora também suporta o parâmetro target, onde podemos colocar vários valores, exceto: 
A) _parent
B) _self
C) _external
D) _top
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'C) _external':
    print('Acertou')
    pontos5 += 1

print('''
6 - A maneira mais recomendada de indicar um link externo é configurando o seguinte par de parâmetro e valor:
A) external = “true”
B) href = “external”
C) target = “_external”
D) rel = “external”
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'D) rel = "external"':
    print('Acertou')
    pontos6 += 1

print('''
7 - Ao criar links que levam a documentos que estão em pastas imediatamente superiores na hierarquia do site, devemos adicionar ao link os símbolos:
A) ../
B) </  
C) #/
D) -/
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'A) ../':
    print('Acertou')
    pontos7 += 1

print('''
8 - Ao criar um link para download, recomenda-se configurar os parâmetros adicionais:
A) link e download 
B) download e type
C) link e type
D) download e link
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'B) download e type':
    print('Acertou')
    pontos8 += 1

print('''
9 - O parâmetro type de um link que vai servir para baixar um arquivo PDF deve estar configurado com o valor:
A) ebook/pdf
B) file/pdf
C) application/pdf
D) download/pdf  
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'C) application/pdf':
    print('Acertou')
    pontos9 += 1

print('''
10 - Os valores application/zip, audio/aac e font/ttf são exemplos de:
A) type files
B) media types
C) multimedia patterns 
D) format files
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'B) media types':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
