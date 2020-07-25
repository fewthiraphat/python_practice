Number = int(input("Enter integer number : "))
#Calculation
First = Number//1000
Second = (Number%1000)//100
Third = (Number%1000%100)//10
Fourth = (Number%1000%100%10)//1
#Text array
msg = str(First) + "\n" + str(Second) +"\n" + str(Third) + "\n" + str(Fourth)
#OUTPUT
print(msg)
