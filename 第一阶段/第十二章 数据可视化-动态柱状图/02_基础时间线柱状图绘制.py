"""
演示带有时间线的柱状图开发
"""
from pyecharts.charts import Bar, Timeline          # 调用柱状图包、时间轴包
from pyecharts.options import LabelOpts             # 调用标签选项包
from pyecharts.globals import ThemeType             # 调用主题包

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP",[30, 30, 20],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP",[50, 50, 50],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP",[70, 60, 60],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 构建时间线对象
timeline = Timeline(
    {"theme": ThemeType.PURPLE_PASSION}      # 主题设置
)
# 在时间线内添加柱状图对象
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")

# 自动播放设置
timeline.add_schema(
    play_interval=1000,     # 自动播放的时间间隔，单位毫秒
    is_timeline_show=True,  # 是否在自动播放的时候，显示时间线
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True,      # 是否循环自动播放
)

# 绘图是使用时间线对象绘图，而不是bar对象了
timeline.render("基础时间线柱状图.html")