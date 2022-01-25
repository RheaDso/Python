num=int(input("Enter number: "))
if num<0:
    print("Sorry! Enter a positive number. Please try again... ")
    
else: 
    sum=0
    while(num>0):
        sum+=num
        num-=1
    print("Sum =", sum)        