# --------------------------------------[ BANNER SECTION HERE ]------------------------------------------------------- #
import os
from time import sleep
from random2 import choice
from sys import stdout
# --------------------------------------[ MAIN ANNIMATION ]------------------------------------------------------------ #
animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
# --------------------------------------[ ANIMATION PROGRAM ]---------------------------------------------------------- #
def anima(animation):
    for i in range(len(animation)):
        sleep(0.5)
        stdout.write("\r[😊] PREPARING... " + animation[i % len(animation)])
        stdout.flush()
# --------------------------------------[ CLEAR PROGRAM ]------------------------------------------------------------- #
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
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
PROGRAM1='python calculator.py'
PROGRAM2='python mait.py'
PROGRAM3='python math.py'
OK_LIST=[PROGRAM1,PROGRAM2,PROGRAM3]
# --------------------------------------[ MAIN BODY ]------------------------------------------------------- #
while True:
    clear()
    anima(animation)
    clear()
    print(BANNER,COMMAND)
    user=int(input('[+] ENTER YOUR CHOICE :~ '))
    if user==1:
        os.system(PROGRAM1)
    elif user==2:
        os.system(PROGRAM2)
    elif user==3:
        os.system(PROGRAM3)
    elif user==4:
        out=choice(OK_LIST)
        os.system(out)
    else:
        for i in range(10,0,-1):
            sleep(0.5)
            os.system('clear')
            print(BANNER)
            print(f'TRY AFTER {i} SECOND')
            sleep(0.5)
# --------------------------------------[ EXIT DEVELOPER NAHID ]------------------------------------------------------- #
