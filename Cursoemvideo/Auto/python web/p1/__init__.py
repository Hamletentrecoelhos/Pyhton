while True:
    from datetime import date
    from time import sleep
    x = list(open('templates/Home.html', 'r+'))
    x[6] = x[6].replace('@', str(date.today()))
    d = open('templates/Home.html', 'w+')
    d.writelines(x)
    d.close()
    sleep(86400)


