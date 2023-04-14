class Phone:
    IMEI = None             # 序列号
    producer = "ITCAST"     # 厂商

    def call_by_5g(self):
        print("使用5g网络进行通话")

# 定义自雷，复写父类成员
# class MyPhone(Phone):
#     producer = "ITHEIMA"    # 复写父类的成员属性
#
#     def call_by_5g(self):
#         print("开启CPU单核模式，确保通话的时候省电")
#         print("使用5g网络进行通话")
#         print("关闭CPU单核模式，确保性能")
# phone = MyPhone()
# phone.call_by_5g()
# print(phone.producer)

# 在子类中，调用父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"    # 复写父类的成员属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # 方式1
        # print(f"父类的厂商是：{Phone.producer}")          # 调用父类成员属性
        # Phone.call_by_5g(self)                          # 调用父类成员方法
        # 方式2
        print(f"父类的厂商是：{super().producer}")          # 调用父类成员属性
        super().call_by_5g()                              # 调用父类成员方法
        print("关闭CPU单核模式，确保性能")
phone = MyPhone()
phone.call_by_5g()
print(phone.producer)