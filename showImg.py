import adafruit_ssd1306
import board
import busio
import digitalio
import time
import os
import argparse

from PIL import Image, ImageDraw, ImageFont


parser.add_argument('-i', '--img', type=str,help='img path (图片路径)')


WIDTH = 128
HEIGHT = 64
BORDER = 5


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

        
def showImg(img_path):
    try:
        im = Image.open(img_path)
        
        #width = im.size[0]   # 获取宽度
        #height = im.size[1]   # 获取高度
        #scale = height / 64
        #im = im.resize((int(width / scale), int(height / scale)))
        
        im = im.resize((128, 64))
        im = im.convert('1')
        oled.image(im)
        oled.show()
    except BaseException as be:
        print(be)
    

if __name__ == "__main__":
    oled = init_oled()

    try:
        jpg(args.img)

    except KeyboardInterrupt:
        oled.fill(0)
        oled.show()


