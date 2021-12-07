i18 = m20 = h = int()
c = str('S')
while True:
    if c == 'S':
        print('=-' * 10)
        print('ADCIONE UMA PESSOA')
        print('*-' * 10)
        i = int(input('Idade: '))
        s = str()
        while True:
            print('--' * 10)
            s = str(input('Sexo [F/M/N]: ')).upper().strip()
            if s in 'FMN':
                break
        if s == 'M':
            h += 1
        elif s == 'F' and i < 20:
            m20 += 1
        if i > 18:
            i18 += 1
        while True:
            c = str(input('Deseja continuar? [S/N]: ')).upper().strip()
            if c in 'SN':
                break
            else:
                print('Resposta inválida')
    elif c == 'N':
        break
print('=-' * 10, f"""
O número de mulheres menores de 20 anos é {m20};
{h} homens foram cadastrados;
E {i18} pessoas possuem mais de 18 anos.""")
