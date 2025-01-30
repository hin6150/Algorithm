a = input()
b = input()
c = input()
number = 0

if(a.isnumeric()):
    number = (int(a)+3)
elif(b.isnumeric()):
    number=(int(b)+2)
elif(c.isnumeric()):
    number=(int(c)+1)

if(number % 15 == 0):
    print("FizzBuzz")
elif(number % 3 == 0):
    print("Fizz")
elif(number % 5 == 0):
    print("Buzz")
else:
    print(number)