def main():
    a=int(input("enter the value:"))
    for i in range(2,a):
        if(a%i==0):
            print("not  prime")
            print(i ,"times", a//i ,"is", a )
            break
    else:
        print("prime number",a)


if __name__ == '__main__':
    main()
