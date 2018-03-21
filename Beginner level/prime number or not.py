def main():
    a=int(input("enter the value:"))
    for i in range(2,a):
        if(a%i==0):
            print("no")
            print(i ,"times", a//i ,"is", a )
            break
    else:
        print("yes")


if __name__ == '__main__':
    main()
