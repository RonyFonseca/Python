salario = float(input('Quanto você ganha R$ ?:'))
aumento = float(input('Quantos por cento de almento % ?:'))
valor = (aumento/100*salario) + salario
print('Seu novo salário com {}% de aumento é de {}R$'.format(aumento,valor))
