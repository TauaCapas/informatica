
somapositivos = 0
quantnegatvos = 0
for bombardilhocrocodilo in range(20):
    valor=int(input("digite um valor: "))
    if valor >=0:
        somapositivos+=valor
    else:
        quantnegatvos+1
print (somapositivos)
print (quantnegatvos)
    