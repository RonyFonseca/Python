preco = float(input('Qual o valor do seu produto?:'))
porcentagem = float(input('Quantos % de desconto ?:'))
valor = preco - (preco*(porcentagem/100))
print("Seu valor com {}% de desconto é {}".format(porcentagem,valor))
