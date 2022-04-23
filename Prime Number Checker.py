number = int(input("Enter The Number: "))

def IsPrime(number):
    if number > 1:
     for i in range(2,int(number/2)+1):
        if (number % i == 0):
            print(number, "is not a prime number")
            break
     else:
        print(number,"is a prime number")
    else:
        print(number,"is not a prime number")
IsPrime(number)