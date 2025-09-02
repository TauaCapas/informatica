maiornariz=0
narinazimperfeitas=0
narinazperfeitas=0
menornariz=8743658730657346587346578364587643534253546598344516354451653445632451983445653451653849841351856913216843520803218643506513205613213546530321651320654365056498497813213231861621324685315653415968341565341562531563345156834516534159864341565314654614546546746564
for mateeeeeeeo in range(10):
    nariz1= float(input("digite á primeira nota"))
    nariz2= float(input("digite á segunda nota"))
    nariz3= float(input("digite á terceira nota"))
    narinas = (nariz1+nariz2+nariz3)/3
    if narinas >= maiornariz:
        maiornariz=narinas
    if narinas<maiornariz:
        menornariz = narinas
    if narinas>6:
        narinazperfeitas += 1
    else:
        narinazimperfeitas +=1
print(" a maior média é ", maiornariz)
print("a menor média é ", menornariz)
print("a quantidade de alinos aprovados é ", narinazperfeitas)
print("a quantidade de alunos reprovados é ", narinazimperfeitas)