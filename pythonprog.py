
#
# 1.- La funcion cutc permite extraer campos de una lista de cadenas de
#     caracteres. Los campos estan delimitados por caracteres.
#
#     Ejemplo.
#     >>> x = ['uno:dos:tres:',  'alpha:beta:omega:']
#     >>> print(cutc(x, ':', 1, None))
#     ['dos', 'beta']
#     >>> print(cut(x, ':', 1, 2))
#     ['dos:tres', 'beta:omega']
#     >>> print(cut(x, ':', None, 1))
#     ['uno:dos',  'alpha:beta']
#
#     >>> print(cut(x, ':', None, None))


def cutc(x, delim, n=None , m=None ):
	
	x=x[:]
	if m!=None:
		if n!=None:
			if m<n:
				m=n
	if (n==None or n<=0) and (m== None or m<= 0):
		for i in range(len(x)):
			x[i]=cut(x[i], delim)
		return (x)
	elif n==None or n<=0:

		for i in range(len(x)):
			b=m
			while cutm(x[i], delim, b)==None:
				b=b-1
			x[i]=cutm(x[i], delim, b)
		return (x)
	elif m==None or m<=0:
		for i in range(len(x)):
			a=n
			while cutn(x[i], delim, a)==None:
				a=a-1
			x[i]=cutn(x[i], delim, a)
		return (x)
	else:

		for i in range(len(x)):
			a=n
			b=m
			while cutnm(x[i],delim, a, b)==None:
				a=a-1
			x[i]=cutnm(x[i],delim, a, b)
		return x






def cutnm(x, delim, n=None, m=None):
	x=x[:]
	z=''
	if n<=0:
		b=m
		while cutm(x, delim, b)==None:
			b=b-1
		return cutm(x, delim, b)
	for i in range (n):
		for j in range(len(x)):
			if x[j]!=delim:
				i=i+1
			else:
				if cutnm(x[i+1:], delim, n-1, m-1)==None:
					return ''
				else:
					return cutnm(x[i+1:], delim, n-1, m-1)	


def cutm(x, delim, m):
		i=0
		z=''
		b=m
		if m<=0:
			return cut(x, delim)
		elif m!=0:
			while i <len(x):
				b=m
				if x[i]!= delim:
					i=i+1
				else:
					z=z+(x[:i])+delim
					while cutm(x[(i+1):], delim, b-1)==None:
					    b=b-1
					return z+cutm(x[(i+1):], delim, b-1)
			
def cutn(x, delim, n):
	z=''
	c=0
	a=n
	if n<=0:
		return cut(x, delim)
	for j in range(len(x)):
		if x[j]==delim:
			z=''
			c=c+1
			n=n-1
			if n==0:
				return cut(x[j+1:],delim)
		else:
			z=z+x[j]
	if a==c+1:
		return z
	else:
		return ''
			
				

			

def cut(x, delim):
	i=0
	while i <len(x):
		if x[i]!= delim:
			i=i+1
		else:
			return x[:i]
	return x
	
        
# 
# 2.- La funcion pastec permite concatenar dos listas de cadenas de
#     caracteres elemento a elemento. Se debe especificar
#     el caracter delimitador
#
#     Ejemplo.
#     >>> x = ['linea 1', 'linea 2', 'linea 3']
#     >>> y = ['x', 'y', 'z']
#     >>> print(pastec(x, y, ';'))
#     ['linea 1;x', 'linea 2;y, 'linea 3;z']
#     >>> w = ['x', 'y', 'z', 'a', 'b']
#     >>> print(pastec(x, w, ';'))
#     ['linea 1;x', 'linea 2;y, 'linea 3;z', 'a', 'b']
#
def pastec(x, y, delim):
	z=x[:]
	y=y[:]
	x=[]
	if len(z)>len(y):
		while (len(z)-len(y))!=0:
			y.append('')			
	elif len(y)>len(z):
		while (len(z)-len(y))!=0:
			z.append('')
	for i in range (len(z)):
		if z[i]=='':
			x.append(y[i])
		elif y[i]=='':
			x.append(z[i])
		else:
			x.append(str(z[i])+delim+str(y[i]))
	return(x)
    #

#
# 3.- La funcion wcc cuenta la ocurrencia de palabras en una lista de
#     cadenas de caracteres. La funcion wcc devuelve el resultado usando
#     un diccionario. Se debe especificar el caracter delimitador.
#
#     Ejemplo.
#     >>> x = ['hola mundo', 'hola mundo feliz', 'hola feliz']
#     >>> print(wcc(x, ' '))
#     {'hola':3, 'mundo':2, 'feliz':2}
#
def wcc(x, delim):
	x=x[:]
	z=[]

	for i in range (len(x)):
		z.append(wcc2(x[i],delim))
	x=[]
	for i in range (len(z)):
		for j in range(len(z[i])):
			x.append(z[i][j])
	import collections
	x=collections.Counter(x)
	return(x)

    #
def wcc2(x, delim):
	c=0
	z=[]
	z.append('')
	for i in range (len(x)):
		if x[i]!=delim:
			z[c]=z[c]+x[i]
		else:
			c=c+1
			z.append('')
	return z
#
# 4.- La funcion sortw ordena las palabras en una lista de cadenas de
#     caracteres ordenadas alfabeticamente. Se debe especificar el caracter
#     delimitador.
#
#     Ejemplo.
#     >>> x = ['hola mundo', 'hola mundo feliz', 'hola feliz']
#     >>> print(sortw(x, ' '))
#     ['feliz', 'feliz', 'hola', 'hola', 'hola','mundo', 'mundo']
#
def sortw(x, delim):
	x=x[:]
	z=[]

	for i in range (len(x)):
		z.append(wcc2(x[i],delim))
	x=[]
	for i in range (len(z)):
		for j in range(len(z[i])):
			x.append(z[i][j])

	return(sorted(x))
    #

#
# 5.- La funcion uniqc genera una lista compuesta por las palabras que
#     conforman una lista de cadenas de caracteres sin repeticion. Se
#     debe especificar el caracter delimitador.
#
#     Ejemplo.
#     >>> x = ['hola mundo', ''hola mundo feliz', ''hola feliz']
#     >>> print(uniqc(x, ' '))
#     ['hola', 'mundo', 'feliz']
#
def uniqc(x, delim):
    z=sortw(x,delim)
    x=[]
    for i in range(len(z)):
    	if z[i] not in x:
    		x.append(z[i])
    	
    return(x)
    #

#
# 6.- La funcion selc genera una lista compuesta por las palabras que
#     conforman una lista de cadenas de caracteres y que ocurren un
#     determinado numero de veces. Se debe especificar el caracter
#     delimitador.
#
#     Ejemplo.
#     >>> x = ['hola mundo', ''hola mundo feliz', ''hola feliz']
#     >>> print(selc(x, 2, ' '))
#     [mundo', 'feliz']
#
def selc(x, n, delim):
	z=sortw(x,delim)
	x=uniqc(z, delim)
	y=[]
	for i in range(len(x)):
		c=0
		for j in range(len(z)):
			if x[i] == z[j]:
				c=c+1
		if c==n:
			y.append(x[i])
	return(y)
    #
