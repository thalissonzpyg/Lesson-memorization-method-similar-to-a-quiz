print(''' 

    Seja bem-vindo a prova da Aula 05 - Como a internet funciona do curso de HTML/CSS do Guanabara. 
    
    Tutorial para memorizar todo o conteúdo:
    - Você vai responder as perguntas de acordo com as respostas configuradas no VSCode;
    - As respostas tem de ser exatamente igual, A e a são diferentes, se atente a isso;
    - Toda vez que você não lembrar ou errar, você vai ler a resposta certa no código do programa 5x, feche o programa e recomece;
    - Repita todo o procedimento até que acerte todas as questões e por fim você terá memorizado todo o conteúdo da aula;
    - Não deixe de praticar, não é por quê acertou todas que já é motivo pra pular para a próxima, sempre pratique mesmo que
    você avance a próxima aula, memorize a próxima aula e continue praticando essa que você já acha q memorizou;
    - Quando se sentir confiante em responder exatamente todas as perguntas toda vez q abre o programa e acerta todas, foco nas próximas aulas.
    
    ''')
print('Vamos começar!')

print('1 - Como é a Representação de Dados de um equipamento eletrônico?')

resposta = input('Digite sua resposta: ')
pontos1 = 0

if resposta == 'Funciona com sinais, e esses sinais são representados para a computação como 0 e 1':
    print('Acertou')
    pontos1 += 5

print('''
2 - Bit e byte: os sinais para a computação são representadas de que forma?''')

resposta = input('Digite sua resposta: ')
pontos2 = 0

if resposta == 'Como ondas quadradas, sinais elétricos com e sem sinal, o com sinal seria o 1 e o sem sinal o 0':
    print('Acertou')
    pontos2 += 5

print('''
3 - Bit e byte: O conjunto 0 e 1 é representado por qual nome?''')

resposta = input('Digite sua resposta: ')
pontos3 = 0

if resposta == 'Binary Digit (bit), 1 bit é um 0 ou um 1':
    print('Acertou')
    pontos3 += 5

print('''
4 - Bit e byte: A computação exige uma porção mínima de dígitos para que se represente um dado, qual é? E qual dado representa a letra A e é em qual representação de código multibyte?''')

resposta = input('Digite sua resposta: ')
pontos4 = 0

if resposta == '8 dígitos, 01000001, UTF-8':
    print('Acertou')
    pontos4 += 5

print('''
5 - O computador entende qual tipo de ondas? E essa onda representa qual tipo de ondas/dígitos?''')

resposta = input('Digite sua resposta: ')
pontos5 = 0

if resposta == 'Ondas quadradas, ondas binárias/binary digit':
    print('Acertou')
    pontos5 += 5

print('''
6 - Como é formado 1 byte?''')

resposta = input('Digite sua resposta: ')
pontos6 = 0

if resposta == '8 bits = 1 byte':
    print('Acertou')
    pontos6 += 5

print('''
7 - Nós humanos trabalhamos com qual base?''')

resposta = input('Digite sua resposta: ')
pontos7 = 0

if resposta == '10, ou seja, 1000g = 1kg':
    print('Acertou')
    pontos7 += 5

print('''
8 - Na computação nós trabalhamos com qual base?''')

resposta = input('Digite sua resposta: ')
pontos8 = 0

if resposta == '2, ou seja, 2^10 = 1024 bytes = 1 KB':
    print('Acertou')
    pontos8 += 5

print('''
9 - Qual é a tabela de representação de bytes?''')

resposta = input('Digite sua resposta: ')
pontos9 = 0

if resposta == 'Byte, KiloByte, MegaByte, GigaByte, TeraByte, PetaByte, ExaByte, ZetaByte, YotaByte':
    print('Acertou')
    pontos9 += 5

print('''
10 - MB e Mb são diferentes? Qual a função de cada um?''')

resposta = input('Digite sua resposta: ')
pontos10 = 0

if resposta == 'Sim, MB usa-se para representar armazenamento e Mb usa-se para representar transmissão':
    print('Acertou')
    pontos10 += 5

print('''
11 - Qual a função do Modem?''')

resposta = input('Digite sua resposta: ')
pontos11 = 0

if resposta == 'Transformar a onda quadrada do dispositivo em ondas senoidal chamado modulação e também receber chamado demodulação':
    print('Acertou')
    pontos11 += 5

print('''
12 - O que é um servidor?''')

resposta = input('Digite sua resposta: ')
pontos12 = 0

if resposta == 'Conjunto de arquivos e fotos, etc':
    print('Acertou')
    pontos12 += 5

print('''
13 - Todos na internet possuem identificação?''')

resposta = input('Digite sua resposta: ')
pontos13 = 0

if resposta == 'Sim, todos possuem um número de identificação, inclusive os servidores':
    print('Acertou')
    pontos13 += 5

print('''
14 - Qual a rota de um dispositivo até um site na internet?''')

resposta = input('Digite sua resposta: ')
pontos14 = 0

if resposta == 'Dispositivo/Cliente, Modem, Internet, Servidor':
    print('Acertou')
    pontos14 += 5

print('''
15 - Como descobre o seu própio IP ou do site desejado?''')

resposta = input('Digite sua resposta: ')
pontos15 = 0

if resposta == '1 - Abra o navegador, 2 - Digite o link www.iplocation.net, 3 - "Your public IP Address is....", este é seu IP público, 4 - "IP Location Finder", digite o site que deseja descobrir o IP':
    print('Acertou')
    pontos15 += 5

print('''
16 - O que é DNS?''')

resposta = input('Digite sua resposta: ')
pontos16 = 0

if resposta == 'DNS (Domain Name System), é um local na internet que eu posso pesquisar listas de nomes de site para que não usemos o número de identificação':
    print('Acertou')
    pontos16 += 5

print('''
17 - Qual a rota completa entre o dispositivo e o site para que apareça todo o conteúdo em sua tela?''')

resposta = input('Digite sua resposta: ')
pontos17 = 0

if resposta == 'Dispositivo/Cliente, Modem, nome do site pro DNS, DNS pro Modem, Modem pro servidor, imagens do servidor vão em pacotes e caminhos diferentes e no fim são exibida na minha tela':
    print('Acertou')
    pontos17 += 5


print('''
Sua pontuação final é''', pontos1+pontos2+pontos3+pontos4+pontos5+pontos6+pontos7+pontos8+pontos9+pontos10+pontos11+pontos12+pontos13+pontos14+pontos15+pontos16+pontos17)
print('Se você tirou 85, PARABÉNS, você acertou todas!')
input("Pressione <enter> para encerrar!")
