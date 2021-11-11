qualquer_coisa = input("Digite qualquer coisa:")
#ÁREAS DOS PRINTS
print("{} é númerico ? {}".format(qualquer_coisa, qualquer_coisa.isnumeric()))
print("{} é alfa númerico ? {}".format(qualquer_coisa, qualquer_coisa.isalnum()))
print("{} está só em maiúsculas ? {}".format(qualquer_coisa, qualquer_coisa.isupper()))
print("{} está só em minúsculas ? {}".format(qualquer_coisa, qualquer_coisa.islower()))
print("{} só tem espaços ? {}".format(qualquer_coisa, qualquer_coisa.isspace()))
