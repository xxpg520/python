"""
演示基础柱状图的开发
"""
from pyecharts.charts import Bar        # 导入Bar 柱状图包
from pyecharts.options import LabelOpts # 导入LabelOpts 标签包
# 使用Bar构建基础柱状图
bar = Bar()
# 添加x轴的数据
bar.add_xaxis(["中国", "美国", "英国"])
# 添加y轴的数据
bar.add_yaxis("GDP", [30, 20 ,10],label_opts=LabelOpts(position="right"))
# 反转xy轴
bar.reversal_axis()
# 设置全局变量


# 绘制折线图
bar.render("基础柱状图.html")