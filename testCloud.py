# 分词
import jieba
# 画图，数据可视化
from matplotlib import pyplot as plt
from wordcloud import WordCloud
# 图形处理
from PIL import Image
# 矩阵运算
import numpy as np
import pymysql

# 准备词云所需的文字，可以从数据库中获取，数据库可以从网上获取
text = '''
君不见 黄河之水天上来，奔流到海 不复回。
君不见 高堂明镜悲白发，朝如青丝 暮成雪。
人生得意 须尽欢，莫使金樽 空对月。
天生我材 必有用，千金散尽 还复来。
烹羊宰牛 且为乐，会须一饮 三百杯。
岑夫子，丹丘生，将进酒，杯莫停。
与君歌一曲，请君为我倾耳听。(倾耳听 一作：侧耳听)
钟鼓馔玉不足贵，但愿长醉不愿醒。(不足贵 一作：何足贵；不愿醒 一作：不复醒)
古来圣贤皆寂寞，惟有饮者留其名。(古来 一作：自古；惟 通：唯)
陈王昔时宴平乐，斗酒十千恣欢谑。
主人何为言少钱，径须沽取对君酌。
五花马、千金裘，呼儿将出换美酒，与尔同销万古愁。
'''

# 分词、
cut = jieba.cut(text)
s = ' '.join(cut)
print(s)


img = Image.open(r'apple.jpg')
# 把一个图片变成数组，三维的
img_array = np.array(img)
# print(img_array, img_array.shape)
# (500, 500, 3)

wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='simsun.ttc'   # windows字体所在路径，C:\Windows\Fonts
)
# 获得已经分好的字词
wc.generate_from_text(s)

# 绘制图片
# 窗口title设置
fig = plt.figure('图片')
# 按照已经建好的wc规则显示图片
plt.imshow(wc)
plt.axis('off')  # 不显示坐标轴
# plt.show()
plt.savefig(r'./static/images/apple.jpg', dpi=500)  # 默认分辨率是400























