import pandas as pd
import matplotlib.pyplot as plt
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker


def my_line_chart(f, i):
    x = df.loc[df['label'] == i]

    dp = x.groupby('date')['title'].count()
    # print(dp)
    # print(dp.idxmax())
    peak = x[x['date'] == dp.idxmax()]
    # print(peak['date'])
    peak.to_csv(f, header=None)

    num = int((dp.max() // 5 + 1) * 5)
    # print(dp.describe)
    # dp.plot()
    # plt.title("第 " + str(i) + "类新闻热度趋势图")
    # plt.xlabel("时间")
    # plt.ylabel("第 " + str(i) + "类新闻条数")
    # plt.xticks(rotation=45)
    # plt.show()
    (
        Line(init_opts=opts.InitOpts(width="1680px", height="800px"))
            .add_xaxis(xaxis_data=[item for item in x['date'].unique()])
            .add_yaxis(
            series_name="",
            y_axis=[item for item in dp],
            yaxis_index=0,
            is_symbol_show=False,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title=("第" + str(i+1) + "类新闻热点趋势"), pos_left="center", title_textstyle_opts=opts.TextStyleOpts(font_weight="bolder", font_size=40)),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(
                save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                    background_color="#fff"))),
            # datazoom_opts=[
            #     opts.DataZoomOpts(yaxis_index=0),
            #     opts.DataZoomOpts(type_="inside", yaxis_index=0),
            # ],
            visualmap_opts=opts.VisualMapOpts(
                pos_top="10",
                pos_right="10",
                is_piecewise=True,
                pieces=[
                    {"gt": 0, "lte": 5, "color": "#096"},
                    {"gt": 5, "lte": 10, "color": "#ffde33"},
                    {"gt": 10, "lte": 15, "color": "#ff9933"},
                    {"gt": 15, "lte": 20, "color": "#cc0033"},
                    {"gt": 20, "lte": 30, "color": "#660099"},
                    {"gt": 30, "color": "#7e0023"},
                ],
                out_of_range={"color": "#999"},
            ),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45, font_weight="bold")),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name=("第" + str(i+1) + "类新闻条数"),
                name_textstyle_opts=opts.TextStyleOpts(
                    font_size=20,
                    font_weight="bold"
                ),
                min_=0,
                max_=num,
                is_scale=True,
                axistick_opts=opts.AxisTickOpts(is_inside=False),
                axislabel_opts=opts.LabelOpts(font_size=20)
            ),
        )
            .set_series_opts(
            markline_opts=opts.MarkLineOpts(
                data=[
                    {"yAxis": 5},
                    {"yAxis": 10},
                    {"yAxis": 15},
                    {"yAxis": 20},
                    {"yAxis": 30},
                ],
                label_opts=opts.LabelOpts(position="end", font_size=20),
            )
        )
            .render("line_" + str(i) + ".html")
    )


def my_line_chart_all(f):
    x = df

    dp = x.groupby('date')['title'].count()
    # print(dp)
    # print(dp.idxmax())
    peak = x[x['date'] == dp.idxmax()]
    # print(peak['date'])
    peak.to_csv(f, header=None)

    num = int((dp.max() // 5 + 1) * 5)
    # print(dp.describe)
    # dp.plot()
    # plt.title("第 " + str(i) + "类新闻热度趋势图")
    # plt.xlabel("时间")
    # plt.ylabel("第 " + str(i) + "类新闻条数")
    # plt.xticks(rotation=45)
    # plt.show()
    (
        Line(init_opts=opts.InitOpts(width="1680px", height="800px"))
            .add_xaxis(xaxis_data=[item for item in x['date'].unique()])
            .add_yaxis(
            series_name="",
            y_axis=[item for item in dp],
            yaxis_index=0,
            is_symbol_show=False,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="新闻热点趋势", pos_left="center", title_textstyle_opts=opts.TextStyleOpts(font_weight="bolder", font_size=40)),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(
                save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                    background_color="#fff"))),
            # datazoom_opts=[
            #     opts.DataZoomOpts(yaxis_index=0),
            #     opts.DataZoomOpts(type_="inside", yaxis_index=0),
            # ],
            visualmap_opts=opts.VisualMapOpts(
                pos_top="10",
                pos_right="10",
                is_piecewise=True,
                pieces=[
                    {"gt": 0, "lte": 50, "color": "#096"},
                    {"gt": 50, "lte": 100, "color": "#ffde33"},
                    {"gt": 100, "lte": 150, "color": "#ff9933"},
                    {"gt": 150, "lte": 200, "color": "#cc0033"},
                    {"gt": 200, "lte": 300, "color": "#660099"},
                    {"gt": 300, "color": "#7e0023"},
                ],
                out_of_range={"color": "#999"},
            ),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45, font_weight="bold")),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name="新闻条数",
                name_textstyle_opts=opts.TextStyleOpts(
                    font_size=20,
                    font_weight="bold"
                ),
                min_=0,
                max_=num,
                is_scale=True,
                axistick_opts=opts.AxisTickOpts(is_inside=False),
                axislabel_opts=opts.LabelOpts(font_size=20)
            ),
        )
            .set_series_opts(
            markline_opts=opts.MarkLineOpts(
                data=[
                    {"yAxis": 50},
                    {"yAxis": 100},
                    {"yAxis": 150},
                    {"yAxis": 200},
                    {"yAxis": 300},
                ],
                label_opts=opts.LabelOpts(position="end", font_size=20),
            )
        )
            .render("all.html")
    )
# plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
# plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
fileNameStr = 'C:/Users/song/github/2022_fengru_cup_nlp/input/kmeans_news_0126.csv'  # 读取Ecxcel数据
df = pd.read_csv(fileNameStr, encoding='utf-8')
df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d').dt.strftime('%Y/%m')
# df['label'] = pd.to_numeric(df['label'])
df = df.sort_values(by='date')
# print(df.groupby(['label', 'date'])['title'].count().describe)
with open('C:/Users/song/All about learning/冯如/output.csv', 'a', encoding="utf-8") as f:
    print(f)
    for i in range(0, 30):
        my_line_chart(f, i)
    # my_line_chart_all(f)
# df=df.set_index(df['date'])
# print(df.describe)
# ts = pd.Series(df['label'], index=df.index)
# print(ts.describe)
# ts.plot()
# print(df.describe)
# dp = df.groupby('label')['date'].count()
# print(dp.describe)

# y = Faker.values()
# y[3], y[5] = None, None
# c = (
#     Line()
#     .add_xaxis(Faker.choose())
#     .add_yaxis("商家A", y, is_connect_nones=True)
#     .set_global_opts(title_opts=opts.TitleOpts(title="Line-连接空数据"))
#     .render("line_connect_null.html")
# )
