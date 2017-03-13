
#
# 1.- La funcion cutc permite extraer campos de una lista de cadenas de
#     caracteres. Los campos estan delimitados por caracteres.
#
#     Ejemplo.
#     >>> x = ['uno:dos:tres',  'alpha:beta:omega']
#     >>> print(cutc(x, ':', 1, None))
#     ['dos', 'beta']
#     >>> print(cut(x, ':', 1, 2))
#     ['dos:tres', 'beta:omega']
#     >>> print(cut(x, ':', None, 1))
#     ['uno:dos',  'alpha:beta']
#
def cutc(x, delim, n=None, m=None):
    for i in range(len(x)):
        x[i]=cut(x[i], delim)
    return (x)
    #
def cut(x, delim):
    i=0
    while i <len(x):
        if x[i]!= delim:
            i=i+1
        else:
            return x[:i]
        
    
print(cutc(x,':', None, None))
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
    #
    return(x)
    #

#
# 3.- La funcion wcc cuenta la ocurrencia de palabras en una lista de
#     cadenas de caracteres. La funcion wcc devuelve el resultado usando
#     un diccionario. Se debe especificar el caracter delimitador.
#
#     Ejemplo.
#     >>> x = ['hola mundo', ''hola mundo feliz', ''hola feliz']
#     >>> print(wcc(x, ' '))
#     {'hola':3, 'mundo':2, 'feliz':2}
#
def wcc(x, delim):
    #
    return(x)
    #

#
# 4.- La funcion sortw ordena las palabras en una lista de cadenas de
#     caracteres ordenadas alfabeticamente. Se debe especificar el caracter
#     delimitador.
#
#     Ejemplo.
#     >>> x = ['hola mundo', ''hola mundo feliz', ''hola feliz']
#     >>> print(sortw(x, ' '))
#     ['feliz', 'feliz', 'hola', 'hola', 'hola','mundo', 'mundo']
#
def sortw(x, delim):
    #
    return(x)
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
    #
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
    #
    return(x)
    #
