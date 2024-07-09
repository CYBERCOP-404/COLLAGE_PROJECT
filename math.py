# --------------------------------------[ IMPORT SECTION HERE ]------------------------------------------------------- #
from time import sleep
import os
# --------------------------------------[ BANNER SECTION HERE ]------------------------------------------------------- #
BANNER='''\033[0;32m
 --------------------------------------------------------------------------------------------------------------------
|   $$$$$\ $$$$$$$\ $$$$$$\        $$$$$$\   $$$$$$\ $$$$$$$$\       $$$$$$\   $$$$$$\          $$$$$$\  $$\   $$\   |
|   \__$$ |$$  __$$  _$$  _|      $$  __$$\ $$  __$$  __$$  __|     $$  __$$\ $$ ___$$\        $$  __$$\ $$ |  $$ |  |
|      $$ |$$ |  $$ | $$ |        $$ /  \__|$$ /  \__|  $$ |        \__/  $$ |\_/   $$ |       \__/  $$ |$$ |  $$ |  |
|      $$ |$$$$$$$  | $$ |$$$$$$\ $$ |      \$$$$$$\    $$ |$$$$$$\  $$$$$$  |  $$$$$ /$$$$$$\  $$$$$$  |$$$$$$$$ |  |
|$$\   $$ |$$  ____/  $$ |\______|$$ |       \____$$\   $$ |\______|$$  ____/   \___$$  ______|$$  ____/ \_____$$ |  |
|$$ |  $$ |$$ |       $$ |        $$ |  $$\ $$\   $$ |  $$ |        $$ |      $$\   $$ |       $$ |            $$ |  |
|\$$$$$$  |$$ |     $$$$$$\       \$$$$$$  |\$$$$$$  |  $$ |        $$$$$$$$\ \$$$$$$  |       $$$$$$$$\       $$ |  |
| \______/ \__|     \______|       \______/  \______/   \__|        \________| \______/        \________|      \__|  |
|                                                                                                                    |    
 ----------------------------------------------\033[0;31m[CODE WITH NAHID]\033[0;32m-----------------------------------------------------
'''
PBANNER='''\033[0;32m
 -----------------------------------------------------       
|  $$$$$$\ $$\     $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\   |     
| $$  __$$  $$\   $$  |$$  __$$\ $$  _____|$$  __$$\  |       
| $$ /  \__|\$$\ $$  / $$ |  $$ |$$ |      $$ |  $$ | |       
| $$ |       \$$$$  /  $$$$$$$\ |$$$$$\    $$$$$$$  | |      
| $$ |        \$$  /   $$  __$$\ $$  __|   $$  __$$<  |      
| $$ |  $$\    $$ |    $$ |  $$ |$$ |      $$ |  $$ | |        
| \$$$$$$  |   $$ |    $$$$$$$  |$$$$$$$$\ $$ |  $$ | |        
|  \______/    \__|    \_______/  \033[0;31mPHONE VERSON > 2.0\033[0;32m  |     
 -----------------------------------------------------        
'''
COMMAND='''
[1] USE THIS TOOL
[2] VISIT WEBSITE
[+] EXIT THE PROGRAM (CTRL+C)
'''
# ----------------------------------------------[ URL ]------------------------------------------------------------- #
url='https://sites.google.com/view/jpicst2324/home'
# --------------------------------------[ MAIN SECTION HERE ]------------------------------------------------------- #
os.system('clear')
user=input('WHAT IS YOUR DEVICE ? (PHONE/PC/LAPTOP) :~ ')
USERX=user.upper()
if USERX in ['PC', 'LAPTOP']:
    import webbrowser as auto
    while True:
        print(BANNER)
        print(COMMAND)
        USER=int(input('[+] ENTER YOUR CHOICE :~ '))
        if USER==1:
            VAL1=int(input('[+] ENTER 1ST PERSON WEIGHT :~ '))
            VAL2=int(input('[+] ENTER 2ND PERSON WEIGHT :~ '))
            SUM=VAL1+VAL2
            print(f'[💘] YOUR ANSWER IS \033[0;31m{SUM}\033[0;32m .')
            sleep(3)
        elif USER==2:
            auto.open(f'{url}')
        else:
            print('YOU ARE TYPE THE WRONG LATTER . PRESS 1 TO RUN THIS FILE')
            sleep(4)
            auto.open(f'{url}')
if USERX=='PHONE':
    while True:
        os.system('clear')
        print(PBANNER)
        print(COMMAND)
        USER=int(input('[+] ENTER YOUR CHOICE :~ '))
        if USER==1:
            VAL1=int(input('[+] ENTER 1ST PERSON WEIGHT :~ '))
            VAL2=int(input('[+] ENTER 2ND PERSON WEIGHT :~ '))
            SUM=VAL1+VAL2
            print(f'[💘] YOUR ANSWER IS \033[0;31m{SUM}\033[0;32m .')
            sleep(3)
        elif USER==2:
            os.system(f'xdg-open {url}')
        else:
            print('YOU ARE TYPE THE WRONG LATTER . PRESS 1 TO RUN THIS FILE')
            sleep(4)
            os.system(f'xdg-open {url}')
else:
    print('YOU ARE A ALIEN YOU NEED TO DOCTOR COLL ME I AM A DOCTOR ')
# --------------------------------------[ EXIT DEVELOPER NAHID ]------------------------------------------------------- #
