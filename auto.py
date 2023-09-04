import pyautogui
from PIL import Image
import time
import random
import keyboard
region = (560,30,1280,720) #vung kiem tra phim
listOfPlayer = ['d', 'f', 'g', 'h', 'j', 'k', 'l']

def timtran():
    while True:
        home_image = Image.open('home.png')
        location_timtran = pyautogui.locateOnScreen(home_image, region=region, confidence=0.8)
        if location_timtran is not None:
            print("home_image found at:", location_timtran)
            pyautogui.press('1')
            time.sleep(0.5)
            pyautogui.press('2')
            time.sleep(0.5)
            pyautogui.press('3')
            time.sleep(0.5)
            break  
        else:
            print("home_image not found on the screen.")
        time.sleep(1)
      
def checklistuser():        
    while True:
        danhsach_image = Image.open('danhsach.png')
        location_danhsach = pyautogui.locateOnScreen(danhsach_image, region=region, confidence=0.8) 
        if location_danhsach is not None:
            print("danhsach_image found at:", location_danhsach)
            break  
        else:
            print("danhsach_image not found on the screen.")
        time.sleep(1)
    

def selectuser():
    while True:
        tancong_image = Image.open('tancong.png')
        danhsach_image = Image.open('danhsach.png')
        location_danhsach = pyautogui.locateOnScreen(danhsach_image, region=region, confidence=0.8) 
        location_tancong = pyautogui.locateOnScreen(tancong_image, region=region, confidence=0.8) 

        if location_danhsach is not None:
            random_index = random.randint(0, len(listOfPlayer) - 1)
            random_key = listOfPlayer[random_index]
            pyautogui.press(random_key)
            time.sleep(0.1) 
            print("khong tim thay danh sach player")         
        if location_tancong is not None:
            print("player selected")
            print("tancong_image found at", location_danhsach)
            break  
        print("chua select player")       
        
def PlayerOnline():
    pyautogui.press('m')
    time.sleep(0.5)
    pyautogui.press('n')
    selectuser()

def VaoTran():
    trongtran_image = Image.open('trongtran.png')
    boqua_image = Image.open('boqua.png')
    victory_image = Image.open('victory.png')
    
    while True:
        location_trongtran = pyautogui.locateOnScreen(trongtran_image, region=region, confidence=0.8)
        location_boqua = pyautogui.locateOnScreen(boqua_image, region=region, confidence=0.8)
       
        if location_trongtran is not None:
            print("dang trong tran", location_trongtran)
            pyautogui.press('b')
            time.sleep(1)  
            continue
        if location_boqua is not None:
            print("da tim thay nut bo qua", location_boqua)
            pyautogui.click(location_boqua)
            print("da cham vao tiep tuc")           
            time.sleep(0.5)
            location_victory = pyautogui.locateOnScreen(victory_image, region=region, confidence=0.8)
            if location_victory is not None:
                print("da tim thay nut tiep tuc", location_boqua)
                time.sleep(1)
                pyautogui.click(location_victory)
                print("da cham vao tiep tuc")           
                break  
        print("dang doi de vao tran")           
    
def MoRuong():
    home_image = Image.open('home.png')
    image_files = [ 'khobau.png','bocuoc.png','nung.png', 'chamdetieptuc.png','ban.png']
    while True:
        for image_file in image_files:
            location = pyautogui.locateOnScreen(image_file, region=region, confidence=0.8)
            if location is not None:
                print(f"{image_file} found at:", location)
                pyautogui.click(location)
                time.sleep(1)
        location_home = pyautogui.locateOnScreen(home_image, region=region, confidence=0.8)
        if location_home is not None:
            print("home_image found at:", location_home)
            break    

def tancong():
    chonguoichoi_image = Image.open('chonguoichoi.png')
    return_image = Image.open('hayduatoitrolai.png')
    enterbattle_image = Image.open('vaotran.png')
    moc = True
    while moc:
        location_chodoi = pyautogui.locateOnScreen(chonguoichoi_image, region=region, confidence=0.8)
        time.sleep(1)
        pyautogui.press('t')
        while True:
            location_vaotran = pyautogui.locateOnScreen(enterbattle_image, region=region, confidence=0.8) 
            if location_vaotran is not None:
                print("bat dau vao tran", location_vaotran)
                moc = False
                break
            location_return = pyautogui.locateOnScreen(return_image, region=region, confidence=0.8)
            if location_return is not None:
                print("tim thay : hay dua toi tro lai", location_return)
                PlayerOnline()
            location_chodoi = pyautogui.locateOnScreen(chonguoichoi_image, region=region, confidence=0.8)
            if location_chodoi is None:
                time.sleep(1)
                pyautogui.press('t')
            print("dang cho doi nut tan cong")
        
    while True:
        location_enterbattle = pyautogui.locateOnScreen(enterbattle_image, region=region, confidence=0.8)
        
        if location_enterbattle is not None:
            print("bat dau vao tran", location_enterbattle)
            VaoTran()
            MoRuong()
            break  
        else:
            time.sleep(2)
            
while True:
    tainguyen_image = Image.open('tainguyen.png')
    while True:
        location_tainguyen = pyautogui.locateOnScreen(tainguyen_image, region=region, confidence=0.8)
        if location_tainguyen is not None:
            pyautogui.click(location_tainguyen)
            print("da tim thay nut tai nguyen")
            break
        time.sleep(1)
    timtran()
    checklistuser()
    selectuser()
    tancong()

    
    
