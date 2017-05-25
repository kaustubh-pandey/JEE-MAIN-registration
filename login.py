#python
#checking from file userpass.txt
#fields- username password int(0-9) uid
from encrypt import *
from edit import *
from payment import *
from paynew import *
import getpass
def login():
	log=0
	while(log==0):
		print "******************************* LOGIN**********************************************************"
		print("Enter # in username to go back")
		print "USERNAME : ",
		username=raw_input()
		if(username=="#"):
				return 0
		
		pas=getpass.getpass("Password:",)
		fp=open("userpass.txt","r+")

		s=fp.readline()
		c=0
		while(s!=""):
			a=s.split()
			password=encrypt(pas,int(a[2]))
			#print(password,a[2])
			if(a[0]==username and a[1]==password):
								c=0
								uid=int(a[3])
								log=1
								break
								c+=1
			s=fp.readline()
		if(c!=0):
							print "Please enter valid username and password\n\n"
							log=0
		if(log==0):
										print "LOGIN AGAIN\n"
		else:
										print "LOGIN SUCCESSFUL...DASHBOARD\n\n"
										dash=0
										f=open("edit1.txt","r+")
										line1=f.readline()
										while(line1!=""):
											if(int(line1.split("##")[3])==uid):
												if(int(line1.split("##")[4])==1):
													login2(username)
													dash=1
													log=0
											line1=f.readline()
										f.close()
										while(dash==0):
											print "PRESS -  e:Edit     p:Pay       x:logout       \n"
											option=raw_input()
											if(option=="x"):
												print "You are logging out.......\n"
												dash=1
												log=0
											elif(option=="e"):
												print "******************************EDITING MODE*****************************************"
												print "\n\n"
												editing(uid)
												dash=0
											elif(option=="p"):
												print "******************************PAYMENT OPTIONS**************************************"
												print "\n\n"
												payment(uid)

#login()
def login2(username):
								log=0
								while(log==0):
												print "PRESS - g: Generate admit card     x:logout\n"
												option=raw_input()
												if(option=="x"):
													print "You are logging out.......\n\n"
													log=1
												elif(option=="g"):
														print "Generating admit card....\n"
														genAdmit(username)
														log=0
