import random
import time
def countdown(t):
    while t:
        mins,secs = divmod(t,60)
        timer ='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t-=1
        
# saqib python develpor 

print("\n"*3)
lent=6
passlen = (input("send OTP :"))
if passlen=="yes":
    no=str(input("please enter your number :"))
    if (len (no))==11:
        t=10
        print("otp sending...")
        countdown(t)
        print()
        s="0123456789"
        p = "".join(random.sample(s,lent))
        
        print("your OTP is ",p,"  Don't share with other     ")
        t=20
        countdown(t)
        print()
        print("        X  OTP deleted"    )
        print()
        resend=str(input(" resend :"))
        if resend=="yes":
            t=10
            print("otp sending...")
            countdown(t)
            print()
            s="0123456789"
            p = "".join(random.sample(s,lent))
        
            print("your OTP is ",p,"  Don't share with other     ")
            t=20
            countdown(t)
            print()
            print("        X  OTP again deleted !!!    pliz try after 1 hour  "   )
            t=3600
            countdown(t)
        else:
            print("finished")
        

        print("\n"*3)
    else:
        print("please provide correct or complete number")
else:
    print(" OK bye")