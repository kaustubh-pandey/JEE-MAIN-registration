#read everyline from a file and store in list.Then modify and write back in file
from encrypt import *
from random import *
import getpass
def addDetails(uid):
        print "Enter your residential address:"
        address=raw_input().strip()
        print "Enter your preferred city for exam:"
        e=1
        while(e==1):
                print "Enter 1:Ranchi  2:Kolkata  3:Chennai  4:Hyderabad  5:Delhi  6:Patna"
                cr=raw_input()
                if(cr=="1"):
                        city="Ranchi"
                        e=0
                elif(cr=="2"):
                        city="Kolkata"
                        e=0
                elif(cr=="3"):
                        city="Chennai"
                        e=0
                elif(cr=="4"):
                        city="Hyderabad"
                        e=0
                elif(cr=="5"):
                        city="Delhi"
                        e=0
                elif(cr=="6"):
                        city="Patna"
                        e=0
                else:
                        print("Enter the correct choice")
                        e=1
        
        print "Enter your preferred center:"
        g=1
        while(g==1):
                print "Enter  1:D.A.V.   2:J.V.M. shyamali    3:D.P.S.   4:VIvekanand     5:Kendriya Vidyalaya      6:Chaitanya"
                ce=raw_input()
                if(ce=="1"):
                        center="D.A.V."
                        g=0
                elif(ce=="2"):
                        center="J.V.M. shyamali"
                        g=0
                elif(ce=="3"):
                        center="D.P.S."
                        g=0
                elif(ce=="4"):
                        center="VIvekanand"
                        g=0
                elif(ce=="5"):
                        center="Kendriya Vidyalaya"
                        g=0
                elif(ce=="6"):
                        center="Chaitanya"
                        g=0
                else:
                        print("Enter the correct choice")
                        g=1
        f=open("edit1.txt","a+")
        f.write(address+"##"+city+"##"+center+"##"+str(uid)+"##"+str("0")+"\n")
        f.close()
def edit(s,z,uid):
        print "Press:  1-edit Address       2-edit city       3-edit center        4-edit password     5-exit"
        q=raw_input()
        for i in range(len(s)):
            if(int(s[i][3])==uid and int(z[i][3])==uid):
                        if(q=="1"):
                                print "Enter new address.(In 1 line only)"
                                s[i][0]=raw_input().strip()
                                edit(s,uid)
                        elif(q=="2"):
                                    print "Enter your preferred city"
                                    s[i][1]=raw_input().strip()
                                    edit(s,uid)
                        elif(q=="3"):
                                    print "Enter your preferred center"
                                    s[i][2]=raw_input().strip()
                                    edit(s,uid)
                        elif(q=="4"):
                                     passw=getpass.getpass("Enter old password:",)
                                     key=int(z[i][2])
                                     passw=encrypt(passw,key)
                                     if(passw==z[i][1]):
                                              
                                             k=randint(0,9)
                                             newpass=getpass.getpass("Enter new password:",)
                                             newpass=regencrypt(newpass,k)
                                             z[i][1]=newpass
                                             z[i][2]=str(k)
                                                                                
                                                        
                        elif(q=="5"):
                                print "Going back to dashboard..."
                        else:
                            print "Please enter a valid number"
                            edit(s,uid)


def editing(uid):
        f=open("edit1.txt","r+")
        g=open("userpass.txt","r+")
        l=f.readline()
        l1=g.readline()
        s=[]
        z=[]
        while(l!=""):
          s.append(l.split("##"))
          z.append(l1.split(' '))
          l=f.readline()
          l1=g.readline()
        #print z
        f.close()
        g.close()
        #write editing part here
        edit(s,z,uid)
        #rewrite in file .

        f=open("edit1.txt","w+")
        g=open("userpass.txt","w+")
        for i in range(len(s)):
            f.write("##".join(s[i]))
        for i in range(len(z)):
                g.write(" ".join(z[i]))
        f.close()
        g.close()
#To test this part main function is being added
#print("enter uid:")
#uid=int(input())
#editing(uid)
