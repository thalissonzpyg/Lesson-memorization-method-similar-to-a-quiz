print(''' 

    Seja bem-vindo a prova da Aula 11 - Imagens dinâmicas, áudios e vídeos do curso de HTML/CSS do Guanabara. 
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Qual das afirmações a seguir é a mais correta em relação ao cuidado que devemos ter em relação ao uso de imagens em sites?
A) Use sempre a imagem com maior qualidade e resolução possível 
B) Use sempre a imagem com menor qualidade e resolução possível 
C) Use sempre a imagem com qualidade e resolução balanceadas 
D) Use sempre a menor quantidade de imagens para não deixar o site pesado
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'C) Use sempre a imagem com qualidade e resolução balanceadas':
    print("Acertou")
    pontos1 += 1

print('''
2 - Deixar um site “pesado” com imagens grandes pode gerar:
A) Aumento nas visitas por conta da qualidade visual 
B) Diminuição na taxa de retenção e possível penalização em mecanismos de busca
C) Aumento na taxa de retenção, pois o usuário passa mais tempo no site 
D) Diminuição no tempo das visitas, mas isso acaba melhorando a indexação 
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'B) Diminuição na taxa de retenção e possível penalização em mecanismos de busca':
    print("Acertou")
    pontos2 += 1

print('''
3 - Para usar imagens dinâmicas em nossos sites, devemos aprender a usar três tags, que são: 
A) <picture>, <source> e <img> 
B) <image>, <picture> e <source> 
C) <picture>, <image> e <img>
D) <img>, <source> e <image>
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'A) <picture>, <source> e <img>':
    print('Acertou')
    pontos3 += 1

print('''
4 - A tag <source> possui o parâmetro _____ para configurar as dimensões da mídia, o _____ para indicar o formato da mídia e o parâmetro _____ para indicar o arquivo de destino. A única opção que mostra os parâmetros que preenchem as colunas na ordem correta é: 
A) media, type e srcset
B) type, media e srcset
C) size, format e src
D) size, type e src
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'A) media, type e srcset':
    print('Acertou')
    pontos4 += 1

print('''
5 - Podemos adicionar arquivos de áudio reproduzíveis às nossas páginas usando a tag: 
A) <sound>
B) <music>
C) <podcast>
D) <audio>
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'D) <audio>':
    print('Acertou')
    pontos5 += 1

print('''
6 - Qual dos valores a seguir é o único que não é um parâmetro da tag de áudio?
A) controls
B) autoplay
C) player
D) loop
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'C) player':
    print('Acertou')
    pontos6 += 1

print('''
7 - Quando inserimos um áudio no site, qual é o comportamento padrão do navegador em relação à carga do conteúdo?
A) o arquivo de áudio não será carregado até que o visitante aperte o Play
B) o arquivo de áudio será completamente carregado, mesmo que nunca seja apertado o Play  
C) os primeiros minutos de áudio serão carregados para facilitar a reprodução
D) apenas os metadados do arquivo (informações básicas sobre o arquivo) serão carregados automaticamente 
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'B) o arquivo de áudio será completamente carregado, mesmo que nunca seja apertado o Play':
    print('Acertou')
    pontos7 += 1

print('''
8 - Para carregar vídeos hospedados localmente, podemos usar a tag HTML:
A) <video> 
B) <iframe>
C) <media>
D) <youtube>
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'A) <video>':
    print('Acertou')
    pontos8 += 1

print('''
9 - Quais são os formatos de vídeo que devemos considerar para manter a compatibilidade com a maioria dos navegadores?
A) .mov .mp4 .avi .webm
B) .m4v .ogv .avi .mov
C) .mp4 .m4v .webm .ogv
D) .mp4 .mov .webm .avi 
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'C) .mp4 .m4v .webm .ogv':
    print('Acertou')
    pontos9 += 1

print('''
10 - Para inserir vídeos do YouTube no nosso site, usamos a tag: 
A) <video>
B) <iframe>
C) <link> 
D) <media>
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'B) <iframe>':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
