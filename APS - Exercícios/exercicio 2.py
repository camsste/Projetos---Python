multa = 0 
vel = int(input("Qual a velocidade do carro em KM?"))

if vel < 80: print("Tudo ok!")
elif vel > 80:
    multa = (vel-80)*5
    print(f"Você foi multado em R${multa}")