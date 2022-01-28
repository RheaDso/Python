print("Enter the lower limit: ")
lr=int(input())

print("Enter the upper limit: ")
ur=int(input())

print("Even numbers are: ")
for i in range(lr, ur):
    if(i%2==0):
        print(i)

print("Odd numbers are: ")
for i in range(lr, ur):
    if(i%2!=0):
        print(i) 

