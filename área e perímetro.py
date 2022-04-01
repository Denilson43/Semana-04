def A_quadrado (lado):
	return lado*lado
def P_quadrado (lado):
	return lado*4
valor = float(input().strip())
print('{:10.4f}'.format(A_quadrado(valor)))
print('{:10.4f}'.format(P_quadrado(valor)))