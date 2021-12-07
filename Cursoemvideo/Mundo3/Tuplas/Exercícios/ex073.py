times = ('Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio',
         'Palmeiras', 'Santos', 'Athletico-PR', 'Corinthians', 'Bragantino', 'Ceará',
         'Atlético-GO', 'Sport', 'Bahia', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Primeros 5 colocados: {times[0:5]}')
print(f'Os ultimos 4 colocados {times[-4:]}')
print(f'Em ordem halfabética: {sorted(times)}')
print(f"O time Bahia está na {times.index('Bahia') + 1}° posição")
