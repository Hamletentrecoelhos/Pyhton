while True:
    co = input('\033[;;40mComando: \033[;;41m').strip()
    if co.upper() == 'FIM':
        print('\033[;;40m='*9+'>')
        print('Encerrado')
        print('='*9+'>')
        break
    print('='*80+'>')
    co = f'{help(co)}'
    co = f'{co[0:-4]}'
    print(f'{co}')
