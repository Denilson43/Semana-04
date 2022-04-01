def percentual (valor, porcento):
	return valor * (porcento / 100)
preco = float(input().strip())
v_percentual = float(input().strip())
pr_acres = preco + percentual(preco, v_percentual)
pr_desc = preco - percentual(preco, v_percentual)
print('{:.2f}'.format(pr_acres))
print ('{:.2f}'.format(pr_desc))