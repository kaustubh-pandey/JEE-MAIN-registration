#PAYMENT
def payment(uid):
        print "Enter your 16 digit credit card number:",
        cno=raw_input()
        if(len(cno)!=16 or cno.isdigit()==False):
                print("Invalid number.Try again")
                payment(uid)
        e=0
        while(e==0):
            print "Enter the expiry date of your debit card(mm/yy):",
            exp=raw_input()
            e=1
            if(exp[2]!='/'):
                    print "Please enter the expiry date in correct format."
                    e=0
            if(exp[0].isdigit() and exp[1].isdigit() and exp[3].isdigit() and exp[4].isdigit()):

                        month=10*int(exp[0])+int(exp[1])
                        if(month<=0 or month>12):
                                    print "Please enter the expiry date correctly"
                                    e=0
                        year=10*int(exp[3])+int(exp[4])
                        if(year<=16 or year>50):
                                    print "Please enter the expiry date correctly"
                                    e=0
            else:
                e=0
                print "Enter the expiry date correctly"
        c=0
        while(c==0):
                print "Enter the CVV/CVC number(3 digit):",
                cvv=raw_input()
                if(len(cvv)==3 and cvv.isdigit()==True):
                        c=1
                else:
                    print "Enter the CVV/CVC number correctly"
                    c=0
        print "A total of 2000 rupees would be deducted from your account"
        print "Do you want to continue payment?  Press y-YES  n-NO"
        response=raw_input()
        if(response=="n" or response=="N"):
                    print "Your transaction was cancelled"
                    payment(uid)
        elif(response=="y" or response=="Y"):
                    print "Your transaction was Successfull. You have been registered"
                    f=open("edit1.txt","r+")
                    l=f.readline()
                    s=[]
                    while(l!=""):
                      s.append(l.split("##"))
                      l=f.readline()
                    f.close()
                    for i in range(len(s)):
                        if(int(s[i][3])==uid):
                            s[i][4]="1\n"
                    f=open("edit1.txt","w+")
                    for i in range(len(s)):
                        f.write("##".join(s[i]))
                    f.close()

        else:
            print "Please enter correct option"
            print "Do you want to continue payment?  Press y-YES  n-NO"
            response=input()
            if(response=="n" or response=="N"):
                        print "Your transaction was cancelled"
                        payment(uid)
            elif(response=="y" or response=="Y"):
                        print "Your transaction was Successfull. You have been registered"
                        f=open("edit1.txt","r+")
                        l=f.readline()
                        s=[]
                        while(l!=""):
                          s.append(l.split("##"))
                          l=f.readline()
                        f.close()
                        for i in range(len(s)):
                            if(int(s[i][3])==uid):
                                s[i][4]="1\n"
                        f=open("edit1.txt","w+")
                        for i in range(len(s)):
                            f.write("##".join(s[i]))
                        f.close()
            else:
                    print "Your transaction was cancelled" 
                    payment(uid)
