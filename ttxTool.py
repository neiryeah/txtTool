# -->> txtTool by ne1ry, 2023 belongs to ttClient...
# htttps://discord.gg/ttClient ----

from colorama import Fore
import pyautogui as py
import os
import time
from pynput.mouse import Button, Controller
import keyboard
import pynput.mouse
import pynput.keyboard


os.system('title txtTool')
mouse = Controller()
renk = Fore.BLUE

print(renk + "\n\n\n\n\n                         __                  __   ________                    __ ")
print(renk + "                        |  \                |  \ |        \                  |  ")
print(renk + "                       _| $$_    __    __  _| $$_ \$$$$$$$$______    ______  | $$")
print(renk + "                      |   $$ \  |  \  /  \|   $$ \  | $$  /      \  /      \ | $$")
print(renk + "                       \$$$$$$   \$$\/  $$ \$$$$$$  | $$ |  $$$$$$\|  $$$$$$\| $$")
print(renk + "                       \$$$$$$   \$$\/  $$ \$$$$$$  | $$ |  $$$$$$\|  $$$$$$\| $$")
print(renk + "                        | $$ __   >$$  $$   | $$ __ | $$ | $$  | $$| $$  | $$| $$")
print(renk + "                        | $$|  \ /  $$$$\   | $$|  \| $$ | $$__/ $$| $$__/ $$| $$")
print(renk + "                         \$$  $$|  $$ \$$\   \$$  $$| $$  \$$    $$ \$$    $$| $$")
print(renk + "                          \$$$$  \$$   \$$    \$$$$  \$$   \$$$$$$   \$$$$$$  \$$\n\n               " + Fore.CYAN +"                   txtTool from ttClient, by ne1ry\n                                  Her turlu iletisim icin ne1ry#1881\n\n")
                                                           
xx = input(Fore.RED + "[X]" + Fore.CYAN +   " --> Başlamak için Enter basınız..\n\n\n")



print(Fore.YELLOW + "###################################---Makro Seçimi---#############################\n")



KEYS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'enter', 'tab', 'space', 'backspace', 'delete', 'insert', 'home', 'end', 'page_up', 'page_down',
    'up', 'down', 'left', 'right',
    'caps_lock', 'num_lock', 'scroll_lock', 'print_screen', 'pause',
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
    'shift', 'ctrl', 'alt', 'alt_gr', 'super', 'menu',
    'plus', 'minus', 'asterisk', 'slash', 'backslash', 'tilde', 'equals', 'comma', 'period', 'apostrophe', 'semicolon', 'left_bracket', 'right_bracket',
    'numpad_0', 'numpad_1', 'numpad_2', 'numpad_3', 'numpad_4', 'numpad_5', 'numpad_6', 'numpad_7', 'numpad_8', 'numpad_9',
    'numpad_add', 'numpad_subtract', 'numpad_multiply', 'numpad_divide', 'numpad_decimal', 'numpad_enter',''
]
          
while True:
    #Durdurma Key seçimi:

    while True:
        durdurma = input(Fore.YELLOW + "          Makronuzu hangi Tuşla durdurmak istersiniz: ")
        if durdurma == "":
            print(Fore.RED + "          Atadığınız tuş, bir klavye tuşuna benzemiyor, lütfen doğru bir tuş giriniz.")
        elif durdurma in KEYS:
            break
        else:
            print(Fore.RED + "          Atadığınız tuş, bir klavye tuşuna benzemiyor, lütfen doğru bir tuş giriniz.")
        

    #Kılıç Slot seçimi


    while True:
        kilicSlot = input(Fore.YELLOW + "          Kılıcınızın slotunuz giriniz: ")
        try:
            kilicSlot = int(kilicSlot)
        except:
            print(Fore.RED + "          Kılıc slotunuza 0-10 arası bir sayı yazmanız gerekmektedir, lütfen doğru yazınız.")
        else:
            if  0<int(kilicSlot)<10: 
                kilicSlot = str(kilicSlot)
                break
            else:
                print(Fore.RED + "          Kılıc slotunuza 0-10 arası bir sayı yazmanız gerekmektedir, lütfen doğru yazınız.")


    # //Hit makrosu atama seçimleri

    while True:
        hitMakrosu = input(Fore.GREEN + "\n          Hit Makrosunu atamak istediğiniz tuşu giriniz, eğer hit makrosu kullanmayacaksanız boş bırakın: ")
        if hitMakrosu in KEYS:
            break
        else:
            print(Fore.RED + "          Atadığınız tuş, bir klavye tuşuna benzemiyor, lütfen doğru bir tuş giriniz.")

    if hitMakrosu != "":
        hitTus = hitMakrosu
        hitMakrosu = 1
    else:
        hitMakrosu = 0
        hitTus = "-"
        hitMakrosuDelay = "-"
    while hitMakrosu == 1:
        hitMakrosuDelay = input(Fore.BLUE + "          Hit makrosu delayini giriniz, bilmiyorsanız boş bırakınız: ")
        if hitMakrosuDelay == "":
            hitMakrosuDelay = .06
            break
        try: 
            hitMakrosuDelay = int(hitMakrosuDelay)
        except:
            print(Fore.RED + "          Makronuzun delayine Sayi yazmaniz gerekmektedir! lütfen tekrar deneyin\n")
        else:
            hitMakrosuDelay = int(hitMakrosuDelay)
            hitMakrosuDelay = hitMakrosuDelay/1000
            break
        

    # // Blok makro seçimleri

    while True:
        blokMakrosu = input(Fore.GREEN + "\n          Blok makrosunu atamak istediğiniz tuşu giriniz, eğer blok makrosu istemiyorsanız boş bırakınız: ")
        if blokMakrosu in KEYS:
            break
        else:
            print(Fore.RED + "          Atadığınız tuş, bir klavye tuşuna benzemiyor, lütfen doğru bir tuş giriniz.")
    if blokMakrosu != "":
        blokTus = blokMakrosu
        blokMakrosu = 1
    else:
        blokMakrosu = 0
    if blokMakrosu != "":
        while blokMakrosu == 1:
            blokSlot = input("          Blok slotunuzu giriniz: ")
            try: 
                blokSlot = int(blokSlot)
            except:
                print(Fore.RED + "          Blok slotunuzun bir sayi olması gerekmektedir! lütfen 1 - 10 arasında bir sayı giriniz! \n")
            else:
                if 0 < blokSlot < 10:
                    break
                else:
                    print(Fore.RED + "          Blok slotunuzun bir sayi olması gerekmektedir! lütfen 1 - 10 arasında bir sayı giriniz! \n")

            blokTus = blokMakrosu
            blokMakrosu = 1
            blokSlot = str(blokSlot)
    if blokMakrosu == 0:
        blokSlot = "-"
        blokTus = "-"
        blokMakrosuDelay = "-"
    while blokMakrosu == 1:
        blokMakrosuDelay = input(Fore.BLUE + "          Blok makronuzun delayini giriniz, bilmiyorsanız boş bırakınız: ")
        if blokMakrosuDelay == "":
            blokMakrosuDelay = .06
            break
        try:
            blokMakrosuDelay = int(blokMakrosuDelay)
        except:
            print(Fore.RED + "          Makronuzun delayine Sayi yazmaniz gerekmektedir! lütfen tekrar deneyin\n")
        else:
            blokMakrosuDelay = int(blokMakrosuDelay)
            blokMakrosuDelay = blokMakrosuDelay / 1000
            break


    # // Olta Makro seçimleri

    while True:
        oltaMakrosu = input(Fore.GREEN + "\n          Olta Makrosunu atamak istediğiniz tuşu giriniz, eğer olta makrosu istemiyorsanız boş bırakınız: ")
        if oltaMakrosu in KEYS:
            break
        else:
            print(Fore.RED + "          Atadığınız tuş, bir klavye tuşuna benzemiyor, lütfen doğru bir tuş giriniz.")
    if oltaMakrosu != "":
        while True:
            oltaSlot = input(Fore.BLUE + "          Oltanızın slotunu giriniz: ")
            try: 
                oltaSlot = int(oltaSlot)
            except:
                print(Fore.RED + "          Olta slotunuzun bir sayi olması gerekmektedir! lütfen 1 - 10 arasında bir sayı giriniz! \n")
            else:
                if 0 < oltaSlot < 10:
                    break
                else:
                    print(Fore.RED + "          Olta slotunuzun bir sayi olması gerekmektedir! lütfen 1 - 10 arasında bir sayı giriniz! \n")
        oltaTus = oltaMakrosu
        oltaMakrosu = 1
        oltaSlot = str(oltaSlot)
    else:
        oltaMakrosu = 0
        oltaSlot = "-"
        oltaTus = "-"
        oltaMakrosuDelay = "-"
    while oltaMakrosu == 1:
        oltaMakrosuDelay = input(Fore.GREEN + "          Olta makronuzun delayini giriniz, bilmiyorsanız boş bırakınız: ")
        if oltaMakrosuDelay == "":
            oltaMakrosuDelay = 0.240
            break
        try:
            oltaMakrosuDelay = int(oltaMakrosuDelay)
        except:
            print(Fore.RED + "\n          Olta Makronuzun delayinin bir sayi olması gerekmektedir!")
        else:
            oltaMakrosuDelay = int(oltaMakrosuDelay)
            oltaMakrosuDelay = oltaMakrosuDelay / 1000
            break
            
    print(Fore.LIGHTBLACK_EX + "\n\n######################################--Made by ne1ry#1881, from ttClient, txtTool --##############\n\n\n")

    print(Fore.YELLOW + "                   Kılıç slotunuz: " + Fore.RED +"[" + Fore.MAGENTA + str(kilicSlot) + Fore.RED +"]" + Fore.YELLOW +" Blok Slotunuz: " +Fore.RED +"[" + Fore.MAGENTA + str(blokSlot) + Fore.RED +"]" + Fore.YELLOW +" Olta Slotunuz: " + Fore.RED +"[" + Fore.MAGENTA + str(oltaSlot) + Fore.RED +"]\n\n")
    

    print(Fore.BLUE + "                       HIT MAKRO TUŞU: " + Fore.RED +"[" + Fore.MAGENTA + str(hitTus).upper() + Fore.RED +"] " + Fore.BLUE + "HIT DELAY: " + Fore.RED +"["+ Fore.MAGENTA +  str(hitMakrosuDelay) + Fore.RED +"]"  )


    print(Fore.BLUE + "\n\n                       BLOK MAKRO TUŞU: " + Fore.RED +"[" + Fore.MAGENTA + str(blokTus).upper() + Fore.RED +"] " + Fore.BLUE + "BLOCK DELAY: " + Fore.RED +"["+ Fore.MAGENTA +  str(blokMakrosuDelay) + Fore.RED +"]")


    print(Fore.BLUE + "\n\n                       OLTA MAKRO TUŞU: " + Fore.RED +"[" + Fore.MAGENTA + str(oltaTus).upper() + Fore.RED +"] " + Fore.BLUE + "OLTA DELAY: " + Fore.RED +"["+ Fore.MAGENTA +  str(oltaMakrosuDelay) + Fore.RED +"]\n")


    print(Fore.GREEN + "    ---------------    MAKROYU DURDURMAK İÇİN " + Fore.RED +"[" + Fore.MAGENTA + str(durdurma).upper() + Fore.RED +"] "+ Fore.GREEN + "TUŞUNA BASINIZ      ---------------")

    print(Fore.LIGHTBLACK_EX +"\n\n########################################--Made by ne1ry#1881, from ttClient, txtTool --##############")
               
    # //Buralar makroların çalışma kısmı.

    blokSlot = blokSlot + 1
    while True:
        if hitMakrosu == 1:
            if keyboard.is_pressed(hitTus):
                mouse.press(Button.left)
                time.sleep(hitMakrosuDelay / 2.1)
                mouse.release(Button.left)
                time.sleep(hitMakrosuDelay / 2.2)
        if blokMakrosu == 1:
            if keyboard.is_pressed(blokTus):
                keyboard.press(blokSlot)
                keyboard.release(blokSlot)
                mouse.press(Button.right)
                time.sleep(blokMakrosuDelay / 2.1)
                mouse.release(Button.right)
                time.sleep(blokMakrosuDelay / 2.2 )
                keyboard.press(kilicSlot)
                keyboard.release(kilicSlot)
        if oltaMakrosu == 1:
            if keyboard.is_pressed(oltaTus):
                keyboard.press(oltaSlot)
                mouse.press(Button.right)
                mouse.release(Button.right)
                keyboard.release(oltaSlot)
                time.sleep(oltaMakrosuDelay)
                keyboard.press(kilicSlot)
                keyboard.release(kilicSlot)




        if keyboard.is_pressed(durdurma):
            print("\n\n" + Fore.RED + "         --------->>> PROGRAM DURDURULDU, TUŞ ATAMALARINI DÜZENLEMEK İÇİN ENTER'A BASINIZ.\n")
            xaca = input("...    ")
            os.system('cls')
            break
            
    




            

            
            








