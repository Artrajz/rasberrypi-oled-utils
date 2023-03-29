import adafruit_ssd1306
import board
import busio
import digitalio
import time
import os
import pickle
import sys

from PIL import Image, ImageDraw, ImageFont


#oled屏幕参数
WIDTH = 128
HEIGHT = 64
BORDER = 5

abs_path = os.path.dirname(os.path.realpath(sys.argv[0]))


def init_oled():
    # SPI初始化
    # pin脚信息在board库里，是BCM模式
    spi = busio.SPI(board.SCK, MOSI=board.MOSI)
    reset_pin = digitalio.DigitalInOut(board.D17)
    dc_pin = digitalio.DigitalInOut(board.D22)
    cs_pin = digitalio.DigitalInOut(board.CE0)
    oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, dc_pin, reset_pin, cs_pin)
    # 初始化 清除屏幕信息
    oled.fill(0)
    oled.show()
    return oled


def dsp_gif():
    print("loading bad apple...")
    flag = False
    img_list = []
    try:
        with open(abs_path+'/bad_apple.pkl','rb') as f:
            img_list = pickle.load(f)
            flag = True
    except:
        flag = False
    if not flag:
        path = abs_path+'/pic/bad_apple_gif2gray_jpg/'
        files = os.listdir(path)  # 不是按顺序读取的
        files.sort(key=lambda x: int(x.split('.')[0]))  # 使用sort进行按顺序读取
        
        for file in files:
            f_path = path + str(file)
    #        print(f_path)
    
            img_list.append(Image.open(f_path).resize((128, 64)).convert('1'))
        
        with open(abs_path+'/bad_apple.pkl','wb') as f:
            pickle.dump(img_list,f,0)
    
    print("start playing bad apple...")
    
    try:
        while True:
            time1 = time.time()
            for img in img_list:
                oled.image(img)
                oled.show()
                time.sleep(0.058)
            #print(time.time() - time1,len(files) / (time.time() - time1),1 / (len(files) / (time.time() - time1)))

    except KeyboardInterrupt:
        oled.fill(0)
        oled.show()
    

if __name__ == "__main__":
    oled = init_oled()
    dsp_gif()


