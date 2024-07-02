# --------------------------[IMPORT]--------------------------- #
import os
import webbrowser as auto
from time import sleep
# --------------------------[BANNAR]--------------------------- #
BANNER = '''\033[0;32m
   .----------------.  .----------------.  .----------------. 
  | .--------------. || .--------------. || .--------------. |
  | |     _____    | || |   ______     | || |     _____    | |
  | |    |_   _|   | || |  |_   __ \   | || |    |_   _|   | |
  | |      | |     | || |    | |__) |  | || |      | |     | |
  | |   _  | |     | || |    |  ___/   | || |      | |     | |
  | |  | |_' |     | || |   _| |_      | || |     _| |_    | |
  | |  `.___.'     | || |  |_____|     | || |    |_____|   | |
  | '--------------' || '--------------' || '--------------' |
   '----------------'  '----------------'  '----------------' 
               \033[0;34mPRO DEVELOPER MD NAHIDUL ISLAM
\033[0;31m________________________________________________________________\033[0;32m
'''
COMMAND ='''
  [1] Suggestion 1 
  [2] Suggestion 2 
  [3] Value of Triangle
  [4] WATE FOR UPDATE  
  [+] VISIT OUR WEBSITE PRESS ENTER 
'''
print(BANNER)
print(COMMAND)
USER = int(input('  [🙅] WHAT IS YOUR CHOICE : '))
if USER==1:
    num1=int(input('  [+] ENTER YOUR FIRST NUMBER : '))
    num2=int(input('  [+] ENTER YOUR SECOND NUMBER : '))
    Sum =num1+num2
    print(f'  [🎯] Your math answer is \033[0;33m{Sum}\033[0;30m ')
elif USER==2:
    num1=int(input('  [+] ENTER YOUR 1st NUMBER : '))
    num2=int(input('  [+] ENTER YOUR 2nd NUMBER : '))
    num3=int(input('  [+] ENTER YOUR 3rd NUMBER : '))
    num4=int(input('  [+] ENTER YOUR 4th NUMBER : '))
    num5=int(input('  [+] ENTER YOUR 5th NUMBER : '))
    SUM=num1+num2+num3+num4+num5
    print(f'  [🎯] Your math answer is \033[0;33m{SUM}\033[0;30m ')
elif USER==3:
    num1=int(input('  [+] ENTER YOUR FIRST NUMBER : '))
    num2=int(input('  [+] ENTER YOUR SECOND NUMBER : '))
    Sum =0.5*num1*num2
    print(f'  [🎯] Your math answer is \033[0;33m{Sum}\033[0;30m ')
sleep(4)
url ='https://sites.google.com/view/jpicst2324/home'
auto.open_new_tab(url)
os.system(f'xdg-open {url}')
