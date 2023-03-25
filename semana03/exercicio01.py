horatrabalhada = float(input("digite horas trabalhadas:"))

salario = horatrabalhada * 35

if salario < 1000:
    salario = salario + 300
    print("seu salario é " ,salario)
else:
    print("seu salario é ", salario)

