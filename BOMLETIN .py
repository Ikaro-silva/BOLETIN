lista = []
resp: str = ''
resp1 =  ''
while resp != 'N':
    nome = input('NOME:')
    nota1 = int(input('NOTA 1:'))
    nota2 = int(input('NOTA 2 :'))
    media = (nota1+nota2)/2
    lista.append([nome, [nota1, nota2], media]) # jeito mais facil qoando tiver varias listas desenhar é melhor
    resp = input('deseja continuar?[S/N]').upper()
print('§=-=§'*10)
print(f'{"no.":<4}{"NOME":<10}{"MEDIA":>8}')# fode ser feito com format
print("-"*30)
for i, l in enumerate(lista):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8.1f}')# fode ser feito com format
while True:
    resp1 = int(input('MOSTRAR NOTAS DE QUAL ALUNO ?'))
    if resp1== 999:
        break
    if resp1 <= len(lista) -1:
        print(f'NOTAS DE {lista[resp1][0]} SÃO {lista[resp1][1]}')
