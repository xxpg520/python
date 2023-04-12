"""
演示河南省疫情地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取文件
f = open("d:/疫情.txt", "r",encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()
# 将json转换成python字典
data_dict = json.loads(data)
# 获取河南省数据
cities_data = data_dict["areaTree"][0]["children"][6]["children"]
# 准备数据为元组并放入list
data_list = []
for city_data in cities_data:
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

# 手动添加恩施，神农架数据
data_list.append(("恩施土家族苗族自治州", 252))
data_list.append(("神农架林区", 11))

# 构建地图
map = Map()
map.add("湖北省疫情分布", data_list, "湖北")
# 设置全局配置，制定分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="湖北省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,       # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99人","color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~999人","color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999人","color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000~9999人","color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000~99999人","color": "#CC3333"},
            {"min": 100000, "lable": "1~99人","color": "#990033"}
        ]
    )
)
# 绘制图形
map.render("湖北省疫情地图.html")
