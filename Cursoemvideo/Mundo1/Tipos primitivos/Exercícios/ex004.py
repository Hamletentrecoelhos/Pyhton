A = input('Digite algo: ')
print(f"""O tipo primitivode de "A" é {type(A)};
"A" só tem espoços? {A.isspace()};
"A" é um número? {A.isnumeric()};
"A" é alfabético? {A.isalpha()};
"A" é alfanumérico {A.isalnum()};
"A" está em maiúsculas? {A.isupper()};
"A" está em minúsculas? {A.islower()};
"A" está capitalizado? {A.istitle()}.""")
