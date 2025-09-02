
somapositivos = 0
quantnegatvos = 0
i = 0
while i != 20:
    i+= 1
    valor=int(input("digite um valor: "))
    if valor >=0:
        somapositivos+=valor
    else:
        quantnegatvos+=1
print (somapositivos)
print (quantnegatvos)
