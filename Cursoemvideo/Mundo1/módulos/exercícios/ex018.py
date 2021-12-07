from math import radians, sin, tan, cos
neum2 = float(input('\033[1:34mDigite um ângulo:\033[m '))
neum2 = radians(neum2)
print('0', '-'*42, '0')
print("""| O \033[1:34mseno\033[m de {:.8f} é \033[4:34m{}\033[m; |
| A \033[1:34mtangente\033[m de {:.4f} é \033[4:34m{}\033[m; |
| E a \033[1:34mtangente\033[m de {:.2f} é \033[4:34m{}\033[m. |""".format(neum2, sin(neum2), neum2, tan(neum2), neum2, cos(neum2)))
print('0', '-'*42, '0')
