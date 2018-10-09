# TFColorTool
Color tool for The Fucking Design.

一个自娱自乐的工具，一个强迫症产品。

「Nlvi」配色思路、心血来潮产物。

![](/screenshots/1.gif)

## 功能

- HEXcolor to RGBcolor
- RGBcolor to HEXcolor
- 展示颜色
- 从输入色到白色色阶，数量自定
- 从输入色到黑色色阶，数量自定

## 未来

- 根据输入色计算彩虹糖果色

## 使用
```python
color = TFColorTool('39C5BB') #初音绿
color.colorGen(8) #从初音绿到白色(默认) 8种颜色色阶图
color.colorGen(8, 'black') #从初音绿到黑色 8种颜色色阶图
```
