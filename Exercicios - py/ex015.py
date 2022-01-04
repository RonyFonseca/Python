quantidade_days = int(input("Quantos dias você alugou o carro?: "))
quantidade_km = float(input("Quantos kms rodados com ele?: "))
calculo_empresa = (quantidade_days * 60) + (0.15 * quantidade_km)
print("Você com {} km rodados em {} dias você necessita pagar {:.2f} R$.".format(quantidade_km, quantidade_days, calculo_empresa))
