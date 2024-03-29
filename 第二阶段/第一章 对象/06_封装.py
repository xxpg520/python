"""
演示面向对象封装思想中私有成员的使用
"""

# 定义一个类，内含私有成员变量和私有成员方法
class Phone:
    # 定义私有成员变量
    __current_voltage = 0.5        # 当前手机运行电压

    def __keep_single_core(self):   # 设置私有成员方法
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:     # 调用私有成员变量进行比较
            print("5g通话已开启")
        else:
            self.__keep_single_core()       # 调用私有成员方法
            print("电量不足，无法使用5g通话，并已设置为单核运行进行省电")

phone = Phone()
phone.call_by_5g()