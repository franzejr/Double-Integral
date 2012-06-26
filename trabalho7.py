#Integracao Numerica - Newton Cotes e Gauss-Legendre
#Universidade Federal do Ceara
#Metodos Numericos 2 - Prof. Creto Vidal
# Trabalho 7 - Integral Dupla
#@franzejr - 0322836

from NewtonCotes import *
from GaussLegendre import *
from Util import *
import sys,math
from Funcao import *

#Dado um Metodo de NewtonCotes, decidir se ele eh aberto ou fechado
def escolherAbertoFechado(metodo):
	aberto = raw_input("aberto[a]/fechado[f]? [a/f]:\n")
		
	#Saber se o Newton Cotes eh aberto ou fechado
	if (aberto == "a"):
		metodoIntegracao = newtonCotesAberto(metodo)
	else:
		metodoIntegracao = newtonCotesFechado(metodo)

	return metodoIntegracao
		
#Decidindo Qual NewtonCotes Aberto
def newtonCotesAberto(metodo):
	if (metodo.lower() == "trapezio"):
		metodoIntegracao = TrapezioAberto()
	elif(metodo.lower() == "simpson"):
		metodoIntegracao = SimpsonAberto()
	elif(metodo.lower() == "simpson38"):
		metodoIntegracao = Simpson38Aberto()
	elif(metodo.lower() == "boole"):
		metodoIntegracao = BooleAberto()

	return metodoIntegracao

#Decidindo Qual NewtonCotes Fechado
def newtonCotesFechado(metodo):

	if (metodo.lower() == "trapezio"):
		metodoIntegracao = Trapezio()
	elif(metodo.lower() == "simpson"):
		metodoIntegracao = Simpson()
	elif(metodo.lower() == "simpson38"):
		metodoIntegracao = Simpson38()
	elif(metodo.lower() == "boole"):
		metodoIntegracao = Boole()

	return metodoIntegracao

def cabecalho():
	print "Trabalho 7 - Metodos Numericos - Integral Dupla\n"
	print  "Eh possivel escolher <metodo> = trapezio, simpson, simpson38, boole, legendre\n"
	print "Se for NewtonCotes Aberto ou Fechado o programa ira perguntar depois\n"
	print "Se for GaussLegendre ira perguntar com quantos pontos depois\n"


def main():
	#Imprimir Cabecalho
	cabecalho()

	#Escolhendo o Metodo para resolver a Integral de Fora
	metodo = raw_input("Qual Metodo externo voce deseja utilizar?\n<metodo> = trapezio, simpson, simpson38, boole, legendre\n")

	a = float(raw_input("Qual o a?"))
	b = float(raw_input("Qual o b?"))
	numParticoes = int(raw_input("Quantas Particoes?"))

	#Quadratura Externa eh NewtonCotes
	if (metodo != "legendre"):
		
		#A Quadratura para calculo da Integral Externa foi Newton Cotes
		metodoIntegracao = escolherAbertoFechado(metodo)


		h = float((b-a)/numParticoes)
		#Primeiro while para sabermos onde iremos cortar
		i = 1
		x = 0.0
		valor_atual = 0.0
		
		while(x < b):
			
			x = a + (i-1)*h
			#Decidindo qual quadratura interna
			metodoInterno = raw_input("Qual quadratura interna?\n<metodo> = trapezio, simpson, simpson38, boole, legendre\n")
			if(metodoInterno.lower() != "legendre"):
				#Chamando para o interno
				metodoIntegracao = escolherAbertoFechado(metodoInterno)

				#Instancando uma funcao que pode ser calculada como uma quadratura de NewtonCotes
				funcao = QuadraturaInternaNewtonCotes(g1(x),g2(x),metodoIntegracao)

				#chamando para o externo, o externo vai ser NewtonCotes
				valor_atual = metodoIntegracao.resolver(a,b,numParticoes,funcao)
				print valor_atual

			elif (metodoInterno == "legendre"):
				metodoInterno = GaussLegendre(g1(x),g2(x))
				
				tamanhoSubIntevalo = (g2(x) - g1(x))/numParticoes

				numPontos = int(raw_input("GaussLegendre com quantos pontos?"))
				
				#Instanciando uma funcao que pode ser calculada como GaussLegendre
				funcao = QuadraturaInternaLegendre(g1(x),g2(x),numPontos,numParticoes,metodoInterno)
				
				#chamando para o externo, o externo vai ser NewtonCotes
				valor_atual = metodoIntegracao.resolver(a,b,numParticoes,funcao)
				print valor_atual

	#Quadratura Externa eh GaussLegendre
	else:

		#A Quadratura de GaussLegendre foi escolhida para calcular a integral externa
		metodoIntegracao = GaussLegendre(a,b)

		tamanhoSubIntervalo = (b - a)/numParticoes

		numPontos = int(raw_input("GaussLegendre com quantos pontos?"))
				

		h = float((b-a)/numParticoes)
		#Primeiro while para sabermos onde iremos cortar
		i = 1
		x = 0.0
		valor_atual = 0.0
		
		while(x < b):
			
			x = a + (i-1)*h
			
			metodoInterno = raw_input("Qual quadratura interna?")
			if(metodoInterno.lower() != "legendre"):
				#A Quadratura escolhida foi Newton Cotes
				metodoInterno = escolherAbertoFechado(metodoInterno)
				
				#Instancando uma funcao que pode ser calculada como uma quadratura de NewtonCotes
				funcao = QuadraturaInternaNewtonCotes(g1(x),g2(x),metodoInterno)

				#chamando para o externo que eh gauss legendre
				valor_atual = metodoIntegracao.calcular(numParticoes,numPontos,tamanhoSubIntervalo,a,b,funcao)
				print valor_atual

			elif (metodoInterno == "legendre"):
				#A Quadratura escolhida foi Gauss Legendre
				metodoInterno = GaussLegendre(g1(x),g2(x))
				
				#Instanciando uma funcao que pode ser calculada como GaussLegendre
				funcao = QuadraturaInternaLegendre(g1(x),g2(x),numPontos,numParticoes,metodoInterno)
				
				#chamando para o externo que eh gauss legendre
				valor_atual = metodoIntegracao.calcular(numParticoes,numPontos,tamanhoSubIntervalo,a,b,funcao)
				print valor_atual
main()