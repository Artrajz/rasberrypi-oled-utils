# raspberry-pi-oled

这是一个在树莓派上使用SSD1306 oled的脚本，测试在128x64可以正常使用，理论上支持其他分辨率的屏幕。可以显示文本、图片、GIF动图、树莓派ip（更换网络也可以轻松找到ip了）

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

目前显示gif需要先将GIF拆分成图片，可以使用

在脚本里修改路径

支持将转换好的图片对象序列化保存，同一个第一次显示会比较慢，第二次以后直接读取缓存文件。

### 显示树莓派ip

```
python showIP.py
```

树莓派连上wifi后，运行脚本可以在oled上显示树莓派的内网ip。如有需要，建议使用systemd等方法设置开机自启，连接到不同WiFi后可以获取到内网ip，以便用于ssh和vnc的连接