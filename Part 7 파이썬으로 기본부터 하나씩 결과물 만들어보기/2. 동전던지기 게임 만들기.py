front = '''
          __-----__
     ..;;;--'~~~`--;;;..
   /;-~IN GOD WE TRUST~-.\
  //      ,;;;;;;;;      \\
.//      ;;;;;    \       \\
||       ;;;;(   /.|       ||
||       ;;;;;;;   _\      ||
||       ';;  ;;;;=        ||
||LIBERTY | ''\;;;;;;      ||
 \\     ,| '\  '|><| 1995 //
  \\   |     |      \  A //
   `;.,|.    |      '\.-'/
     ~~;;;,._|___.,-;;;~'
         ''=--'

'''

back = '''

           _.-------._
        _-'_.------._ `-_
      _- _-          `-_/
     -  -
 ___/  /______________
/___  .______________/
 ___| |_____________
/___  .____________/
    \  \
     -_ -_             /|
       -_ -._        _- |
 Benoit  -._ `------'_./
 Rigaut     `-------'
 
 
'''

print("동전게임에 오신것을 환영합니다.")
answer = int(input("앞면일까요? 뒷면일까요? 0:앞면 , 1:뒷면\n"))

import random

computer = random.randint(0,1)
print("동전결과 : ")
if computer == 0:
    print(front)
else:
    print(back)
    
print("나의선택 : ")
if answer == 0:
    print(front)
else:
    print(back)
print("게임결과 : ")
if computer == answer:
    print("정답입니다.")
else:
    print("오답입니다.")

