import Tkinter as tk
import tkFont
def genAdmit(u):
            the_window = tk.Tk()
            label_font = tkFont.Font(family='Helvetica', size=55)
            labe_font = tkFont.Font(family='Times', size=32)
            la1_font = tkFont.Font(family='Arial',underline="1", size=38)
            f1=open("about.txt","r")
            f2=open("userpass.txt","r")
            f3=open("edit1.txt","r")
            f4=open("additional.txt","r")
            s=f1.readline()
            t=f2.readline()
            v=f3.readline()
            i1=1
            k=0
            str=""
            while(t!=""):
                        a=t.split(" ")
                        if(a[0]==u):
                                    k=int(a[3])
                                    break
                        t=f2.readline()
            while(v!=""):
                        d=v.split("##")
                        l1=len(d)
                        if(int(d[l1-2])==k):
                                    str+=d[2]+","+d[1]
                                    #lbl = tk.Label(the_window,text="CENTER:"+d[2]+","+d[1], font=label_font, borderwidth=0, relief=tk.SOLID)
                                    #lbl.pack()
                                    #print("CENTER:",end="")
                                    #print(d[2]+","+d[1])
                                    break
                        v=f3.readline()
            g=f4.readline()
            sty=""
            while(g!=""):
                h=g.split("##")
                #print(h)
                #print(h[0])
                
                lent=len(h)
                #print(int(h[lent-1]))
                #print(k)
                if(int(h[lent-1])==k):
                    sty+=h[0]
                    break
                g=f4.readline()
            #print(sty)
            while(s!=""):

                        la_font = tkFont.Font(family='Arial', size=25)
                        b=s.split(" ")
                        c=list(s)
		#print(c)
                        st=""
                        l=len(b)
                        i2=0
                        ch="2016010"
                        if(int(b[l-1])==k):
                                    for j in c:
                                                if(j==" "):
                                                            i2+=1
                                                if((j>='A' and j<='Z')or(j>='a' and j<='z')or(j==" ")):
                                                            st+=j
                                                else:
                                                            break
                                    lbl = tk.Label(the_window,text="********"+"ADMIT CARD"+"********", font=label_font, borderwidth=0, relief=tk.RIDGE,fg="red")
                                    lbl.pack()
                                    lbl = tk.Label(the_window,text=" JEE MAINS 2017  ", font=la1_font, borderwidth=0, relief=tk.SOLID)
                                    lbl.pack()
                                    lbl = tk.Label(the_window,text="\n", font=la_font, borderwidth=0, relief=tk.SOLID)
                                    lbl.pack()
                                    lbl = tk.Label(the_window,text="NAME"+" :"+"   "+st, font=la_font, borderwidth=0, relief=tk.SOLID)
                                    lbl.pack()
                                    lbl = tk.Label(the_window,text="  DATE OF BIRTH :"+"   "+b[i2], font=la_font, borderwidth=0, relief=tk.SOLID)
                                    lbl.pack()
                                    lbl = tk.Label(the_window,text="  FATHER'S NAME :"+"   "+sty, font=la_font, borderwidth=0, relief=tk.SOLID)
                                    lbl.pack()
                                    lbl = tk.Label(the_window,text="  EMAIL ADDRESS :"+"   "+b[l-2], font=la_font, borderwidth=0, relief=tk.SOLID)
                                    lbl.pack()
                                    lbl = tk.Label(the_window,text="ROLL NUMBER :   "+ch+b[l-1], font=la_font, borderwidth=0, relief=tk.SOLID)
                                    lbl.pack()
                                    lbl = tk.Label(the_window,text="CENTER  :   "+str, font=labe_font, borderwidth=14, relief=tk.SOLID)
                                    lbl.pack()
			#print("NAME:",end="")
			#print(st)
			#print("DATE OF BIRTH:",end="")
			#print(b[i2])
			#print("E-MAIL:",end="")
			#print(b[l-2])
			#print("ROLL NUMBER:",end="")
			#print(ch+b[l-1])'''
                        s=f1.readline()


            the_window.mainloop()
            f1.close()
            f2.close()
            f3.close()
#genAdmit("As2345")
