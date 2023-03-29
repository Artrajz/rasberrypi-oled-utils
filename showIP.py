import adafruit_ssd1306
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import time
import socket

# oled屏幕参数
WIDTH = 128
HEIGHT = 64
BORDER = 5


# 初始化oled
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


# 创建一个滚动文字的图像
def create_text(text,text_height):
    # 创建一个空白的图像
    # 确保用“1”表示 1bit 的颜色
    image = Image.new("1", (oled.width, oled.height))
    # 获取绘制对象来绘制图像
    draw = ImageDraw.Draw(image)
    # 加载默认样式
    font = ImageFont.load_default()
    # 绘制一些文字
    text = text
    (font_width, font_height) = font.getsize(text)
    draw.text(
        (oled.width // 2 - font_width // 2, text_height),
        text,
        font=font,
        fill=255,
    )
    return image


def get_host_ip():
    # 查询本机ip地址
    ip = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
        

def showIP():
    text_height = 0
    roll = 1
    try:
        while True:
            if text_height > 52 or text_height < 0:
                roll = -roll
            text_height = text_height + roll
                
            # 获取树莓派的内网ip
            ip = get_host_ip()
            if ip != None:
                ip_text = create_text('ip:' + ip,text_height)
                # 加载树莓派ip图像
                oled.image(ip_text)
                oled.show()
                
            else:
                error_text = create_text('no net QAQ',text_height)
                oled.image(error_text)
                oled.show()
            time.sleep(1)

    except KeyboardInterrupt:
        oled.fill(0)
        oled.show()
    


if __name__ == "__main__":
    oled = init_oled()
    showIP()
    
