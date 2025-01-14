a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(                    #usa-se string.format    #format é um argumento 
    nome1= a, nome2= b, nome3= c                                     #nome3 é um parametro e c é um argumento
    ) 

print(formato)