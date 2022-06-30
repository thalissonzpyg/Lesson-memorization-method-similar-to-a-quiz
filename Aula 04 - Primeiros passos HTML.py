print(''' 

    Seja bem-vindo a prova da Aula 04 - Primeiros passos HTML do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Qual dos programas a seguir é o único que não pode ser utilizado para escrever códigos em texto sem formatação para HTML + CSS + JS?
A) Atom
B) VIM
C) Brackets
D) Word 
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'D) Word':
    print("Acertou")
    pontos1 += 1

print('''
2 - Qual é a empresa que fabrica o VSCode, o editor que escolhemos para escrever códigos para nosso curso? 
A) Microsoft 
B) Apple
C) Adobe
D) Google 
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'A) Microsoft':
    print("Acertou")
    pontos2 += 1

print('''
3 - É possível usar o VSCode em idioma Português do Brasil? 
A) Sim. O editor já é instalado em PT-BR como padrão 
B) Sim. Porém, precisamos escolher o idioma durante a instalação
C) Sim. Mas não existe suporte nativo para PT-BR, mas existe uma extensão para isso. 
D) Não. O VSCode ainda não funciona em PT-BR. 
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'C) Sim. Mas não existe suporte nativo para PT-BR, mas existe uma extensão para isso':
    print('Acertou')
    pontos3 += 1

print('''
4 - Qual é a opção que devemos habilitar nas configurações para que as instruções muito longas sejam quebradas em várias linhas automaticamente?
A) Wrap Line 
B) Multi Line 
C) Auto Break
D) Word Wrap
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'D) Word Wrap':
    print('Acertou')
    pontos4 += 1

print('''
5 - Qual é o caminho correto que devemos seguir para ligar o salvamento automático de arquivos no VSCode? 
A) Arquivo > Salvar Automaticamente
B) Terminal > Salvar Automaticamente 
C) Configurações > Salvar Automaticamente 
D) Editar > Salvar Automaticamente 
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'A) Arquivo > Salvar Automaticamente':
    print('Acertou')
    pontos5 += 1

print('''
6 - Qual é o nome do arquivo principal de um site feito em HTML, que será aberto assim que o visitante solicitar a abertura do site?
A) first.html 
B) www.html 
C) index.html 
D) 001.html 
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'C) index.html':
    print('Acertou')
    pontos6 += 1

print('''
7 - Ao criar um arquivo HTML, o VSCode tem um atalho simples para criar o código base para um arquivo desse tipo. Que atalho é esse?  
A) ! + Enter
B) # + Enter 
C) ^ + Enter 
D) ? + Enter 
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'A) ! + Enter':
    print('Acertou')
    pontos7 += 1

print('''
8 - Qual é a tag HTML para criar uma
linha horizontal no corpo do navegador?
A) <line> 
B) <row> 
C) <!--> 
D) <hr> 
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'D) <hr>':
    print('Acertou')
    pontos8 += 1

print('''
9 - Para criar um parágrafo em HTML, usamos a tag: 
A) <p> 
B) <para> 
C) <paragraph> 
D) <h1> 
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'A) <p>':
    print('Acertou')
    pontos9 += 1

print('''
10 - A tag <title> é adicionada dentro
de qual área de um documento HTML? 
A) <h1>
B) <p> 
C) <head> 
D) <body> 
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'C) <head>':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
