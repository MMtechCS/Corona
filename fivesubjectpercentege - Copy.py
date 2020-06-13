try:
    st=int(input("enter the number of student"))
    count=0
    result=[]
    while count < st:
        print("Enter the marks of student ", count+1)
        s1 = int(input("enter first subject marks"))
        s2 = int(input("enter second subject marks"))
        s3 = int(input("enter third subject marks"))
        s4 = int(input("enter fourth subject marks"))
        s5 = int(input('enter fifth subject marks'))
        total=s1+s2+s3+s4+s5
        print("total marks is =",total)

        per=(total/500)*100
        print("obtained percentage is", per)

        if (per>=75):
            print("You are passed with First dividion")
        elif (per>=60) and (per<=75):
            print("you are passed with second division")
        elif (per>=40) and (per<=60):
            print("You are passed with third division")
        else:
            print("You marks bellow the 40 % you are fail")


        result.append(total)
        count = count + 1
except ValueError:
    print("something is wronge")