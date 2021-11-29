number0 = int(input("Primeiro número: "))
number1 = int(input("Segundo número: "))
x = 1
result = 0
while x <= number1:
    r = result + number0
    x = x + 1
print("%d x %d = %d" % (number0, number1, result))
