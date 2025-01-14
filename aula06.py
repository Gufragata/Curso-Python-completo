# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
# print(1 + 1) # isso é um exemplo 
# print('a' + 'b') #isso é um exemplo 
print(int('1'),type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')   # Maneira utilizada para concatenar strings, é necessario dizer que o int é uma string para que possa ser concatenado
# print(11 + 'b') # Antes de ser concatenado para a maneira correta, é necessário converter o int para string
# print(str(11) + 'b') # Maneira correta para que possa ser concatenado de maneira certa