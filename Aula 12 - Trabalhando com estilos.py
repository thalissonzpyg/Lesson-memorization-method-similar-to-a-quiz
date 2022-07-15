print(''' 

    Seja bem-vindo a prova da Aula 12 - Trabalhando com estilos do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 -  A sigla CSS significa:
A) Content Style Setup
B) Content Smart Sheets
C) Cascading Style Sheets
D) Cascading Setup Style
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'C) Cascading Style Sheets':
    print("Acertou")
    pontos1 += 1

print('''
2 - Ao configurar os estilos com a técnica inline, as propriedades CSS são colocadas em que local?
A) Dentro da própria tag HTML, em um parâmetro chamado style
B) Dentro da área <head> do documento HTML, na área delimitada por <style>
C) Em um arquivo separado dentro da própria pasta onde o documento HTML está
D) Dentro de uma pasta especial chamada /style que fica no diretório atual do site 
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'A) Dentro da própia tag HTML, em um parâmetros chamado style':
    print("Acertou")
    pontos2 += 1

print('''
3 - O que aconteceu com configurações como <body bgcolor=“blue”> e <font color=“yellow”> que eram usadas em sites mais antigos? 
A) Continuam funcionando perfeitamente e podem ser usadas normalmente
B) Continuam funcionando, mas não é nada recomendável pois as CSS são mais atuais 
C) Não funcionam mais de forma alguma
D) Ainda são a única opção de mudar
cores
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'C) Não funcionam mais de forma alguma':
    print('Acertou')
    pontos3 += 1

print('''
4 - Qual das opções a seguir é a única que configura corretamente a cor da letra de um título usando CSS inline?
A) <h1 color=“blue”>Título</h1>
B) <h1 style=“blue”>Título</h1>
C) <h1 style=“font-color: blue”>Título</h1>
D) <h1 style=“color: blue”>Título</h1>
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'D) <h1 style="color: blue">Título</h1>':
    print('Acertou')
    pontos4 += 1

print('''
5 - Para usar a técnica de estilos
internos, a tag <style> deve estar em
que local?
A) logo depois da tag HTML que queremos configurar
B) dentro da área <head> do seu documento HTML
C) no final do arquivo, logo depois do </body>
D) em qualquer lugar do arquivo HTML
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'B) dentro da área <head> do seu documento HTML':
    print('Acertou')
    pontos5 += 1

print('''
6 - Em um mesmo documento HTML, utilizamos as técnicas de CSS interno e CSS inline para mudar a cor de um elemento e acabamos usando duas cores diferentes. Quais configurações vão prevalecer na versão final do site?
A) as configurações duplicadas feitas nas CSS inline vão prevalecer
B) as configurações duplicadas feitas nas CSS internas vão prevalecer
C) as duas configurações vão prevalecer e o texto será exibido duplicado com cores diferentes
D) o seu navegador vai decidir qual cor utilizar. Não existe uma regra para esses casos.
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'A) as configurações duplicadas feitas nas CSS inline vão prevalecer':
    print('Acertou')
    pontos6 += 1

print('''
7 - Para utilizar estilos CSS externos, devemos usar a tag _____ no documento HTML para fazer o carregamento:
A) <style>
B) <css>
C) <external>
D) <link>
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'D) <link>':
    print('Acertou')
    pontos7 += 1

print('''
8 - A tag de carga de estilos externos deve estar localizada em que local do documento HTML?
A) deve ser a primeira linha do arquivo HTML
B) deve estar dentro da área <body> do documento
C) deve estar dentro da área <head> do documento
D) pode estar em qualquer lugar, desde que esteja dentro do documento HTML
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'C) deve estar dentro da área <head> do documento':
    print('Acertou')
    pontos8 += 1

print('''
9 - Para que os arquivos externos em CSS tenham compatibilidade com caracteres acentuados , devemos adicionar a regra:
A) @UTF-8;
B) @charset “UTF-8”;
C) @charset “PT-BR”;
D) @PT-BR;
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'B) @charset "UTF-8";':
    print('Acertou')
    pontos9 += 1

print('''
10 - No fim das contas, vamos dar preferência à técnica de _____ sempre que for possível e vamos tentar evitar a técnica de _____ em nossos sites. A opção que apresenta os termos que completam as lacunas na ordem correta é: 
A) CSS externo / CSS interno
B) CSS inline / CSS interno
C) CSS externo / CSS inline
D) CSS interno / CSS externo
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'C) CSS externo / CSS inline':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
