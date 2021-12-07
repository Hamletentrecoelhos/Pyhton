import json
a = 10
b = 30
list1 = []
x = json.dumps([a, b, list1])
print(x)

arquivo = open('test.txt', 'w')
json.dump([a + b, list1], arquivo)

arquivo = open('test.txt', 'r')
t = json.load(arquivo)
print(t)
