import pymysql
from flask import Flask, render_template, request
import re

app = Flask(__name__)




@app.route('/')
def main_index():
    data = sql_exe('select score, count(*) as people_count from douban_data group by score;')
    score_list = []
    count_list = []
    k_v_data = dict(data)
    for item in data:
        tmp = item[0] + '分'
        score_list.append(tmp)
        count_list.append(item[1])
    data = sql_exe('select people_count from douban_data;')
    people_count = []
    for item in data:
        people_count.append(item[0])
    for i in range(len(people_count)):
        people_count[i] = int(int(people_count[i]) / 10000)

    data = sql_exe("select id,name,mingyan,score,people_count from douban_data")
    info_list = []
    text = ''
    for i in data:
        text += list(i)[2]
        info_list.append(list(i))
    print(info_list)
    # nake_word_cloud(text)

    return render_template('index.html', score_list=score_list, count_list=count_list, people_count=people_count,
                           k_v_data=k_v_data, info_list=info_list)


def sql_exe(sql):
    try:
        db = pymysql.connect("localhost", "root", "", "douban_db",
                             charset='utf8mb4')
        cursor = db.cursor()
        print("当前sql语句为：", sql)
        row = cursor.execute(sql)
        print("当期sql操作影响行数：", row)
        db.commit()
        date = cursor.fetchall()
        print("命令行输出数据为：", date)
        if date:
            return date
        else:
            return row
    except:
        db.rollback()  # 撤回一个DDL ，也就是操作数据库的语句，增删改之类的
    finally:
        db.close()


def nake_word_cloud(text):
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
        font_path='simsun.ttc'  # windows字体所在路径，C:\Windows\Fonts
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
    plt.savefig(r'./static/images/apple.jpg', dpi=800)  # 默认分辨率是400


if __name__ == '__main__':
    app.run(debug=True)
