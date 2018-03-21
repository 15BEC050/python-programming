def main():
    a=int(input("enter the value:"))
    k=a
    sum=0
    while(a!=0):
        val=a%10
        sum=sum*10+val
        a=a/10
    if(sum==k):
        print("yes")
    else:
        print("no")



if __name__ == '__main__':
    main()
