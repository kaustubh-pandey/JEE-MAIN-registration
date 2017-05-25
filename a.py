#HOMEPAGE
from regnew import reg as Registration
from login import login as Login
from sup import *
f1=open("userpass.txt","a+")
f2=open("about.txt","a+")
f3=open("not.txt","r")
rege=0
t=f3.read()
f3.close()
while(rege==0):
	print "\n\n"
	print "\033[93m"+"       * * * * *   * * * * *   * * * * *      *       *        *         * * * * *  *       *   "
	print "           *       *           *              * *   * *       * *           *       **      *           "
	print "           *       *           *              *   *   *      *   *          *       * *     *           "
	print "           *       * * * *     * * * *        *       *     *     *         *       *  *    *   "
	print "           *       *           *              *       *    * * * * *        *       *   *   *           "
	print "       *   *       *           *              *       *   *         *       *       *     * *           "
	print "       * * *       * * * * *   * * * * *      *       *  *           *  * * * * *   *       *   "
	print "\n"
	print "                                  * * *     * * * * *     *   * * * * *                                   "
	print "                                 *     *    *       *   * *           *                                   "
	print "                                       *    *       *     *          *                                    "
	print "                                      *     *       *     *         *                                     "
	print "                                    *       *       *     *        *                                      "
	print "                                  *         *       *     *       *                                       "
	print "                                *           *       *     *      *                                        "
	print "                               *            *       *     *     *                                         "
	print "                               * * * **     * * * * *   * * *  *                                          "
	print "\n"
	print "          Enter 1 for Login                    Enter 2 for Registration                     \n "
	print "NOTIFICATIONS"+"\033[0m"

	print "\033[91m"+t+"\033[0m"
	print "\n\n"
	print "Enter your choice: 1 or 2",

	n=raw_input()
	if(n=="#$%&*"):
		t=superuser()

	elif(int(n)==1):
		d=Login()
		rege=1
		if(d==0):
			rege=0

	elif(int(n)==2):
		Registration(f1,f2)
		rege=0
	else:
		print "Input Number is not valid."
		rege=0
