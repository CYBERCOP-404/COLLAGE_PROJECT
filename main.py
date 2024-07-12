# --------------------------------------[ BANNER SECTION HERE ]------------------------------------------------------- #
import os
from time import sleep
from random2 import choice
# --------------------------------------[ BANNER SECTION HERE ]------------------------------------------------------- #
BANNER='''\033[0;32m
 -----------------------------------------------------       
|  $$$$$$\ $$\     $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\   |     
| $$  __$$  $$\   $$  |$$  __$$\ $$  _____|$$  __$$\  |       
| $$ /  \__|\$$\ $$  / $$ |  $$ |$$ |      $$ |  $$ | |       
| $$ |       \$$$$  /  $$$$$$$\ |$$$$$\    $$$$$$$  | |      
| $$ |        \$$  /   $$  __$$\ $$  __|   $$  __$$<  |      
| $$ |  $$\    $$ |    $$ |  $$ |$$ |      $$ |  $$ | |        
| \$$$$$$  |   $$ |    $$$$$$$  |$$$$$$$$\ $$ |  $$ | |        
|  \______/    \__|    \_______/  \033[0;31mPHONE VERSON > 2.3\033[0;32m  |     
 -----------------------------------------------------        
'''
COMMAND='''
[1] USE VIP CALCULATOR
[2] USE THIS JPI MATH
[3] USE CALCULATOR NORMAL PROGRAM
[4] USE RANDOM PROGRAM
[+] WATE FOR UPDATE
'''
# --------------------------------------[ MAIN BODY ]------------------------------------------------------- #
while True:
    print(BANNER,COMMAND)
    user=int(input('[+] ENTER YOUR CHOICE :~ '))
    if user==1:
        os.system('python calculator.py')
    elif user==2:
        os.system('python mait.py')
    elif user==3:
        os.system('python simple_math.py')
    else:
        for i in range(10,0,-1):
            sleep(0.5)
            os.system('clear')
            print(BANNER)
            print(f'TRY AFTER {i} SECOND')
            sleep(0.5)
# --------------------------------------[ EXIT DEVELOPER NAHID ]------------------------------------------------------- #
