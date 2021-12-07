import smtplib

mail_de = 'tainamgrs2000@yahpp.com.br'
mail_para = 'tgrsbrasil@gmail.com'
mail_assunto = 'Explorando'
mail_corpo_da_mensagem = 'Tirando as rodinhas'

mail_mensagem = f'''
From: {mail_de}
To: {mail_para}
Subject: {mail_assunto}

{mail_corpo_da_mensagem}
'''

servidor = smtplib.SMTP('localhost')
servidor.sendmail(mail_de, mail_para, mail_mensagem)
servidor.quit()