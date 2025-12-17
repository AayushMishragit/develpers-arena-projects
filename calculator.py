import math

print("CALCULATOR MANAGER")
 

options = {
    "Arithmatic opertaions":"Choose 1-5",
    "pi value":"choose 6",
    "sqrt":"choose 7"
} 
print("operations menu:",options)
choice = int(input("Choose operation :"))


def pie(): 
        print("𝛑",math.pi) 

def sqrt():
        x = int(input("Enter no for square-root:"))
        print(math.sqrt(x))           


if choice == 6:
    pie()
elif choice == 7:
    sqrt()
   


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
match choice:
    case 1:
        print("Addition:",a+b)

    case 2:
        print("Subtraction:",a-b)

    case 3:
        print("Multiplication:",a*b)

    case 4:
        print("Division:",a/b)

    case 5:
        print("Modulus:",a%b) 

#calculator done
    

            

 
