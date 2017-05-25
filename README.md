# JEE-MAIN-registration
Author(s): Kaustubh Pandey , Ashish Kumar Patel
----------------------------------------------------------------------------------------------------------------------------------------
*Needs Python 2*
This application lets an organisation to host online exam like JEE MAIN by providing registration facilities.

How to use:
-----------------------------------------------------------------------------------------------------------------------------------------
1. Download all the files and keep them in the same folder
2. Run a.py file using Python 2 on Terminal
3. Follow the instructions on the Terminal
*All the database is stored in the same folder*

Features availabe:
------------------------------------------------------------------------------------------------------------------------------------------
1. Registration
2. Individual Personal Account for every registered user
3. Payment
4. Admit Card generation using GUI
5. Super-user mode(for exam hosting organisation)
6. Notifications
7. Password Encryption

Description:
------------------------------------------------------------------------------------------------------------------------------------------
Registration:
This allows you to register a new user. A new account is created on registration and the password is stored only after encrypting it using a simple technique by generating random integers.

Login:
A user is automatically logged out after completing registration. Login again with the registered username and password to access your account.Payment option is available here along with edit details option and logout option.

Payment:
This allows a user to do one-time payment. After payment, the user can no longer edit details of registration.
The user now gets an option to download admit card with a unique roll no. and the center choosen earlier.

Admit Card:
This function uses Tkinter module of python to generate an admit card(GUI).

Notifications and Super-User:
The notifications are displayed on the starting(home) page. The notifications can't be changed by any normal registered user except the super-user which is only for the hosting organisation.
**************************************************************************************************************************************
Accsessing Super-User:
1. When terminal asks to enter 1-for Login and 2-for Registartion, enter "#$%&*" (without quotes) to enter the super user mode.
2. Enter "admin007" as the superuser name and "!@#$%^&*" as Security Code.
3. The cursor will wait for you to enter a new notification to be displayed under Notifications on the start page.
4. Enter a one line notification and press enter.
The notification gets added in the list of notifications. 
*Note- This project doesn't use any data structure though it can be added easily.
