# PIL
# pip install pillow

from PIL import Image, ImageDraw, ImageFont
import string
import random
from io import BytesIO


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


str_all = string.digits + string.ascii_letters


def random_code(size=(100, 42), length=4, point_num=80, line_num=5):
    width, height = size
    # 生成一个100*42的白色背景图片
    img = Image.new('RGB', (width, height), color=(255, 255, 255))

    # 新建一个图片同大小的画布
    draw = ImageDraw.Draw(img)

    # 生成字体对象
    font = ImageFont.truetype(font=r'static/my/font/HuaGuangGangTieZhi.ttf', size=20)

    # 书写文字
    valid_code = ''

    for i in range(length):
        random_chart = random.choice(str_all)
        draw.text((20 * i + 20, 10), random_chart, (0, 0, 0), font=font)
        valid_code += random_chart
    print(valid_code)

    # 随机生成点
    for i in range(point_num):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), random_color())
    # 随机画线条
    for i in range(line_num):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=random_color())

    # 创建一个内存句柄
    f = BytesIO()
    # 将图片保存到内存句柄中
    img.save(f, 'PNG')
    # 读取内存句柄 字节码
    data = f.getvalue()
    # print(data)
    return (data, valid_code)


if __name__ == '__main__':
    random_code()
