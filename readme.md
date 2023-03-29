[TOC]

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

### 显示图片

```
python showImg.py -i img_path
```

### 显示GIF动图

```
python showGIF.py
```

- 目前显示gif需要先将GIF拆分成图片，可以使用[gif-split](https://github.com/Artrajz/gif-split)，也可以自行拆分。

- 拆分后在脚本里修改路径

- 支持将转换好的图片对象序列化保存，同一个第一次显示会比较慢，第二次以后直接读取缓存文件。


### 显示树莓派ip

```
python showIP.py
```

树莓派连上wifi后，运行脚本可以在oled上显示树莓派的内网ip。如有需要，建议使用**systemd**等方法设置开机自启，连接到不同WiFi后可以获取到内网ip，以便用于ssh和vnc的连接

## 使用实例

### 播放bad apple

我准备了bad apple的序列化文件，文件名是**bad_apple.pkl**,安装好依赖直接运行showGIF.py就可以播放bad apple了。

<img src="https://github.com/Artrajz/picgo-img/blob/main/img/bad_apple.gif?raw=true" />