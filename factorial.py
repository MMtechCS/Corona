try:

    num=int(input("enter the number to get its factorial"))
    fact=1
    for i in range(num,0,-1):
        print(i,'*')
        fact=i*fact
        print("=",fact)
except ValueError:
    print("Enter only number to get its factorial")



