# Developer ~ MD.NAHIDUL ISLAM
# Team ~ CYBER-COP
# --------------------------------------[ IMPORT SECTION HERE ]------------------------------------------------------- #
from time import sleep
from random import choice
from sys import *
import os
import webbrowser as auto
from math import *
# --------------------------------------[ CLEAR SCKIN PROGRAM ]------------------------------------------------------------- #
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# --------------------------------------[ MAIN ANNIMATION ]------------------------------------------------------------ #
animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
# --------------------------------------[ ANIMATION PROGRAM ]---------------------------------------------------------- #
def anima(animation):
    for i in range(len(animation)):
        sleep(0.5)
        stdout.write("\r[😊] PREPARING... " + animation[i % len(animation)])
        stdout.flush()
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
[1]   USE PROGRAM 1
[2]   USE PROGRAM 2
[3]   USE PROGRAM 3
[4]   USE PROGRAM 4
[5]   USE PROGRAM 5
[6]   USE PROGRAM 6
[7]   USE PROGRAM 7
[8]   USE PROGRAM 8  (This is calculator .)
[9]   USE PROGRAM 9
[10]  USE PROGRAM 10
[11]  USE PROGRAM 11
[+]   JOIN OUR GROUP 
'''
# --------------------------------------[ EXTRA CODE HERE ]--------------------------------------------------------- #
url='https://www.github.com/cybercop-404'
# --------------------------------------[ MAIN SECTION HERE ]--------------------------------------------------------- #
clear()
anima(animation)
while True:
    clear()
    print(BANNER,COMMAND)
    choice=input('\033[0;33mENTER YOUR CHOICE :~ ')
    # ------------------------------[PROGRAM 1] ----------------------------- #
    if choice =='1':
        for i in range(0,3):
            user=input('\033[0;33m[+] ENTER YOUR WORD :~ ')
            user=user.casefold()
            reverse_word= user[::-1]
            if user==reverse_word:
                print('\033[0;32mYOUR WORD IS PALLINDROME ')
                sleep(3)
            else:
                print('\033[0;31mYOUR WORD IS NOT PALLINDROME')
                sleep(3)
        print('YOUR TOKEN IS OVER .\n ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)
    # -----------------------------[PROGRAM 2] ------------------------------- #
    elif choice=='2':
        for i in range(3):
            user=int(input('\033[0;33mENTER YOUR NUMBER :~ '))
            if user%2==0:
                if user%3==0:
                    print('\033[0;32mThis Number is divisible by 2 and 3 ')
                else:
                    print('\033[0;32mThis number id divisible by 2 ')
            elif user%3==0:
                print('\033[0;32mThis Number is divisible by 3 ')
            else:    
                print('\033[0;31mThis Number is not divisible by 2 and 3 ')
        print('YOUR TOKEN IS OVER .\n ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)
    # -----------------------------[PROGRAM 3] ------------------------------- #
    elif choice=='3':
        for i in range(3):
            user=int(input('\033[0;33mENTER YOUR MARKS :~ '))
            if user>100:
                print('\033[0;31mPlease enter valid number ... ')
            else:
                if user>=90:
                    print('\033[0;32mYour grade is  A+')
                else:
                    if user>=80:
                        print('\033[0;32mYour grade is  A')
                    else:
                        if user>=70:
                            print('\033[0;32mYour grade is  A-')
                        else:
                            if user>=60:
                                print('\033[0;32mYour grade is  B ')
                            else:
                                if user>=50:
                                    print('\033[0;32mYour grade is  C ')
                                else:
                                    if user>=33:
                                        print('\033[0;32mYour grade is  D')
                                    else:
                                        if user<33:
                                            print('\033[0;31mYour grade is  fail ')
        print('YOUR TOKEN IS OVER .\n ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)           
    # -----------------------------[PROGRAM 4] ------------------------------- #
    elif choice=='4':
        for i in range(3):
            user=int(input('\033[0;33mENTER YOUR NUMBER :~ '))
            if user%2==0:
                print('\033[0;34mThis Number Was Even Number .')
            else:
                print('\033[0;30mThis number was odd number ')
        print('YOUR TOKEN IS OVER .\n ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)
    # -----------------------------[PROGRAM 5] ------------------------------- #
    elif choice=='5':
        for i in range(3):
            user_mark=int(input('\033[0;33mENTER YOUR MARKS :~ '))
            if user_mark>100:
                print('\033[0;31mPLEASE ENTER VALID MARKS ')
                breakpoint
            elif user_mark>=90:
                print('\033[0;32mYour grade is  A+')
            elif user_mark>=80:
                print('\033[0;32mYour grade is  A')
            elif user_mark>=70:
                print('\033[0;32mYour grade is  A-')
            elif user_mark>=60:
                print('\033[0;32mYour grade is  B')
            elif user_mark>=50:
                print('\033[0;32mYour grade is  C')
            elif user_mark>=33:
                print('\033[0;32mYour grade is  D')
            else:
                print("\033[0;31mYOU ARE FAIL BRO . JOIN OUR TEAM TO PASS THE EXAM .")
                os.system(f'xdg-open {url}')
                auto.open_new(url)
        print('YOUR TOKEN IS OVER .\t ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)
    # -----------------------------[PROGRAM 6] ------------------------------- #
    elif choice=='6':
        for i in range(3):
            time=int(input('\033[0;33mENTER YOUR TIME HOUR :~ '))
            if time in [4,5,6,7,8,9,10]:
                print('\033[0;32mgood morning....')
            elif time in [11,12,13,14,15]:
                print('\033[0;34mgoon noon .... ')
            elif time in [16,17,18]:
                print('\033[0;35mgood evening .....')
            elif time in [19,20,21,22,23,24]:
                print('\033[0;33mgood night .....')
            else:
                print('\033[0;31mplease enter the valid time')
        print('YOUR TOKEN IS OVER .\t ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)
    # -----------------------------[PROGRAM 7] ------------------------------- #
    elif choice=='7':
        for i in range(3):
            a=int(input('\033[0;33mEnter your 1st Number :~ '))
            b=int(input('\033[0;33mEnter your 2nd NUMBER :~ '))
            c=int(input('\033[0;33mEnter your 3rd NUMBER :~ '))
            if a>b and a>c:
                print(f'\033[0;32myour big number is {a} .')
            elif b>a and b>c:
                print(f'\033[0;32myour big number is {b} .')
            else:
                print(f'\033[0;32myour big number is {c} .')
        print('\033[0;31mYOUR TOKEN IS OVER .\t ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)
    # -----------------------------[PROGRAM 8] ------------------------------- #
    elif choice=='8':
        for i in range(3):
            user=input('\033[0;33mENTER YOUR MATH HERE (2+5-4) :~ ')
            print(f'\033[0;32mYour math answer is \033[0;31m{eval(user)}')
        print('\033[0;31mYOUR TOKEN IS OVER .\t ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)
    # -----------------------------[PROGRAM 9] ------------------------------- #
    elif choice=='9':
        for i in range(3):
            A=int(input('VAL A :~ '))
            B=int(input('VAL B :~ '))
            C=int(input('VAL C :~ '))
            if (A+B)>C and (B+C)>A and (C+A)>B:
                S=(A+B+C)/2
                AREA=sqrt(S*(S-A)*(S-B)*(S-C))
                print(AREA)
            else:
                print('TRIANGLE NOT POSSIBLE ')
        print('\033[0;31mYOUR TOKEN IS OVER .\t ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)
    # -----------------------------[PROGRAM 10] ------------------------------- #   
    elif choice=='10':
        for i in range(3):
            A=int(input('VAL A :~ '))
            B=int(input('VAL B :~ '))
            C=int(input('VAL C :~ '))
            dis=(B**2)-(4*A*C)
            if (dis>0):
                root1=(-B+sqrt(dis)/(2*A))
                root2=(-B -sqrt(dis)/(2*A))
                print('Two distinct real roots are %.2f and %.2f'%(root1,root2))
            elif (dis==0):
                root1=root2=-B/(2*A)
                print('Two equal and real roots are %.2f and %.2f'%(root1,root2))
            elif(dis<0):
                root1=root2=-B/(2*A)
                imaginary =sqrt(-dis)/(2*A)
                print('Two distinct complex roots are %.2f+%.2f and %.2f-%.2f'%(root1,imaginary,root2,imaginary))
        print('\033[0;31mYOUR TOKEN IS OVER .\t ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)
    # -----------------------------[PROGRAM 11] ------------------------------- # 
    elif choice=='11':
        for i in range(3):
            NUM1=int(input('ENTER YOUR NUMBER 1 :~ '))
            NUM2=int(input('ENTER YOUR NUMBER 2 :~ '))
            NUM3=int(input('ENTER YOUR NUMBER 3 :~ '))
            if NUM1>NUM2 and NUM1>NUM3:
                print(f'Your large number is {NUM1} .')
            elif NUM2>NUM1 and NUM2>NUM3:
                print(f'Your large number is {NUM2} .')
            elif NUM3>NUM1 and NUM3>NUM2:
                print(f'Your large number is {NUM3} .')
        print('\033[0;31mYOUR TOKEN IS OVER .\t ENTER 0 TO CLOSE PROGRAM .')
        publisity = input(' > ')
        if publisity=="0":
            breakpoint
        else:
            os.system(f'xdg-open {url}')
            auto.open_new(url)
    # -----------------------------[Footer] ------------------------------- # 
    else:
        os.system(f'xdg-open {url}')
        auto.open_new(url)
# --------------------------------------[ PROGRAM END  ]-------------------------------------------------------------- # 
