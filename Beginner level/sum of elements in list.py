def main():
   arr = []
   sum=0
   n=int(raw_input())
   k=int(raw_input())
   for i in range(n):
    a=int(raw_input())
    arr.append(a)
    print(a)
   for i in range(k):
    sum=sum + a
   print(sum)



if __name__ == '__main__':
    main()
