from urllib.error import URLError
try:
    import urllib.request
    urllib.request.urlopen('http://pudim.com.br/')
except URLError:
    print('Não é possível acessar o site do pudim.')
else:
    print('Foi possível acessar o site do pudim.')
