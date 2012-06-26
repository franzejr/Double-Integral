#Newton-Cotes Formulas
from Util import *
from Funcao import *

#Classe 'abstrata' de Newton Cotes
class NewtonCotes():
	pass

################
###Trapezio#####
################

#Metodo de Trapezio Fechado
#Utilizando Polinomios de Grau 1
# I = [(b-a) / 2] * [(f(x0) + f(x1)]
class Trapezio(NewtonCotes):
	
	def resolver(self,a,b,n,funcao):
		tamIntervalo = float(b-a)
		nlinha = float(n)
		tamParticao = float(tamIntervalo /nlinha)
		integral = 0.0

		i = a	
		while(i<b):
				
			integral += funcao.f( i ) + funcao.f( i + tamParticao )
			
			i += tamParticao
		
		return ( tamParticao /2) * integral


#Metodo de Trapezio Aberto
#Utilizando Polinomios de Grau 1
# I = [(b-a) / 3] * [(f(x0) + f(x1)]
class TrapezioAberto(Trapezio):
	
	def resolver(self,a,b,n,funcao):
		integral=0.0
		tamanhoSubIntervalo = (b-a)/n
		ai = a
		bi = b
		for i in range(0,n):
			bi = ai + tamanhoSubIntervalo
			x1 = calcularXi(ai,bi,1,3)
			x2 = calcularXi(ai,bi,2,3)
			integral += funcao.f(x1) + funcao.f(x2)
			ai = bi
		integral *= tamanhoSubIntervalo/2

		return integral


################
###Simpson######
################

#Metodo de Simpson Fechado
#Utilizando Polinomios de Grau 2
# I = [(b-a) / 6] * [(f(x0) + 4*f(x1) + f(x2)]
class Simpson(NewtonCotes):
	
	def resolver(self,a,b,n,funcao):
		integral = 0.0
		h = float((b-a)/n)


		#x = a
		for i in range(0,n):
			#integral +=  ( f(x) + 4*f( x +(h/2) ) + f(x+h) )
			b = a + h
			x0 = calcularXi(a,b,0,2)
			x1 = calcularXi(a,b,1,2)
			x2 = calcularXi(a,b,2,2)
			integral += funcao.f(x0) + 4*funcao.f(x1) + funcao.f(x2)
			a = b
			
		integral *= h/6
		
		return integral

#Metodo de Simpson Aberto
#Utilizando Polinomios de Grau 2
# I = [(b-a) / 4] * [2*f(x0) - f(x1) + 2*f(x2)]
class SimpsonAberto(Simpson):
	
	def resolver(self,a,b,n,funcao):
		integral = 0.0
		tamanhoSubIntervalo = (b-a)/n
		ai = a
		bi = b

		for i in range(0,n):
			bi = ai + tamanhoSubIntervalo
			x1 = calcularXi(ai,bi,1,4)
			x2 = calcularXi(ai,bi,2,4)
			x3 = calcularXi(ai,bi,3,4)
			integral += 2*funcao.f(x1) - funcao.f(x2) + 2*funcao.f(x3)
			ai = bi
		integral *= tamanhoSubIntervalo/3
		
		return integral


################
###Simpson3/8###
################

#Metodo de Simpson 3/8 Fechado
#Utilizando Polinomios de Grau 3
# I = [(b-a) / 8] * [(f(x0) + 3*f(x1) + 3*f(x2) + f(x3)]
class Simpson38(NewtonCotes):
	
	def resolver(self,a,b,n,funcao):
		integral = 0.0
		h = (b-a)/n

		for i in range(0,n):
			b = a + h
			x0 = calcularXi(a,b,0,3)
			x1 = calcularXi(a,b,1,3)
			x2 = calcularXi(a,b,2,3)
			x3 = calcularXi(a,b,3,3)
			integral += funcao.f(x0) + 3*funcao.f(x1) + 3*funcao.f(x2) + funcao.f(x3)
			a = b

		integral *= h/8

		return integral

#Metodo de Simpson 3/8 Aberto
#Utilizando Polinomios de Grau 3
# I = [(b-a) / 24] * [11*f(x0) + f(x1) + f(x2) + 11*f(x3)]
class Simpson38Aberto(Simpson38):
	
	def resolver(self,a,b,n,funcao):
		integral = 0.0
		tamanhoSubIntervalo = (b-a)/n
		ai = a
		bi = b

		for i in range(0,n):
			bi = ai + tamanhoSubIntervalo
			x1 = calcularXi(ai,bi,1,5)
			x2 = calcularXi(ai,bi,2,5)
			x3 = calcularXi(ai,bi,3,5)
			x4 = calcularXi(ai,bi,4,5)
			integral += 11*funcao.f(x1) + funcao.f(x2) + funcao.f(x3) + 11*funcao.f(x4)
			ai = bi

		integral *= tamanhoSubIntervalo/24

		return integral
		

################
###Boole########
################

#Metodo de Boole Fechado
#Utilizando Polinomios de Grau 4
# I = [(b-a) / 90] * [7*f(x0) + 32*f(x1) + 12*f(x2) + 32*f(x3) + 7*f(x4)]
class Boole(NewtonCotes):

	def resolver(self,a,b,n,funcao):
		integral = 0.0
		tamanhoSubIntervalo = (b-a)/n
		ai = a
		bi = b

		for i in range(0,n):
			bi = ai + tamanhoSubIntervalo
			x0 = calcularXi(a,b,0,4)
			x1 = calcularXi(a,b,1,4)
			x2 = calcularXi(a,b,2,4)
			x3 = calcularXi(a,b,3,4)
			x4 = calcularXi(a,b,4,4)
			integral += 7*funcao.f(x0) + 32*funcao.f(x1) + 12*funcao.f(x2) + 32*funcao.f(x3) + 7*funcao.f(x4)
			ai = bi

		integral *= tamanhoSubIntervalo/90

		return integral

#Metodo de Boole Aberto
#Utilizando Polinomios de Grau 4
# I = [(b-a) /20] * [11*f(x1) - 14*f(x2) + 26*f(x3) -14*f(x4) + 11*f(x5)]
class BooleAberto(Boole):

	def resolver(self,a,b,n,funcao):
		integral = 0.0
		tamanhoSubIntervalo = (b-a)/n
		ai = a 
		bi = b

		for i in range(0,n):
			bi = ai + tamanhoSubIntervalo
			x1 = calcularXi(a,b,1,6)
			x2 = calcularXi(a,b,2,6)
			x3 = calcularXi(a,b,3,6)
			x4 = calcularXi(a,b,4,6)
			x5 = calcularXi(a,b,5,6)
			integral += 11*funcao.f(x1) - 14*funcao.f(x2) + 26*funcao.f(x3) -14*funcao.f(x4) + 11*funcao.f(x5)
			ai = bi

		integral *= tamanhoSubIntervalo/20

		return integral
