n=int(input("enter a number:"))
if n < 0:
        print(none)
elif n == 0:
        print(1)
else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
            print(fact)
