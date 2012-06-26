from Funcao import *

#Gauss Legendre
class GaussLegendre():

	def __init__(self,a,b):
		#Intervalos de Integracao
		self.a = a
		self.b = b
		#Vetores com [raiz,peso]
		self.n2 = [ -0.577350269, 1.0 ],[ 0.577350269, 1.0 ]
		self.n3 = [ -0.774596669, 0.555555556 ],[ 0, 0.888888889 ],[ 0.774596669, 0.555555556 ]
		self.n4 = [ -0.861136312, 0.347854845 ],[ -0.339981043, 0.652145155 ], [0.339981043, 0.652145155 ],[ 0.861136312, 0.347854845 ]
		
	def calcular(self,n,numPontos,tamanhoSubIntevalo,ai,bi,funcao):
		integral = 0
		raiz = 0
		peso = 0
		
		#Numero de Intervalos para ele tentar ir ate sempre +1 a mais
		for numIntervalos in range(1,n+1):
			
			#Andando com o bi
			bi = ai + tamanhoSubIntevalo
			#Zerando o resultado do SubIntervalo
			resultadoSubIntervalo = 0

			for i in range(0,numPontos):

				if numPontos == 2:
					raiz = self.n2[i][0]
					peso = self.n2[i][1]

				elif numPontos == 3:
					raiz = self.n3[i][0]
					peso = self.n3[i][1]

				elif numPontos == 4:
					raiz = self.n4[i][0]
					peso = self.n4[i][1]	
			
				#Calculando quem sera o xi para esse intervalo, no caso ai e bi
				xi = ( raiz*(bi - ai) + ai + bi  )/2
				resultadoSubIntervalo += peso*funcao.f(xi)
			
			#Calculando a integral peso*f(parametrizacao(xi))
			integral += resultadoSubIntervalo
			#Andando no subintervalo
			ai = bi 

		return integral * tamanhoSubIntevalo /2
		
