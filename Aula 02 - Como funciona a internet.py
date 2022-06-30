print(''' 

    Seja bem-vindo a prova da Aula 02 - Como funciona a internet do curso de HTML/CSS do Guanabara.  
    
    Você responderá 10 perguntas e verá o quanto entende do assunto.
    
    ''')
print('Vamos começar!')

print('''1 - Atualmente, na maioria das transmissões feitas mundialmente pela Internet, por onde a maior quantidade de sinais vai passar?
A) Por baixo da água, em cabos submarinos
B) Por sinais de satélite, partindo de antenas
C) Por antenas de comunicação via celular
D) Por cabos enterrados nos continentes
''')

resposta = input('''Qual é a resposta?
''')
pontos1 = 0

if resposta == 'A) Por baixo da água, em cabos submarinos':
    print("Acertou")
    pontos1 += 1

print('''
2 - Os dados que vão trafegar pelas redes e chegar aos computadores vão estar codificados em:
A) letras e símbolos
B) conjuntos de bits e bytes (0s e 1s)
C) ondas codificadas sem um padrão definido
D) arquivos de imagem / textos
''')

resposta = input('''Qual é a resposta?
''')
pontos2 = 0

if resposta == 'B) conjuntos de bits e bytes (0s e 1s)':
    print("Acertou")
    pontos2 += 1

print('''
3 - Quando um sinal está representado em um determinado tipo de onda (codificação) e precisamos transformá-lo em outro tipo, dizemos que estamos realizando uma:
A) extração
B) composição
C) descompressão
D) modulação
''')

resposta = input('''Qual é a resposta?
''')
pontos3 = 0

if resposta == 'D) modulação':
    print('Acertou')
    pontos3 += 1

print('''
4 - Na maioria das vezes que estamos realizando algum tipo de acesso via rede, um lado será o ______ e vai solicitar o uso de um determinado serviço. Quem vai atender à essa solicitação é considerado um _____.
A) servidor / cliente
B) cliente / servidor
C) solicitante / provedor
D) provedor / servidor
''')

resposta = input('''Qual é a resposta?
''')
pontos4 = 0

if resposta == 'B) cliente / servidor':
    print('Acertou')
    pontos4 += 1

print('''
5 - Todo e qualquer ponto conectado à Internet recebe um identificador, que se chama “endereço IP”. Na versão IPv4, um endereço possui _____ bits, já a versão IPv6 necessita de _____ bits para identificar um ponto. 
A) 32 bits / 64 bits
B) 64 bits / 128 bits
C) 32 bits / 128 bits
D) 16 bits / 64 bits 
''')

resposta = input('''Qual é a resposta?
''')
pontos5 = 0

if resposta == 'C) 32 bits / 128 bits':
    print('Acertou')
    pontos5 += 1

print('''
6 - Qual é o serviço (e seu respectivo significado) responsável por resolver os endereços IP dos servidores a partir de um nome? Ele faz com que os usuários não precisem decorar números IP (que inclusive, mudam constantemente)
A) DNS - Domain Name System 
B) DNS - Domain Name Service
C) DNS - Domain Name Server
D) DNS - Data Name Server
''')

resposta = input('''Qual é a resposta?
''')
pontos6 = 0

if resposta == 'C) DNS - Domain Name Server':
    print('Acertou')
    pontos6 += 1

print('''
7 - Uma URL é composta por vários componentes. Na URL https://www.github.com/gustavoguanabara, por exemplo, são respectivamente o domínio, o protocolo e o caminho os itens apontados na opção:
A) github.com / https / gustavoguanabara
B) github.com / www / gustavoguanabara
C) github / https / gustavoguanabara
D) www.github.com / www / gustavoguanabara
''')

resposta = input('''Qual é a resposta?
''')
pontos7 = 0

if resposta == 'A) github.com / https / gustavoguanabara':
    print('Acertou')
    pontos7 += 1

print('''
8 - Quando chegar a hora de construir nossos sites, devemos informar aos nossos clientes que geralmente o domínio tem uma taxa de pagamento _____, enquanto as hospedagens são de pagamento _____ de forma geral.
A) mensal / anual
B) anual / diário
C) mensal / diário
D) anual / mensal
''')

resposta = input('''Qual é a resposta?
''')
pontos8 = 0

if resposta == 'D) anual / mensal':
    print('Acertou')
    pontos8 += 1

print('''
9 - Os domínios possuem seus Top Level Domains. Vejamos como exemplo os domínios estudonauta.com.br e cursoemvideo.com. No primeiro caso, temos um _____ e no segundo caso, temos um _____.
A) GTLD / ccTLD
B) ccTLD / GTLD
C) DTLD / CTLD
D) CTLD / DTLD
''')

resposta = input('''Qual é a resposta?
''')
pontos9 = 0

if resposta == 'B) ccTLD / GTLD':
    print('Acertou')
    pontos9 += 1

print('''
10 - Todo bom serviço de hospedagem deve fornecer recursos e serviços valiosos para seus clientes. Entre os itens a seguir, qual é o único que NÃO É oferecido por uma empresa de hospedagem?
A) atendimento de suporte
B) espaço em disco para armazenamento
C) manutenção periódica no PC do cliente
D) backup constante dos arquivos e bancos de dados
''')

resposta = input('''Qual é a resposta?
''')
pontos10 = 0

if resposta == 'C) manutenção periódica no PC do cliente':
    print('Acertou')
    pontos10 += 1


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10)
print('Se você tirou 10, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
