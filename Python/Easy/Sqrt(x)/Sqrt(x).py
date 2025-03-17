#Square root of a given number
def square_root(num):
    root = 0

    while root*root <= num:
        root += 1
    return root - 1
#User input
num = int(input("Enter a positive number:"))

#Display output
print("The square root of",num,"is :",square_root(num))