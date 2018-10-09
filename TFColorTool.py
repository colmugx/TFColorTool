import re
from sty import bg


class TFColorTool:
    def __init__(self, color):
        if (len(color) != 6 or not re.match(r'[a-zA-Z0-9]', color)):
            raise Exception("不合法RGB色值")
        self.colorStr = color

    def colorGen(self, number):
        colors = []
        sgl = 1 / number
        r_color = [255 - c for c in self.hex2rgb()]
        for i in range(number + 1):
            color = [255 - round(c * (1 - i * sgl)) for c in r_color]
            colors.append(color)
        self.printColors(colors)

    def hex2rgb(self):
        rgb_list = re.findall(r'\w{2}', self.colorStr)
        red = int(rgb_list[0], 16)
        green = int(rgb_list[1], 16)
        blue = int(rgb_list[2], 16)
        return [red, green, blue]

    def rgb2hex(self, color):
        hex_color = ''
        for c in color:
            s = hex(c).strip('0x')
            s = s.zfill(2)
            hex_color += s
        return hex_color

    def printColor(self, color):
        block = ' ' + '　' * 4
        out_color = bg(color[0], color[1], color[2]) + block + bg.rs
        for i in range(2):
            print(out_color)
        print(' #%s ' % self.rgb2hex(color))

    def printColors(self, colors):
        block = ' ' + '　' * 4
        out_color = ''
        label = ''

        for color in colors:
            single_c = bg(color[0], color[1], color[2]) + block + bg.rs
            out_color += single_c
            label += ' #%s ' % self.rgb2hex(color)

        for i in range(2):
            print(out_color)
        print(label)
