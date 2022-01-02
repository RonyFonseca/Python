n1 = int(input("Digite o primerio número?:"))
n2 = int(input("Digite o segundo número?:"))
s = n1 + n2 #soma
m = n1 * n2 #multiplicação
d = n1 / n2 #divisão
di = n1 // n2 #divisão inteira
resto_d = n1 % n2 #resto da divisão
pot = n1 ** n2 #potencia
print("A multiplicação é {}, a divisão é {:.2f}".format(m,d))
print("A divisão inteira é {} e o resto da divisão é {}, a potencia {}".format(di, resto_d, pot))
