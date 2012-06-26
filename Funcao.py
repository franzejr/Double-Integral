#funcao que iremos utilizar
import math
from NewtonCotes import *

########## Trigonometric functions
# math.acos(x)
# 	Return the arc cosine of x, in radians.
# math.asin(x)
# 	Return the arc sine of x, in radians.
# math.atan(x)
# 	Return the arc tangent of x, in radians.
# math.atan2(y, x)
# 	Return atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.
# math.cos(x)
# 	Return the cosine of x radians.
# math.hypot(x, y)
# 	Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).
# math.sin(x)
# 	Return the sine of x radians.
# math.tan(x)
# 	Return the tangent of x radians.

########## Hyperbolic functions
# math.acosh(x)
# 	Return the inverse hyperbolic cosine of x.
# math.asinh(x)
# 	Return the inverse hyperbolic sine of x.
# math.atanh(x)
# 	Return the inverse hyperbolic tangent of x.
# math.cosh(x)
# 	Return the hyperbolic cosine of x.
# math.sinh(x)
# 	Return the hyperbolic sine of x.
# math.tanh(x)
# 	Return the hyperbolic tangent of x.

#Funcao Exponencial
class Funcao:
	def __init__(self,x):
		self. x = x

	#Funcao que iremos parametrizar
	def f(self,y):
		#print  "y: ", y
		return fx(self.x,y)

#Funcoes para a parametrizacao
def g1(x):
	return 0.0
def g2(x):
	return 4.0

def fx(x,y):
	return x*y;
