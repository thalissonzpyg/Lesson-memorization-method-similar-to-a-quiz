print(''' 

    Seja bem-vindo a prova da Aula 08 - Formatação de Textos do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - A versão anterior da linguagem, a HTML4 era bastante focada no(a) _____ do conteúdo. Já a versão HTML5 já fica mais voltada para o(a) _____ da estrutura desse conteúdo.
A) ordenação/ significado
B) forma / significado
C) ordenação / forma
D) forma / ordenação
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'B) forma / significado':
    print("Acertou")
    pontos1 += 1

print('''
2 - A HTML5 chegou com a proposta de definir as chamadas ______, onde cada instrução passa a ter um significado, não apenas uma forma.
A) tags obsoletas
B) tags mecânicas
C) tags objetivas
D) tags semânticas
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'D) tags semânticas':
    print("Acertou")
    pontos2 += 1

print('''
3 - Na lista a seguir, qual é a única tag que é focada em significado e não em forma?
A) <b>
B) <blink>
C) <strong>
D) <applet>
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'C) <strong>':
    print('Acertou')
    pontos3 += 1

print('''
4 - Qual das tags abaixo é a única que ainda permanece ativa? (todas as demais já estão na lista oficial de elementos obsoletos da HTML, disponível no link oficial da W3C) 
A) <big>
B) <center>
C) <aside>
D) <tt>
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'C) <aside>':
    print('Acertou')
    pontos4 += 1

print('''
5 - No lugar da tag <b> para negrito e <i> para itálico, é recomendável usar em HTML5 as novas tags: 
A) <strong> e <em>
B) <bold> e <italic>
C) <strong> e <italic>
D) <bold> e <em>
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'A) <strong> e <em>':
    print('Acertou')
    pontos5 += 1

print('''
6 - Em relação ao tamanho das letras de um texto e o uso das tags <big> e <small> em documentos HTML5 , assinale a única afirmativa correta:
A) a tag <big> ainda pode ser usada, mas a <small> não pode mais
B) todas as duas tags deixaram de existir
C) todas as duas tags seguem funcionando corretamente 
D) a tag <big> deixou de existir e a tag <small> segue funcionando
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'D) a tag <big> deixou de existir e a tag <small> segue funcionando':
    print('Acertou')
    pontos6 += 1

print('''
7 - Quando for para sublinhar um texto no sentido de chamar a atenção para ele, deixamos de usar o antigo <u> e passamos a usar o novo:
A) <underline>
B) <ins>
C) <sub>
D) <strike>
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'B) <ins>':
    print('Acertou')
    pontos7 += 1

print('''
8 - Para criar um texto sobrescrito (como em x2) usamos a tag _____ e para criar um texto subscrito (como em H2O), usamos a tag ______.
A) <sub> / <sup>
B) <up> / <down>
C) <down> / <up>
D) <sup> / <sub>
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'D) <sup> / <sub>':
    print('Acertou')
    pontos8 += 1

print('''
9 - Em HTML5, podemos criar citações utilizando a tag _____, incluindo o parâmetro _____ para indicar o link para o conteúdo original da citação.
A) <cite> / src
B) <blockquote> / cite
C) <quote> / src
D) <cite> / quote
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'B) <blockquote> / cite':
    print('Acertou')
    pontos9 += 1

print('''
10 - Para inverter uma palavra ou frase, devemos usar a tag _____ com o parâmetro dir configurado para o valor _____.
A) <bdo> / rtl
B) <bdo> / ltr
C) <direction> / rtl
D) <direction> / ltr
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'A) <bdo> / rtl':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
