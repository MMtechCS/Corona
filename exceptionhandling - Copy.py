try:
    print("Freez is open")
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    print("a=",a,"b=",b)
    if b==0:
        print("division is not possible")
    else:
        d = a / b
        print("div", d)
        print("thanks you")
except ValueError:
    print("you have enter the character not number")


except ZeroDivsionError:
    print('value of b can not zero')

except Exception:
    print("something is wrong")

finally:
    print("Freez is close")
    print("thanks you")