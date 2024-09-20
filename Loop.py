# number = int(input("Enter the Number : "))
# count = 1
# while count<=10:
#     print(number*count)
#     count =count+1

# numbers = [1,4,9,16,25,36,49,64,81,100]
# count = 1
# while count<= len(numbers):
#     print(numbers[count-1])
#     count+=1

num = int(input("Enter the Number: "))

def EvenOdd(n):
    if n%2==0:
        return print("Even")
    else:
        return print("Odd")

EvenOdd(num)