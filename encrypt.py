#encrypt
#import rand in registration

def encrypt(string,j):
			s=[]
			for i in range(len(string)):
						s.append(str(ord(string[i])-j))
			s=str("".join(s))
			return s

def regencrypt(string,rand):
			x=[]
			for i in range(len(string)):
						x.append(str(ord(string[i])-rand))
			x=str("".join(x))
			return x
