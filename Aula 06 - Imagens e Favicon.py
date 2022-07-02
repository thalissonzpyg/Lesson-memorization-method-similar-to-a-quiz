print(''' 

    Seja bem-vindo a prova da Aula 06 - Imagens e Favicon do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Quando você está criando um site ou qualquer outro tipo de conteúdo, deve se preocupar bastante com os direitos de uso de determinada mídia (imagem, som, vídeo, etc). Qual dos itens a seguir melhor define esse assunto? 
A) Se a mídia estiver em um site público como Google e YouTube, podemos usar sem problemas. 
B) Não podemos usar nenhuma mídia sem a prévia autorização do seu criador.
C) Enquanto estamos estudando e aprendendo, temos total permissão para usar mídias de terceiros. 
D) Podemos usar qualquer mídia e pagar uma multa quando formos descobertos.
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'C) Enquanto estamos estudando e aprendendo, temos total permissão para usar mídias de terceiros':
    print("Acertou")
    pontos1 += 1

print('''
2 - Qual dos itens a seguir é incorreto quando o assunto é não passar por problemas relacionados a direitos autorais?
A) seja o criador das suas próprias artes
B) consiga uma autorização legal do detentor dos direitos autorais
C) compre os direitos de uso em sites especializados e use quantas vezes quiser
D) use imagens com licenças públicas, como Creative Commons
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'C) compre os direitos de uso em sites especializados e use quantas vezes quiser':
    print("Acertou")
    pontos2 += 1

print('''
3 - Qual dos sites a seguir é especializado em disponibilizar apenas imagens para uso liberado, sem direitos autorais? 
A) Google Imagens
B) Getty Imagens
C) Shutterstock
D) Pexels
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'D) Pexels':
    print('Acertou')
    pontos3 += 1

print('''
4 - Qual foi o formato de imagens criado na década de 80 com o objetivo de reduzir o tamanho dos arquivos das imagens, sem reduzir sua dimensão? 
A) JPEG
B) PNG 
C) GIF
D) ZIP
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'A) JPEG':
    print('Acertou')
    pontos4 += 1

print('''
5 - Qual é o único dos formatos a seguir que possui suporte para imagens com partes transparentes e compactadas?
A) JPEG  
B) BMP 
C) TIFF
D) PNG 
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'D) PNG':
    print('Acertou')
    pontos5 += 1

print('''
6 - O que significa a sigla JPEG? 
A) Joint Photographics Experts Group
B) JPG Photo Enhancement Graphic 
C) Join Picture Enlarge Group 
D) JPG Photographics Enhancement Group 
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'A) Joint Photographics Experts Group':
    print('Acertou')
    pontos6 += 1

print('''
7 - Muita gente fica na dúvida sobre o tamanho da imagem
A) use sempre a melhor qualidade possível para que seu site fique bonito 
B) use sempre a pior qualidade possível, pois os sites precisam ser rápidos
C) tente balancear sempre qualidade e tamanho, para que seu site não fique pesado mas não se esqueça da experiência proporcionada ao seu visitante
D) deixe o visitante escolher se quer imagens grandes ou sites rápidos
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'C) tente balancear sempre qualidade e tamanho, para que seu site não fique pesado mas não se esqueça da experiência proporcionada ao seu visitante':
    print('Acertou')
    pontos7 += 1

print('''
8 - Qual é a tag usada na HTML para inserir imagens como parte do conteúdo do site? 
A) <image>
B) <photo>
C) <picture> 
D) <img> 
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'D) <img>':
    print('Acertou')
    pontos8 += 1

print('''
9 - Dentro da tag para inserir a imagem, usamos um parâmetro especial para indicar a localização da imagem a ser carregada. Que parâmetro é esse? 
A) src
B) source
C) photo
D) jpeg
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'A) src':
    print('Acertou')
    pontos9 += 1

print('''
10 - Para configurar uma imagem como ícone de favoritos de uma página (favicon), usamos a tag _____ dentro da área ________ do seu site. Qual dos itens a seguir, é o único que preenche corretamente as lacunas da frase anterior?  
A) <img> / <body>
B) <favicon> / <head> 
C) <link> / <head> 
D) <meta> / <body> 
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'C) <link> / <head>':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
