n1 = int(input("Digite o primerio número?:"))
n2 = int(input("Digite o segundo número?:"))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
resto_d = n1 % n2
pot = n1 ** n2
print("A multiplicação é {}, a divisão é {:.2f}".format(m,d))
print("A divisão inteira é {} e o resto da divisão é {}, a potencia {}".format(di, resto_d, pot))
