# raspberry-pi-oled

- 这是一个在树莓派上使用SSD1306 oled的脚本，测试在SPI协议、128x64分辨率下可以正常使用，理论上支持其他分辨率的屏幕和I2C协议。
- 可以显示文本、图片、GIF动图、树莓派ip（更换网络也可以轻松找到ip了）
- 附带播放bad apple实例。

# 使用方法

## 安装依赖

```
pip install -r requirements.txt
```

## 使用脚本

### 显示文本

```
python showText.py -t text
```

- text是要显示的文本。

### 显示图片

```
python showImg.py -i img_path
```

- img_path是要显示的图片路径。

### 显示GIF动图

```
python showGIF.py
```

- 目前显示gif需要先将GIF拆分成图片，可以使用[gif-split](https://github.com/Artrajz/gif-split)，也可以自行拆分。
- 拆分后在脚本里修改所拆分图片的路径。
- 支持将转换好的图片对象序列化保存：同一个gif第一次运行会比较慢，第二次以后直接读取序列化文件播放。
- 序列化之后不用原图片只需要**.pkl**文件就可以播放，如果要重新生成则需删除.pkl文件或者重命名为其他名字。


### 显示树莓派ip

```
python showIP.py
```

- 树莓派连上wifi后，运行脚本可以在oled上显示树莓派的内网ip。
- 为了防止烧屏，延长oled使用寿命，脚本做了滚动处理，ip会在屏幕中上下滚动，可以修改脚本中的sleep()函数调节滚动速度。
- 如有需要，可以使用**systemd**等方法设置开机自启，连接到不同WiFi后可以获取到内网ip，以便于ssh和vnc的连接。

## 使用实例

### 播放bad apple

我准备了bad apple的序列化文件，文件名是**bad_apple.pkl**，安装好依赖直接运行showGIF.py就可以播放bad apple了。
<img src="https://github.com/Artrajz/picgo-img/blob/main/img/bad_apple.gif?raw=true" />