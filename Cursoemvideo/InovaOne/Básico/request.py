import requests
site = requests.get('https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956')
print(site.text)
