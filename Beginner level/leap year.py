a=int(input("enter the inpurt:"))
if((a%4)==0):
    print("leap")
elif((a%100)==0):
    print("leap")
elif((a%400)==0):
    print("leap")
else:
    print("not leap")
