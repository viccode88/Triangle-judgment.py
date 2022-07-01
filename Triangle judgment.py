import colorama
from colorama import Fore
from colorama import Style
import time

colorama.init()

print(Fore.GREEN+'此程式會重複接受輸入，若要停止請輸入 stop 即可停止'+ Style.RESET_ALL)
while(True):
    try:
        colorama.init()
        print(Fore.BLUE+Style.BRIGHT+'輸入三角形邊長(輸入完畢後請按ENTER確定)'+Style.RESET_ALL)
        a = input()
        if a == 'stop':
            
            print(Fore.RED+'程式已結束，將在3秒後退出'+ Style.RESET_ALL)
            print(Fore.RED+'3'+ Style.RESET_ALL)
            time.sleep(1)
            print(Fore.RED+'2'+ Style.RESET_ALL)
            time.sleep(1)
            print(Fore.RED+'1'+ Style.RESET_ALL)
            time.sleep(1)
            break
        a = list(map(int,a.split()))
        a = sorted(a)
        if a[0]+a[1] > a[2] :
            print(Fore.GREEN+'是三角形'+ Style.RESET_ALL)
        elif a[0]+a[1] == a[2]:
            print(Fore.YELLOW+'不是三角形(原因:邊長 %d 與邊長 %d 之和等於邊長 %d '% (a[0],a[1],a[2])+ Style.RESET_ALL)
        else:
            print(Fore.YELLOW+'不是三角形(原因:邊長 %d 與邊長 %d 之和小於邊長 %d '% (a[0],a[1],a[2])+ Style.RESET_ALL)
    except:
        colorama.init()
        print(Fore.RED+'ERROR:您輸入了此程式無法接受之數據，將跳回上一個動作'+ Style.RESET_ALL)
