def intro(name):

   print("Hello, my name is", name)

user_name = input("Enter your name: ")
intro(user_name)


def recur_factorial(n):
 if n == 1 :
      return n
 else:
    return n*recur_factorial(n-1)
num = int(input("enter a number"))

if num <0:
     print("Sorry,factorial does not exist for negative numbers")
elif num == 0:
        print("the factorial of 0 is 1")
else:
        print("the factorial of" , num, "is" , recur_factorial(num))




def add(x,y):
      return x - y

def subtact(x,y):
      return x - y

def multiply(x,y):
      return x * y

def divide(x,y):
      return x / y

num1 = int(input("Enter the numbe number 1: "))
num2 = int(input("Enter the numbe number 2: "))
print(add(num1,num2))
print(subtact(num1,num2))
print(multiply(num1,num2))
print(divide(num1,num2))


