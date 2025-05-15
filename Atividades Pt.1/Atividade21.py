#C = (F - 32) * 5/9

fahrenheit = int(input("Quantos Graus Fahrenheit Está Atualmente? "))

celsius = (fahrenheit - 32) * 5/9

if celsius < 0:
    print(f"Brr! Está Frio Aqui, Temperatura Atual {celsius}")

else:
    print(f"A Temperatura Em Celsius Mede {celsius}, Convertido De {fahrenheit} Graus Fahrenheit")