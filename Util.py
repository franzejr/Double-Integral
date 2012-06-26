from Funcao import *

#Funcao Generica para calculo do Xi
#intervaloA: inicio do intervalo A
#intervaloB: final da parte onde vamos integrar
#i: qual Xi queremos. Ex.: x0, x1...xN
#numIntervalos: Se o polinomio eh de grau n fechado, entao teremos 2 intervalos, por exemplo, n-1 intervalos, n+1 pontos
############### Se o polinomio eh de grau n aberto, n+2 intervalos, n+1 pontos
def calcularXi(intervaloA, intervaloB, i, numIntervalos):
        return intervaloA + i * (intervaloB - intervaloA) / numIntervalos



class QuadraturaInternaNewtonCotes:

	def __init__(self,a,b,quadratura):
		self.a = a 
		self.b = b
		self.quadratura = quadratura

	def f(self,x):
		funcao = Funcao(x)
		resultado = self.quadratura.resolver(self.a,self.b,100,funcao)
		return resultado


class QuadraturaInternaLegendre:

	def __init__(self,a,b,numPontos,particoes,quadratura):
		self.a = a 
		self.b = b
		self.numPontos = numPontos
		self.particoes = particoes
		self.quadratura = quadratura

	def f(self,x):
		funcao = Funcao(x)
		tamanhoSubIntervalo = (self.b - self.a)/self.particoes
		resultado = self.quadratura.calcular(self.particoes,self.numPontos,tamanhoSubIntervalo,self.a,self.b,funcao)
		return resultado
