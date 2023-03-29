import adafruit_ssd1306
import board
import busio
import digitalio
import time
import os
import argparse

from PIL import Image, ImageDraw, ImageFont

parser.add_argument('-t', '--text', type=str,help='text (显示文本)')


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

def img_text(text):
    # 创建一个空白的图像
    # 确保用“1”表示 1bit 的颜色
    image = Image.new("1", (oled.width, oled.height))
    # 获取绘制对象来绘制图像
    draw = ImageDraw.Draw(image)
    # 绘制一个白色的背景
    draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)
    # 绘制一个小的内边框
    draw.rectangle((BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1), fill=0, outline=0)
    # 加载默认样式
    font = ImageFont.load_default()
    # 绘制一些文字
    text = text
    (font_width, font_height) = font.getsize(text)
    draw.text(
        (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
        text,
        font=font,
        fill=255,
    )


def showText(text,height):
    try:
        text_obj = create_text(text,int(height))
        oled.image(text_obj)
        oled.show()
    except BaseException as be:
        print(be)
    

if __name__ == "__main__":
    oled = init_oled()

    try:
        showText(args.text,args.height)

    except KeyboardInterrupt:
        oled.fill(0)
        oled.show()


