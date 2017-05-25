import getpass
def superuser():
    text="No notifications"
    fw=open("not.txt","a+")
    print "Enter your superuser name"
    sup=raw_input()
    if(sup=="admin007"):
        print "Enter the security code"
        p=getpass.getpass()
        if(p=="!@#$%^&*"):
            text=raw_input()
            fw.write("\n")
            fw.write(text)
    fw.close()
    fw=open("not.txt","r")
    l=fw.read()
    return l
