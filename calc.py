def add(num):
   return sum(num)

def subtract(num):
    ans = num[0]
    for i in range (1, len(num)):
        ans = ans - num[i]    
    return ans

def multiply(num):
    ans = num[0]
    for i in range (1, len(num)):
        ans = ans * num[i]    
    return ans

def divide(num):
    ans = num[0]
    for i in range (1, len(num)):
        ans = ans / num[i]    
    return ans

def exponent(num1,num2):
    return num1**num2

def inputNumber(msg):
    while True:
        try:
            res = int(input(msg))
            break
        except ValueError:
            print("Number ba yan ha?  ulit!...")

    return res
        

def main():
    # take input from the user
    print("~~~~Select operation.~~~~")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exponent")
    
    choice = 0
    while not (1 <= choice <= 5):
        choice = inputNumber(" Enter valid choice:")
    
    ans = 0
    if 1 <= choice <= 4:
        temp = 0;
        num = []
        print("~~~~~~Enter 10 numbers~~~~~~~")
        for i in range(0,10):
            temp = inputNumber(str(i+1) + " Enter number: ")
            num.append(temp)
 

        if choice == 1:
            ans = add(num)
        elif choice == 2:
            ans = subtract(num) 
        elif choice == 3:
            ans = multiply(num)
        elif choice == 4:
            ans = divide(num)
            
    elif choice == 5:
        num1 = inputNumber("Enter number: ")
        num2 = inputNumber("Enter exponent: ")
        ans = exponent(num1,num2)
    
    

    print("Answer is: " + str(ans))


main()

