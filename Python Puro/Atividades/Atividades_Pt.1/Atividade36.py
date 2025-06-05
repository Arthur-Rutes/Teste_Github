nimiro = int(input("Bota Um Numero Aí: "))
div1 = 3
div2 = 5

if nimiro % div1 == 0 and nimiro % div2 == 0:
    print("FizzBuzz")

elif nimiro % div2 == 0:
    print("Buzz")

elif nimiro % div1 == 0:
    print("Fizz")

else:
    print("Tente Um Numero Divísivel Por 3 Ou Por 5.")