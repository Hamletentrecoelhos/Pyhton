try:
    pessoas = open('pessoas.txt', 'r')
except:
    pessoas = open('pessoas.txt', 'w+')
    pessoas.close()
p = int()
c = '\033[1;34m', '\033[1;33m', '\033[m'
while p != 3:
    from errorsl import verificaop
    print('-'*40)
    print('             MENU PRINCIPAL')
    print('-'*40)
    print(f"""{c[1]}1 -{c[0]} Ver lista de pessoas cadastradas;
{c[1]}2 -{c[0]} Adicionar uma pessoa;
{c[1]}3 -{c[0]} Encerrar o programa.{c[2]}""")
    print('-'*40)
    p = verificaop(input(f'{c[1]}Sua Opção:{c[2]} ').strip())
    print('-'*40)
    if p == 1:
        pessoas = open('pessoas.txt', 'r')
        print('           PESSOAS CADATRADAS')
        print('='*40)
        print(f'{"Nome:":<42}Idade:')
        for c1 in pessoas:
            print('>', c1, end='')
        pessoas.close()
    elif p == 2:
        from errorsl import verificanum, verificatx
        pessoas = open('pessoas.txt', 'a')
        t = f'{verificatx(input("Nome: ")):<40}', verificanum(input("Idade: ").strip()), '\n'
        pessoas.writelines(t)
        pessoas.close()
print('Programa encerrado...')
