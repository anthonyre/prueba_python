num = input('inserte numeros a sumar separados en espacios ej: 1 2 3 : ').split()
num = [int(x) for x in num]
sum = sum(num)
print(sum)