import re
from sty import bg

from util import verify, listDec


class TFColorTool:
    def __init__(self, color):
        verify(color)
        self.colorStr = color

    def colorGen(self, number, to='white'):
        colors = []
        r_list = number
        sgl = 1

        if (type(number) != list):
            r_list = range(number + 1)
            sgl = 1 / number

        r_color = [c if to == 'black' else 255 - c for c in self.hex2rgb()]
        for i in r_list:
            prop = i if type(number) == list else (1 - i * sgl)
            color = [
                round(c * prop) if to == 'black' else 255 - round(c * prop)
                for c in r_color
            ]
            colors.append(color)
        self.printColors(colors)

    def colorGradual(self, to, number):
        verify(to)
        colors = []
        sgl = 1 / number

        from_color = self.hex2rgb()
        to_color = self.hex2rgb(to)
        diffs = [x > 0 for x in listDec(from_color, to_color)]
        diffc = [abs(x) for x in listDec(from_color, to_color)]
        props = [round(sgl * x) for x in diffc]

        for i in range(number):
            cs = []
            for cp in range(len(diffs)):
                c = from_color[cp] + props[cp] * i if diffs[
                    cp] else from_color[cp] - props[cp] * i
                cs.append(c)
            colors.append(cs)
            cs = []

        colors.append(to_color)
        self.printColors(colors)

    def hex2rgb(self, color=None):
        rgb_list = re.findall(r'\w{2}', color or self.colorStr)
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
