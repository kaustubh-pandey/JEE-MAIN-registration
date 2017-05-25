from encrypt import regencrypt
from random import *
from edit import *
import getpass
def count():
		c=0
		r=open("userpass.txt","r")
		l=r.readline()
		while(l!=""):
			c+=1
			l=r.readline()
		r.close()
		return c
def printf(f1,f2,s1,a,s2,sr,c,s3,r):
	f1.close()
	uid=count()
	f1=open("userpass.txt","a+")
	f1.write(s1)
	f1.write(" ")
	f1.write(str(regencrypt(a,r))+" "+str(r)+" "+str(uid)+"\n")
	#f1.write("\n")
	f2.write(s2)
	f2.write(" ")
	f2.write(sr)
	f2.write(" ")
	f2.write(c)
	f2.write(" ")
	f2.write(s3)
	f2.write(" ")
	f2.write(str(uid))
	f2.write("\n")
	print("#------------Registration Successfull------------#")
	print "Enter your Father's name:",
        father=raw_input()
        print "Enter your Mother's name:",
        mother=raw_input()
        ro=open("additional.txt","a+")
        ro.write(father+"##"+mother+"##"+str(uid)+"\n")
        ro.close()
	addDetails(uid)
	print "Your account has been created.....Login to go to Dashboard"
	f1.close()
	f2.close()
def mail(f1,f2,s1,a,s2,sr,c,r):
	print "EMAIL-ID:",
	try:
		s3=raw_input()
		l1=len(s3)
		t3=0
		a1=s3.count("@")
		b1=s3.count(".")
		c1=s3.index("@")
		d1=0
		if(a1>1 or a1==0 or b1<1 or c1==0 or s3[l1-1]=="." or s3[l1-1]=="@"):
			t3=1
		else:
		 	for i in range(l1):
 				if(s3[i]=="." and i>c1):
 					d1=i
 					break
		if(d1-c1<2):
 			t3=1
	except :
 		t3=1
	if(t3==1):
 		print "#---------Enter Valid E-mail ID-----------#"
 		mail(f1,f2,s1,a,s2,sr,c,r)
	if(t3==0):
 		printf(f1,f2,s1,a,s2,sr,c,s3,r)
def mobile(f1,f2,s1,a,s2,sr,r):
	print "MOBILE NUMBER:",
	c=raw_input()
	e=list(c)
	t=0
	if(e[0]=='0'):
		t=1
	if(len(c)==10):
		 for i in e:
		 	if(i<'0' or i>'9'):
		 		t=1
	if(t==1 or len(c)!=10):
		 print "#-----------Please enter correct 10 digit mobile number------------#"
		 mobile(f1,f2,s1,a,s2,sr,r)
	if(t==0 and len(c)==10):
		mail(f1,f2,s1,a,s2,sr,c,r)
def DOB(f1,f2,s1,a,s2,r):
	print "DATE OF BIRTH(dd/mm/yyyy):",
	sr=raw_input()
	t=list(sr)
	s=sr.split("/")
	val=0
	st=""
	try:
		d1,m1,y1=int(s[0]),int(s[1]),int(s[2])
		if((d1<1 or d1>31)or y1<1 or (m1<1 or m1>12)):
    			val=1
    			print("#-----------Enter correct DOB-----------#")
		for i in s:
			 st=st+i;
		if(len(st)==8 and len(t)==10):
			if(int(s[2])<1998 or int(s[2])>2001):
				print "#----------You are Not eligible for Jee Main Registration-----------#"
    				val=1
		if(len(st)!=8 or len(t)!=10):
			print "#------------Please Enter your Datail carefully------------#"
			DOB(f1,f2,s1,a,s2,r)
	except:
		val=1
		print "#-------Enter Correct Date of Birth in the given format--------#"
	if(val==1):
            DOB(f1,f2,s1,a,s2,r)
	if(len(st)==8 and len(t)==10 and val==0):
		mobile(f1,f2,s1,a,s2,sr,r)
def name(f1,f2,s1,a,r):
	print "NAME:",
	s2=raw_input()
	if(len(s2)<3):
		print "#--------Enter Data Carefully----------#"
		name(f1,f2,s1,a,r)
	if(len(s2)>=4):
		DOB(f1,f2,s1,a,s2,r)

def password(f1,f2,s1):
    try:
	r=randint(0,9)
	#print "PASSWORD:",
	a=getpass.getpass()
	v=0
 	j=0
 	u=0
	#a=getpass.getpass(prompt='PASSWORD:',stream=None)
	if(len(a)<6):
 		u=1
	elif(len(a)>=6):
 		
 		b=getpass.getpass("Re-Enter PASSWORD:",)
 		if(len(b)<6):
 			#print "#--------Please Enter atleast 6 characters--------#"
 			#password(f1,f2,s1)
                        u=1
 		elif(len(a)!=len(b)):
 	 		v=1
 		for i in range(len(a)):
 			if(a[i]!=b[j]):
 				v=1
		 		break
		 	j+=1
    except:
        v=1
    if(u==1):
        print "#----------Please Enter atleast 6 characters------------#"
 	password(f1,f2,s1)
    elif(v==1 or j>len(a)):
 		    print "#-------Password do not match with other--------#"
 		    password(f1,f2,s1)
    elif(v==0 or j<=len(a)):
 		    name(f1,f2,s1,a,r)
 		    
def reg(f1,f2):
	print "USERNAME:",
	s1=raw_input()
	s2=list(s1)
	h=0
	f9=open("userpass.txt","r")
	g=f9.readline()
	for j in s2:
            if(j==" "):
                h=1
                break
        if(h==0):
            while(g!=""):
                f=g.split()
                if(f[0]==s1):
                    print("#---------USERNAME ALREADY EXISTS----------#")
                    reg(f1,f2)
                g=f9.readline() 
	
        if(len(s1)<6):
            	print "#---------Please Enter atleast 6 characters---------#"
		reg(f1,f2)
	elif(h==1):
                print "#-----------Spaces are not allowed----------#"
                reg(f1,f2)
	elif(len(s1)>=6):
		password(f1,f2,s1)
		



f1=open("userpass.txt","a+")
f2=open("about.txt","a+")
#reg(f1,f2)
