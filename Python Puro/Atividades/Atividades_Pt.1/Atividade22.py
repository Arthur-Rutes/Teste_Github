salario = float(input("Quanto É Seu Salário(Hora): "))
horas = int(input("Quantas Horas Você Trabalha Por Dia: "))
dia = (input("Qual Dia Da Semana É? "))

salarioDiario = salario * horas
domingos = 2 * (salario * horas)
salarioMensal = (salarioDiario * 20) + domingos * 4

if horas != ("Domingo, domingo"):
    print(f"Seu Salario Diario É {salarioDiario}, Sendo Seu Salário Mensal Também {salarioMensal}")


else:
    print(f"Seu Salario Aos Domingos É {domingos}, Totalizando Com Sua Outra Parte Do Salário Soma {salarioMensal} Ao Mês")